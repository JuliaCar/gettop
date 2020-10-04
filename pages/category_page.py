from selenium.webdriver.common.by import By
from pages.base_page import Page


class Category(Page):
    ITEMS_CATEGORY = (By.CSS_SELECTOR, "p.category.uppercase.is-smaller.no-text-overflow.product-cat.op-7")
    RESULTS_SHOWN_TEXT = (By.CSS_SELECTOR, "p.woocommerce-result-count.hide-for-medium")
    PRODUCTS_PRESENT = (By.CSS_SELECTOR, "div.box-text.box-text-products")
    ITEMS_NAME = (By.CSS_SELECTOR, "p.name.product-title")
    ITEMS_PRICE = (By.CSS_SELECTOR, "span.price")
    PRODUCT_IMAGE = (By.CSS_SELECTOR, "img.show-on-hover.absolute.fill.hide-for-small.back-image")
    QUICK_VIEW_BTN_OPEN = (By.CSS_SELECTOR, "a.quick-view.quick-view-added")
    QUICK_VIEW_BTN_CLOSE = (By.CSS_SELECTOR,)
    ADD_CART_BTN_QUICK_VIEW = (By.NAME, "add-to-cart")

    def open_category_page(self, category):
        self.open_page(f'product-category/{category}/')

    def correct_category_items_shown(self, category_name):
        category_items_shown = self.find_elements(*self.ITEMS_CATEGORY)
        print(len(category_items_shown))
        for i in range(len(category_items_shown)):
            assert category_name.upper() in category_items_shown[i].text, \
                f'Expected {category_name.upper()}, but got {category_items_shown[i].text}'

    def shown_results_text_present(self, shown_results_text):
        self.verify_text(shown_results_text, *self.RESULTS_SHOWN_TEXT)

    def correct_amount_items_present(self, amount):
        items = self.find_elements(*self.PRODUCTS_PRESENT)
        counter = 0
        for i in range(len(items)):
            counter += 1
        assert int(amount) == counter, f'Expected {amount} items are shown, but got {counter}'
        assert int(amount) == len(items), f'Expected {amount} items are shown, but got {len(items)}'

    def items_category_name_price(self):
        items = self.find_elements(*self.PRODUCTS_PRESENT)
        for i in range(len(items)):
            assert items[i].find_element(*self.ITEMS_CATEGORY), f"Expected item to have category"
            assert items[i].find_element(*self.ITEMS_NAME), f"Expected item to have product name"
            assert items[i].find_element(*self.ITEMS_PRICE), f"Expected item to have product price"

    def user_open_quick_view(self):
        product = self.find_element(*self.PRODUCT_IMAGE)
        self.actions.move_to_element(product)
        self.actions.perform()
        self.click(*self.QUICK_VIEW_BTN_OPEN)

    def add_product_cart_quck_view(self):
        self.click(*self.ADD_CART_BTN_QUICK_VIEW)
