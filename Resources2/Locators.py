from selenium.webdriver.common import by
from selenium.webdriver.common.by import By

class Locators():

    # ---- Home Page Locators. ----

    LOGIN_SCREEN = (By.ID, "nav-link-accountList")

    # ---- Login Page Locators. ----

    EMAIL = (By.ID, 'ap_email')
    PASS_EMAIL = (By.ID, 'continue')
    PASSWORD = (By.ID, 'ap_password')
    PASS_PASSWORD = (By.ID, 'signInSubmit')  

    # ---- Search Page Locators. ----

    SEARCH_BOX = (By.ID, 'twotabsearchtextbox')
    SEARCH_BUTTON = (By.ID, 'nav-search-submit-button')
    SEARCH_RESULTS = (By.CLASS_NAME, ".s-include-content-margin.s-latency-cf-section")
    
    # ---- Category Page Locators. ----
    
    PAGES = (By.CLASS_NAME ,'a-normal') # There will be more than 1 class with this name so. It should be a list.
    PRODUCT_THIRD = (By.CLASS_NAME, ".s-result-item.s-asin") # [2] will be  chosen
    PRODUCT_LIST = (By.XPATH, "//span[@class='a-size-medium.a-color-base']") # product lists on category page. need to get their text version.

    # ---- Product Page Locators. ----

    ADD_TO_LIST = (By.ID, "wishlistButtonStack")
    VIEW_YOUR_LIST = (By.ID, "WLHUC_viewlist")

    # ---- WishList Page Locators. ----

    PRODUCT_TITLE_PP = (By.ID, 'productTitle')
    CART_PRODUCT_LIST = (By.CLASS_NAME, 'g-item-sortable')[0]
    DELETE_ITEM = (By.NAME, 'submit.deleteItem')
    ITERATION = 0