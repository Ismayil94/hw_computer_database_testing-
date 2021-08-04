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



class AddComputerTest(unittest.TestCase):
    """
        Test for adding computer
            Steps:
                1. Generating for fake data
    """

    computer = {
            "name": "Ismayil",
            "introduce": '2021-08-02',
            "discontinued": '2021-08-02',
            'select_option': '2'
        }

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

    def test_add_button_existance(self):
        self.driver.get(self.url)

        button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, 'add')))
        
        self.assertIsInstance(button, selenium.webdriver.remote.webelement.WebElement, "Result is not Button type!")

    def test_add_computer_form_full(self):
        self.driver.get(self.url)

        add_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, 'add'))).click()

        # Form fields

        name_field =  WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, 'name'))) 
        introduce_field = self.driver.find_element_by_id('introduced')
        discontinued_field = self.driver.find_element_by_id('discontinued')
        select_field = Select(self.driver.find_element_by_id('company'))

        # Filling form data

        name_field.send_keys(self.computer['name'])
        introduce_field.send_keys(self.computer['introduce'])
        discontinued_field.send_keys(self.computer['discontinued'])
        select_field.select_by_value(self.computer['select_option'])

        submit = self.driver.find_element_by_css_selector(".btn.primary[value='Create this computer']")
        submit.click()

        self._search(self.computer["name"])
        # expecting failure
        self.assertNotEqual(self.assertIsNotNone(self.driver.find_elements_by_xpath(f"""//*[@id="main"]/table/tbody/tr[1]/td[1]/a""")), None, "Add computer form when fully filled not works!")

    def test_add_form_required_fields_only(self):
        self.driver.get(self.url)
        add_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, 'add'))).click()

        

        name_field =  WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, 'name')))
        introduce_field = self.driver.find_element_by_id('introduced')
        discontinued_field = self.driver.find_element_by_id('discontinued')
        select_field = Select(self.driver.find_element_by_id('company'))

        name_field.send_keys(self.computer['name'])

        submit = self.driver.find_element_by_css_selector(".btn.primary[value='Create this computer']")
        submit.click()

        self._search(self.computer["name"])
        # expecting failure
        self.assertNotEqual(self.assertIsNotNone(self.driver.find_elements_by_xpath(f"""//*[@id="main"]/table/tbody/tr[1]/td[1]/a""")), None, "Add computer form when required fields only filled not works!")

    def test_add_computer_form_partially(self):
        self.driver.get(self.url)
        add_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, 'add'))).click()

        

        name_field =  WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, 'name')))
        introduce_field = self.driver.find_element_by_id('introduced')
        discontinued_field = self.driver.find_element_by_id('discontinued')
        select_field = Select(self.driver.find_element_by_id('company'))

        name_field.send_keys(self.computer['name'])
        introduce_field.send_keys(self.computer['introduce'])
        select_field.select_by_value(self.computer['select_option'])

        submit = self.driver.find_element_by_css_selector(".btn.primary[value='Create this computer']")
        submit.click()

        self._search(self.computer["name"])        
        # expecting failure
        self.assertNotEqual(self.assertIsNotNone(self.driver.find_elements_by_xpath(f"""//*[@id="main"]/table/tbody/tr[1]/td[1]/a""")), None, "Add computer form when partially filled not works!")


    def tearDown(self):
        self.driver.close()    

if __name__ == '__main__':
    unittest.main(verbosity=2)