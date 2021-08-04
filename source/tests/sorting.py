import os
import unittest
import warnings
from datetime import datetime
from . import utils


import selenium
from selenium import webdriver
from selenium.webdriver.firefox.firefox_profile import WEBDRIVER_EXT
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys



class SortingTest(unittest.TestCase):
    """
    Testing all 4 types of sorting functionality:
        - sorting by computer name
        - sorting by company name
        - sorting by introduced date
        - sorting by discontinued date
    """
    def setUp(self):
        self.url = 'https://computer-database.gatling.io/computers'
        warnings.simplefilter('ignore', ResourceWarning)
        
        caps = {'browserName': os.getenv('BROWSER', 'chrome')}
        
        self.driver = webdriver.Remote(
            command_executor='http://localhost:4444/wd/hub',
            desired_capabilities=caps
        )
    
    def test_sorting_by_name(self):
        """
            Test Case for name sort button functionality
                Steps:
                    1. Parse data from ascending order view
                    2. Get descending order url by clicking sort_button
                    3. Reverse sort of list by  name property of dictionary
                    4. Checking equality between reverse_sorted_ascending and  descending order
        """
        self.driver.get("https://computer-database.gatling.io/computers?p=0&n=10000&s=name&d=asc") # URL of Sorting in ascending order by computer name which shows first 1000 rows which contains all of our database
        
        ascending_order = utils.get_table_data(self.driver.current_url)
        
        sort_button = self.driver.find_element_by_css_selector('#main > table > thead > tr > th.col-name.header.headerSortUp > a')
        sort_button.click()
        
        descending_order = utils.get_table_data(self.driver.current_url) # Current_url after clicking sort_button basicly means desc. order by computer name

        reverse_sorted_ascending = sorted(ascending_order, key=lambda x: x['name'], reverse=True) # sorting ascending_order list by name property of dictionaries

        self.assertEqual(reverse_sorted_ascending, descending_order, "Name Sort not works properly")


    def test_sorting_by_company(self):
        """
            Test Case for company name sort button functionality
                Steps:
                    1. Parse data from ascending order view
                    2. Get descending order url by clicking sort_button
                    3. Reverse sort of list by  company name property of dictionary
                    4. Checking equality between reverse_sorted_ascending and  descending order
        """
        self.driver.get("https://computer-database.gatling.io/computers?p=0&n=1000&s=companyName&d=asc")
        
        ascending_order = utils.get_table_data(self.driver.current_url)
        
        sort_button = self.driver.find_element_by_css_selector('#main > table > thead > tr > th.col-company.header > a')
        sort_button.click()
        
        WebDriverWait(self.driver, 5)
        descending_order = utils.get_table_data(self.driver.current_url)

        reverse_sorted_ascending = sorted(ascending_order, key=lambda x: x['company'], reverse=True)
        
        self.assertEqual(reverse_sorted_ascending, descending_order, "Company Sort not works properly")

    def test_sorting_by_discontinued(self):
        """
            Test Case for discontinued sort button functionality
                Steps:
                    1. Parse data from ascending order view
                    2. Get descending order url by clicking sort_button
                    3. Reverse sort of list by  discontinued propery of dictionary
                    4. Checking equality between reverse_sorted_ascending and  descending order
        """
        self.driver.get("https://computer-database.gatling.io/computers?p=0&n=1000&s=discontinued&d=asc")
        
        ascending_order = utils.get_table_data(self.driver.current_url)
        
        sort_button = self.driver.find_element_by_css_selector('#main > table > thead > tr > th.col-discontinued.header.headerSortUp > a')
        sort_button.click()
        
        WebDriverWait(self.driver, 5)
        descending_order = utils.get_table_data(self.driver.current_url)

        reverse_sorted_ascending = sorted(ascending_order, key= lambda x : x['discontinued'] , reverse=True)
        
        self.assertEqual(reverse_sorted_ascending, descending_order, "Sort by discontinued date not works properly")
    
    def test_sorting_by_introduced(self):
        """
            Test Case for introduced sort button functionality
                Steps:
                    1. Parse data from ascending order view
                    2. Get descending order url by clicking sort_button
                    3. Reverse sort of list by  introduced propery of dictionary
                    4. Checking equality between reverse_sorted_ascending and  descending order
        """
        self.driver.get("https://computer-database.gatling.io/computers?p=0&n=1000&s=introduced&d=asc")
       
        ascending_order = utils.get_table_data(self.driver.current_url)
       
        sort_button = self.driver.find_element_by_css_selector('#main > table > thead > tr > th.col-introduced.header.headerSortUp > a')
        sort_button.click()
       
        WebDriverWait(self.driver, 5)
        descending_order = utils.get_table_data(self.driver.current_url)

        reverse_sorted_ascending = sorted(ascending_order, key= lambda x : x['introduced'] , reverse=True)
        
        self.assertEqual(reverse_sorted_ascending, descending_order, "Sort by introduced date not works properly")

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main(verbosity=2)