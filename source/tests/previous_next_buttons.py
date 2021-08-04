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



class PreviousButtonTest(unittest.TestCase):
    """
        Testing functionality of Previous Button
            Steps:
                1. Test whether button generates
                2. Test whether button is disabled on first page of table
                3. Test functionality of previous button 
    """
    def setUp(self):
        self.url = 'https://computer-database.gatling.io/computers'
        warnings.simplefilter('ignore', ResourceWarning)
        
        caps = {'browserName': os.getenv('BROWSER', 'chrome')}
        
        self.driver = webdriver.Remote(
            command_executor='http://localhost:4444/wd/hub',
            desired_capabilities=caps
        )
    
    def test_previous_button_exists_on_first_page(self):
        self.driver.get(self.url)

        prev_button = self.driver.find_element_by_css_selector("#pagination > ul > li.prev > a")

        self.assertIsNotNone(prev_button, "Previous button not exists on first page")
    
    def test_previous_disabled_on_first_page(self):
        self.driver.get(self.url)
        
        prev_button = self.driver.find_element_by_css_selector("#pagination > ul > li.prev")
        
        self.assertIn('disabled', prev_button.get_attribute('class').split(), "Previous button is not disabled on first page") # checking by disables class

    def test_previous_button_functionality(self):
        """
            Test case for functionality of previous button 
        """
        first_page_table_data = utils.get_table_data(self.url)

        self.driver.get('https://computer-database.gatling.io/computers?p=1&n=10&s=name&d=asc') # URL of second page
        
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#pagination > ul > li.prev > a")))
        prev_button = self.driver.find_element_by_css_selector("#pagination > ul > li.prev > a")
        prev_button.click()

        data = utils.get_table_data(self.driver.current_url) #URL of first page


        self.assertEqual(first_page_table_data, data, "Previous button not working properly")

    
    def tearDown(self):
        self.driver.close()


class NextButtonTest(unittest.TestCase):
    """
        Testing functionality of Next Button
            Steps:
                1. Test whether button generates
                2. Test whether button is disabled on first page of table
                3. Test functionality of next button 
    """
    def setUp(self):
        self.url = 'https://computer-database.gatling.io/computers'
        warnings.simplefilter('ignore', ResourceWarning)
        
        caps = {'browserName': os.getenv('BROWSER', 'chrome')}
        
        self.driver = webdriver.Remote(
            command_executor='http://localhost:4444/wd/hub',
            desired_capabilities=caps
        )
    
    def test_next_button_exists_on_last_page(self):
        self.driver.get("https://computer-database.gatling.io/computers?p=57&n=10&s=name&d=asc")
        
        next_button = self.driver.find_element_by_css_selector("#pagination > ul > li.next > a")
        
        self.assertIsNotNone(next_button, "Next button not exists on last page")
    
    def test_next_disabled_on_last_page(self):
        self.driver.get("https://computer-database.gatling.io/computers?p=57&n=10&s=name&d=asc")
        
        next_button = self.driver.find_element_by_css_selector("#pagination > ul > li.next")

        self.assertIn('disabled', next_button.get_attribute('class').split(), "Next button is not disabled on last page")

    def test_previous_button_functionality(self):
        second_page = utils.get_table_data("https://computer-database.gatling.io/computers?p=1&n=10&s=name&d=asc") # url of 2nd page

        self.driver.get('https://computer-database.gatling.io/computers?p=0&n=10&s=name&d=asc')
        
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#pagination > ul > li.next > a")))
        next_button = self.driver.find_element_by_css_selector("#pagination > ul > li.next > a")
        next_button.click()

        data = utils.get_table_data(self.driver.current_url) #url of first page


        self.assertEqual(second_page, data, "Next button not working properly")

# nothing to verify on big pages
    
    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main(verbosity=2)