from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.base_page import Page
from time import sleep

class Home(Page):

    LEFT_ARROW = (By.CSS_SELECTOR, "button.flickity-button.flickity-prev-next-button.previous")
    RIGHT_ARROW = (By.CSS_SELECTOR, "button.flickity-button.flickity-prev-next-button.next")
    LEFT_DOT = (By.CSS_SELECTOR, "li.dot")
    RIGHT_DOT = (By.CSS_SELECTOR, "li.dot.is-selected")
    BANNER = (By.CSS_SELECTOR, "div.fill.banner-link")
    HEADER_PRODUCT_PAGE = (By.CSS_SELECTOR, "nav.woocommerce-breadcrumb.breadcrumbs.uppercase")
    LATEST_SALES_HEADER = (By.XPATH, "//*[contains(text(), 'Latest products on sale')]")
    PRODUCTS_ON_SALE = (By.CSS_SELECTOR, "div.product-small.box")
    PRODUCTS_ON_SALE_IMAGE = (By.CSS_SELECTOR, "div.image-fade_in_back")
    PRODUCTS_ON_SALE_PRICE = (By.CSS_SELECTOR, "span.price")
    PRODUCTS_ON_SALE_ICON_SALE = (By.CSS_SELECTOR, "div.badge-inner.secondary.on-sale")
    PRODUCTS_ON_SALE_HEART_ICON = (By.CSS_SELECTOR, "i.icon-heart")
    PRODUCTS_ON_SALE_CATEGORY = (By.CSS_SELECTOR, "p.category.uppercase.is-smaller.no-text-overflow.product-cat.op-7")
    PRODUCTS_ON_SALE_NAME = (By.CSS_SELECTOR, "p.name.product-title")
    PRODUCTS_ON_SALE_RATING = (By.CSS_SELECTOR, "div.star-rating span")
    MESSAGE_ADDED_WISHLIST = (By.ID, "#yith-wcwl-popup-message")
    QUICK_VIEW_OPEN = (By.CSS_SELECTOR, "a.quick-view.quick-view-added")
    QUICK_VIEW_CLOSE = (By.CSS_SELECTOR, "button.mfp-close")
    QUICK_VIEW_IMAGES = (By.CSS_SELECTOR, "div.slide")
    QUICK_VIEW_LEFT_ARROW = (By.CSS_SELECTOR, "div.mfp-container.mfp-s-ready.mfp-inline-holder")
    CATEGORIES_TEXT = (By.XPATH, "//*[contains(text(), 'Browse our Categories')]")
    CATEGORIES = (By.CSS_SELECTOR, "h5.uppercase.header-title")
    CATEGORIES_CLICK = (By.CSS_SELECTOR, "div.product-category.col.is-selected")

    def banner_left_dot(self):
        self.wait_for_element_click(*self.LEFT_DOT)

    def banner_right_dot(self):
        self.wait_for_element_click(*self.RIGHT_DOT)

    def banner_left_arrow(self):
        banner_left_arrow = self.find_element(*self.RIGHT_ARROW)
        self.actions.move_to_element(banner_left_arrow)
        self.actions.perform()
        self.click(*self.LEFT_ARROW)

    def banner_right_arrow(self):
        banner_right_arrow = self.find_element(*self.RIGHT_ARROW)
        self.actions.move_to_element(banner_right_arrow)
        self.actions.perform()
        self.click(*self.RIGHT_ARROW)

    def banner_click(self):
        self.click(*self.BANNER)

#latest on sale
    def correct_category_page(self):
        self.verify_text('HOME / IPAD', *self.HEADER_PRODUCT_PAGE)

    def text_is_shown(self, text_shown):
        self.verify_text(text_shown, *self.LATEST_SALES_HEADER)

    def click_heart_icon(self):
        heart_icon = self.find_element(*self.PRODUCTS_ON_SALE_HEART_ICON)
        self.actions.move_to_element(heart_icon)
        self.actions.perform()
        self.click(*self.PRODUCTS_ON_SALE_HEART_ICON)

    def sales_product_all_icons(self):
        all_products = self.find_elements(*self.PRODUCTS_ON_SALE)
        print(len(all_products))
        for item_index in range(len(all_products)):
            print(item_index)
            print(all_products[item_index].text)
            assert all_products[item_index].find_element(*self.PRODUCTS_ON_SALE_IMAGE), f"Expected image"
            assert all_products[item_index].find_element(*self.PRODUCTS_ON_SALE_CATEGORY), f"Expected category"
            assert all_products[item_index].find_element(*self.PRODUCTS_ON_SALE_NAME), f"Expected name"
            assert all_products[item_index].find_element(*self.PRODUCTS_ON_SALE_PRICE), f"Expected price"
            assert all_products[item_index].find_element(*self.PRODUCTS_ON_SALE_HEART_ICON), f"Expected Heart icon"
            ###TODO Lana how to fix the sale icon and heart icon??
            # assert all_products[item_index].find_element(*self.PRODUCTS_ON_SALE_RATING), f"Expected rating, but got {}"
            # assert all_products[item_index].find_element(*self.PRODUCTS_ON_SALE_ICON_SALE), f"Expected Sale icon"

    def open_product_sale(self):
        products_on_sale = self.find_elements(*self.PRODUCTS_ON_SALE)
        products_on_sale[3].click()

    def open_quick_view(self):
        open_quick_view = self.find_element(*self.QUICK_VIEW_OPEN)
        self.actions.move_to_element(open_quick_view)
        self.actions.perform()
        open_quick_view.click()

    def verify_quick_view_open(self):
        self.wait_for_element_appear(*self.PRODUCTS_ON_SALE_IMAGE)

    def close_quick_view(self):
        self.click(*self.QUICK_VIEW_CLOSE)

    def quick_view_click_images(self):
        images = self.find_elements(*self.QUICK_VIEW_IMAGES)
        print(len(images))
        for index in range(len(images)):
            self.click(*self.QUICK_VIEW_LEFT_ARROW)

#browse categories
    def categories_text_shown(self, categories_text_shown):
        self.verify_text(categories_text_shown, *self.CATEGORIES_TEXT)

    def correct_categories_shown(self):
        categories = self.find_elements(*self.CATEGORIES)
        categories_list = ['ACCESSORIES', 'IPAD', 'IPHONE', 'MACBOOK']
        # print(len(categories))
        for index in range(len(categories)):
            # print(categories[index].text)
            assert categories[index].text in categories_list[index],\
                f"Expected {categories_list[index]}, but got {categories[index].text}"
            categories = self.find_elements(*self.CATEGORIES)

    def correct_page_opens(self):
        categories_click = self.find_elements(*self.CATEGORIES_CLICK)
        categories_list = ['ACCESSORIES', 'IPAD', 'IPHONE', 'MACBOOK']
        for index in range(len(categories_click)):
            categories_click[index].click()
            header_name = self.find_element(*self.HEADER_PRODUCT_PAGE)
            # print(header_name.text)
            assert categories_list[index] in header_name.text, f"Expected {categories_list[index]}, but got {header_name.text}"
            self.open_page()
            categories_click = self.find_elements(*self.CATEGORIES_CLICK)

    def click_quick_view_and_add_product_to_cart(self):
        open_quick_view = self.find_elements(*self.PRODUCTS_ON_SALE_IMAGE)
        print(len(open_quick_view))
        for item in range(len(open_quick_view)):
            open_quick_view = self.find_elements(*self.QUICK_VIEW_OPEN)
            open_quick_view_item = open_quick_view.find_element()
            self.actions.move_to_element(open_quick_view_item)
            self.actions.perform()
            open_quick_view.click()
            self.click(*self.QUICK_VIEW_CLOSE)

    def vefiry_home_page(self):
        self.wait_for_element_appear(*self.RIGHT_ARROW)
