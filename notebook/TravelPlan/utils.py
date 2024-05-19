import json
import time

from openai import OpenAI


def requestLLM(role_prompt, task):
    while True:
        try:
            # 模拟网络请求的延迟
            # time.sleep(3)
            client = OpenAI()
            # 这里假设连接可能会失败，导致抛出异常
            completion = client.chat.completions.create(
                model="gpt-4-0125-preview",
                # model="gpt-3.5-turbo-0125",
                messages=[
                    {"role": "system", "content": role_prompt},
                    {"role": "user", "content": task}
                ]
            )
            # 如果请求成功，跳出循环
            # return completion.choices[0].message
            return completion
        except Exception as e:
            # 打印异常信息
            print(f"An error occurred: {e}. Retrying...")
            # 可以在这里添加一个短暂的延时，避免立即重试
            time.sleep(1)


def extract_content(text, headings):
    content_dict = {}
    current_heading = None
    for line in text.split('\n'):
        # Check if the line is a heading
        if any(heading in line for heading in headings):
            current_heading = line.split(':')[0].strip()
            content_dict[current_heading] = ""
        elif current_heading:
            # Add the line to the current heading content
            content_dict[current_heading] += line.strip() + "\n"
    return content_dict
