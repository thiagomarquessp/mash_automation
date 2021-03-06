URL = "https://www.google.fi"
MASH_FINNISH_URL = "https://www.mash.com/fi"
SEARCH_INPUT = "Mash"

# Google main page
MAIN_PAGE_SEARCH_INPUT_FIELD = "xpath=//input[@class='gLFyf gsfi']"
MAIN_PAGE_SEARCH_BUTTON = "xpath=//div[@class='VlcLAe']//input[@name='btnK']"

# Google search results page
SEARCH_RESULT_PAGE_SEARCH_RESULT = "xpath=//input[@class='gLFyf gsfi'][@value='Mash']"
SEARCH_RESULT_PAGE_GO_TO_SECOND_PAGE_BUTTON = "xpath=//a[@class='fl'][text()='2']"
SEARCH_RESULT_PAGE_SECOND_PAGE_ACTIVE = "xpath=//td[@class='cur'][text()='2']//span[@class='csb']"
SEARCH_RESULT_MASH_LINK = f"xpath=//cite[text()='{MASH_FINNISH_URL}']"
