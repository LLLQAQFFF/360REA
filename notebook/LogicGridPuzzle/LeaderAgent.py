import re

from utils import requestLLM, extract_content
from prompt_concise import Leader_prompt, Meeting_prompt_Leader, Complete_prompt_Leader_prompt, \
    summarize_experience_leader_prompt, guidance_leader_prompt


def decompose_response(response):
    member_tasks = {}
    for line in response.split('\n'):
        if ':' in line:
            job_title, task = line.split(':', 1)
            job_title = job_title.replace("-", "").strip()
            role_pre = job_title
            member_tasks[job_title] = task

    return member_tasks


class Leader:
    def __init__(self, name, total_task, Leader_experience=None):
        self.name = name
        self.total_task = total_task
        self.experience = Leader_experience
        self.team_members = []
        self.history = []
        self.final_res = None
        self.feedback_dict = {}
        self.guidance = None
        if Leader_experience is not None:
            self.history.append(
                "This is the experience from previous tasks. You can refer to it for future tasks.\n" + self.experience)
        self.tokens = 0

    def decompose_task(self):
        completion = requestLLM(Leader_prompt.format(task=self.total_task), "")
        response = completion.choices[0].message.content
        self.tokens += completion.usage.total_tokens
        self.history.append("User\n\n" + Leader_prompt.format(task=self.total_task))
        self.history.append("Leader\n\n" + response)
        return decompose_response(response)

    def meeting(self, res_others):
        completion = requestLLM('\n'.join(
            self.history) + "\nThe above is our previous conversation.\n" + "\n There are others' work\n" + res_others,
                                Meeting_prompt_Leader.format(total_task=self.total_task)
                                )
        response = completion.choices[0].message.content.replace('*', '')
        self.tokens += completion.usage.total_tokens
        self.history.append(
            "User\n\n" + "\n There are others' work\n" + res_others + Meeting_prompt_Leader.format(
                total_task=self.total_task))
        self.history.append("Leader\n\n" + response)
        headings = ["Team Member Score and Evaluation", "Self-Evaluation Score and Reflection",
                    "Project Overview and Strategy"]
        feedback_dict = extract_content(response, headings)
        self.feedback_dict = feedback_dict
        return feedback_dict

    def complete_task(self, subtask_res, feedback_received=""):
        completion = requestLLM("\n".join(
            self.history) + "\nThe above is our previous conversation.\n" + "\nThere are the feedback you received\n" + feedback_received + "\nThere are the result from your team members\n" + subtask_res,
                                Complete_prompt_Leader_prompt)
        response = completion.choices[0].message.content
        self.tokens += completion.usage.total_tokens
        self.history.append(
            # "User\n\nThere are the feedback you received\n" + feedback_received + Complete_prompt_Leader_prompt)
            "User\n\n" + "\nThere are the feedback you received\n" + feedback_received + "\nThere are the result from your team members\n" + subtask_res + Complete_prompt_Leader_prompt)
        self.history.append("Leader\n\n" + response)
        self.final_res = response
        return response

    def generate_leadership_summary(self, evaluation_metric, evaluation):
        # generate a leadership summary
        response = requestLLM("\n".join(
            self.history) + "\nthis is the evaluation metric\n" + evaluation_metric + "\nThis is an evaluation of your results." + evaluation,
                              summarize_experience_leader_prompt).content
        self.experience = response
        return response

    def generate_guidance(self, evaluation_metric, evaluation):
        response = requestLLM("\n".join(
            self.history) + "\nthis is the evaluation metric\n" + evaluation_metric + "\nThis is an evaluation of your results." + evaluation,
                              guidance_leader_prompt).content
        self.guidance = response
        return response
