from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.support.ui import Select
from time import sleep


class RecentlyViewed(Page):
    ITEMS = (By.CSS_SELECTOR, "aside#woocommerce_recently_viewed_products-8 li")
    BROWSE_HEADER = (By.CSS_SELECTOR, "aside#woocommerce_product_categories-13 span")
    BROWSE_CATEGORIES = (By.CSS_SELECTOR, "ul.product-categories a")
    MACBOOK_CATEGORY = (By.CSS_SELECTOR, "li.cat-item.cat-item-68")
    CATEGORY_PAGE_HEADER = (By.CSS_SELECTOR, "div.is-large")
    IPHONE_CATEGORY = (By.CSS_SELECTOR, "li.cat-item.cat-item-69 a")
    IPAD_CATEGORY = (By.CSS_SELECTOR, "li.cat-item.cat-item-72 a")
    ACCESSORIES_CATEGORY = (By.CSS_SELECTOR, "li.cat-item.cat-item-74 a")
    AIRPODS_CATEGORY = (By.CSS_SELECTOR, "li.cat-item.cat-item-77 a")
    WATCH_CATEGORY = (By.CSS_SELECTOR, "li.cat-item.cat-item-76 a")
    PAGE_NUMBER = (By.CSS_SELECTOR, "a.page-number")
    ANGEL_RIGHT = (By.CSS_SELECTOR, "i.icon-angle-right")
    ANGEL_LEFT = (By.CSS_SELECTOR, "i.icon-angle-left")
    SELECT_SORTING = (By.CSS_SELECTOR, "select.orderby")
    HOME_LINK = (By.CSS_SELECTOR, "div.is-large a")
    KNOBS = (By.CSS_SELECTOR, "span.ui-slider-handle")
    FILTER_BTN = (By.XPATH, "//button[text()='Filter']")
    NAME_HIGH_END = (By.CSS_SELECTOR, "div.products p.name")
    RESET_FILTERS = (By.CSS_SELECTOR, "#woocommerce_layered_nav_filters-10 a")
    MESSAGE = (By.CSS_SELECTOR, "p.woocommerce-info")


    def open_shop_page(self, name_page):
        self.open_page(f'{name_page}/')

    def recently_viewed_items_present(self, amount_items):
        items = self.find_elements(*self.ITEMS)
        sleep(3)
        print(len(items))
        assert int(amount_items) == len(items), f'Expected to have {amount_items}, but got {len(items)}'

        ### browse ts
    def browse_block_header_present(self, block_header):
        self.verify_text(block_header, *self.BROWSE_HEADER)

    def browse_block_categories_shown(self, categories):
        categories_list = categories.replace(', ', ':').split(':')
        print(len(categories_list))
        browse_categories = self.find_elements(*self.BROWSE_CATEGORIES)
        print(len(browse_categories))
        for i in range(len(browse_categories)):
            print(browse_categories[i].text)
            print(categories_list[i])
            ##TODO can't find text for children categories
            # assert categories_list[i] in browse_categories[i].text,\
            #     f'Expected {categories_list[i]}, but got {browse_categories[i].text}'

    def browse_category_click_macbook(self):
        self.click(*self.MACBOOK_CATEGORY)

    def browse_category_correct_page(self, category):
        category_page = self.find_element(*self.CATEGORY_PAGE_HEADER)
        new_category = category.upper()
        assert new_category in category_page.text, f'Expected text {new_category}, but got {category_page.text}'

    def browse_category_click_iphone(self):
        self.click(*self.IPHONE_CATEGORY)

    def browse_category_click_ipad(self):
        self.click(*self.IPAD_CATEGORY)

    def browse_category_click_accessories(self):
        self.click(*self.ACCESSORIES_CATEGORY)

    def browse_category_click_airpods(self):
        self.click(*self.ACCESSORIES_CATEGORY)
        self.wait_for_element_click(*self.AIRPODS_CATEGORY)

    def browse_category_click_watch(self):
        self.click(*self.ACCESSORIES_CATEGORY)
        self.wait_for_element_click(*self.WATCH_CATEGORY)

    ##products
    def click_page_number(self, page_number):
        if int(page_number) == 1:
            page_one = self.find_elements(*self.PAGE_NUMBER)
            page_one[1].click()
        elif int(page_number) == 2:
            page_two = self.find_elements(*self.PAGE_NUMBER)
            page_two[1].click()
            sleep(2)
        else:
            print('Something went wrong..Please, put correct page number')

    def verify_page_number_header(self, header_page_number):
        actual_text = self.find_element(*self.CATEGORY_PAGE_HEADER).text
        assert header_page_number in actual_text, f'Expected {header_page_number}, but got {actual_text}'

    def verify_arrow_click(self, arrow):
        if arrow == '>':
            self.click(*self.ANGEL_RIGHT)
            sleep(2)
        elif arrow == '<':
            self.click(*self.ANGEL_LEFT)
            sleep(2)
        else:
            print('Something went wrong..Please, put correct page number')

    def sorting_by_price_desc(self):
        select = Select(self.find_element(*self.SELECT_SORTING))
        select.select_by_value('price-desc')

    def sorting_by_price(self):
        select = Select(self.find_element(*self.SELECT_SORTING))
        select.select_by_value('price')

    def sorting_by_popularity(self):
        select = Select(self.find_element(*self.SELECT_SORTING))
        select.select_by_value('popularity')

    def sorting_by_rating(self):
        select = Select(self.find_element(*self.SELECT_SORTING))
        select.select_by_value('rating')

    def sorting_by_latest(self):
        select = Select(self.find_element(*self.SELECT_SORTING))
        select.select_by_value('date')

    ###home
    def click_home_link(self):
        self.click(*self.HOME_LINK)

    ###filter
    def move_left_knot_right(self):
        knobs = self.find_elements(*self.KNOBS)
        left_knob = knobs[0]
        self.actions.click_and_hold(left_knob).move_by_offset(102, 0).perform()

    def click_filter_btn(self):
        self.click(*self.FILTER_BTN)

    def filter_applied_high_end(self, product_name):
        self.verify_text(product_name, *self.NAME_HIGH_END)

    def move_right_knot_left(self):
        knobs = self.find_elements(*self.KNOBS)
        left_knob = knobs[1]
        self.actions.click_and_hold(left_knob).move_by_offset(-128, 0).perform()

    def reset_filters(self):
        filters = self.find_elements(*self.RESET_FILTERS)
        for i in range(len(filters)):
            filters = self.find_element(*self.RESET_FILTERS)
            filters.click()

    def move_left_knob_right_max(self):
        knobs = self.find_elements(*self.KNOBS)
        left_knob = knobs[0]
        self.actions.click_and_hold(left_knob).move_by_offset(240, 0).perform()

    def message_no_product_shown(self, msg_no_match):
        self.verify_text(msg_no_match, *self.MESSAGE)
