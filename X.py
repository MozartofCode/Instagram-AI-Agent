# @Author: Bertan Berker
# @Language: Python
# 

import tweepy
from dotenv import load_dotenv
from datetime import date
import shutil, pathlib, os

load_dotenv()

API_KEY = os.getenv('TWITTER_API_KEY')
API_SECRET_KEY = os.getenv('TWITTER_API_SECRET')
ACCESS_TOKEN = os.getenv('TWITTER_ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.getenv('TWITTER_ACCESS_TOKEN_SECRET')
BEARER_TOKEN = os.getenv('TWITTER_BEARER_TOKEN')


# Authenticate to Twitter
auth = tweepy.OAuthHandler(
    API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET
)

# Twitter API 2.0
newApi = tweepy.Client(
    bearer_token=BEARER_TOKEN,
     access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_TOKEN_SECRET,
    consumer_key=API_KEY,
    consumer_secret=API_SECRET_KEY,
)

# Create an API object
api = tweepy.API(auth)

# Post a tweet with text and media
tweet = "This is a tweet with an image!"
image_path = "img.png"

media = api.media_upload(image_path)
post_result = newApi.create_tweet(text=tweet, media_ids=[media.media_id])


print("Tweet with image posted successfully!")


