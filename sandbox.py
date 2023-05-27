from bs4 import BeautifulSoup
import requests

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36"
}

html_content = requests.get('https://books.toscrape.com', headers=HEADERS).content.decode('utf-8')
soup = BeautifulSoup(html_content, 'lxml')

book_elements = soup.find_all('li', class_='col-xs-6 col-sm-4 col-md-3 col-lg-3')

for book in book_elements:
    title = book.find('h3').find('a')['title']
    price = book.find('div', class_='product_price').find('p').text.strip()
    print(title)
    print(price)
    print('-----')


