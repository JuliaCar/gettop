from selenium.webdriver.common.by import By
from gettop.pages.base_page import Page
from time import sleep


class Product(Page):
    ADD_TO_CART_BTN = (By.NAME, 'add-to-cart')
    PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price.product-page-price.price-on-sale")
    PRODUCT_DESCRIPTION = (By.CSS_SELECTOR, "div.product-short-description")
    PRODUCT_NAME = (By.CSS_SELECTOR, "h1.product-title.product_title.entry-title")
    PRODUCT_IMAGE = (By.CSS_SELECTOR, "img.wp-post-image.skip-lazy")
    PRODUCT_IMAGE_ZOOM = (By.CSS_SELECTOR, "img.pswp__img")
    PRODUCT_IMAGE_ZOOM_CLOSE = (By.CSS_SELECTOR, "button.pswp__button.pswp__button--close")
    IMAGE_ZOOM_RIGHT_ARROW = (By.CSS_SELECTOR, "button.pswp__button--arrow--right")
    IMAGE_ZOOM_LEFT_ARROW = (By.CSS_SELECTOR, "button.pswp__button--arrow--left")
    IMAGE_HEART_ICON = (By.CSS_SELECTOR, "i.icon-heart")
    HOME_CATEGORY_PRODUCT_LINK = (By.CSS_SELECTOR, "nav.woocommerce-breadcrumb.breadcrumbs.uppercase a")
    NOTIFICATION_NO_PRODUCT = (By.CSS_SELECTOR, "p.woocommerce-info")
    HEADER_CATEGORY_PAGE = (By.CSS_SELECTOR, "nav.woocommerce-breadcrumb.breadcrumbs.uppercase")
    HEADER_CHECKOUT_PAGE = (By.CSS_SELECTOR, "a.current")
    LOGOS = (By.CSS_SELECTOR, "div.social-icons.share-icons.share-row.relative i")
    PRODUCT_SUMMERY = (By.CSS_SELECTOR, "div.product-info.summary.col-fit.col.entry-summary.product-summary")

    def open_product_page(self, product_id):
        self.open_page(f'product/{product_id}/')

    def add_product_to_cart(self):
        self.click(*self.ADD_TO_CART_BTN)

    # product
    def product_name_price_description(self):
        self.find_element(*self.PRODUCT_NAME)
        self.find_element(*self.PRODUCT_PRICE)
        self.find_element(*self.PRODUCT_DESCRIPTION)

    def zoom_in_image(self):
        self.click(*self.PRODUCT_IMAGE)

    def scroll_zoom_images(self):
        e = self.find_elements(*self.PRODUCT_IMAGE_ZOOM)
        # print(len(e))
        for i in range(len(e)+1):
            self.click(*self.IMAGE_ZOOM_RIGHT_ARROW)

    def click_home_link(self, text_link):
        self.click(*self.HOME_CATEGORY_PRODUCT_LINK)

    def click_category_link(self):
        e = self.find_elements(*self.HOME_CATEGORY_PRODUCT_LINK)
        e[1].click()

    def click_heart_icon(self):
        self.click(*self.IMAGE_HEART_ICON)

    def close_zoom_images(self):
        self.click(*self.PRODUCT_IMAGE_ZOOM_CLOSE)

    def hover_over_product_image(self):
        product_image = self.find_element(*self.PRODUCT_IMAGE)
        self.actions.move_to_element(product_image)
        self.actions.perform()

    def logos_present(self, logos):
        logos_icons = self.find_elements(*self.LOGOS)
        print(len(logos_icons))
        for i in range(len(logos_icons)):
            print(logos_icons[i].text)

        # latest on sale
    def price_description_shown(self):
        self.find_element(*self.PRODUCT_PRICE)
        self.find_element(*self.PRODUCT_DESCRIPTION)

    # search
    def open_correct_product_page(self, product_name: str):
        product_name_header = self.find_element(*self.PRODUCT_NAME).text
        assert product_name in product_name_header, f'Incorrect header: {product_name_header}'

    def notification_no_product(self, notification_no_product: str):
        no_product_sign = self.find_element(*self.NOTIFICATION_NO_PRODUCT).text
        assert notification_no_product in no_product_sign, f'Incorrect header: {no_product_sign}'

    # product_categories
    def open_correct_category_page(self, category_name):
        header_category_page = self.find_element(*self.HEADER_CATEGORY_PAGE).text
        assert category_name in header_category_page,\
            f'Incorrect header: {header_category_page}, waiting for {category_name}'

    # cart
    def verify_checkout_page(self, correct_page):
        self.verify_text(correct_page, *self.HEADER_CHECKOUT_PAGE)

    # old
    # def verify_size_tooltip(self):
    #     self.wait_for_element_appear(*self.SIZE_SELECTION_TOOLTIP)
    #