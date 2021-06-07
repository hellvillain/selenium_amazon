import time
import re
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from constants import *


class BasePage:
    """
    Base class to initialize the base page that will be called from all pages.
    Also contains common methods for pages.
    """
    def __init__(self, driver):
        self.driver = driver

    def wait_element(self, locator, method=ec.visibility_of_element_located, time=5):
        """This is used by pages methods to change parameters wait of elements."""
        return WebDriverWait(self.driver, time).until(method(locator), message=f"Element not found: {locator}")


class LoginPage(BasePage):
    def login(self):
        self.driver.find_element(*CaseLocators.SIGN_IN_BUTTON).click()
        self.wait_element(CaseLocators.SIGN_IN_EMAIL).send_keys(Constants.USERNAME)
        self.driver.find_element(*CaseLocators.SIGN_IN_CONTINUE_BUTTON).click()
        self.wait_element(CaseLocators.SIGN_IN_PASSWORD).send_keys(Constants.PASSWORD)
        self.driver.find_element(*CaseLocators.SIGN_IN_SUBMIT).click()
        self.wait_element(CaseLocators.GIFT_CARDS_ALL)
        if not re.findall('.+/', self.driver.current_url)[0] == 'https://www.amazon.com/':
            self.driver.find_element(*CaseLocators.SIGN_IN_SKIP_PHONE).click()
        return self.driver.find_element(*CaseLocators.SIGN_IN_GREETING).text

    def choose_purchase_category(self):
        self.driver.find_element(*CaseLocators.GIFT_CARDS_ALL).click()
        self.driver.find_element(*CaseLocators.GIFT_CARDS_BIRTHDAY).click()
        self.driver.find_element(*CaseLocators.GIFT_EGIFT_CATEGORY).click()
        self.driver.find_element(*CaseLocators.GIFT_BIRTHDAY_CARD).click()
        self.driver.find_element(*CaseLocators.GIFT_STANDARD_DESIGN)


class GiftCardPage(BasePage):
    def specify_gift_card(self):
        self.driver.find_element(*CaseLocators.CARD_DESIGN_MORE).click()
        self.wait_element(CaseLocators.CARD_PARTY_ANIMALS_DESIGN).click()
        self.driver.find_element(*CaseLocators.CARD_USE_THAT_BUTTON).click()
        self.driver.find_element(*CaseLocators.CARD_GIFT_AMOUNT).send_keys(Constants.CARD_AMOUNT)
        self.driver.find_element(*CaseLocators.CARD_DELIVERY_MECHANISM).click()
        self.driver.find_element(*CaseLocators.CARD_RECEPIENT).clear()
        self.driver.find_element(*CaseLocators.CARD_RECEPIENT).send_keys(Constants.RECEPIENT)
        self.driver.find_element(*CaseLocators.CARD_SENDER).clear()
        self.driver.find_element(*CaseLocators.CARD_SENDER).send_keys(Constants.SENDER)
        self.driver.find_element(*CaseLocators.CARD_MESSAGE).clear()
        self.driver.find_element(*CaseLocators.CARD_MESSAGE).send_keys(Constants.CARD_MESSAGE)
        self.driver.find_element(*CaseLocators.CARD_ADD_TO_CARD).click()
        self.driver.find_element(*CaseLocators.CARD_TO_CHECKOUT).click()


class OrderPage(BasePage):
    def review_your_order(self):
        return (
            self.driver.find_element(*CaseLocators.ORDER_CLICK_TO_PAY).is_displayed(),
            self.driver.find_element(*CaseLocators.ORDER_MESSAGE).text,
            self.driver.find_element(*CaseLocators.ORDER_SENDER).text,
            self.driver.find_element(*CaseLocators.ORDER_RECEPIENT).text,
            self.driver.find_element(*CaseLocators.ORDER_TOTAL).text,
            self.driver.find_element(*CaseLocators.ORDER_CARD_TYPE).text
        )
