from pages.base_page import Page
from pages.top_nav_menu_page import TopNavMenu
from pages.shopping_cart_page import ShoppingCart
from pages.product_page import Product
from pages.home_page import Home
from pages.footer_page import Footer
from pages.logos_page import LogosIcon
from pages.description_review_page import DescriptionReview
from pages.category_page import Category
from pages.shop_page import RecentlyViewed
from pages.checkout_page import Checkout
from pages.wishlist_page import Wishlist

class Application:

    def __init__(self, driver):
        self.driver = driver
        self.page = Page(self.driver)
        self.top_nav_menu_page = TopNavMenu(self.driver)
        self.shopping_cart_page = ShoppingCart(self.driver)
        self.product_page = Product(self.driver)
        self.home_page = Home(self.driver)
        self.footer_page = Footer(self.driver)
        self.logos_page = LogosIcon(self.driver)
        self.description_review_page = DescriptionReview(self.driver)
        self.category_page = Category(self.driver)
        self.shop_page = RecentlyViewed(self.driver)
        self.checkout_page = Checkout(self.driver)
        self.wishlist_page = Wishlist(self.driver)
