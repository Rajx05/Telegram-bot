import os
import praw
import requests, telebot
from urllib.parse import urlparse
from io import BytesIO

# TG bot initialization
bot = telebot.TeleBot(os.getenv("BOT_TOKEN"))
id = os.getenv("CHAT_ID")
# Initialize PRAW
reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
    user_agent=os.getenv("REDDIT_USER_AGENT")
)

def send_meme(url):
    response = requests.get(url, stream=True)
    meme = BytesIO(response.content)
    # send meme
    bot.send_photo(id,meme,caption="Today's meme")
    #print(response.text)
    

def fetch_memes(subreddit_name="memes", limit=5, save_dir="memes"):
    """Fetches top meme posts from a subreddit and downloads their media."""
    #os.makedirs(save_dir, exist_ok=True)
    
    subreddit = reddit.subreddit(subreddit_name)
    count = 0  # Counter to track successful downloads

    for post in subreddit.top(time_filter="day",limit=limit * 2):  # Fetch extra posts in case some don't have media
        if post.url.endswith((".jpg", ".png", ".gif", ".mp4", ".webm",".jpeg",".gifv",".webp")):
            count += 1
            send_meme(post.url, save_dir, f"meme_{count}")
        
        if count >= limit:  # Stop when we reach the desired limit
            break

# Run the scraper
fetch_memes(limit=1)

