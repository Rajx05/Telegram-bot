import os
from telegram import Bot

TOKEN = os.getenv("BOT_TOKEN")  # Fetch token from GitHub Secrets
bot = Bot(token=TOKEN)

bot.send_message(chat_id="1661706465", text="Hello from GitHub Actions!")
