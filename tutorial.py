import requests
from bs4 import BeautifulSoup

res = requests.get('http://quotes.toscrape.com/')

soup = BeautifulSoup(res.text, 'html.parser')

title_text = soup.find('title').get_text()
print(title_text)

links = [url.get('href') for url in soup.find_all('a')]
print(links)

quote_elms = soup.find_all('div', {'class': 'quote'})
print(len(quote_elms))
