# import all the locators from the locator file
from locator import *
from element import BasePageElement

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