# Description: This script is used to call the OpenAI API to get a response for a given prompt. 
# @Author: Bertan Berker
# @Language: Python

from dotenv import load_dotenv
import os
import openai

load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')
client = openai.OpenAI()


# This function takes a prompt as input and returns the response from the OpenAI API
# :prompt: str: The prompt to send to the OpenAI API
# :return: str: The response from the OpenAI API
def get_openai_text(prompt):

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        messages=[
            {"role": "system", "content": "You are a world-class instagram influencer and you are excellent at generating posts"},
            {"role": "user", "content": prompt}
        ]
    )

    return completion.choices[0].message.content


# This function takes a prompt as input and returns an image URL from the OpenAI API
# :prompt: str: The prompt to send to the OpenAI API
# :return: str: The URL of the generated image from the OpenAI API
def get_openai_image(prompt):
    response = client.images.generate(
        prompt=prompt,
        n=1,
        size="1024x1024"
    )    
    return response.data[0].url