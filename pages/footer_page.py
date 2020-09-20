from selenium.webdriver.common.by import By
from pages.base_page import Page


class Footer(Page):
    FOOTER_CATEGORIES = (By.CSS_SELECTOR, "span.widget-title")
    COPYRIGHT = (By.CSS_SELECTOR, "div.copyright-footer")
    BACK_TO_TOP_BTN = (By.CSS_SELECTOR, "i.icon-angle-up")
    PRODUCTS_LIST_ALL = (By.CSS_SELECTOR, "div.row.large-columns-3.mb-0 li") ##div.footer-widgets.footer.footer-1 li")
    PRODUCT_NAME = (By.CSS_SELECTOR, "span.product-title")
    PRODUCT_IMAGE = (By.CSS_SELECTOR, "img.attachment-woocommerce_gallery_thumbnail.size-woocommerce_gallery_thumbnail")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "span.woocommerce-Price-amount.amount")
    PRODUCT_RATING = (By.CSS_SELECTOR, "div.star-rating span")
    PRODUCT_NAME_PRODUCT_PAGE = (By.CSS_SELECTOR, "h1.product-title.product_title.entry-title")

    def footer_categories_shown(self, footer_categories_list):
        categories = self.find_elements(*self.FOOTER_CATEGORIES)
        new_footer_categories_list = footer_categories_list.replace(', ', ':').split(':')
        for i in range(len(categories)):
            # print(categories[i].text)
            # print(new_footer_categories_list[i])
            assert categories[i].text == new_footer_categories_list[i], \
                f'Expected text {new_footer_categories_list[i]}, but got {categories[i].text}'

    def footer_copyright_text(self, copyright_text):
        self.verify_text(copyright_text, *self.COPYRIGHT)

    def footer_back_top_btn(self):
        self.wait_for_element_appear(*self.BACK_TO_TOP_BTN)

    def footer_products_tags(self):
        products_list_all = self.find_elements(*self.PRODUCTS_LIST_ALL)
        # print(len(products_list_all))
        for i in range(len(products_list_all)):
            # print(products_list_all[i].text)
            assert products_list_all[i].find_element(*self.PRODUCT_NAME), \
                f"Expected item to have name"
            assert products_list_all[i].find_element(*self.PRODUCT_PRICE), \
                f"Expected item to have price"
            assert products_list_all[i].find_element(*self.PRODUCT_IMAGE), \
                f"Expected item to have image"
            assert products_list_all[i].find_element(*self.PRODUCT_RATING),\
                f"Expected item to have star-rating"

    def footer_links_categories(self):
        products_list_all = self.find_elements(*self.PRODUCTS_LIST_ALL)
        print(len(products_list_all))
        for i in range(len(products_list_all)):
            footer_product_name = products_list_all[i].find_element(*self.PRODUCT_NAME).click()
            products_list_all = self.find_elements(*self.PRODUCTS_LIST_ALL)
            footer_product_name = products_list_all[i].find_element(*self.PRODUCT_NAME).text
            # print(footer_product_name)
            product_page_product_name = self.find_element(*self.PRODUCT_NAME_PRODUCT_PAGE).text
            # print(product_page_product_name)
            assert footer_product_name == product_page_product_name, \
                f"Expected item to {footer_product_name}, but got {product_page_product_name}."
