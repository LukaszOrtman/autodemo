from helpers.wrappers import screenshot_decorator
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from helpers.base_test_class import BaseTestClass
import time



class CheckProductSizeChange(BaseTestClass):

   @screenshot_decorator
   def test_check_product_size_change(self):
      expected_product_changed_size = 'L'
      size_select_xpath = '//*[@id="group_1"]'
      driver = self.driver
      driver.get(self.man_t_shirt_url)

      product_size_select_element = driver.find_element(By.XPATH, size_select_xpath)

      product_size_select = Select(product_size_select_element)

      product_size_select.select_by_visible_text(expected_product_changed_size)

      observed_product_size_changed_text = product_size_select.first_selected_option.text

      self.assertEqual(expected_product_changed_size, observed_product_size_changed_text, f'SMTH IS WRONG!')




