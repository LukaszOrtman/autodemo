import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from helpers.wrappers import screenshot_decorator
from helpers.base_test_class import BaseTestClass

class LostHatSanityTests2(BaseTestClass):

    @screenshot_decorator
    def test_searching_particular_product_by_searchbox(self):

        driver = self.conf_driver
        driver.get(self.base_url)

        searching_phrase = 'HUMMINGBIRD'
        expected_element_name = 'Hummingbird Printed Sweater'

        searching_box = driver.find_element(By.XPATH, '//*[@id="search_widget"]/form/input[2]')
        searching_box.send_keys(searching_phrase)
        searching_box.send_keys(Keys.ENTER)

        searching_element_row = driver.find_elements(By.XPATH, '//*[@id="js-product-list"]/div[1]')

        found_elements_number = 0

        for element in searching_element_row:
            if expected_element_name in element.text:
                found_elements_number = found_elements_number + 1

        self.assertEqual(1, found_elements_number,
                         f"We expect 1 and actual number of found items is {found_elements_number}")

