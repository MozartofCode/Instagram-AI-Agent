# Description: This script is used to call the OpenAI API to get a response for a given prompt. 
# @Author: Bertan Berker

from dotenv import load_dotenv
import os
import openai


load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')


client = openai.OpenAI()


def get_openai_response(prompt):

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )

    return completion.choices[0].message.content


user_prompt = "Write a short story about a robot learning to love."
response = get_openai_response(user_prompt)
print(response)
