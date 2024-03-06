import requests
import re

def fetch_wiki(title):
    url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{title}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        text = data.get('extract', '')
        text = re.sub('<[^<]+?>', '', text)
        text = re.sub('&[a-z]+;', '', text)
        return text

def result():
    title = input("Enter the title of the Wikipedia page: ")
    text = fetch_wiki(title)
    if text:
        print(text)
    else:
        raise Exception("Failed to fetch Wikipedia page.")

if __name__ == "__main__":
    result()