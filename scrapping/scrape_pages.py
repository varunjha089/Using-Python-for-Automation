"""
    https://scrapingclub.com/
"""
from bs4 import BeautifulSoup
import requests

URL = 'https://scrapingclub.com/exercise/list_basic/?page=1'

# generating a 'get' request
RESPONSE = requests.get(URL)

# making soup
SOUP = BeautifulSoup(RESPONSE.text, 'lxml')

PAGES = SOUP.find('ul', class_='pagination')
URLS = []
LINKS = PAGES.find_all('a', class_='page-link')
for link in LINKS:
    pageNum = int(link.text) if link.text.isdigit() else None
    if pageNum is not None:
        x = link.get('href')
        URLS.append(x)
# print(URLS)
count = 1
for i in URLS:
    newUrl = URL + i
    RESPONSE = requests.get(newUrl)
    # making soup
    SOUP = BeautifulSoup(RESPONSE.text, 'lxml')

    # searching for item
    ITEM = SOUP.find_all('div', class_='col-lg-4 col-md-6 mb-4')

    for j in ITEM:
        itemName = j.find('h4', class_='card-title').text.strip('\n')
        itemPrice = j.find('h5').text

        print("%s ) Price: %s, Item Name: %s" % (count, itemPrice, itemName))
        count += 1
