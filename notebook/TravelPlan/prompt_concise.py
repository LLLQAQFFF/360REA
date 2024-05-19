# Leader Prompt with Structured Output Requirements
Leader_prompt = """
As the leader of a travel planning team. Your team can have up to five members. Your role is to guide the team in creating a comprehensive, practical, and innovative travel plan with a robust emergency strategy. Your team's work will involve collaborative and process-oriented efforts, akin to an assembly line. Please output the task assignments and professions in order, following the structured format. Your answer should be concise. You can refer to the example I provided.

Structured output requirements:
Main Goals:
[List main goals related to travel planning]

Guidance:
[Provide objectives and methods specific to travel planning]

Task Assignment(List each profession and their job descriptions in order. One profession per line and corresponding tasks,Separate with colons. Also, remember your team can have up to five members):
[Assign roles and tasks related to travel planning]

For example:
Main Goals:
Develop a comprehensive and engaging travel itinerary, ensure operational feasibility, infuse innovation, while considering budget control and emergency preparedness

Guidance:
Ensure smooth team collaboration, prioritize customer satisfaction, find a balance between innovation and practicality, ensure the travel plan is within budget, and be ready to address potential challenges and changes.

Task Assignment:
Integrated Travel Planner: Responsible for designing the entire travel itinerary, including destination selection, activity planning, ensuring the route's innovativeness and customer preferences;
Logistics and Risk Management Coordinator: Manage all logistics arrangements, including transportation, accommodations, and emergency plans, ensuring smooth and safe itinerary execution;
Finance and Budget Manager: Handle budget planning and control, ensuring all plans are financially feasible and efficient;
Creative Consultant: Provide unique travel experience and activity suggestions, adding attractiveness and uniqueness to the itinerary.
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
Output a complete final plan based on the work results of the members. As a leader, you should ensure the Alignment with Interests and Preferences, Seasonal Appropriateness, Variety and Balance, Feasibility and Logistics and Local Insights and Unique Experiences. And summarize the results of the other members into the final result, the final plan needs to be evaluated and done well. Do not output other non output required content.

Structured output requirements:
Task: [Overall task]
Final Plan: [Details of the complete travel plan]
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
As a leader, you need to learn experience from this task, and the format should be "Where did I do well this time... why didn't I do well this time... next time I should...".Note that these experiences are for this type of task, and it is important to summarize the experience of this type of task from this experience. The answer should be as concise as possible.
"""
