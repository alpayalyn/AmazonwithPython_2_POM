from Pages.BasePage import BasePage
from Resources.Locators import Locators
from Resources.TestData import TestData
import time

class CartPage(BasePage):
    """Cart Page on Amazon India"""
    def __init__(self,driver):
        super().__init__(driver)
    
    def delete_item(self):
        cartCount=int(self.driver.find_element(*Locators.CART_COUNT).text)
        # print ("Cart Count is"+ str(cartCount))
        if(cartCount<1):
            print("Cart is empty")
            exit()
        if(self.driver.title.startswith("Amazon.in Shopping Cart")):
            #to delete an item from the Cart
            self.click(Locators.DELETE_ITEM_LINK)
            time.sleep(2)        
    
    def click_proceed_to_checkout_button(self):
        self.click(Locators.PROCEED_TO_CHECKOUT_BUTTON) 