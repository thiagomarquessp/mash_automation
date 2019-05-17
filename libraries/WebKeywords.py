from selenium import webdriver


class WebKeywords:

    def initialize_and_open_browser_with_url(self, url):

        self.driver = webdriver.Chrome()
        # self.driver.desired_capabilities.update(SELENIUM_DESIRED_CAPS)
        self.driver.maximize_window()
        self.driver.get(url)
