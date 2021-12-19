import logging

from bs4 import BeautifulSoup

from locators.all_phones_page import AllPhonesPageLocators
from parsers.andriod_phones_parser import PhoneParser

Jumia_Logger = logging.getLogger('Jumia Scraping.all_phones_page')

class Meta:
    def __init__(self, jumia_andriod_content):
        Jumia_Logger.debug('Parsing page content with Beautiful Soup page content parser...')
        self.soup = BeautifulSoup (jumia_andriod_content, 'html.parser')

    @property
    def phones(self):
        Jumia_Logger.debug(f'Finding all phones in the page using `{AllPhonesPageLocators.PHONES}`.')
        return [PhoneParser(p) for p in self.soup.select(AllPhonesPageLocators.PHONES)]
