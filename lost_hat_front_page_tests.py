import time
from selenium.webdriver.common.by import By
from helpers.wrappers import screenshot_decorator
from helpers.base_test_class import BaseTestClass


class LostHatFrontPageTests(BaseTestClass):

    @screenshot_decorator
    def test_main_page_website_title(self):
        driver = self.conf_driver
        driver.get(self.base_url)
        expected_name_main_page = "Lost Hat"
        title_main_page = driver.title
        print(title_main_page)
        if title_main_page == expected_name_main_page:
            print("It's ok!")
        else:
            print("Smth goes wrong!")

    @screenshot_decorator
    def test_slider_presentation(self):
        slider_xpath = '//*[@id="carousel"]'
        driver = self.conf_driver
        driver.get(self.base_url)
        driver.find_element(By.XPATH, slider_xpath)

    @screenshot_decorator
    def test_slides_required_title_text(self):
        driver = self.conf_driver
        driver.get(self.base_url)
        expected_text_included_in_slide = "sample"
        slider_xpath_sample_word = '//*[@id="carousel"]/ul/li//*[contains(@class, "text-uppercase")]'

        title_elements = driver.find_elements(By.XPATH, slider_xpath_sample_word)

        for title_element in title_elements:
            title_element_text = title_element.get_attribute("textContent")
            title_element_text_lower = title_element_text.lower()
            with self.subTest(title_element_text_lower):
                self.assertIn(expected_text_included_in_slide, title_element_text_lower,
                              f"Word 'sample' doesn't exist on this slider.")


    @screenshot_decorator
    def test_slider_contain_exact_number_of_slides(self):
        driver = self.conf_driver
        driver.get(self.base_url)
        slider_xpath = '//*[@id="carousel"]/ul/li'
        expected_numbers_of_sliders = 3

        slider_element = driver.find_elements(By.XPATH, slider_xpath)

        actual_numbers_of_sliders = len(slider_element)
        print(actual_numbers_of_sliders)
        self.assertEqual(expected_numbers_of_sliders, actual_numbers_of_sliders,
                         f'Number is differrent, smth is wrong with this {slider_xpath} slider on this website: {self.base_url}')

    @screenshot_decorator
    def test_slider_minimum_size(self):
        expected_min_height = 300
        expected_min_width = 600
        slider_xpath = '//*[@id="carousel"]'
        driver = self.conf_driver
        driver.get(self.base_url)
        slider_element = driver.find_element(By.XPATH, slider_xpath)

        actual_slider_hight = slider_element.size["height"]
        actual_slider_width = slider_element.size["width"]

        with self.subTest('Element height'):
            self.assertLess(expected_min_height, actual_slider_hight,
                            f'Element height found by xpath {slider_xpath} on page {self.base_url} is smaller than expected {expected_min_height}.')

        with self.subTest('Element width'):
            self.assertLess(expected_min_width, actual_slider_width,
                            f'Element width found by xpath {slider_xpath} on page {self.base_url} is smaller than expected {expected_min_height}.')

    @screenshot_decorator
    def test_checking_slider_under_bar_menu(self):
        driver = self.conf_driver
        driver.get(self.base_url)
        slider_element = driver.find_element(By.XPATH, '//*[@id="carousel"]')
        slider_element_text = slider_element.text
        print(slider_element_text)
        time.sleep(2)

    @screenshot_decorator
    def test_number_of_featured_products(self):
        expected_number_of_featured = 8
        product_xpath = '//*[@class="product-miniature js-product-miniature"]'
        driver = self.conf_driver
        driver.get(self.base_url)
        product_element = driver.find_elements(By.XPATH, product_xpath)
        actual_number_of_product = len(product_element)
        self.assertEqual(expected_number_of_featured, actual_number_of_product,
                         f'Product number differ for page {self.base_url}')

    @screenshot_decorator
    def test_all_products_have_price_in_pln_on_main_page(self):
        expected_products_in_currency = 'PLN'
        product_price_xpath = '//*[@class="price"]'

        driver = self.conf_driver
        driver.get(self.base_url)

        product_price_elements = driver.find_elements(By.XPATH, product_price_xpath)

        for product_price_element in product_price_elements:
            price_element_text = product_price_element.get_attribute("textContent")
            with self.subTest(price_element_text):
                self.assertIn(expected_products_in_currency, price_element_text,
                              f'Expected text not found in product description for page:{self.base_url}')

    @screenshot_decorator
    def test_loop_usage(self):
        expected_text_icluded_in_string = "star"
        list_of_iteams = ['stargate', 'starship', 'stardust', 'startreck', 'dyststar']

        for item in list_of_iteams:
            with self.subTest(item):
                self.assertIn(expected_text_icluded_in_string, item,
                              f"Word 'star' does not exist on soma worlds.")
