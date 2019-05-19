from libraries.Base import Base
from libraries.CommonKeywords import CommonKeywords
from libraries.PageObjects.locators import *
from selenium.webdriver import ActionChains


class WebKeywords(Base):
    def __init__(self):
        super(WebKeywords, self).__init__()
        self.common_kw = CommonKeywords()

    def input_text_to_search_field(self, search_input):
        """
        Pass string from parameter into search input field
        :param search_input:
        :return:
        """

        try:
            self.selenium_lib.input_text(MAIN_PAGE_SEARCH_INPUT_FIELD, search_input)
        except:
            raise AssertionError(f"Could not input {search_input} text into search")

    def execute_search(self):
        """Execute search by pressing Enter key
        and verifying if given link is displayed at first search result page
        """

        valid = True

        try:
            action = ActionChains(self.selenium_lib.driver)
            action.send_keys(u'\ue007')
            action.perform()
        except:
            self.builtin_lib.log("Clicking Enter did not perform search.", "ERROR")
            valid = False

        try:
            self.selenium_lib.wait_until_element_is_visible(SEARCH_RESULT_MASH_LINK)
            self.builtin_lib.log("Mash link is displayed in front page")
        except:
            self.builtin_lib.log("Mash link is not displayed in front page.", "ERROR")
            valid = False

        if not valid:
            raise AssertionError(f"Searching for {SEARCH_INPUT} failed.")

    def navigate_to_second_results_page(self):
        """Scrolling down to bottom of current page
        and navigating to second page of search results"""

        valid = True

        self.common_kw.scroll_to_bottom_of_current_page()

        try:
            self.selenium_lib.click_element(SEARCH_RESULT_PAGE_GO_TO_SECOND_PAGE_BUTTON)
        except:
            self.builtin_lib.log("Clicking at second page of search result failed.", "ERROR")
            valid = False

        try:
            self.selenium_lib.wait_until_element_is_visible(SEARCH_RESULT_PAGE_SECOND_PAGE_ACTIVE)
        except:
            self.builtin_lib.log("Second page of search results is not active after click", "ERROR")
            valid = False

        if not valid:
            raise AssertionError("Navigating to second page of search result failed")

    def verify_if_link_to_mash_site_is_not_visible(self):
        """Checking if given link is not displayed on current page"""

        try:
            self.selenium_lib.element_should_not_be_visible(SEARCH_RESULT_MASH_LINK)
        except:
            raise AssertionError("Link to Mash site is displayed at second page of search results, but should not!")
