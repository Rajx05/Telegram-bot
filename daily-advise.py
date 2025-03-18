import requests, telebot, os, json

TOKEN = os.getenv("BOT_TOKEN")
ID = os.getenv("CHAT_ID")
bot = telebot.TeleBot(TOKEN)
api_url = 'https://api.api-ninjas.com/v1/advice'
response = requests.get(api_url, headers={'X-Api-Key': 'QqDxZFRyZ9iV6SdFznkiUA==9RQu3gJhcs1Bt4kI'})

if response.status_code == requests.codes.ok:
    #print(response.text)
    bot.send_message(ID,f"Todays Life Advise:\n->{response.json()["advice"]})")

else:
    print("Error:", response.status_code, response.text)
