from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from pages.base_page import Page


class Checkout(Page):
    FIRST_NAME = (By.ID, "billing_first_name")
    LAST_NAME = (By.ID, "billing_last_name")
    COMPANY_NAME = (By.ID, "billing_company")
    COUNTRY = (By.ID, "select2-billing_country-results")
    STREET_ONE = (By.ID, "billing_address_1")
    STREET_TWO = (By.ID, "billing_address_2")
    CITY = (By.ID, "billing_city")
    POSTCODE = (By.ID, "billing_postcode")
    PHONE = (By.ID, "billing_phone")
    EMAIL = (By.ID, "billing_email")
    SELECT_COUNTRIES = (By.ID, "select2-billing_country-container")
    US = (By.ID, "select2-billing_country-result-4pko-UM")
    PLACE_ORDER_BTN = (By.ID, "place_order")
    MSG = (By.CSS_SELECTOR, "div.message-container.container.alert-color.medium-text-center strong")
    HEADER = (By.CSS_SELECTOR, "a.current")

    def move_driver_checkout_page(self):
        self.driver.get("http://www.gettop.us/checkout/")

    def fillout_first_name(self, first_name):
        self.input(first_name, *self.FIRST_NAME)

    def fillout_last_name(self, last_name):
        self.input(last_name, *self.LAST_NAME)

    def fillout_company_name(self, company_name):
        self.input(company_name, *self.COMPANY_NAME)

    def fillout_street_address(self, billing_address_1, billing_address_2):
        self.input(billing_address_1, *self.STREET_ONE)
        self.input(billing_address_2, *self.STREET_TWO)

    def fillout_city(self, city):
        self.input(city, *self.CITY)

    def fillout_postcode(self, city):
        self.input(city, *self.POSTCODE)

    def fillout_phone(self, phone):
        self.input(phone, *self.PHONE)

    def fillout_email(self, email):
        self.input(email, *self.EMAIL)

    def fillout_country(self, country):
        open_country_selection = self.find_element(*self.SELECT_COUNTRIES)
        self.actions.move_to_element(open_country_selection)
        self.actions.perform()
        open_country_selection.click()
        self.find_element(*self.US).click()

    def click_place_order_btn(self):
        self.click(*self.PLACE_ORDER_BTN)

    def see_required_field_msg(self, message_required_field):
        self.verify_text(message_required_field, *self.MSG)

    def verify_header_shopping_cart(self, shopping_cart_header):
        self.verify_text(shopping_cart_header.upper(), *self.HEADER)
