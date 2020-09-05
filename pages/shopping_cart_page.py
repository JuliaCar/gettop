from selenium.webdriver.common.by import By
from .base_page import Page

class ShoppingCart(Page):
    CART_EMPTY = (By.CSS_SELECTOR, "p.cart-empty.woocommerce-info")

    def verify_cart_empty_text(self, search_word: str):
        search_result_header = self.find_element(*self.CART_EMPTY).text
        assert search_word in search_result_header, f'Incorrect header: {search_result_header}'