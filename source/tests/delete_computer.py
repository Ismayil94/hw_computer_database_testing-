import os
import unittest
import warnings
from . import utils

import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys



class DeleteComputerTest(unittest.TestCase):
    """
        Testing functionality of Delete button
            Steps:
                1. Test whether button generates on a computer info page
                2. Testing button func. by searchin after deleting computer 
    """
    def setUp(self):
        self.url = 'https://computer-database.gatling.io/computers'
        warnings.simplefilter('ignore', ResourceWarning)
        
        caps = {'browserName': os.getenv('BROWSER', 'chrome')}
        
        self.driver = webdriver.Remote(
            command_executor='http://localhost:4444/wd/hub',
            desired_capabilities=caps
        )
    
    def _search(self, key):
        self.driver.get(self.url)

        search_bar = self.driver.find_element_by_id('searchbox')        
        search_button = self.driver.find_element_by_id('searchsubmit')
        
        search_bar.send_keys(key)
        search_button.click()

    def test_delete_function_existance(self):
        self.driver.get(self.url)
        
        computer_url = self.driver.find_element_by_css_selector("#main > table > tbody > tr:nth-child(1) > td:nth-child(1) > a")
        computer_url.click() # opening computer info page

        computer_name = self.driver.find_element_by_css_selector("#name").get_attribute("value") # saving name for search

        delete_button = self.driver.find_element_by_css_selector("#main > form.topRight > input")
        
        self.assertIsInstance(delete_button, selenium.webdriver.remote.webelement.WebElement, "Delete button not exists!")

    def test_delete_button_functionality(self):
        self.driver.get(self.url)

        computer_url = self.driver.find_element_by_css_selector("#main > table > tbody > tr:nth-child(1) > td:nth-child(1) > a")
        computer_url.click()

        computer_name = self.driver.find_element_by_css_selector("#name").get_attribute("value")
        delete_button = self.driver.find_element_by_css_selector("#main > form.topRight > input")

        delete_button.click() # deleting computer

        self._search(computer_name) # searching it on page again
        search_result = utils.get_table_data(self.driver.current_url)
        
        # expecting failure
        self.assertIsNone(search_result, "Delete button not works!")

    def tearDown(self):
        self.driver.close()    

if __name__ == '__main__':
    unittest.main(verbosity=2)