import requests

from pages.all_books_page import Catalogue

page_content = requests.get('http://books.toscrape.com').content
page = Catalogue(page_content)

books = page.books

for book in books:
    print(book)
