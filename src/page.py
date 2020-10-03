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
    def toggle_advanced_options(self):
        """
        Use this to toggle the advanced options
        """
        # find the button
        button = self.driver.find_element(*MainPageLocators.ANTVANCED_OPTIONS_BUTTON)
        # click it
        button.click()
    
    def choose_monospace_setting(self):
        """
        Set the spacing to the monospace setting
        """
        option = self.driver.find_element(*MainPageLocators.MONOSPACE_SETTING)
        option.click()

    def choose_doublespace_setting(self):
        """
        Set the spacing to the doublespace setting
        """
        option = self.driver.find_element(*MainPageLocators.DOUBLESPACE_SETTING)
        option.click()
    
    def choose_antey_no_setting(self):
        """
        Set the antey to the 'no' setting
        """
        option = self.driver.find_element(*MainPageLocators.ANTEY_OPTION_NO)
        option.click()
    
    def choose_antey_yes_setting(self):
        """
        Set the antey to the 'yes' setting
        """
        option = self.driver.find_element(*MainPageLocators.ANTEY_OPTION_YES)
        option.click()

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
    
    def fill_input_field(self, text):
        # get the element
        input_field = self.driver.find_element(*MainPageLocators.INPUT_FIELD)
        
        # clear and fill the input
        input_field.clear()
        input_field.send_keys(text)

    def get_output_field(self):
        output_field = self.driver.find_element(*MainPageLocators.OUTPUT_FIELD)       
        return output_field