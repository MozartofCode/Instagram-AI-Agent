from prompt import get_openai_text, get_openai_image



def main():
    text_prompt = input("Enter what kind of a post you want to generate: ")
    post_caption = get_openai_text(text_prompt)
    print(post_caption)

    image_prompt = ""
    post_image = get_openai_image(image_prompt)
    print(post_image)


if __name__ == "__main__":
    main()
