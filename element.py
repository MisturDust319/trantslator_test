from selenium.webdriver.support.ui import WebDriverWait

class BasePageElement(object):
    """
    This will represent an element on the page
    Like a search bar or menu
    """

    def __set__(self, obj, value):
        driver = obj.driver
        
        # wait until we can find the element described by locator
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element_by_name(self.locator))

        # now that the element is available, clear it and search for value
        driver.find_element_by_name(self.locator).clear()
        driver.find_element_by_name(self.locator).send_keys(value)
    
    def __get__(self, obj, owner):
        driver = obj.driver
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element_by_name(self.locator))
        
        # once the element is located
        # return the element's value
        element = driver.find_element_by_name(self.locator)
        return element.get_attributes_value("value")