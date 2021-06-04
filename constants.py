from selenium.webdriver.common.by import By


class Constants:
    BINARY_LOCATION = 'C:\\Program Files\\Google\\Chrome\\Application\\new_chrome.exe'
    USERNAME = "username@gmail.com"
    PASSWORD = "password"
    CARD_TYPE = "Birthday Party Animals"
    RECEPIENT = 'recepient@gmail.com'
    SENDER = 'Rodney'
    CARD_MESSAGE = 'From Me to You'
    CARD_AMOUNT = '77'


class CaseLocators:
    SIGN_IN_BUTTON = (By.ID, 'a-autoid-0-announce')
    SIGN_IN_EMAIL = (By.ID, 'ap_email')
    SIGN_IN_CONTINUE_BUTTON = (By.ID, 'continue')
    SIGN_IN_PASSWORD = (By.ID, 'ap_password')
    SIGN_IN_SUBMIT = (By.ID, 'signInSubmit')
    SIGN_IN_SKIP_PHONE = (By.ID, 'ap-account-fixup-phone-skip-link')
    SIGN_IN_GREETING = (By.ID, 'nav-link-accountList-nav-line-1')

    GIFT_CARDS_ALL = (By.XPATH, '//*[@id="nav-xshop"]/a[text()[contains(.,"Gift Cards")]]')
    GIFT_EGIFT_CATEGORY = (By.ID, 'a-autoid-0-announce')
    GIFT_CARDS_BIRTHDAY = (By.XPATH, '//a[@aria-label="Birthday Gift Cards"]')
    CARD_BIRTHDAY_CARD = (By.XPATH, '//*[@id="search"]//div[@data-index="0"]')
    CARD_STANDARD_DESIGN = (By.XPATH, '//*[@id="gc-design-mini-picker-customizationTypes"]//'
                                      'button[@id="gc-customization-type-button-Designs"]')
    CARD_DESIGN_MORE = (By.ID, 'gc-detail-design-more-link')
    CARD_PARTY_ANIMALS_DESIGN = (By.XPATH, f'//*[@id="gc-picker-designs"]//'
                                           f'span[contains(@data-gc-picker-highlight-design,"{Constants.CARD_TYPE}")]')
    CARD_USE_THAT_BUTTON = (By.ID, 'gc-picker-use-this-design')
    CARD_GIFT_AMOUNT = (By.XPATH, '//*[@id="gc-amount-mini-picker-wrapper"]//*[@id="gc-order-form-custom-amount"]')
    CARD_DELIVERY_MECHANISM = (By.ID, 'gc-delivery-mechanism-button-Email')
    CARD_RECEPIENT = (By.XPATH, '//*[@id="gc-recipient-field"]//textarea')
    CARD_SENDER = (By.XPATH, '//*[@id="gc-order-form-senderName"][@value]')
    CARD_MESSAGE = (By.ID, 'gc-order-form-message')
    CARD_ADD_TO_CARD = (By.ID, 'gc-buy-box-atc')
    CARD_TO_CHECKOUT = (By.ID, 'hlb-ptc-btn-native')

    ORDER_CLICK_TO_PAY = (By.ID, 'placeYourOrder')
    ORDER_MESSAGE = (By.XPATH, '//*[@id="spc-orders"]//span/'
                               'strong[text()[contains(.,"Message:")]]/following::span')
    ORDER_SENDER = (By.XPATH, '//*[@id="spc-orders"]//span/strong[text()[contains(.,"From:")]]/following::span')
    ORDER_RECEPIENT = (By.XPATH, '//*[@id="spc-orders"]//span/'
                                 'strong[text()[contains(.,"Send to:")]]/following::span')
    ORDER_TOTAL = (By.XPATH, '//*[@id="subtotals-transactional-table"]//'
                             'span[text()[contains(.,"Order total:")]]/following::td')
    ORDER_CARD_TYPE = (By.XPATH, f'//*[@id="spc-orders"]//div/strong'
                                 f'[text()[contains(.,"Amazon eGift Card - {Constants.CARD_TYPE}")]]')
