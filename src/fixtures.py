"""
Fixtures for the site tests
"""
from os import environ
import pytest
from selenium import webdriver

# CONSTANTS

# the URL of the selenium hub container
# HUB_HOST = environ["HUB_HOST"]
HUB_PORT = environ["HUB_PORT"]
# REMOTE_WEBDRIVER_URL = f"http://{HUB_HOST}:{HUB_PORT}/wd/hub"
REMOTE_WEBDRIVER_URL = f"http://hub:{HUB_PORT}/wd/hub"

@pytest.fixture(scope="class")
def set_up_driver():
    """
    A fixture factory that will set up a driver in the specified page
    """
    def _set_up_driver(url):
        # create the webdriver object
        # first set up the options
        # options = webdriver.FirefoxOptions()
        # options = webdriver.Options()
        # set it to headless mode
        # options.headless = True      
        # initialize the webdriver
        # driver = webdriver.Firefox(options=options)
        # driver = webdriver.Remote(command_executor=REMOTE_WEBDRIVER_URL,
        #     options=options)
        capabilities = webdriver.DesiredCapabilities.FIREFOX
        driver = webdriver.Remote(command_executor=REMOTE_WEBDRIVER_URL, desired_capabilities=capabilities)
        # grab the site specified by url
        driver.get(url)

        return driver
            
    return _set_up_driver

@pytest.fixture(scope="class")
def set_up_driver_chrome():
    capabilities = webdriver.DesiredCapabilities.CHROME
    driver = webdriver.Remote(command_executor=REMOTE_WEBDRIVER_URL,
        desired_capabilities=capabilities)
    
    return driver

@pytest.fixture(scope="class")
def set_up_driver_firefox():
    capabilities = webdriver.DesiredCapabilities.FIREFOX
    driver = webdriver.Remote(command_executor=REMOTE_WEBDRIVER_URL,
        desired_capabilities=capabilities)
    
    return driver

# @pytest.fixture
# def set_up_header(driver):
#     """
#     A fixture factory that will set up the header templates
#     """
#     header = HeaderTemplate(driver)
#     return header


# @pytest.fixture
# def set_up_footer(driver):
#     """
#     A fixture factory that will set up the footer templates
#     """
#     footer = FooterTemplate(driver)
#     return footer
