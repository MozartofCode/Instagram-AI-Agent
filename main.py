# Description: This is the main file that runs the program. 
# It takes user input for the text prompt and generates a post caption and image using OpenAI's GPT-3 API.
# @Author: Bertan Berker
# @Language: Python

from prompt import get_openai_text, get_openai_image

# Main function to run the program
def main():
    text_prompt = input("Enter what kind of a post you want to generate: ")
    post_caption = get_openai_text(text_prompt)
    print(post_caption)

    image_prompt = ""
    post_image = get_openai_image(image_prompt)
    print(post_image)

    #post_on_instagram(post_caption, post_image)

    # Preview, confirmation step?
    # Chrome extension

    # print("Post successfully created and uploaded to Instagram!")



if __name__ == "__main__":
    main()
