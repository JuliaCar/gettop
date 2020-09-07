from selenium.webdriver.common.by import By
from .base_page import Page

class ShoppingCart(Page):
    CART_EMPTY = (By.CSS_SELECTOR, "p.cart-empty.woocommerce-info")

    def verify_cart_empty_text(self, search_word):
        self.verify_text(search_word, *self.CART_EMPTY)



