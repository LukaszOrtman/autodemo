import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.events import EventFiringWebDriver
from helpers.screenshot_listener import ScreenshotListener
from helpers.wrappers import screenshot_decorator
import config_reader
from selenium.webdriver.common.by import By


class LostHatSmokeTests(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        config = config_reader.load()
        self.base_url = config["base_url"]
        self.url_clothes_page = self.base_url + '3-clothes'
        self.url_accessories_page = self.base_url + '6-accessories'
        self.url_art_page = self.base_url + '9-art'
        self.url_log_page = self.base_url + 'login?back=my-account'

        options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(options=options)

        self.ef_driver = EventFiringWebDriver(self.driver, ScreenshotListener())

    @classmethod
    def tearDownClass(self):
        self.ef_driver.quit()

    @screenshot_decorator
    def test_base_page_title(self):
        expected_title = 'Lost Hat'
        self.assert_title(self.base_url, expected_title)

    @screenshot_decorator
    def test_art_page_website_title(self):
        expected_name_art_page = "Art"
        self.assert_title(self.url_art_page, expected_name_art_page)

    @screenshot_decorator
    def test_clothes_page_website_title(self):
        expected_name_clothes_page = "Clothes"
        self.assert_title(self.url_clothes_page, expected_name_clothes_page)

    @screenshot_decorator
    def test_accessories_website_title(self):
        expected_name_accessories_page = "Accessories"
        self.assert_title(self.url_accessories_page, expected_name_accessories_page)

    @screenshot_decorator
    def test_log_page_website_title(self):
        expected_name_log_page = "Login"
        self.assert_title(self.url_log_page, expected_name_log_page)

    @screenshot_decorator
    def test_searching_product_by_searchbox(self):
        searching_product = "mug"
        expected_searching_product = 5
        search_input_xpath = '//*[@name="s"]'
        result_element_xpath = '//*[@class="product-miniature js-product-miniature"]'

        self.ef_driver.get(self.base_url)
        search_input_element = self.ef_driver.find_element(By.XPATH, search_input_xpath)
        search_input_element.send_keys(searching_product)
        search_input_element.send_keys(Keys.ENTER)
        result_elements = self.ef_driver.find_elements(By.XPATH, result_element_xpath)
        self.assertGreaterEqual(len(result_elements), expected_searching_product,
                                f'Actual number of elements found: {len(result_elements)}; expected was {expected_searching_product} or more')

    def get_page_title(self, url):
        self.ef_driver.get(url)
        return self.ef_driver.title

    def assert_title(self, url, expected_title):
        actual_title = self.get_page_title(url)
        self.assertEqual(expected_title, actual_title,
                         f'Expected {expected_title} differ from actual title {actual_title} on page: {url}')
