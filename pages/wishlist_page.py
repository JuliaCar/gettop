from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep

class Wishlist(Page):
    PRODUCT_NAME = (By.CSS_SELECTOR, "td.product-name")
    PRODUCT_IMAGE = (By.CSS_SELECTOR, "td.product-thumbnail")
    SECOND_PRODUCT_ADD = (By.CSS_SELECTOR, "span.product-title")
    PIC = (By.CSS_SELECTOR, "img.wp-post-image.skip-lazy")
    HEART_ICON = (By.CSS_SELECTOR, "i.icon-heart")
    SOCIAL_LOGOS = (By.CSS_SELECTOR, "div.social-icons.share-icons a")
    REMOVE_ITEM = (By.CSS_SELECTOR, "a.remove_from_wishlist")
    EMPTY_WISHLIST = (By.CSS_SELECTOR, "td.wishlist-empty")
    MSG_PRODUCT_REMOVED = (By.CSS_SELECTOR, "div.message-container.container.success-color")
    PRODUCT_PAGE_NAME = (By.CSS_SELECTOR, "h1.product-title")


    def user_see_correct_product_name(self, product):
        self.verify_text(product, *self.PRODUCT_NAME)

    def another_product_page(self):
        product = self.find_elements(*self.SECOND_PRODUCT_ADD)[5]
        product.click()

    def click_heart_icon(self):
        heart_icon = self.find_element(*self.HEART_ICON)
        actions = ActionChains(self.driver)
        actions.move_to_element(heart_icon)
        actions.perform()
        self.click(*self.HEART_ICON)

    def wishlist_social_logos_present(self, amount_logos):
        logos = self.find_elements(*self.SOCIAL_LOGOS)
        assert int(amount_logos) == len(logos)

    def delete_item_wishlist(self):
        self.click(*self.REMOVE_ITEM)
        sleep(5)

    def no_item_wishlist_text(self, no_item_wishlist):
        self.verify_text(no_item_wishlist, *self.EMPTY_WISHLIST)

    def wishlist_successfully_removed_msg(self, msg_product_removed):
        self.verify_text(msg_product_removed, *self.MSG_PRODUCT_REMOVED)

    def wishlist_click_item(self):
        self.click(*self.PRODUCT_IMAGE)

    def wishlist_correct_product_page(self, name_of_product):
        self.wait_for_element_appear(*self.PRODUCT_PAGE_NAME)
        self.verify_text(name_of_product,*self.PRODUCT_PAGE_NAME)
