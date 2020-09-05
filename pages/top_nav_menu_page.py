from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from gettop.pages.base_page import Page
from time import sleep

class TopNavMenu(Page):
    GETTOP_LOGO = (By.CSS_SELECTOR, "div#logo.flex-col.logo")
    ACCOUNT_ICON = (By.CSS_SELECTOR, "i.icon-user")
    LOGIN_PAGE_TEXT = (By.CSS_SELECTOR, "h3.uppercase")
    SEARCH_ICON = (By.CSS_SELECTOR, "i.icon-search")
    SEARCH_WINDOW = (By.CSS_SELECTOR, "input#woocommerce-product-search-field-0")
    SEARCH_CLICK_BTN = (By.CSS_SELECTOR, "button.ux-search-submit.submit-button.secondary.button.icon.mb-0 i.icon-search")
    SHOPPING_CART_ICON = (By.CSS_SELECTOR, "span.cart-icon.image-icon")
    CART_NO_PRODUCT = (By.CSS_SELECTOR, "p.woocommerce-mini-cart__empty-message")
    PRICE_IN_CART_NAV_MENU = (By.CSS_SELECTOR, "span.cart-price")
    PRICE_PRODUCT = (By.CSS_SELECTOR, "span.woocommerce-Price-amount.amount")
    REMOVE_FROM_CART_BTN = (By.CSS_SELECTOR, "a.remove.remove_from_cart_button")
    SECOND_PRODUCT = (By.ID, "menu-item-469")
    ALL_IPONES = (By.CSS_SELECTOR, "div.shop-container")
    CHECKOUT_BTN = (By.XPATH, "//*[contains(text(), 'Checkout')]")
    DEPARTMENTS = (By.CSS_SELECTOR, "a.nav-top-link")
    MAC_BTN = (By.CSS_SELECTOR, "li#menu-item-468 i.icon-angle-down")
    IPHONE_BTN = (By.CSS_SELECTOR, "li#menu-item-469 i.icon-angle-down")
    IPAD_BTN = (By.CSS_SELECTOR, "li#menu-item-470 i.icon-angle-down")
    WATCH_BTN = (By.CSS_SELECTOR, "li#menu-item-471 i.icon-angle-down")
    ACCESSORIES_BTN = (By.CSS_SELECTOR, "li#menu-item-472 i.icon-angle-down")
    MAC_OPTIONS = (By.CSS_SELECTOR, "li#menu-item-468 ul.sub-menu.nav-dropdown.nav-dropdown-default")
    TOTAL_PRICE_CART_TOPMENU = (By.CSS_SELECTOR, "p.woocommerce-mini-cart__total.total span.woocommerce-Price-amount.amount")
    PRODUCT_1_CART = (By.XPATH, "//*[contains(text(), 'AirPods Pro')]")
    PRODUCT_2_CART = (By.XPATH, "//*[contains(text(), 'iPhone 11 Pro')]")
    VIEW_CART_BTN = (By.CSS_SELECTOR, "p.woocommerce-mini-cart__buttons.buttons a.button.wc-forward")

    #logo"
    def logo_click(self):
        self.click(*self.GETTOP_LOGO)

    #account
    def account_icon_login_form(self, login_form):
        self.wait_for_element_click(*self.ACCOUNT_ICON)
        text = self.find_element(*self.LOGIN_PAGE_TEXT)
        print(text.text)
        self.verify_text(login_form, *self.LOGIN_PAGE_TEXT)

    def hover_over_search_window(self, product_name):
        open_search_window = self.find_element(*self.SEARCH_ICON)
        self.actions.move_to_element(open_search_window)
        self.actions.perform()
        open_search_window.click()
        self.input(product_name, *self.SEARCH_WINDOW)
        self.wait_for_element_click(*self.SEARCH_CLICK_BTN)

    def shopping_cart_icon_click(self):
        self.click(*self.SHOPPING_CART_ICON)

    def hover_over_shopping_cart(self):
        self.refresh()
        shopping_cart_icon = self.find_element(*self.SHOPPING_CART_ICON)
        self.actions.move_to_element(shopping_cart_icon)
        self.actions.perform()

    def verify_cart_empty_text(self, search_word: str):
        self.verify_text(search_word, *self.CART_NO_PRODUCT)

    def verify_topmenu_cart_same_price(self):
        price_of_product = self.find_element(*self.PRICE_PRODUCT).text
        price_in_shopping_cart = self.find_element(*self.PRICE_IN_CART_NAV_MENU).text
        assert price_of_product in price_in_shopping_cart, f'Incorrect header: {price_in_shopping_cart}'

    def verify_amount_items_topmenu_cart(self, amount):
        self.verify_text(str(amount), *self.SHOPPING_CART_ICON)

    def remove_from_cart_btn(self):
        self.click(*self.REMOVE_FROM_CART_BTN)

    def open_products_page_topmenu(self):
        hover_over_topmenu_product = self.find_element(*self.SECOND_PRODUCT)
        self.actions.move_to_element(hover_over_topmenu_product)
        self.actions.perform()
        self.click(*self.SECOND_PRODUCT)

    def open_product_page_topmenu(self):
        self.click(*self.ALL_IPONES)

    def checkout_btn_click(self):
       self.click(*self.CHECKOUT_BTN)

    def price_subtotal_shown_top_cart(self, total_price):
        self.verify_text((str(total_price)), *self.TOTAL_PRICE_CART_TOPMENU)

    def products_in_cart(self, product_1, product_2):
        item_1 = self.find_elements(*self.PRODUCT_1_CART)
        print(item_1[1].text)
        assert product_1 in item_1[1].text, f'Incorrect header: {item_1[1].text}'
        item_2 = self.find_elements(*self.PRODUCT_2_CART)
        print(item_2[2].text)
        # assert product_2 in item_2[1].text, f'Incorrect header: {item_2[1].text}'

    #product categories
    def hover_over_categories_topmenu(self, number_categories):
        departments = self.find_elements(*self.DEPARTMENTS)
        depar_list = ('MAC', 'IPHONE', 'IPAD', 'WATCH', 'ACCESSORIES')
        for i in range(0, (int(number_categories))):
            self.actions.move_to_element(departments[i])
            self.actions.perform()
            assert departments[i].text in depar_list, f'Incorrect name of department: {departments[i].text}'
            departments = self.find_elements(*self.DEPARTMENTS)

    def hover_over_category(self, category_name):
        topmenu_category = self.find_element(*self.DEPARTMENTS)
        self.actions.move_to_element(topmenu_category)
        self.actions.perform()
        self.verify_text(category_name, *self.DEPARTMENTS)

    def department_menu_options(self):
        mac_options_list = ('MacBook Pro 13-inch', 'MacBook Pro 16-inch', 'MacBook Air')
        mac_options_web = self.find_elements(*self.MAC_OPTIONS)
        print(len(mac_options_web))
        for i in range(len(mac_options_web)):
            print(mac_options_web[i].text)
            assert mac_options_web[i].text in mac_options_list[i], f'Incorrect options: {mac_options_web[i].text}, waiting for {mac_options_list}'
            print(mac_options_list[i])

    def click_view_cart_btn(self):
        self.click(*self.VIEW_CART_BTN)

    def click_mac_category(self):
        self.click(*self.MAC_BTN)

    def click_iphone_category(self):
        self.click(*self.IPHONE_BTN)

    def click_ipad_category(self):
        self.click(*self.IPAD_BTN)

    def click_watch_category(self):
        self.click(*self.WATCH_BTN)

    def click_accessories_category(self):
        self.click(*self.ACCESSORIES_BTN)
