import requests
import json
from datetime import datetime

NEWS_API_ENDPOINT = "https://newsapi.org/v2/top-headlines"
API_KEY = "2f1b877218e84eeaa5c47eef5680e77c"

parameters = {
    "country": "us",
    "apiKey": API_KEY
}

response = requests.get(NEWS_API_ENDPOINT, params=parameters)

if response.status_code == 200:
    articles = response.json()["articles"]
    news_data = {"last_updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "news": []}

    for article in articles:
        news_data["news"].append({
            "title": article['title'],
            "description": article['description'],
            "url": article['url']
        })

    with open("latest_news.json", "w") as json_file:
        json.dump(news_data, json_file, indent=4)
        
    print("Latest news has been written to latest_news.json.")
else:
    print("Failed to fetch news. Status code:", response.status_code)
