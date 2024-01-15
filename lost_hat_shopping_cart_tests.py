from selenium.webdriver.common.by import By
from helpers import optional_helpers as oh
from helpers.wrappers import screenshot_decorator
from helpers.base_test_class import BaseTestClass
import time


class LostHatShoppingCartTests(BaseTestClass):

    @screenshot_decorator
    def test_adding_product_to_the_shopping_cart(self):

        expected_confirmation_modal_text = '\ue876Product successfully added to your shopping cart'
        item_xpath = '//*[@alt="Mountain fox - Vector graphics"]'
        shopping_cart_button_xpath = '//*[@class="btn btn-primary add-to-cart"]'
        confirmation_modal_title_xpath = '//*[@id="myModalLabel"]'

        driver = self.conf_driver
        driver.get(self.subpage_art_url)

        item_element = driver.find_element(By.XPATH, item_xpath)
        item_element.click()

        shopping_cart_button_element = driver.find_element(By.XPATH, shopping_cart_button_xpath)
        shopping_cart_button_element.click()
        time.sleep(3)

        confirmation_modal_element = oh.visibility_of_element_wait(driver, confirmation_modal_title_xpath)
        self.assertEqual(expected_confirmation_modal_text, confirmation_modal_element.text)

    @screenshot_decorator
    def test_adding_multiple_items_to_shopping_cart(self):
        expected_cart_products_count_xpath = '(2)'
        item_xpath = '//*[@alt="Mountain fox - Vector graphics"]'
        shopping_cart_button_xpath = '//*[@class="btn btn-primary add-to-cart"]'
        confirmation_modal_title_xpath = '//*[@id="myModalLabel"]'
        continue_shopping_button_xpath = '//*[@class="btn btn-secondary"]'
        cart_products_count_xpath = './/*[@class="cart-products-count"]'

        driver = self.conf_driver
        driver.get(self.subpage_art_url)

        item_element = driver.find_element(By.XPATH, item_xpath)
        item_element.click()

        # adding product 1:
        shopping_cart_button_element = driver.find_element(By.XPATH, shopping_cart_button_xpath)
        shopping_cart_button_element.click()
        oh.visibility_of_element_wait(driver, confirmation_modal_title_xpath)
        continue_shopping_button_element = driver.find_element(By.XPATH, continue_shopping_button_xpath)
        continue_shopping_button_element.click()


        # adding product 2:
        shopping_cart_button_element.click()
        oh.visibility_of_element_wait(driver, confirmation_modal_title_xpath)
        continue_shopping_button_element = oh.visibility_of_element_wait(driver, continue_shopping_button_xpath)
        continue_shopping_button_element.click()


        cart_products_count_element = oh.visibility_of_element_wait(driver, cart_products_count_xpath)
        observed_cart_products_count = cart_products_count_element.text


        self.assertEqual(expected_cart_products_count_xpath, observed_cart_products_count)



