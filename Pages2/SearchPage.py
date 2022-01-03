from Pages2.BasePage import BasePage
from Resources2.Locators import Locators
from Resources2.TestData import TestData


class SearchResultsPage(BasePage):
    """Search Results Page of Amazon India"""
    def __init__(self, driver):
        super().__init__(driver)        

    def click_search_result(self):
        self.enter_text(Locators.SEARCH_BOX, TestData.TEXT_TO_BE_SEARCHED)
        self.click(Locators.SEARCH_BUTTON)
        

