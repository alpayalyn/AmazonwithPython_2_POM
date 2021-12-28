from Pages.BasePage import BasePage
from Resources.Locators import Locators
from Resources.TestData import TestData


class SubCartPage(BasePage):
    """Sub Cart Page on Amazon India"""
    def __init__(self,driver):
        super().__init__(driver)

    def click_cart_link(self):
        self.click(Locators.CART_LINK)