# import all the locators from the locator file
from locator import *
from element import BasePageElement

class SearchTextElement(BasePageElement):
    locator = "q"

class BasePage(object):
    """
    This is a base class for all our page objects
    """
    def __init__(self, driver):
        self.driver = driver

class MainPage(BasePage):
    # make the search bar element available on the main page object
    search_text_element = SearchTextElement()

    def is_title_matches(self):
        return "Python" in self.driver.title
    
    def click_go_button(self):
        element = self.driver.find_element(*MainPageLocators.GO_BUTTON)
        # the star unpacks the tuple, allow it to be used as two args
        element.click()
   
class SearchResultPage(BasePage):
    def is_results_found(self):
        return "No results found." not in self.driver.page_source