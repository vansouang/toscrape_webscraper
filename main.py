import requests
from bs4 import BeautifulSoup
import httpx

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36"
}

html_text = requests.get('https://books.toscrape.com', headers=HEADERS).content.decode('utf-8')
#html_text = httpx.get('https://www.indeed.com/jobs?q=python#l=Texas', headers=HEADERS).text

soup = BeautifulSoup(html_text, 'lxml')

book_elements = soup.find_all('li', class_="col-xs-6 col-sm-4 col-md-3 col-lg-3")

for book in book_elements:
    
  title = book.find('h3').find('a')['title']
  price = book.find('div', class_='product_price').find('p').text.strip()

#stock = book.find('div', class_='product_price').find('p', class_='instock availability').text.strip()

  print(f'''
  Book Title: {title}
  Price: {price}
  ''')
