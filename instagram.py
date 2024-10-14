import requests
import os
from dotenv import load_dotenv

load_dotenv()
INSTAGRAM_ACCOUNT_ID = os.getenv('INSTAGRAM_ACCOUNT_ID')
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')

def post_on_instagram(caption, image_url):
    url = f"https://graph.facebook.com/v12.0/{INSTAGRAM_ACCOUNT_ID}/media"
    data = {
        "caption": caption,
        "image_url": image_url,
        "access_token": ACCESS_TOKEN
    }
    response = requests.post(url, data=data)
    return response.json()


