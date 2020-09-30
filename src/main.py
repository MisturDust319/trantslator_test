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

    # test the body
    # check that default translation settings are working
    page.fill_input_field("the quick brown fox jumped over the lazy dog")
    page.click_translate_button()
    # get the output field
    output_field = page.get_output_field()
    # check the output field's value
    assert output_field.text == "THE QUICK BROWN FOX JUMPED OVER THE LAZY DOG"
    
    # open the options panel
    page.toggle_advanced_options()

    # change the spacing option to double space
    page.choose_doublespace_setting()
    page.click_translate_button()
    # get the output field
    output_field = page.get_output_field()
    # check the output field's value
    assert output_field.text == "THE  QUICK  BROWN  FOX  JUMPED  OVER  THE  LAZY  DOG"

    # change the spacing option to monospace and antey option
    # change the input text to something that will trigger the "ant" substitution
    page.fill_input_field("yes we can")
    page.choose_monospace_setting()
    page.choose_antey_yes_setting()
    page.click_translate_button()
    # get the output field
    output_field = page.get_output_field()
    # check the output field's value
    assert output_field.text == "YES WE CANT"

    # change the spacing option to doublespace and antey option
    # change the input text to something that will trigger the "ant" substitution
    page.fill_input_field("yes we can")
    page.choose_doublespace_setting()
    page.click_translate_button()
    # get the output field
    output_field = page.get_output_field()
    # check the output field's value
    assert output_field.text == "YES  WE  CANT"

    # test the footer
    assert footer.check_for_hr1() is True, "hr 1 not found in footer"
    assert footer.get_pages_heading() == "PAGES", "PAGES heading in footer wrong"
    assert footer.get_home_link() == "https://www.trantslator.com/", "Home link in footer wrong"
    assert footer.get_help_link() == "https://www.trantslator.com/help/", "Help link in footer wrong"
    assert footer.get_about_link() == "https://www.trantslator.com/about/", "About link in footer wrong"
    
    assert footer.check_for_hr2() is True, "hr 2 not found in footer"
    
    assert footer.get_external_links_header() == "LINKS", "LINKS heading in footer wrong"
    assert footer.get_twitter_link() == "https://twitter.com/hermetikosmedia", "Twitter link in footer wrong"
    assert footer.check_for_twitter_svg() is True, "Twitter link SVG not found"
    assert footer.get_instagram_link() == "https://instagram.com/stan_the_freelancer?igshid=a2r2ytdwa2ys", "Instagram link in footer wrong"
    assert footer.check_for_instagram_svg() is True, "Instagram link SVG not found"
    assert footer.get_website_link() == "https://www.hermetikos.com/", "Website link in footer wrong"
    assert footer.check_for_website_svg() is True, "Website link SVG not found"
    

