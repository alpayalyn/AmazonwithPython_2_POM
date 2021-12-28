from Pages.BasePage import BasePage
from Resources.Locators import Locators
from Resources.TestData import TestData


class SignInPage(BasePage):
    """SignIn Page on Amazon India"""
    def __init__(self,driver):
        super().__init__(driver)