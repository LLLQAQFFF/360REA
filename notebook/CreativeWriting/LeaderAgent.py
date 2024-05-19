import re

from utils import requestLLM, extract_content
from prompt_concise import Leader_prompt, Meeting_prompt_Leader, Complete_prompt_Leader_prompt, \
    summarize_experience_leader_prompt, guidance_leader_prompt


def decompose_response(response):
    # print(response)
    # Parsing the output
    sections = ["Main Goals:", "Task Assignment:", "Guidance:"]
    data = {section: "" for section in sections}
    current_section = None

    for line in response.split('\n'):
        if line in sections:
            current_section = line
        elif current_section:
            data[current_section] += line + '\n'

    # Extracted information
    main_goals = data["Main Goals:"]
    task_assignment = data["Task Assignment:"]
    guidance = data["Guidance:"]

    # Creating a dictionary to store the results
    member_tasks = {}
    role_pre = ""
    print(task_assignment)
    for line in task_assignment.split('\n'):
        if ':' in line:
            job_title, task = line.split(':', 1)
            job_title = job_title.replace("-", "").strip()
            role_pre = job_title
            member_tasks[job_title] = task

    return main_goals, member_tasks, guidance


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
        else:
            self.history.append("")
        self.tokens = 0

    def decompose_task(self):
        # print(Leader_prompt)
        completion = requestLLM('\n'.join(self.history), Leader_prompt + self.total_task)
        response = completion.choices[0].message.content
        self.tokens += completion.usage.total_tokens
        # print(response)
        # response = exp4
        self.history.append("User\n\n" + Leader_prompt + self.total_task)
        self.history.append("Leader\n\n" + response)
        return decompose_response(response)

    def meeting(self, res_others):
        completion = requestLLM("\n There are others' work\n" + res_others,
                                Meeting_prompt_Leader.format(total_task=self.total_task)
                                )
        response = completion.choices[0].message.content.replace("*", '')
        self.tokens += completion.usage.total_tokens
        self.history.append(
            "User\n\n" + "\n There are others' work\n" + res_others + Meeting_prompt_Leader.format(
                total_task=self.total_task))
        self.history.append("Leader\n\n" + response)
        headings = ["Team Member Score and Evaluation", "Self-Evaluation Score and Feedback"]
        feedback_dict = extract_content(response, headings)
        self.feedback_dict = feedback_dict
        return feedback_dict

    def complete_task(self, subtask_res):
        completion = requestLLM("\nThere are the result from your team members\n" + subtask_res,
                              Complete_prompt_Leader_prompt + "\n\nRemember to consider your experience:\n")
        response = completion.choices[0].message.content
        self.tokens += completion.usage.total_tokens
        self.history.append(
            # "User\n\nThere are the feedback you received\n" + feedback_received + Complete_prompt_Leader_prompt)
            "User\n\n" + "\nThere are the result from your team members\n" + subtask_res + Complete_prompt_Leader_prompt)
        self.history.append("Leader\n\n" + response)
        self.final_res = response
        return response

    def generate_leadership_summary(self, evaluation_metric, evaluation):
        # generate a leadership summary
        completion = requestLLM("\n".join(
            self.history) + "\nthis is the evaluation metric\n" + evaluation_metric + "\nThis is an evaluation of your results." + evaluation,
                              summarize_experience_leader_prompt)
        response = completion.choices[0].message.content
        self.tokens += completion.usage.total_tokens
        self.experience = response
        return response

    def generate_guidance(self, evaluation_metric, evaluation):
        completion = requestLLM("\n".join(
            self.history) + "\nthis is the evaluation metric\n" + evaluation_metric + "\nThis is an evaluation of your results." + evaluation,
                              guidance_leader_prompt)
        response = completion.choices[0].message.content
        self.tokens += completion.usage.total_tokens
        self.guidance = response
        return response

    def sum_up_experience(self, exp):
        completion = requestLLM(
            "As the leader of a Trivia Creative Writing team, your team consists of four members. Your role is to steer the team towards creating a coherent and engaging story that not only incorporates answers to five trivia questions but also places a heightened focus on the accuracy of these answers. This requires collaborative and creative efforts, with an added emphasis on ensuring that the trivia integrated into the narrative is both accurate and seamlessly blended.\n",
            "This is the Previous experience\n" + exp + "Use them to summarize ten experiences that can be applied to your task\n" + self.total_task)
        response = completion.choices[0].message.content
        self.tokens += completion.usage.total_tokens
        self.history.append(response)
        print(response)
