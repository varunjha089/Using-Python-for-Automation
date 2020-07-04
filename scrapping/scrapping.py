import requests
from bs4 import BeautifulSoup

URL = "http://quotes.toscrape.com/"

# Generating get request
RESPONSE = requests.get(URL)
# scrapping the site
SOUP = BeautifulSoup(RESPONSE.text, 'lxml')
# printing the soup
# print(SOUP)

# just searching for quotes
QUOTES = SOUP.find_all('span', class_='text')
# print(QUOTES)

# searching for author of the quotes
AUTHOR = SOUP.find_all('small', class_='author')

# searching for tags
TAGS = SOUP.find_all('div', class_='tags')

# looping through each
for i in range(0, len(QUOTES)):
    print(QUOTES[i].text)
    print(AUTHOR[i].text)
    QUOTE_TAG = TAGS[i].find_all('a', class_='tag')
    for tag in QUOTE_TAG:
        print(tag.text)
    print('')
    print('')
