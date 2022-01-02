from Pages.BasePage import BasePage
from Resources.Locators import Locators
from Resources.TestData import TestData


class SearchResultsPage(BasePage):
    """Search Results Page of Amazon India"""
    def __init__(self, driver):
        super().__init__(driver)        

    def click_search_result(self):
        self.click(Locators.PRODUCT_CLICK)

