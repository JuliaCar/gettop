from selenium.webdriver.common.by import By
from pages.base_page import Page

class DescriptionReview(Page):
    DESCRIPTION_BLOCK = (By.CSS_SELECTOR, "li#tab-title-description a")
    REVIEW_BLOCK = (By.CSS_SELECTOR, "li#tab-title-reviews a")
    REVIEW_HEADER = (By.ID, "reply-title")
    REVIEW_FORM = (By.ID, "comment")
    REVIEW_FIVE_STARS = (By.CSS_SELECTOR, "a.star-5")
    REVIEW_AUTHOR = (By.ID, "author")
    REVIEW_EMAIL = (By.ID, "email")
    REVIEW_COOKIES_BUTTON = (By.ID, "#wp-comment-cookies-consent")
    SUBMIT_BUTTON = (By.ID, "submit")
    REVIEW_SHOWN = (By.CSS_SELECTOR, "div.description")
    NAME = (By.CSS_SELECTOR, "div#comments span")

    def description_block_shown(self):
        self.click(*self.DESCRIPTION_BLOCK)

    def open_review_block(self):
        self.click(*self.REVIEW_BLOCK)

    def user_submit_review(self, header_review):
        header = self.find_element(*self.REVIEW_HEADER).text
        assert header_review in header_review, f'Waited for {header_review}, but got {header}'
        self.click(*self.REVIEW_FIVE_STARS)
        self.input("I like this product! The best!", *self.REVIEW_FORM)
        self.input('Julia', *self.REVIEW_AUTHOR)
        self.input('mjp54321@gmail.com', *self.REVIEW_EMAIL)
        ### TODO lana =  find out how to check box for cookies button - link or kye works how to search will be good!!
        # self.click(*self.REVIEW_COOKIES_BUTTON)
        self.click(*self.SUBMIT_BUTTON)
        ### TODO Lana how to write this TC and make it reusable and stable if website doesn't let to submit same review second time?

    def review_submitted(self):
        self.find_element(*self.REVIEW_SHOWN)

    def correct_amount_reviews(self, amount_reviews, product_name):
        self.verify_text(amount_reviews, *self.REVIEW_BLOCK)
        header_review = self.find_element(*self.NAME).text
        assert product_name in header_review, f'Waited for {product_name}, but got {header_review}'
