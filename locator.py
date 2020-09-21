# it is best practice to put an CSS selector, id, etc in one location
# if we need to change them, it's easier to do it from one location

from selenium.webdriver.common.by import By

class MainPageLocators(object):
    """
    Define a class to hold all the locators for the main page
    """
    # GO_BUTTON = (By.ID, "submit") # (how we access the element, what that value should be)
    ANTVANCED_OPTIONS_BUTTON = (By.NAME, "ANTVANCED OPTIONS")

class SearchResultsPageLocators(object):
    """
    if you have to define locators for the search results, define them here
    """
    pass