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

    def close_browser(self):
        self.selenium_lib.driver.close()
