from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep


class Product(Page):
    ADD_TO_CART_BTN = (By.NAME, 'add-to-cart')
    PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price.product-page-price ")
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
    PRODUCT_SUMMERY = (By.CSS_SELECTOR, "div.product-info.summary.col-fit.col.entry-summary.product-summary")
    MESSAGE_ADDED_CART = (By.CSS_SELECTOR, "div.message-container.container.success-color.medium-text-center a")
    PLUS_TO_CART = (By.CSS_SELECTOR, "input.plus.button.is-form")
    MINUS_TO_CART = (By.CSS_SELECTOR, "input.minus.button.is-form")
    AMOUNT_INPUT_WINDOW = (By.CSS_SELECTOR, "input[type='number']")
    OUT_OF_STOCK = (By.CSS_SELECTOR, "p.stock.out-of-stock")
    IMAGE_RIGHT_ARROW = (By.CSS_SELECTOR, "button.flickity-button.flickity-prev-next-button.next")
    IMAGE_LEFT_ARROW = (By.CSS_SELECTOR, "button.flickity-button.flickity-prev-next-button.previous")
    YOU_MAY_ALSO_LIKE = (By.CSS_SELECTOR, "h3.widget-title.shop-sidebar")
    PRODUCT_TITLES = (By.CSS_SELECTOR, "#product-sidebar .product-title")
    PRODUCT_1 = (By.CSS_SELECTOR, "a[title='iPhone']")
    MENU_OPTIONS_MAC = (By.CSS_SELECTOR, "li#menu-item-468 li a")
    MENU_OPTIONS_IPHONE = (By.CSS_SELECTOR, "li#menu-item-469 li a")
    MENU_OPTIONS_IPAD = (By.CSS_SELECTOR, "li#menu-item-470 li a")
    MENU_OPTIONS_WATCH = (By.CSS_SELECTOR, "li#menu-item-471 li a")
    MENU_OPTIONS_ACCESSORIES = (By.CSS_SELECTOR, "li#menu-item-472 li a")

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
        for i in range(len(e) + 1):
            self.click(*self.IMAGE_ZOOM_RIGHT_ARROW)

    def click_home_link(self):
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

    # latest on sale
    def price_description_shown(self):
        self.find_element(*self.PRODUCT_PRICE)
        self.find_element(*self.PRODUCT_DESCRIPTION)

    # search
    def open_correct_product_page(self, product_name: str):
        self.verify_text(product_name, *self.PRODUCT_NAME)

    def notification_no_product(self, notification_no_product):
        self.verify_text(notification_no_product, *self.NOTIFICATION_NO_PRODUCT)

    # product_categories
    def open_correct_category_page(self, category_name):
        header_category_page = self.find_element(*self.HEADER_CATEGORY_PAGE).text
        assert category_name in header_category_page, \
            f'Incorrect header: {header_category_page}, waiting for {category_name}'

    def correct_menu_options_mac(self, menu_options):
        options = self.find_elements(*self.MENU_OPTIONS_MAC)
        menu = menu_options.replace(', ', ':').split(':')
        for i in range(len(options)):
            assert options[i].text == menu[i], f'Expected text {menu[i]}, but got {options[i].text}'

    def correct_menu_options_iphone(self, menu_options):
        options = self.find_elements(*self.MENU_OPTIONS_IPHONE)
        menu = menu_options.replace(', ', ':').split(':')
        for i in range(len(options)):
            assert options[i].text == menu[i], f'Expected text {menu[i]}, but got {options[i].text}'

    def correct_menu_options_ipad(self, menu_options):
        options = self.find_elements(*self.MENU_OPTIONS_IPAD)
        menu = menu_options.replace(', ', ':').split(':')
        for i in range(len(options)):
            assert options[i].text == menu[i], f'Expected text {menu[i]}, but got {options[i].text}'


    def correct_menu_options_watch(self, menu_options):
        options = self.find_elements(*self.MENU_OPTIONS_WATCH)
        menu = menu_options.replace(', ', ':').split(':')
        for i in range(len(options)):
            assert options[i].text == menu[i], f'Expected text {menu[i]}, but got {options[i].text}'

    def correct_menu_options_accessories(self, menu_options):
        options = self.find_elements(*self.MENU_OPTIONS_ACCESSORIES)
        menu = menu_options.replace(', ', ':').split(':')
        for i in range(len(options)):
            assert options[i].text == menu[i], f'Expected text {menu[i]}, but got {options[i].text}'

    # cart
    def verify_checkout_page(self, correct_page):
        self.verify_text(correct_page, *self.HEADER_CHECKOUT_PAGE)

    # adding to shopping cart _product
    def item_added_to_cart(self):
        self.wait_for_element_appear(*self.MESSAGE_ADDED_CART)

    def click_plus_or_minus_button(self, plus_minus_sign, amount_times):
        n = 0
        if plus_minus_sign == '+':
            while n < int(amount_times):
                self.click(*self.PLUS_TO_CART)
                n += 1
        elif plus_minus_sign == '-':
            while n < int(amount_times):
                self.wait_for_element_click(*self.MINUS_TO_CART)
                n += 1
        else:
            f'Something went wrong...'

    def input_amount_items_add_window(self, amount):
        self.input(amount, *self.AMOUNT_INPUT_WINDOW)

    def click_left_right_arrow(self, direction_arrow):
        if direction_arrow == 'right':
            product_image = self.find_element(*self.IMAGE_RIGHT_ARROW)
            self.actions.move_to_element(product_image)
            self.actions.perform()
            product_image.click()
            product_image.click()
        elif direction_arrow == 'left':
            product_image = self.find_element(*self.IMAGE_LEFT_ARROW)
            self.actions.move_to_element(product_image)
            self.actions.perform()
            product_image.click()
            product_image.click()
        else:
            f'Something went wrong....'

    def our_of_stock(self, text):
        self.verify_text(text, *self.OUT_OF_STOCK)

    def you_may_also_like_text_shown(self, block_header):
        print(block_header)
        self.verify_text(block_header, *self.YOU_MAY_ALSO_LIKE)

     ### you may like bloke
    def you_block_contains_products(self):
        self.find_elements(*self.PRODUCT_TITLES)

    def you_click_product1_take_correct_page(self, product_name):
        amount = self.find_elements(*self.PRODUCT_TITLES)
        name = amount[0].click()
        sleep(3)
        self.wait_for_element_appear(*self.PRODUCT_NAME)
        # self.verify_text(product_name, *self.PRODUCT_NAME)
        new_product_name = self.find_element(*self.PRODUCT_NAME)
        assert new_product_name


    def you_click_product2_take_correct_page(self, product_name):
        amount = self.find_elements(*self.PRODUCT_TITLES)
        name = amount[1].click()
        sleep(2)
        self.wait_for_element_appear(*self.PRODUCT_NAME)
        # self.verify_text(product_name, *self.PRODUCT_NAME)
        new_product_name = self.find_element(*self.PRODUCT_NAME)
        assert new_product_name
