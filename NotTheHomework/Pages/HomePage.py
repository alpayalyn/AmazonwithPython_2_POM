from Pages.BasePage import BasePage
from Resources.Locators import Locators
from Resources.TestData import TestData


class HomePage(BasePage):
    """Home Page of Amazon"""
    def __init__(self, driver):
        super().__init__(driver)  # Anlamadım.
        self.driver.get(TestData.BASE_URL) # a variable in class can be called by , " . "

    def search(self):
        self.driver.find_element(*Locators.SEARCH_TEXT_BOX).clear() # * Kullanılmasının anlamı, bir classı nasıl direkt çekti. * tuple olarak kullanım olmalı
        self.enter_text(Locators.SEARCH_TEXT_BOX, TestData.SEARCH_TERM)        
        self.click(Locators.SEARCH_SUBMIT_BUTTON)        