import os
import telebot

TOKEN = os.getenv("BOT_TOKEN")  # Fetch token from GitHub Secrets
bot = telebot.TeleBot(TOKEN)

bot.send_message(chat_id="1661706465", text="Hello from GitHub Actions!")
