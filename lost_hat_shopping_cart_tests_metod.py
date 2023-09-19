import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By


class LostHatShoppingCartTests(unittest.TestCase):

    def setUp(self):
        self.subpage_art_url = 'https://autodemo.testoneo.com/en/9-art'
        max_seconds_to_wait = 3
        number_of_expected_elements = 1

        options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(options=options)
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.quit()

    def test_adding_product_to_the_shopping_cart(self, confirmation_modal_element=None):
        expected_confirmation_modal_text = '\ue876Product successfully added to your shopping cart'
        product_xpath = '//*[@alt="Mountain fox - Vector graphics"]'
        shopping_card_button_xpath = '//*[@class="btn btn-primary add-to-cart"]'
        confirmation_modal_title_xpath = '//*[@id="myModalLabel"]'


        driver = self.driver
        driver.get(self.subpage_art_url)

        product_element = driver.find_element(By.XPATH, product_xpath)
        product_element.click()

        shopping_card_button_element = driver.find_element(By.XPATH, shopping_card_button_xpath)
        shopping_card_button_element.click()

        """confirmation_modal_element = WebDriverWait(driver, 4).until(
            EC.visibility_of_element_located((By.XPATH, confirmation_modal_title_xpath)))
"""
        # confirmation_modal_element = oh.visibility_of_element_wait(driver, confirmation_modal_title_xpath)
        self.assertEqual(expected_confirmation_modal_text, confirmation_modal_element.text)
