import os, telebot, json, requests, random
from bs4 import BeautifulSoup as bs

url = "https://api.api-ninjas.com/v1/webscraper"
headers={'X-Api-Key': 'QqDxZFRyZ9iV6SdFznkiUA==9RQu3gJhcs1Bt4kI',
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
]

headers["User-Agent"] = random.choice(user_agents)

# Target Website to Scrape
payload = {
    "url": "https://www.xvideos.com/?k=indian+bhabhi&sort=relevance&datef=today",
    
}

# Fetch Data from API
response = requests.get(url, headers=headers, params=payload)

# Extract All Links

data = response.json()
html_content = data.get("data","")

#parsing the html
soup = bs(html_content,"html.parser")
all_links = [a["href"] for a in soup.find_all("a", href=True)]

print("🔗 Links Found:")
video_links = []
for div in soup.find_all("div", class_="thumb"):
    a_tag = div.find("a", href=True)  # Find <a> inside <div>
    if a_tag:
        video_url = f"https://www.xvideos.com{a_tag['href']}"
        video_links.append(video_url)
#for link in video_links[:5]:  # Show first 10 links
#       print(link)

TOKEN = os.getenv("BOT_TOKEN")  # Fetch token from GitHub Secrets
bot = telebot.TeleBot(TOKEN)
bot.send_message(chat_id="-1002188987126", text=f"Today's Top 5 Trending Bhabhi porn:")
for link in video_links[:5]:
  bot.send_message(chat_id="-1002188987126", text=f"{link}")
