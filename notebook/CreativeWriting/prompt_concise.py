# Leader Prompt with Structured Output Requirements
Leader_prompt = """
As the leader of a Trivia Creative Writing team, your team consists of three or four members. Your role is to steer the team towards creating a coherent and engaging story that not only incorporates answers to five trivia questions but also places a heightened focus on the accuracy of these answers. This requires collaborative and creative efforts, with an added emphasis on ensuring that the trivia integrated into the narrative is both accurate and seamlessly blended. Your answer should include concise task assignments and professions, following the structured format we discussed. Focus on the key roles that contribute to achieving high factual accuracy alongside creative storytelling.

Just output what i require!!!!! no need to writing story.

Structured output requirements:
Main Goals:
[List main goals related to trivia-based story writing]

Guidance:
[Provide objectives and methods specific to trivia integration and storytelling]

Task Assignment(One profession per line and corresponding tasks,Separate with colons. Also, remember your team has four members):
[Assign roles and tasks related to trivia-based story writing]

For example:

---
Main Goals:

xxx

Guidance:

xxx

Task Assignment:

role1 xxx: xxx
role2 xxx: xxx
role3 xxx: xxx
---

"""

summarize_global_experience_prompt = """
You are a {role} of the team, and your team's overall task is {total_task}.

Main Goals:
{main_goals}
Guidance:
{guidance}

Your subtask is {subtask}.

Here is the previous experience, and you have summarized three to ten experiences that can be used for this task
{global_exp}
"""


# Meeting Prompt with Structured Output Requirements
Meeting_prompt = """
Provide feedback on the {total_task}. Do not output other non output required content.

Structured output requirements:
Self-Evaluation Score and Feedback:
[Rate yourself and comment on your contributions and improvement areas using degree adverbs (Extremely poor, Very bad, Poor, Fair, Good, Very good, Excellent).]

Peer Score and Feedback:
[Rate each colleague and comment on their contributions and improvement areas using degree adverbs (Extremely poor, Very bad, Poor, Fair, Good, Very good, Excellent).]

For example:
Self-Evaluation Score and Feedback:
Good - Contributed innovative ideas, need to improve time management

Peer Score and Feedback:
Colleague A: Very good - Thorough research, could improve presentation skills
"""


# Leader Meeting Prompt with Structured Output Requirements
Meeting_prompt_Leader = """
As the leader, evaluate team performance and reflect on your leadership. Do not output other non-required content.

Structured output requirements:
Self-Evaluation Score and Feedback:
[Rate yourself and comment on your contributions and improvement areas using degree adverbs (Extremely poor, Very bad, Poor, Fair, Good, Very good, Excellent).]


Team Member Score and Evaluation:
[Rate each team member and provide a performance review, including improvement areas, using degree adverbs (Extremely poor, Very bad, Poor, Fair, Good, Very good, Excellent).]


For example:
Self-Evaluation Score and Feedback:
Good - Contributed innovative ideas, need to improve time management

Team Member Score and Evaluation:
Member A: Excellent - Excelled in creativity; Member B: Fair - Needs to improve time management

"""

# Completion Prompt with Structured Output Requirements
Complete_prompt = """
You are {role} of a team, and your overall task is {total_task}. Your work style is in the form of an assembly line, and you need to rely on the work of the previous person just provided to complete your own work. Your task is {subtask} Here are the important and guiding points proposed by the Leader. Complete your part of the work.

Main Goals:
{main_goals}
Guidance:
{guidance}

Output your detailed work results to the leader. Do not output other non output required content.

Structured output requirements:
Role: [Your Role]
Task: [Your subtask]
Final Results: [Detailed and complete results of the task]

"""

# Leader Completion Prompt with Structured Output Requirements
Complete_prompt_Leader_prompt = """
Output a complete story based on the work results of the members. Do not output other non output required content.

Structured output requirements:
Final Res: [Details of the complete travel plan]

For example:
Final Res:
In the bustling corridors of Hogwarts, Harry Potter stumbled upon Hermione Granger, who excitedly waved a faded flyer of 'The Chipmunk Champions' in the air. "They were a fantastic wizarding band modeled after Muggle 'Alvin and the Chipmunks', created by that Muggle Ross Bagdasarian!" Hermione exclaimed, her nose buried in "The Weird and Wonderful in Muggle Music," a book she'd borrowed for Muggle Studies.

Later that evening, as the golden sunset painted the sky over Hogwarts, an announcement echoed through the halls informing the students of a magical rendition of the famous musical "Sunset Boulevard," which was set to premiere that very evening in the grand banquet hall.

Harry, Hermione, and Ron attended the play, with Hermione whispering historical facts into Ron's ear. "This reminds me of a Muggle play that premiered on December 10th, 1993," she said. "It's fascinating how Muggles create such marvelous things without magic."

After the play, the trio huddled beside the fireplace in the Gryffindor common room. Neville Longbottom joined them, excitedly brandishing a book titled "Muggle Leaders Through the Ages." "Did you know that after Arthur Balfour, it was Sir Henry Campbell-Bannerman who became the British Prime Minister?" he asked with his newfound interest in Muggle politics.

Amidst their conversations, the wireless radio crooned a soft melody, capturing the attention of Dean Thomas. "That's 'Kiss You All Over' by Exile," he mentioned. "One of my mum's favorites. I heard it while working on my summer job at the Muggle café."

Their evening concluded with a discussion on the charity event happening next week for St. Mungo's Hospital, named in honor of the Muggle singer Kathleen Ferrier, who was claimed by a Muggle illness known as breast cancer. "We need to help those who suffer from ailments for which magic has yet to find a cure," said Hermione, compassionate as always.

Harry nodded in agreement, feeling a deep respect for those who battled diseases, both magical and Muggle.
"""

summarize_local_experience_prompt = """
Based on feedback from others, past experiences, and from the perspective of one's own role, summarize some experiences that you may use in the future. Your answer should be as concise as possible. Do not output other non output required content.

Your role: {role}.

Previous experience: 

{pre_exp}

Structured output requirements:
Role: [Your Role]
Experience: [Short experience description]
"""

# Guidance for Team Members (Leader) Prompt with Structured Output Requirements
guidance_leader_prompt = """
As the Leader of this project, your insight is crucial for guiding each team member's growth. Please provide specific feedback for each member, highlighting their strengths and areas for improvement. Do not output other non output required content.

Structured output requirements:
Feedback for Member: [Name, strengths, areas for improvement, guidance]
Overall Team Guidance: [General advice for the team]

For example:
Feedback for Member: John, excellent in analytics, needs to improve presentation skills, recommended to attend a workshop
Overall Team Guidance: Focus on continuous learning and open communication
"""

summarize_experience_prompt = """
As a Member of this team, you need to learn experience from this task, and the format should be "As [your role], Where did I do well this time... why didn't I do well this time... next time I should...", and the answer should be as concise as possible.
"""

summarize_experience_leader_prompt = """
Obtain new experiences based on previous experiences and current scores. The new experience should be summarized while presenting the experience gained from this task.
As a leader, you need to learn experience from this task, and the format should be "Where did I do well this time... why didn't I do well this time... next time I should...".Note that these experiences are for this type of task. The answer should be as concise as possible.
"""
