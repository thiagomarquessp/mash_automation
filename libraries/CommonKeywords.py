from libraries.Base import Base


class CommonKeywords(Base):

    def __init__(self):
        super(CommonKeywords, self).__init__()

    def initialize_and_open_browser_with_url(self, url, browser):

        self.selenium_lib.open_browser(url, browser=browser)
        self.selenium_lib.maximize_browser_window()

    def close_browser(self):
        self.selenium_lib.driver.close()

    def scroll_to_bottom_of_current_page(self):
        """"""
        scroll = self.selenium_lib.driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        return scroll
