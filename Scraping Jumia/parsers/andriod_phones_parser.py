import logging

from locators.phone_locators import PhoneLocators

Jumia_Logger = logging.getLogger('Jumia Scraping.andriod_phones_parser')

class PhoneParser:
    def __init__(self, parent):
        Jumia_Logger.debug(f'New phone parser created from `{parent}`')
        self.parent = parent

    def __repr__(self):
        return f"{self.phone_name} with old price {self.phone_old_price} and a current price of {self.phone_current_price} shows a price reduction of {self.phone_percentage_reduction} reduction."

    @property
    def phone_name(self):
        Jumia_Logger.debug('Finding phone name..')
        locator = PhoneLocators.Name_Locator
        Jumia_Logger.debug(f'Found book `{locator}`')
        return locator

    @property
    def phone_old_price(self):
        Jumia_Logger.debug('Finding phone old price..')
        old_price = PhoneLocators.Old_Price_Locator
        Jumia_Logger.debug(f'Found book price {old_price}')
        return old_price

    @property
    def phone_current_price(self):
        Jumia_Logger.debug('Finding current price..')
        current_price = PhoneLocators.Current_Price_Locator
        Jumia_Logger.debug(f'Found current price {current_price}')
        return current_price

    @property
    def phone_percentage_reduction(self):
        Jumia_Logger.debug('Finding phone percentage reduction..')
        percentage_reduction = PhoneLocators.Percentage_Reduction
        Jumia_Logger.debug(f'Found phone percentage reduction {percentage_reduction}%')
        return percentage_reduction
