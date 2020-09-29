from locator import HeaderLocators, FooterLocators

class Template:
    """
    Represents a template on a website, reusable collections of elements
    that should be tested to be functioning as intended on each page
    Using a template object is meant to avoid boilerplate code
    """
    def __init__(self, driver):
        """
        Each template element needs access to the driver
        so it can be used to test for elements
        """
        self.driver = driver

    def check_for_element(self, locator):
        try:
            self.driver.find_element(*locator)
        except NoSuchElementException:
            return False
        return True

class HeaderTemplate(Template):
    def check_for_header(self):
        return self.check_for_element(HeaderLocators.HEADER_ELEMENT)

    def check_header_title(self):
        return self.driver.find_element(*HeaderLocators.TITLE).text == "TRANTSLATOR"
    
    def check_for_icon(self):
        return self.check_for_element(HeaderLocators.ICON)

class FooterTemplate(Template):
    def check_for_hr1(self):
        return self.check_for_element(FooterLocators.HR_1)
    
    def get_pages_heading(self):
        return self.driver.find_element(*FooterLocators.PAGES_HEADING).text

    def get_home_link(self):
        return self.driver.find_element(*FooterLocators.HOME_LINK).get_attribute('href')
    
    def get_help_link(self):
        return self.driver.find_element(*FooterLocators.HELP_LINK).get_attribute('href')
    
    def get_about_link(self):
        return self.driver.find_element(*FooterLocators.ABOUT_LINK).get_attribute('href')
    
    def check_for_hr2(self):
        return self.check_for_element(FooterLocators.HR_2)

    def get_external_links_header(self):
        return self.driver.find_element(*FooterLocators.EXTERNAL_LINKS_HEADER).text

    def get_twitter_link(self):
        return self.driver.find_element(*FooterLocators.TWITTER_LINK).get_attribute('href')
    
    def check_for_twitter_svg(self):
        return self.check_for_element(FooterLocators.TWITTER_SVG)

    def get_instagram_link(self):
        return self.driver.find_element(*FooterLocators.INSTAGRAM_LINK).get_attribute('href')
    
    def check_for_instagram_svg(self):
        return self.check_for_element(FooterLocators.INSTAGRAM_SVG)
    
    def get_website_link(self):
        return self.driver.find_element(*FooterLocators.WEBSITE_LINK).get_attribute('href')
    
    def check_for_website_svg(self):
        return self.check_for_element(FooterLocators.WEBSITE_SVG)