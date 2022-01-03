from Pages2.BasePage import BasePage
from Resources2.Locators import Locators
from Resources2.TestData import TestData

class CategoryPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)        

    def clicked_to_the_second(self):
        self.click(*Locators.PAGES)[1]

    def third_product_select(self):
        self.click(*Locators.PRODUCT_THIRD)[2].click()
        
        