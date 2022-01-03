from Pages2.BasePage import BasePage
from Resources2.Locators import Locators
from Resources2.TestData import TestData


class ProductPage(BasePage):
    """Product Details Page for the clicked product on Amazon India"""

    def __init__(self,driver):
        super().__init__(driver)

    def click_add_to_cart_button(self):
        self.PRODUCT_NAME = self.wait_for_element(Locators.PRODUCT_TITLE_PP).text()
        self.click(Locators.ADD_TO_LIST)
        self.click(Locators.VIEW_YOUR_LIST)
        self.PRODUCT_NAME_IN_CART = self.wait_for_element(Locators.CART_PRODUCT_LIST).text()
