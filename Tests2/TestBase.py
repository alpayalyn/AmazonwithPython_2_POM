import unittest
from selenium import webdriver
from Resources2 import Locators
from Pages2 import BasePage, CategoryPage, HomePage, LoginPage, ProductPage, SearchPage, WishListPage
from Resources2.TestData import TestData

# Base Class for the tests
class Test_AMZN_Search_Base(unittest.TestCase):

    def setUp(self):
        # Setting up how we want Chrome to run
        chrome_options=webdriver.ChromeOptions()
        # chrome_options.add_argument('headless')
        # chrome_options.add_argument('window-size=1920x1080')
        # print ("Chrome Path:   " + TestData.CHROME_EXECUTABLE_PATH + "  ends here")
        self.driver=webdriver.Chrome(TestData.CHROME_EXECUTABLE_PATH, options=chrome_options)
        #browser should be loaded in maximized window
        self.driver.maximize_window()
    
    def tearDown(self):
        # To do the cleanup after test has executed.
        self.driver.close()
        self.driver.quit()

# Test Class containing all tests
class Test_AMZN_Search(Test_AMZN_Search_Base):
    def setUp(self):
        super().setUp()

    def test_home_page_loaded_successfully(self):
        # instantiate an object of HomePage class. Remember when the constructor of HomePage class is called
        # it opens up the browser and navigates to Home Page of the site under test.
        # 
        self.homePage = HomePage(self.driver)
        # assert if the title of Home Page contains Amazon.in
        self.assertIn(TestData.HOMEPAGE_TITLE, self.homePage.driver.title)

    def test_to_login(self):
        self.loginPage = LoginPage(self.homePage.driver)

    def test_to_search(self):
        self.searchPage=SearchPage(self.loginPage.driver)
        # search for the search term on Home Page. The search term would be picked from
        # test data file
        self.searchPage.click_search_result()
        # instantiate an object of SearchResultsPage class passing in the driver as parameter.
        # this will allow the newly created object to have access to the browser and perform
        # operations further.
        self.categoryPage = CategoryPage(self.searchPage.driver)

    def test_search_results(self):
        # assert if the search term is present in the title of the Amazon's Search Results Page
        self.assertIn(TestData.TEXT_TO_BE_SEARCHED, self.categoryPage.driver.title)
        # assert that the search term indeed return some results.
        self.assertNotIn(TestData.NO_RESULTS_TEXT, self.categoryPage.driver.page_source)

    def test_go_to_second_page_second_product(self):
        # 2.sf mı asserti atılabilir.
        self.categoryPage.clicked_to_the_second()
        self.categoryPage.third_product_select()
    
    def test_add_item_to_cart(self):
        self.productPage = ProductPage(self.categoryPage.driver)
        # click on the Add To Cart button
        self.productPage.click_add_to_cart_button()
        # instantiate an object of Sub Cart Page class
        # assert if the sub cart page has indeed loaded
        self.assertIn(ProductPage.)
        # assert if the product was added to the cart successfully

    def test_user_should_be_able_to_delete_item_from_cart(self):
        self.homePage=HomePage(self.driver)
        self.homePage.search()
        self.searchResultsPage=SearchResultsPage(self.homePage.driver)
        self.searchResultsPage.click_search_result()
        self.searchResultsPage.driver.switch_to_window(self.searchResultsPage.driver.window_handles[1])
        self.productDetailsPage=ProductDetailsPage(self.searchResultsPage.driver)
        self.productDetailsPage.click_add_to_cart_button()
        self.subCartPage=SubCartPage(self.productDetailsPage.driver)
        # click on the Cart's hyperlink to load the cart page
        self.subCartPage.click_cart_link()
         # instantiate an object of Cart Page class
        self.cartPage=WishListPage(self.subCartPage.driver)
        # find the cart count before deleting an item from the cart
        cartCountBeforeDeletion=int(self.driver.find_element(*Locators.CART_COUNT).text)
        # delete an item from cart
        self.cartPage.delete_item()
         #to assert the item was deleted successfully
        self.assertTrue(int(self.driver.find_element(*Locators.CART_COUNT).text) < cartCountBeforeDeletion) 

    def test_user_must_signin_to_checkout(self):
        self.homePage=HomePage(self.driver)
        self.homePage.search()
        self.searchResultsPage=SearchResultsPage(self.homePage.driver)
        self.searchResultsPage.click_search_result()
        self.searchResultsPage.driver.switch_to_window(self.searchResultsPage.driver.window_handles[1])
        self.productDetailsPage=ProductDetailsPage(self.searchResultsPage.driver)
        self.productDetailsPage.click_add_to_cart_button()
        self.subCartPage=SubCartPage(self.productDetailsPage.driver)
        self.subCartPage.click_cart_link()
        # instantiate an object of Cart Page class
        self.cartPage=WishListPage(self.subCartPage.driver)    
        #click on Proceed to Checkout button
        self.cartPage.click_proceed_to_checkout_button()
        # instantiate an object of SignIn Page class
        self.signInPage=SignInPage(self.cartPage.driver)
        # to assert we are in indeed on Sign In Page, first we assert the title of the page
        self.assertTrue(TestData.SIGN_IN_PAGE_TITLE,self.signInPage.driver.title)
        # and then we assert for presence of email textbox on the page
        self.assertTrue(self.signInPage.is_visible(Locators.USER_EMAIL_OR_MOBIL_NO_TEXTBOX))

if __name__ == '__main__':
    # specify path where the HTML reports for testcase execution are to be generated
    unittest.main()