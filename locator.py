# it is best practice to put an CSS selector, id, etc in one location
# if we need to change them, it's easier to do it from one location

from selenium.webdriver.common.by import By

class MainPageLocators(object):
    """
    Define a class to hold all the locators for the main page
    """
    # text fields
    INPUT_FIELD = (By.XPATH, "//div[@class='input']/textarea")
    OUTPUT_FIELD = (By.XPATH, "//div[@class='output']/textarea")

    # buttons
    ANTVANCED_OPTIONS_BUTTON = (By.XPATH, "//div[@class='input']/button[1]")
    TRANTSLATE_BUTTON = (By.XPATH, "//div[@class='input']/button[2]")
    COPY_BUTTON = (By.XPATH, "//outbut[@class='input']/button")

    # dropdowns
    SPACING_DROPDOWN = (By.ID, 'spacing between words')
    ANTEY_DROPDOWN = (By.ID, 'make it more ant-ey')

    # text elements
    SPACING_LABEL = (By.XPATH, "//div[@class='options']/label[1]")
    ANTEY_LABEL = (By.XPATH, "//div[@class='options']/label[2]")

class HeaderLocators(object):
    # header
    TITLE = (By.XPATH, "//header/h1")
    ICON = (By.XPATH, "//header/*[name()='svg']")

class FooterLocators(object):
    # internal links
    HR_1 = (By.XPATH, "//footer/hr[1]")
    PAGES_HEADER = (By.XPATH, "//div[@class='footer-link'][1]/h3")
    HOME_LINK = (By.XPATH, "//div[@class='footer-link'][1]/ul/li[1]/a")
    HELP_LINK = (By.XPATH, "//div[@class='footer-link'][1]/ul/li[2]/a")
    ABOUT_LINK = (By.XPATH, "//div[@class='footer-link'][1]/ul/li[3]/a")
    
    HR_2 = (By.XPATH, "//footer/hr[2]")

    # external links
    EXTERNAL_LINKS_HEADER = (By.XPATH, "//div[@class='footer-link'][2]/h3")
    TWITTER_LINK = (By.XPATH, "//div[@class='footer-link'][2]/ul/li[1]/a")
    TWITTER_SVG = (By.XPATH, "//div[@class='footer-link'][2]/ul/li[1]/a/*[name()='svg']")
    INSTAGRAM_LINK = (By.XPATH, "//div[@class='footer-link'][2]/ul/li[2]/a")
    INSTAGRAM_SVG = (By.XPATH, "//div[@class='footer-link'][2]/ul/li[2]/a/*[name()='svg']")
    WEBSITE_LINK = (By.XPATH, "//div[@class='footer-link'][2]/ul/li[3]/a")
    WEBSITE_SVG = (By.XPATH, "//div[@class='footer-link'][2]/ul/li[3]/a/*[name()='svg']")


class SearchResultsPageLocators(object):
    """
    if you have to define locators for the search results, define them here
    """
    pass