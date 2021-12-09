import requests

from pages.all_books_page import Catalogue

page_content = requests.get('http://books.toscrape.com').content
page = Catalogue(page_content)

books = page.books

for book in books:
    print(book)

for page_num in range(1, 50):
    website = f"http://books.toscrape.com/catalogue/page-{page_num+1}.html"
    page_content = requests.get(website).content
    page = Catalogue(page_content)
    books.extend(page.books)
