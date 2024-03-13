from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
try:
    html = urlopen('https://webscraper.io/test-sites/e-commerce/allinone')
except HTTPError as e:
    print(e)
except URLError as e:
    print('The server could not be found!')
else:
    bs = BeautifulSoup(html, 'lxml')
    prices = bs.find_all('h4', class_ = "price")
    desc = bs.find_all('p', class_="description card-text")
    names = bs.find_all('a', class_ = "title")
    reviews = bs.find_all('p' , class_ = "review-count")
    with open('scraped_data.txt', 'w') as scr:
        i = 0
        j = 0
        k = 0
        m = 0
        while i < len(names) and j < len(prices) and k < len(desc) and m < len(reviews):
            scr.write(f"Name:{names[i].get_text()}\n")
            
            scr.write(f"Price: {prices[j].get_text()}\n")
            scr.write(f"Description:{desc[k].get_text()}\n")
            scr.write(f"Review count: {reviews[m].get_text()}\n")
            i += 1
            j+= 1
            k += 1
            m += 1
