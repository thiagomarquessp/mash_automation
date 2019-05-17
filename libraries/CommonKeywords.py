from libraries.Base import Base
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains


class CommonKeywords(Base):

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

    def hoover_over_element(self, element):
        """"""

        try:
            element = self.selenium_lib.find_element(element)
            element.send_keys(Keys.RETURN)
            element.submit()
        except:
            raise AssertionError(f"Hoovering over element {element} failed")
