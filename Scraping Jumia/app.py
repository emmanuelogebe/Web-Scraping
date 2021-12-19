import requests
import logging

from pages.all_phones_page import Meta

logging.basicConfig(format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
                    level=logging.DEBUG,
                    filename='Jumia Project/logs.txt')

Jumia_Logger = logging.getLogger('Jumia Scraping')

Jumia_Logger.info('Loading Page Content...')

page_content = requests.get('https://www.jumia.com.ng/android-phones').content
Jumia_Logger.debug('Creating AllPhonesPage from pages...')

page = Meta(page_content)

phones = page.phones

for phone in phones:
    print(phone)

