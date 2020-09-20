from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep

class Wishlist(Page):
    PRODUCT_NAME = (By.CSS_SELECTOR, "td.product-name")
    PHONE_CATEGORY = (By.ID, "#menu-item-469")
    PHONE = (By.ID, "menu-item-469")

    def user_see_correct_product_name(self, product):
        self.verify_text(product, *self.PRODUCT_NAME)

    def another_product_page(self):
        self.click(*self.PHONE_CATEGORY)



