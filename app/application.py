from gettop.pages.base_page import Page
from gettop.pages.top_nav_menu_page import TopNavMenu
from gettop.pages.shopping_cart_page import ShoppingCart
from gettop.pages.product_page import Product
from gettop.pages.home_page import Home
from gettop.pages.footer_page import Footer

# from gettop.pages.search_result_page import SearchResults
# from pages.sign_in_page import SignInPage
# from python_selenium_automation.pages.sign_into_account_page import SignIntoAccount


class Application:

    def __init__(self, driver):
        self.driver = driver
        self.page = Page(self.driver)
        self.top_nav_menu_page = TopNavMenu(self.driver)
        self.shopping_cart_page = ShoppingCart(self.driver)
        self.product_page = Product(self.driver)
        self.home_page = Home(self.driver)
        self.footer_page = Footer(self.driver)
        # self.sign_in_page = SignInPage(self.driver)
        # self.hamburger_menu_page = HamburgerMenu(self.driver)
        # #self.sign_into_account = SignIntoAccount(self.driver)

