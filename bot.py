import os
import telebot
from flask import Flask, request 
import praw
import requests
from io import BytesIO

TOKEN = os.environ.get("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

# Initialize PRAW for Reddit
reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
    user_agent=os.getenv("REDDIT_USER_AGENT")
)

def send_meme(chat_id, subreddit_name="memes", limit=1):
    """Fetches top meme posts from a subreddit and sends their media to chat_id."""
    subreddit = reddit.subreddit(subreddit_name)
    count = 0
    for post in subreddit.top(time_filter="day", limit=limit * 2):
        if post.url.endswith((".jpg", ".png", ".gif", ".mp4", ".webm", ".jpeg", ".gifv", ".webp")):
            response = requests.get(post.url, stream=True)
            meme = BytesIO(response.content)
            bot.send_photo(chat_id, meme, caption="Today's meme")
            count += 1
        if count >= limit:
            break

# Basic command
@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "Yo")

# Webhook endpoint
@app.route('/' + TOKEN, methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "OK", 200

# Endpoint for external cron job to trigger meme reminder
@app.route('/remind', methods=['POST'])
def remind():
    chat_id = os.environ.get("CHAT_ID")  # Set this in your Render environment
    if chat_id:
        send_meme(chat_id)
        return "Meme sent", 200
    return "Chat ID not set", 400

# Home route for sanity check
@app.route('/')
def webhook():
    return "Bot is running!"

# Start Flask app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
