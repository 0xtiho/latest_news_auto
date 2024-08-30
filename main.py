import requests
import json
from datetime import datetime

NEWS_API_ENDPOINT = "https://newsapi.org/v2/top-headlines"
API_KEY = "2f1b877218e84eeaa5c47eef5680e77c"

parameters = {
    "country": "fr",
    "apiKey": API_KEY
}

response = requests.get(NEWS_API_ENDPOINT, params=parameters)

if response.status_code == 200:
    articles = response.json()["articles"]
    news_data = {"last_updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "news": []}

    for article in articles:
        news_data["news"].append({
            "title": article['title'],
            "description": article.get('description', 'No description available'),
            "url": article['url']
        })

    # Write to latest_news.json file
    with open("latest_news.json", "w") as json_file:
        json.dump(news_data, json_file, indent=4)

    # Create a stylish README.md update
    with open("README.md", "w") as readme_file:
        readme_file.write("# 📰 Latest News Updates\n")
        readme_file.write(f"**Last Updated:** {news_data['last_updated']}\n\n")
        readme_file.write("Welcome to the latest news updates fetched automatically by our bot! Stay informed with the top headlines right here. 🚀\n\n")
        readme_file.write("## 🗞️ Top Headlines\n\n")

        for article in news_data["news"][:5]:  # Limiting to top 5 headlines for brevity
            readme_file.write(f"### [{article['title']}]({article['url']})\n")
            readme_file.write(f"{article['description']}\n\n")
        
        readme_file.write("---\n")
        readme_file.write("*(This README is automatically updated every 1 minutes with the latest news.)*\n")

    print("README.md has been updated with the latest news.")
else:
    print("Failed to fetch news. Status code:", response.status_code)
