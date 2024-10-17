# @Author: Bertan Berker
# @Language: Python
# Description: This is the main file that runs the program. 
# It takes user input for the text prompt and generates a post caption and image using OpenAI's GPT-3 API.


from langchain.agents import initialize_agent, Tool
from langchain.chat_models import ChatOpenAI
from llm import get_openai_text, get_openai_image
from X import post_on_X
import requests

# Main function to run the program
def post_image_with_caption(text_prompt):
    
    post_caption = get_openai_text(text_prompt)
    print(post_caption)

    post_image = get_openai_image(text_prompt)
    print(post_image)

    post_on_X(post_caption, post_image)


def create(text_prompt):
    # Creating the Agent 

    tools = [
        Tool(
            name="Generate and Post",
            func=post_image_with_caption,
            description="This tool generates a post caption and an image based on a given prompt and posts it on Twitter",
        )
    ]

    llm = ChatOpenAI(model="gpt-3.5-turbo")
    agent = initialize_agent(tools, llm, agent="zero-shot-react-description")

    # Executing the agent
    agent.invoke(text_prompt)


def main():
    text_prompt = input("What kind of a post you want to generate: ")
    create(text_prompt)
    