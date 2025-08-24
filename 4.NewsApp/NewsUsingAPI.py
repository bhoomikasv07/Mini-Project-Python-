import requests

q = input("Hey..!!What's Up?? What type of news are you looking for now?")
api = "f7d5a711fbd54e83976ae395a1e4efa7"

url = f"https://newsapi.org/v2/everything?q={q}&from=2025-08-22&to=2025-08-22&sortBy=popularity&apiKey={api}"

print(url)
a = requests.get(url)

data = a.json()
articles = data["articles"]

for index, article in enumerate(articles):
    print(index +1, article["title"])
    print(article["description"])
    print(article["url"])
    print("\n**************************************************\n")