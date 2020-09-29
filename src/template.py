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
    pass