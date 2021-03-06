from libraries.Base import Base


class TestSetup(Base):

    def initialize_and_open_browser_with_url(self, url, browser):
        """Opens browser with given URL specified by parameters"""

        self.selenium_lib.open_browser(url, browser=browser)
        self.selenium_lib.maximize_browser_window()

    def close_browser(self):
        """Close active browser"""
        
        self.selenium_lib.driver.close()
