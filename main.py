# Importing neeccessary librariesrequests for making HTTP requests, BeautifulSoup for parsing HTML, and pandas for data manipulation and analysis
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Assigning the URL of the website we want to scrape to the variable "url"
url = 'https://quotes.toscrape.com/'

# Sending an HTTP GET request to the specified URL and storeing the response in the variable r.
r = requests.get(url)

soup = BeautifulSoup(r.text, 'html.parser')

# Using find_all method to find all the 'div' tags with the class 'quote' on the page
quotes = soup.find_all('div', class_="quote")

# Creating an empty list called "quotes_data" to store the scraped data.
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

# Creating a pandas DataFrame called data from the quotes_data list.
data = pd.DataFrame(quotes_data)

# Savng the DataFrame in a CSV file named as "quotes.csv"
data.to_csv(r'F:\SCRAPPPPY\QUOTES_SCRAPE\quotes.csv')
