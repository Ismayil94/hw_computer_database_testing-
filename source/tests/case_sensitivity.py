import os
import unittest
import warnings
from . import utils

import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By



class CaseSensitivityTest(unittest.TestCase):
    """
        Testing Case Sensitive Searches
            Steps:
                1. Testing several versions word
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
        search_bar = self.driver.find_element_by_id('searchbox')        
        search_button = self.driver.find_element_by_id('searchsubmit')
        search_bar.send_keys(key)
        search_button.click()

    def test_case_sensitivity(self):
        results = []

        for key in ['ace', 'ACE', 'Ace', 'aCE', 'AcE']: # loop over computer name variation with compination of lower and upper cases
            self.driver.get(self.url)
            self._search(key) # searching them

            results.append(utils.get_table_data(self.driver.current_url))

        for result in results:
            self.assertEqual(result, results[0], "Case Sensitivity Not Working, Results are not equal when searching!")

    def tearDown(self):
        self.driver.close()    

if __name__ == '__main__':
    unittest.main(verbosity=2)