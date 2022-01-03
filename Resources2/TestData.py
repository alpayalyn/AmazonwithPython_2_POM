from selenium.webdriver.common import by
from selenium.webdriver.common.by import By

class TestData():
    """Website login page for users to logging in"""

    # ---- Home Page Datas. ----

    CHROME_EXECUTABLE_PATH = "C:/seleniumdriver/chromedriver"
    BASE_URL = "https://www.amazon.com"
    HOMEPAGE_TITLE = "Amazon.com"

    # ---- Login Page Datas. ----

    EMAIL_TO_LOGIN = 'alpaylui78@gmail.com'
    PASSWORD_TO_LOGIN = 'Zemmenilone123'
  
    # ---- Search Page Datas. ----

    TEXT_TO_BE_SEARCHED = 'samsung'
    NO_RESULTS_TEXT = "No results found."




