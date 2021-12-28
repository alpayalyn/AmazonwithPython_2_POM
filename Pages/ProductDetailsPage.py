from Pages.BasePage import BasePage
from Resources.Locators import Locators
from Resources.TestData import TestData


class ProductDetailsPage(BasePage):
    """Product Details Page for the clicked product on Amazon India"""
    def __init__(self,driver):
        super().__init__(driver)

    def click_add_to_cart_button(self):
        self.click(Locators.ADD_TO_CART_BUTTON)