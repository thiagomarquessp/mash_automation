from libraries.Base import Base
from libraries.CommonKeywords import CommonKeywords
from libraries.locators import *
from selenium.webdriver import ActionChains
import time


class WebKeywords(Base):
    def __init__(self):
        super(WebKeywords, self).__init__()
        self.common_kw = CommonKeywords()

    def initialize_and_open_browser_with_url(self, url, browser):

        self.selenium_lib.open_browser(url, browser=browser)
        # self.driver.desired_capabilities.update(SELENIUM_DESIRED_CAPS)
        self.selenium_lib.maximize_browser_window()

    def input_text_to_search_field(self):

        self.selenium_lib.click_element(MAIN_PAGE_SEARCH_INPUT_FIELD)
        time.sleep(1)
        self.selenium_lib.input_text(MAIN_PAGE_SEARCH_INPUT_FIELD, "Mash")
        time.sleep(2)

    def execute_search(self):
        action = ActionChains(self.selenium_lib.driver)
        action.send_keys(u'\ue007')
        action.perform()
        self.selenium_lib.wait_until_element_is_visible(SEARCH_RESULT_MASH_LINK)
        self.builtin_lib.log(SEARCH_RESULT_MASH_LINK)
        self.scroll_to_bottom()
        time.sleep(5)

    def scroll_to_bottom(self):
        scroll = self.selenium_lib.driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        return scroll

    def navigate_to_second_results_page(self):
        self.click_element(SEARCH_RESULT_PAGE_GO_TO_SECOND_PAGE_BUTTON, SEARCH_RESULT_PAGE_SECOND_PAGE_ACTIVE)

    def verify_if_link_to_finnish_mash_site_is_not_visible(self):
        self.selenium_lib.element_should_not_be_visible()

    def close_browser(self):
        self.selenium_lib.driver.close()

    def click_element(self, element, expected_element):
        """"""

        valid = True

        try:
            self.selenium_lib.wait_until_element_is_visible(element)
        except:
            self.builtin_lib.log(f"Element {element} is not present", "ERROR")
            valid = False

        try:
            self.selenium_lib.click_element(element)
        except:
            self.builtin_lib.log(f"Element {element} could not be clicked", "ERROR")
            valid = False

        try:
            self.selenium_lib.wait_until_element_is_visible(expected_element)
        except:
            self.builtin_lib.log(f"Expected element {expected_element} is not present")
            valid = False

        if not valid:
            raise AssertionError(f"Clicking {element} element failed")