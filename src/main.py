import pytest
from selenium import webdriver

from page import MainPage
from template import HeaderTemplate, FooterTemplate

BASE_URL = "https://www.trantslator.com/"


@pytest.fixture
def set_up_page():
    """
    A fixture factory that will set up a driver in the specified page
    """
    def _set_up_page(url):
        # create the webdriver object
        options = webdriver.FirefoxOptions()
        # set it to headless mode
        options.headless = True      
        # initialize the object
        driver = webdriver.Firefox(options=options)

        # grab the site specified by url
        driver.get(url)
        
        # create the corresponding header and footer elements for the page
        header = HeaderTemplate(driver)
        footer = FooterTemplate(driver)

        return driver, header, footer
    
    return _set_up_page


@pytest.mark.home
def test_home_page(set_up_page):
    # set up the driver, header, and footer
    driver, header, footer = set_up_page(BASE_URL)
    # pass it to the Main Page object
    page = MainPage(driver)

    # test the page title is correct
    assert page.getPageTitle() == "TRANTSLATOR | HOME"

    # test the header
    assert header.check_for_header() is True, "Header not found"
    assert header.check_header_title() is True, "Header title incorrect"
    assert header.check_for_icon() is True, "Icon not found"
