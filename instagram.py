import requests
import os
from dotenv import load_dotenv

load_dotenv()
INSTAGRAM_ACCOUNT_ID = os.getenv('INSTAGRAM_ACCOUNT_ID')
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')

def get_instagram_account_info():
    url = f"https://graph.facebook.com/v15.0/{INSTAGRAM_ACCOUNT_ID}?fields=id,username,name,media_count&access_token={ACCESS_TOKEN}"
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        account_info = response.json()
        print("Account Information:")
        print(account_info)
    else:
        print(f"Error: Received status code {response.status_code}")
        print(f"Response Text: {response.text}")

# Run the test
get_instagram_account_info()
