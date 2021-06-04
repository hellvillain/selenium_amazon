import os
import unittest
from selenium import webdriver
from constants import Constants
from pages import Pages


class Case(unittest.TestCase):
    """
       Test actions:
       - login to main page https://amazon.com/
       - choose a card gift
       - specify parameters of the card gift
       - check an order review
    """
    def setUp(self):
        self.driver = self.get_driver()
        self.driver.get('https://amazon.com')
        self.pages = Pages(self.driver)

    def tearDown(self):
        self.driver.close()

    def get_driver(self):
        options = webdriver.ChromeOptions()
        options.binary_location = Constants.BINARY_LOCATION
        driver = webdriver.Chrome(
            executable_path=os.getcwd() + '\chromedriver.exe',
            options=options
        )
        return driver

    def test_login_purchase_gift_card(self):
        login_success_message = self.pages.login()
        assert login_success_message == f'Hello, {Constants.SENDER}'

        self.pages.choose_purchase_category()
        self.pages.specify_gift_card()
        assert self.pages.review_your_order() == (
            True,
            Constants.CARD_MESSAGE,
            Constants.SENDER,
            Constants.RECEPIENT,
            f'USD {format(float(Constants.CARD_AMOUNT), ".2f")}',
            f'Amazon eGift Card - {Constants.CARD_TYPE}'
        )


if __name__ == "__main__":
    unittest.main()
