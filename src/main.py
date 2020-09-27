import pytest
from selenium import webdriver
from page import MainPage

BASE_URL = "https://www.trantslator.com/"


@pytest.fixture
def set_up_driver():
    """
    A fixture factory that will set up a driver in the specified page
    """
    def _set_up_driver(url):
        # create the webdriver object
        options = webdriver.FirefoxOptions()
        # set it to headless mode
        options.headless = True      
        # initialize the object
        driver = webdriver.Firefox(options=options)

        # grab the site specified by url
        driver.get(url)

        # return the driver
        return driver
    
    return _set_up_driver

@pytest.mark.home
def test_home_page(set_up_driver):
    # set up the driver
    driver = set_up_driver(BASE_URL)
    # pass it to the Main Page object
    page = MainPage(driver)

    # test the page title is correct
    assert page.getPageTitle() == "TRANTSLATOR | HOME"

    # test the header