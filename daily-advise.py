import requests, telebot, os

BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)
api_url = 'https://api.api-ninjas.com/v1/advice'
response = requests.get(api_url, headers={'X-Api-Key': 'QqDxZFRyZ9iV6SdFznkiUA==9RQu3gJhcs1Bt4kI'})
advice = response.text

if response.status_code == requests.codes.ok:
    #print(response.text)

else:
    print("Error:", response.status_code, response.text)
