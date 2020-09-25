# import all the locators from the locator file
from locator import *
from element import BasePageElement

# class SearchTextElement(BasePageElement):
#     locator = "q"

class BasePage(object):
    """
    This is a base class for all our page objects
    """
    def __init__(self, driver):
        self.driver = driver
    
    def getPageTitle(self):
        """
        Get the page title
        """
        return self.driver.title

class MainPage(BasePage):
    # # make the search bar element available on the main page object
    # search_text_element = SearchTextElement()

    # def is_title_matches(self):
    #     return "Python" in self.driver.title
    
    # def click_go_button(self):
    #     element = self.driver.find_element(*MainPageLocators.GO_BUTTON)
    #     # the star unpacks the tuple, allow it to be used as two args
    #     element.click()

    def click_advanced_options(self):
        """
        Use this to toggle the advanced options
        """
        # find the button
        button = self.driver.find_element(*MainPageLocators.ANTVANCED_OPTIONS_BUTTON)
        # click it
        button.click()
    
    def cycle_spacing_options(self):
        pass

    def cycle_antey_options(self):
        pass

    def click_translate_button(self):
        """
        Use this to start text translation
        """
        # find the button
        button = self.driver.find_element(*MainPageLocators.TRANTSLATE_BUTTON)
        # click it
        button.click()
    
    def click_copy_button(self):
        """
        Use this to translate text
        """
        # find the button
        button = self.driver.find_element(*MainPageLocators.COPY_BUTTON)
        # click it
        button.click()

class SearchResultPage(BasePage):
    def is_results_found(self):
        return "No results found." not in self.driver.page_source