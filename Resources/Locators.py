from selenium.webdriver.common import by
from selenium.webdriver.common.by import By

import sys
sys.path.insert(0, 'AmazonwithPython_2_POM\Resources')


class Locators():
    # HOME PAGE Locators
    SEARCH_TEXT_BOX = (By.ID, "twotabsearchtextbox")
    SEARCH_SUBMIT_BUTTON = (By.CLASS_NAME, "nav-search-submit")

    # CATEGORY PAGE Locators
    PRODUCT_CLICK = (By.CLASS_NAME, "aok-relative") # [1] Should be taken.

    # PRODUCT PAGE Locators
    ADD_TO_LIST_BUTTON = (By.ID, "wishlistButtonStack")
    GO_TO_CART_PAGE = (By.ID, "nav-cart")
    
    # SUB CART PAGE Locators
    SUB_CART_DIV = (By.ID,"hlb-subcart")
    PROCEED_TO_BUY_BUTTON = (By.ID,"hlb-ptc-btn-native")
    CART_COUNT = (By.ID,"nav-cart-count")
    CART_LINK = (By.ID,"nav-cart")

    # --- Cart Page Locators ---
    DELETE_ITEM_LINK = (By.XPATH,"//div[contains(@class,'a-row sc-action-links')]//span[contains(@class,'sc-action-delete')]")
    CART_COUNT = (By.ID,'nav-cart-count')
    PROCEED_TO_CHECKOUT_BUTTON = (By.NAME,"proceedToCheckout")
    DELETE_BUTTON = (By.CLASS_NAME, "sc-action-delete")

    # --- Signin Page Locators ---
    USER_EMAIL_OR_MOBIL_NO_TEXTBOX = (By.ID,"ap_email")
    USER_LOGIN_BUTTON = (By.ID,"continue")
    USER_PASSWORD = (By.ID,"ap_password")
    USER_PASSWORD_BUTTON = (By.ID, "signInSubmit")

    # --- PopUp AddtoList ---
    VALIDATION_VIEW_LIST = (By.ID, "WLHUC_viewlist")

    






