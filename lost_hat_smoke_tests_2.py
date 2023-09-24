import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class LostHatSmokeTests2(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(options=options)
        self.url = 'https://autodemo.testoneo.com/en/'

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

    def test_searching_product_by_searchbox(self):
        driver = self.driver
        driver.get(self.url)
        search_box = driver.find_element(By.XPATH, '//*[@id="search_widget"]/form/input[2]')
        searching_product = "mug"
        search_box.send_keys(searching_product)
        search_box.send_keys(Keys.ENTER)

        row_searching_product = driver.find_element(By.XPATH, '//*[@id="js-product-list"]/div[1]')
        product_element_count = row_searching_product.get_attribute("childElementCount")
        product_element_count_in_type_int = int(product_element_count)

        expected_searching_product = 5

        if expected_searching_product == product_element_count_in_type_int:
            print ("Everything is ok.")
        else:
            print("Something went wrong!")

