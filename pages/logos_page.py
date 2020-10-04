from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


class LogosIcon(Page):
    SOCIAL_LOGOS = (By.CSS_SELECTOR, "div.social-icons.share-icons.relative a")
    FACEBOOK_LOGO = (By.CSS_SELECTOR, "a.icon.button.facebook")
    TWITTER_LOGO = (By.CSS_SELECTOR, "a.icon.button.twitter")
    EMAIL_LOGO = (By.CSS_SELECTOR, "a.icon.button.email")
    PINTEREST_LOGO = (By.CSS_SELECTOR, "a.icon.button.pinterest")
    TUMBLR_LOGO = (By.CSS_SELECTOR, "a.icon.button.tumblr")
    ICON_TOOLTIP = (By.CSS_SELECTOR, "div.tooltipster-content")

    def logos_present_facebook(self, social_icons):
        logo_fb = self.find_element(*self.FACEBOOK_LOGO)
        self.actions.move_to_element(logo_fb)
        self.actions.perform()
        popup_window = self.find_element(*self.ICON_TOOLTIP)
        print(popup_window.text)
        social_icons_list = social_icons.replace(', ', ':').split(':')
        assert popup_window
        assert social_icons_list[0] in popup_window.text, \
            f'Expected text {social_icons_list[0]}, but got {popup_window.text}'

    def logos_present_twitter(self, social_icons):
        logos_icons = self.find_element(*self.TWITTER_LOGO)
        self.actions.move_to_element(logos_icons)
        self.actions.perform()
        sleep(3)
        ### TODO Lana - all TCs works only with sleep, How to avoid it? Even wait for element appear doesn't help.
        popup_windows = self.wait_for_element_appear(*self.ICON_TOOLTIP)
        popup_windows = self.find_element(*self.ICON_TOOLTIP)
        social_icons_list = social_icons.replace(', ', ':').split(':')
        assert social_icons_list[1] in popup_windows.text, \
            f'Expected text {social_icons_list[1]}, but got {popup_windows.text}'

    def logos_present_email(self, social_icons):
        logos_list = social_icons.replace(', ', ':').split(':')
        logos_icons = self.find_element(*self.EMAIL_LOGO)
        self.actions.move_to_element(logos_icons)
        self.actions.perform()
        sleep(3)
        popup_window = self.find_element(*self.ICON_TOOLTIP)
        assert logos_list[2] in popup_window.text, \
            f'Expected text {logos_list[2]}, but got {popup_window.text}'

    def logos_present_pinterest(self, social_icons):
        social_icons_list = social_icons.replace(', ', ':').split(':')
        logos_icons = self.find_element(*self.PINTEREST_LOGO)
        self.actions.move_to_element(logos_icons)
        self.actions.perform()
        sleep(3)
        popup_window = self.find_element(*self.ICON_TOOLTIP)
        assert social_icons_list[3] in popup_window.text, \
            f'Expected text {social_icons_list[3]}, but got {popup_window.text}'

    def logos_present_tumblr(self, social_icons):
        social_icons_list = social_icons.replace(', ', ':').split(':')
        logos_icons = self.find_element(*self.TUMBLR_LOGO)
        self.actions.move_to_element(logos_icons)
        self.actions.perform()
        sleep(3)
        popup_window = self.find_element(*self.ICON_TOOLTIP)
        assert social_icons_list[4] in popup_window.text, \
            f'Expected text {social_icons_list[4]}, but got {popup_window.text}'

    def loop_logos_present(self, logos_icons):
        logos_list = logos_icons.replace(', ', ':').split(':')
        social_icons = self.find_elements(*self.SOCIAL_LOGOS)
        for i in range(len(social_icons)):
            # social_icons = self.find_elements(*self.SOCIAL_LOGOS)
            self.actions.move_to_element(social_icons[i])
            self.actions.perform()
            sleep(3)
            logos_text = self.find_element(*self.ICON_TOOLTIP)
            assert logos_list[i] in logos_text.text, \
                f'Waited for {logos_list[i]}, but got {logos_text.text}'

    def fb_click_switch_new_window(self):
        self.click(*self.FACEBOOK_LOGO)
        self.driver.wait.until(EC.new_window_is_opened)
        current_windows = self.driver.window_handles
        self.driver.switch_to_window(current_windows[1])
        assert 'facebook.com' in self.driver.current_url,\
            f'Expected Facebook page, but got {self.driver.current_url}'

    def tw_click_switch_new_window(self):
        self.click(*self.TWITTER_LOGO)
        self.driver.wait.until(EC.new_window_is_opened)
        current_windows = self.driver.window_handles
        self.driver.switch_to_window(current_windows[1])
        assert 'twitter.com' in self.driver.current_url, \
            f'Expected Twitter page, but got {self.driver.current_url}'

    def email_click_switch_new_window(self):
        self.click(*self.EMAIL_LOGO)
        self.driver.wait.until(EC.new_window_is_opened)
        current_windows = self.driver.window_handles
        self.driver.switch_to_window(current_windows[1])
        assert 'google.com' in self.driver.current_url, \
            f'Expected email page, but got {self.driver.current_url}'

    def pinterest_click_switch_new_window(self):
        self.click(*self.PINTEREST_LOGO)
        self.driver.wait.until(EC.new_window_is_opened)
        current_windows = self.driver.window_handles
        self.driver.switch_to_window(current_windows[1])
        assert 'pinterest.com' in self.driver.current_url, \
            f'Expected Pinterest page, but got {self.driver.current_url}'

    def tumblr_click_switch_new_window(self):
        self.click(*self.TUMBLR_LOGO)
        self.driver.wait.until(EC.new_window_is_opened)
        current_windows = self.driver.window_handles
        self.driver.switch_to_window(current_windows[1])
        assert 'tumblr.com' in self.driver.current_url, \
            f'Expected LinkedIn page, but got {self.driver.current_url}'

    def switch_old_window(self):
        current_windows = self.driver.window_handles
        self.driver.close()
        self.driver.switch_to_window(current_windows[0])

    def social_links_opens(self, links):
        links_name = links.replace(', ', ':').split(':')
        social_links = self.find_elements(*self.SOCIAL_LOGOS)
        logo_links = social_links[1:]
        for i in range(len(logo_links)):
            print(i)
            self.wait_for_element_click(logo_links[i])
            self.driver.wait.until(EC.new_window_is_opened)
            current_windows = self.driver.window_handles
            self.driver.switch_to_window(current_windows[1])
            assert links_name[i] in self.driver.current_url, \
                f'Expected {links_name[i]}, but got {self.driver.current_url}'
            sleep(3)
            self.driver.close()
            self.driver.switch_to_window(current_windows[0])


