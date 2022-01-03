from Pages2.BasePage import BasePage
from Resources2.Locators import Locators
from Resources2.TestData import TestData


class HomePage(BasePage):
    """Home Page of Amazon"""
    def __init__(self, driver):
        super().__init__(driver)  # Anlamadım.
        self.driver.get(TestData.BASE_URL) # a variable in class can be called by , " . "

    def navigating_to_login_page(self):
        self.click(self.LOGIN_SCREEN)   

    