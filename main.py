import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://quotes.toscrape.com/'

r = requests.get(url)

soup = BeautifulSoup(r.text, 'html.parser')

quotes = soup.find_all('div', class_="quote")

quotes_data = []

for quote in quotes:
    contents = quote.find('span', class_="text").text
    sayer = quote.find('small', class_="author").text
    tags = quote.find_all('div', class_="tags")

    for tag in tags:
        all_tags = tag.find("a", class_="tag").text

    quote_data = {
        "Author": sayer,
        "Quote": contents,
        "Tags": all_tags
    }

    quotes_data.append(quote_data)

data = pd.DataFrame(quotes_data)
data.to_csv(r'F:\SCRAPPPPY\QUOTES_SCRAPE\quotes.csv')
