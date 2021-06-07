import os
import unittest
from selenium import webdriver
from pages import *


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
        self.pages = LoginPage(self.driver)

    def tearDown(self):
        self.driver.close()

    def get_driver(self):
        options = webdriver.ChromeOptions()
        options.binary_location = Constants.BINARY_LOCATION
        options.add_argument("start-maximized")
        driver = webdriver.Chrome(
            executable_path=os.getcwd() + '\chromedriver.exe',
            options=options
        )
        return driver

    def test_login_purchase_gift_card(self):
        login_page = LoginPage(self.driver)
        login_success_message = login_page.login()
        assert login_success_message == f'Hello, {Constants.SENDER}'
        assert self.driver.current_url == 'https://www.amazon.com/ref=gw_sgn_ib?'

        login_page.choose_purchase_category()

        gift_card_page = GiftCardPage(self.driver)
        gift_card_page.specify_gift_card()

        order_page = OrderPage(self.driver)
        assert order_page.review_your_order() == (
            True,
            Constants.CARD_MESSAGE,
            Constants.SENDER,
            Constants.RECEPIENT,
            f'USD {format(float(Constants.CARD_AMOUNT), ".2f")}',
            f'Amazon eGift Card - {Constants.CARD_TYPE}'
        )


if __name__ == "__main__":
    unittest.main()
