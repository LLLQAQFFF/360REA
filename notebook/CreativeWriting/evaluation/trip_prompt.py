evaluation_prompt = """
You will be given a multi-day travel plan. The task is {total_task}

Your task is to evaluate the travel plan on specific criteria.

Please make sure you read and understand these instructions carefully. Please keep this document open while reviewing, and refer to it as needed.

Evaluation Criteria:
    
Completeness (1-20): Does the plan cover all necessary aspects for each day, including accommodations, transportation, activities, and meals?
Practicality (1-20): Is the itinerary feasible, considering travel times and realistic scheduling?
Creativity and Uniqueness (1-20): Does the plan include innovative or unique suggestions?
Logical Flow and Coherence (1-20): Is the plan logically organized with a clear day-to-day progression?
Evaluation Steps:

Review the travel plan in detail.
Compare the plan against each criterion.
Assign a score for each criterion on a scale of 1 to 20, where 1 is the lowest and 20 is the highest based on the Evaluation Criteria.

Travel Plan:

{Travel_Plan}

Evaluation Form:

Completeness:
Practicality:
Creativity and Uniqueness:
Logical Flow and Coherence:
"""

evaluation_metric = """
Practicality (1-20): Is the itinerary feasible, considering travel times, realistic scheduling, and accommodation arrangements?
Safety (1-20): Does the plan address safety concerns, including health precautions and emergency preparedness?
Flexibility (1-20): Can the plan be easily adjusted to accommodate unforeseen circumstances or changes in preferences?
Personalization and Cultural Experience (1-20): Does the plan cater to the traveler's interests and include opportunities to engage with local culture and traditions?
"""

evaluation_prompt_test = """
You will be given a multi-day travel plan. The task is {total_task}

Your task is to evaluate the travel plan on specific criteria.

Please make sure you read and understand these instructions carefully. Please keep this document open while reviewing, and refer to it as needed.

Evaluation Criteria:

Completeness (1-20): Does the plan cover all necessary aspects for each day, including accommodations, transportation, activities, and meals?
Practicality (1-20): Is the itinerary feasible, considering travel times and realistic scheduling?
Creativity and Uniqueness (1-20): Does the plan include innovative or unique suggestions?
Logical Flow and Coherence (1-20): Is the plan logically organized with a clear day-to-day progression?
Evaluation Steps:

Review the travel plan in detail.
Compare the plan against each criterion.
Assign a score for each criterion on a scale of 1 to 20, where 1 is the lowest and 20 is the highest based on the Evaluation Criteria.

Travel Plan:

{Travel_Plan}

Evaluation Form (scores ONLY, No need for extra output):

Completeness:
Practicality:
Creativity and Uniqueness:
Logical Flow and Coherence:

for example:

Completeness: 18
Practicality: 19
Creativity and Uniqueness: 20
Logical Flow and Coherence: 18
"""

evaluation_CW_prompt = """
You will be given a piece of creative writing that incorporates trivia questions and answers. The task is to evaluate the creative writing on specific criteria.

Please make sure you read and understand these instructions carefully. Please keep this document open while reviewing, and refer to it as needed.

Evaluation Criteria:

Originality and Creativity (1-20): How unique and imaginative is the story?
Coherence and Structure (1-20): Does the story flow logically with a clear structure?
Integration of Trivia (1-20): How seamlessly are trivia questions and answers woven into the narrative?
Language and Style (1-20): Is the language and style appropriate and effective for the intended audience and genre?
Engagement and Interest (1-20): Does the story capture and maintain the reader's interest?

Evaluation Steps:

Review the creative writing piece in detail.
Compare the writing against each criterion.
Assign a score for each criterion on a scale of 1 to 20, where 1 is the lowest and 20 is the highest based on the Evaluation Criteria.
Creative Writing Piece:

{res_CW}

Evaluation Form:

Originality and Creativity:
Coherence and Structure:
Integration of Trivia:
Language and Style:
Engagement and Interest:
"""

evaluation_CW_prompt_test = """
You will be given a piece of creative writing that incorporates trivia questions and answers. The task is to evaluate the creative writing on specific criteria.

Please make sure you read and understand these instructions carefully. Please keep this document open while reviewing, and refer to it as needed.

Evaluation Criteria:

Originality and Creativity (1-20): How unique and imaginative is the story?
Coherence and Structure (1-20): Does the story flow logically with a clear structure?
Integration of Trivia (1-20): How seamlessly are trivia questions and answers woven into the narrative?
Language and Style (1-20): Is the language and style appropriate and effective for the intended audience and genre?
Engagement and Interest (1-20): Does the story capture and maintain the reader's interest?

Evaluation Steps:

Review the creative writing piece in detail.
Compare the writing against each criterion.
Assign a score for each criterion on a scale of 1 to 20, where 1 is the lowest and 20 is the highest based on the Evaluation Criteria.
Creative Writing Piece:

{res_CW}

Evaluation Form (scores ONLY, No need for extra output):

Originality and Creativity:
Coherence and Structure:
Integration of Trivia:
Language and Style:
Engagement and Interest:


for example:

Originality and Creativity: 20
Coherence and Structure: 18
Integration of Trivia: 19
Language and Style: 20
Engagement and Interest: 17
"""

new_travel_train = """
You will be given a multi-day travel plan. The task is {total_task}

Your task is to evaluate the travel plan on specific criteria.

Please make sure you read and understand these instructions carefully. Please keep this document open while reviewing, and refer to it as needed.

Evaluation Criteria:

1. Alignment with Interests and Preferences (1-20): Does the travel plan align with the specified interests and preferences of the travelers, including activities that cater to all age groups involved?
2. Seasonal Appropriateness (1-20): Are the activities and destinations chosen appropriate for the season and month of travel, maximizing the enjoyment and suitability of the weather conditions?
3. Variety and Balance (1-20): Does the itinerary offer a balanced mix of activities (e.g., adventure, relaxation, cultural exploration), ensuring a diverse and engaging experience for the traveler?
4. Feasibility and Logistics (1-20): Is the plan logistically sound, with realistic travel times, accommodation arrangements, and schedules that are achievable and considerate of the traveler's comfort?
5. Local Insights and Unique Experiences (1-20): Does the plan include unique, local experiences or insights that offer an authentic and memorable exploration of the destination?

Evaluation Steps:

1. Review the travel plan in detail.
2. Compare the plan against each criterion.
3. Assign a score for each criterion on a scale of 1 to 20, where 1 is the lowest and 20 is the highest, based on the Evaluation Criteria.

Travel Plan:

{Travel_Plan}

Evaluation Form:

Alignment with Interests and Preferences:
Seasonal Appropriateness:
Variety and Balance:
Feasibility and Logistics:
Local Insights and Unique Experiences:

For example:
Alignment with Interests and Preferences: 18
Seasonal Appropriateness: 20
Variety and Balance: 19
Feasibility and Logistics: 17
Local Insights and Unique Experiences: 20

"""

new_travel_test = """
You will be given a multi-day travel plan. The task is {total_task}

Your task is to evaluate the travel plan on specific criteria.

Please make sure you read and understand these instructions carefully. Please keep this document open while reviewing, and refer to it as needed.

Evaluation Criteria:

1. Alignment with Interests and Preferences (1-20): Does the travel plan align with the specified interests and preferences of the travelers, including activities that cater to all age groups involved?
2. Seasonal Appropriateness (1-20): Are the activities and destinations chosen appropriate for the season and month of travel, maximizing the enjoyment and suitability of the weather conditions?
3. Variety and Balance (1-20): Does the itinerary offer a balanced mix of activities (e.g., adventure, relaxation, cultural exploration), ensuring a diverse and engaging experience for the traveler?
4. Feasibility and Logistics (1-20): Is the plan logistically sound, with realistic travel times, accommodation arrangements, and schedules that are achievable and considerate of the traveler's comfort?
5. Local Insights and Unique Experiences (1-20): Does the plan include unique, local experiences or insights that offer an authentic and memorable exploration of the destination?

Evaluation Steps:

1. Review the travel plan in detail.
2. Compare the plan against each criterion.
3. Assign a score for each criterion on a scale of 1 to 20, where 1 is the lowest and 20 is the highest, based on the Evaluation Criteria.

Travel Plan:

{Travel_Plan}

Evaluation Form (scores ONLY, No need for extra output):

Alignment with Interests and Preferences:
Seasonal Appropriateness:
Variety and Balance:
Feasibility and Logistics:
Local Insights and Unique Experiences:

For example:
Alignment with Interests and Preferences: 18
Seasonal Appropriateness: 20
Variety and Balance: 19
Feasibility and Logistics: 17
Local Insights and Unique Experiences: 20

"""

ev_prompt = """
Story Evaluation Test:

You will be given a story that incorporates answers to trivia questions. The task is to evaluate the story on specific criteria.

Answer is {answer}

Please make sure you read and understand these instructions carefully. Please keep this document open while reviewing, and refer to it as needed.

Evaluation Criteria:

1. Coherence and Flow (1-20): Does the story maintain a logical progression and smooth flow, making it easy for readers to follow without confusion?
2. Integration of Trivia Answers (1-20): Are the trivia answers seamlessly integrated into the story, enhancing the narrative rather than feeling forced or out of place?
3. Creativity and Originality (1-20): Does the story exhibit unique ideas and perspectives, exploring and expanding upon the trivia answers in innovative ways?
4. Language and Style (1-20): Is the language engaging and vivid, with a style that complements the story's theme and holds the reader's attention?
5. Emotional Engagement (1-20): Does the story evoke emotions, creating a connection with the reader through its characters, settings, or events?
6. Theme and Meaning (1-20): Does the story convey a deeper message or theme, encouraging the reader to think beyond the surface narrative?
7. Character Development (1-20): If applicable, do the characters show growth and complexity, with clear motivations and emotional depth?

Evaluation Steps:

1. Review the story in detail.
2. Compare the story against each criterion.
3. Assign a score for each criterion on a scale of 1 to 20, where 1 is the lowest and 20 is the highest, based on the Evaluation Criteria.

Story:

{Story_Content}

Evaluation Form:

Coherence and Flow:
Integration of Trivia Answers:
Creativity and Originality:
Language and Style:
Emotional Engagement:
Theme and Meaning:
Character Development:

For example (scores ONLY, No need for extra output):
Coherence and Flow: 18
Integration of Trivia Answers: 17
Creativity and Originality: 19
Language and Style: 16
Emotional Engagement: 20
Theme and Meaning: 18
Character Development: 15
"""

ev_metric = """
1. Coherence and Flow (1-20): Does the story maintain a logical progression and smooth flow, making it easy for readers to follow without confusion?
2. Integration of Trivia Answers (1-20): Are the trivia answers seamlessly integrated into the story, enhancing the narrative rather than feeling forced or out of place?
3. Creativity and Originality (1-20): Does the story exhibit unique ideas and perspectives, exploring and expanding upon the trivia answers in innovative ways?
4. Language and Style (1-20): Is the language engaging and vivid, with a style that complements the story's theme and holds the reader's attention?
5. Emotional Engagement (1-20): Does the story evoke emotions, creating a connection with the reader through its characters, settings, or events?
6. Theme and Meaning (1-20): Does the story convey a deeper message or theme, encouraging the reader to think beyond the surface narrative?
7. Character Development (1-20): If applicable, do the characters show growth and complexity, with clear motivations and emotional depth?
"""
