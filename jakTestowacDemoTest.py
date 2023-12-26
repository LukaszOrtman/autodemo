import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from helpers import functional_helpers
from helpers.wrappers import screenshot_decorator
from helpers.base_test_class import BaseTestClass

import time

class ProductTests(BaseTestClass):

   def assert_elemnt_text(self,driver, xpath, expected_text):
       self.header = driver.find_element(By.XPATH, xpath )
       header_text = self.header.text
       self.assertEqual(expected_text, header_text,
                        f'Expected login button text: log in to your account , differ from actual {header_text}')
   @screenshot_decorator
   def test_checking_header_is_log_in_to_your_account(self):
       driver = self.conf_driver
       driver.get(self.url_log_page)
       self.assert_elemnt_text(driver, '//*[@id="main"]/header/h1', expected_text='Log in to your account')
       time.sleep(2)


#metoda user_correct_login
class ProductTests_1(BaseTestClass):

   @screenshot_decorator
   def test_user_login(self):
       driver=self.conf_driver
       driver.get(self.url_log_page)
       functional_helpers.user_login(driver, self.user_mail, self.user_password)

class ProductTests_2(BaseTestClass):

    def fill_input(self, driver, xpath, value):
        self.input_box = driver.find_element(By.XPATH, xpath)
        self.input_box.clear()
        self.input_box.send_keys(value)

    @screenshot_decorator
    def test_sign_in_using_fake_email_and_password(self):
        driver = self.conf_driver
        driver.get(self.url_log_page)

        # finding password box 1 and fill in faild email
        self.fill_input(self.driver, '//*[@id="login-form"]/section/div[1]/div[1]/input', self.fail_email)

        # finding password box 2 and fill in faild password
        self.fill_input(self.driver, '//*[@id="login-form"]/section/div[2]/div[1]/div/input', self.fail_password)

        sign_in_button = driver.find_element(By.XPATH, '//*[@id="submit-login"]')
        sign_in_button.click()
        time.sleep(2)

        # checking alert information
        faild_sign_alert = driver.find_element(By.XPATH, '//*[@id="content"]/section/div/ul/li')
        faild_sign_alert_text = faild_sign_alert.text
        self.assertEqual(self.fail_alert, faild_sign_alert_text,
                         f"If you don't see this message, probably your email and password are correct")

        time.sleep(3)

class ProductTests_3(BaseTestClass):

    @screenshot_decorator
    def test_checking_product_on_website(self):
        driver = self.conf_driver
        driver.get(self.url)
        expected_tshirt_name='HUMMINGBIRD PRINTED T-SHIRT'
        tshirt_name = driver.find_element(By.XPATH, '//*[@id="main"]/div[1]/div[2]/h1')
        tshirt_name_text = tshirt_name.text
        self.assertEqual(expected_tshirt_name, tshirt_name_text,
                         f'Expected tshirt name: HUMMINGBIRD PRINTED T-SHIRT , differ from actual {tshirt_name_text}')
        time.sleep(2)

    @screenshot_decorator
    def test_checking_product_price_on_website(self):
        driver = self.conf_driver
        driver.get(self.url)
        expected_tshirt_price='PLN23.52'
        tshirt_price = driver.find_element(By.XPATH, '//*[@id="main"]/div[1]/div[2]/div[1]/div[2]/div/span[1]')
        tshirt_price_text = tshirt_price.text
        self.assertEqual(expected_tshirt_price, tshirt_price_text,
                         f'Expected tshirt price: PLN23.52 , differ from actual {tshirt_price_text}')
        time.sleep(2)

