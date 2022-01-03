from Pages2.BasePage import BasePage
from Resources2.Locators import Locators
from Resources2.TestData import TestData
from time import sleep

class LoginPage(BasePage):
    """Home Page of Amazon"""
    def __init__(self, driver):
        super().__init__(driver)  # Anlamadım.
        self.driver.get(TestData.BASE_URL) # a variable in class can be called by , " . "

    def amazon_login(self):
        """Logging into the account."""
        sleep(2)
        self.enter_text(Locators.EMAIL, TestData.EMAIL_TO_LOGIN)
        self.click(Locators.PASS_EMAIL)
        self.enter_text(Locators.PASSWORD, TestData.PASSWORD_TO_LOGIN)
        self.click(Locators.PASS_PASSWORD)
