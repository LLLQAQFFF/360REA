# Leader Prompt with Structured Output Requirements
Leader_prompt = """
As the leader of a logic grid puzzle team. Your team can have up to two members. Your role is to division of labor for the team. Your team's work will involve collaborative and process-oriented efforts, akin to an assembly line. Please output the task assignments and professions in order, following the structured format. Your answer should be concise. You can refer to the example I provided. Do not output any additional content.

{task}


Structured output requirements:
(List each profession and their job descriptions in order. One profession per line and corresponding tasks,Separate with colons. Also, remember your team can have up to two members)
[Assign roles and tasks]

For example:

role1: task description1
role1: task description1
"""

# Meeting Prompt with Structured Output Requirements

Meeting_prompt = """
Provide feedback on the {total_task}. Do not output other non output required content.

Structured output requirements:
Self-Evaluation Score and Feedback:
[Rate yourself and comment on your contributions and improvement areas using degree adverbs (Extremely poor, Very bad, Poor, Fair, Good, Very good, Excellent).]

Peer Score and Feedback:
[Rate each colleague and comment on their contributions and improvement areas using degree adverbs (Extremely poor, Very bad, Poor, Fair, Good, Very good, Excellent).]

Leader Score and Feedback:
[Rate the leader and comment on their leadership and areas for improvement using degree adverbs (Extremely poor, Very bad, Poor, Fair, Good, Very good, Excellent).]

Collaboration Opportunities:
[Integration ideas, joint efforts]

Open Questions:
[Any queries]

For example:
Self-Evaluation Score and Feedback:
Good - Contributed innovative ideas, need to improve time management

Peer Score and Feedback:
Colleague A: Very good - Thorough research, could improve presentation skills

Leader Score and Feedback:
Excellent - Provided good guidance, could involve team more in decision-making

Collaboration Opportunities:
Combine research findings, joint brainstorm sessions

Open Questions:
How can we better align our goals?
"""

# Leader Meeting Prompt with Structured Output Requirements
Meeting_prompt_Leader = """
As the leader, evaluate team performance and reflect on your leadership. Do not output other non-required content.

Structured output requirements:
Team Member Score and Evaluation:
[Rate each team member and provide a performance review, including improvement areas, using degree adverbs (Extremely poor, Very bad, Poor, Fair, Good, Very good, Excellent).]

Self-Evaluation Score and Reflection:
[Rate your leadership style and reflect on personal development using degree adverbs (Extremely poor, Very bad, Poor, Fair, Good, Very good, Excellent).]

Project Overview and Strategy:
[Assess the overall progress of the project and outline future strategy.]

For example:
Team Member Score and Evaluation:
Member A: Excellent - Excelled in creativity; Member B: Fair - Needs to improve time management

Self-Evaluation Score and Reflection:
Good - Effective delegation, need to improve communication

Project Overview and Strategy:
On track with current goals, next phase focuses on enhancing marketing strategy.
"""

# Completion Prompt with Structured Output Requirements
Complete_prompt = """
You are {role} of a team, and your overall task is {total_task}. Your work style is in the form of an assembly line, and you need to rely on the work of the previous person just provided to complete your own work. Your task is {subtask} Here are the important and guiding points proposed by the Leader. Complete your part of the work.

Output your detailed work results to the leader. Do not output other non output required content.

Structured output requirements:
Role: [Your Role]
Final Results: [Detailed and complete results of the task]

"""

# Leader Completion Prompt with Structured Output Requirements
Complete_prompt_Leader_prompt = """
Output a complete final ans based on the work results of the members. Do not output other non output required content.
Output the final house number without the need for additional content.

Structured output requirements:
final house number: []
"""

summarize_local_experience_prompt = """
Based on feedback from others, past experiences, and from the perspective of one's own role, summarize some experiences that everyone may use. Your answer should be as concise as possible. Do not output other non output required content.

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
As a leader, you need to learn experience from this task, and the format should be "Where did I do well this time... why didn't I do well this time... next time I should...".Note that these experiences are for this type of task, and it is important to summarize the experience of this type of task from this experience. The answer should be as concise as possible.
"""
