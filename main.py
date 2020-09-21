import unittest
from selenium import webdriver
import page

class TrantslatorTest(unittest.TestCase):
    def setUp(self):
        options = webdriver.FirefoxOptions()
        options.headless = True
        
        self.driver = webdriver.Firefox(options=options)
        self.driver.get("https://www.trantslator.com/")

    def tearDown(self):
        self.driver.close()
    
    def test_title(self):
        mainPage = page.MainPage(self.driver)
        assert mainPage.is_title_matches()
    
    def test_search_python(self):
        mainPage = page.MainPage(self.driver)
        assert mainPage.is_title_matches()
        mainPage.search_text_element = "pycon"
        mainPage.click_go_button()
        search_page_result = page.SearchResultPage(self.driver)
        assert search_page_result.is_results_found()

if __name__ == "__main__":
    unittest.main()