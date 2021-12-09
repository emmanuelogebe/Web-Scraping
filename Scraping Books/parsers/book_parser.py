

from locators.book_locators import BookLocators

class BookParser:
    """
    A class to take in an HTML page(or part of it) and find properties of an item in it
    """

    RATINGS = {
        'One': 1,
        'Two': 2,
        'Three': 3,
        'Four': 4,
        'Five': 5
    }

    def __init__(self, parent):
        self.parent = parent

    def __repr__(self):
        return f'A book titled -- {self.name}, has a price of {self.price} and is rated {self.rating} stars.'

    @property
    def name(self):
        locator = BookLocators.NAME_LOCATOR
        item_link = self.parent.select_one(locator)
        item_name = item_link.attrs['title']
        return item_name

    @property
    def link(self):
        locator = BookLocators.LINK_LOCATOR
        item_link = self.parent.select_one(locator).attrs['href']
        return item_link

    @property
    def price(self):
        locator = BookLocators.PRICE_LOCATOR
        item_price = self.parent.select_one(locator).string #$51.45
        
        return item_price
    

    @property
    def rating(self):
        locator = BookLocators.RATING_LOCATOR
        star_rating_tag = self.parent.select_one(locator)
        classes = star_rating_tag.attrs['class'] #['star-rating', 'Three]
        rating_classes = [r for r in classes if r!= 'star-rating']
        rating_number = BookParser.RATINGS.get(rating_classes[0])
        return rating_number
        
