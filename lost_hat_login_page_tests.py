from selenium.webdriver.common.by import By
from helpers.wrappers import screenshot_decorator
from helpers.base_test_class import BaseTestClass
import config_reader
from helpers import functional_helpers as fh

class LostHatLoginPageTests(BaseTestClass):

    @screenshot_decorator
    def test_login_text_header(self):
        expected_text = 'Log in to your account'
        header_xpath = '//header[@class="page-header"]'
        driver = self.conf_driver
        driver.get(self.url_log_page)

        self.assert_element_text(driver, header_xpath, expected_text)


    @screenshot_decorator
    def test_log_page_website_title(self):
        driver = self.conf_driver

        driver.get(self.url_log_page)
        expected_name_log_page = "Login"
        title_log_page = driver.title
        print(title_log_page)
        if title_log_page == expected_name_log_page:
            print("It's ok!")
        else:
            print("Smth goes wrong!")

    def user_login(driver, user_mail, user_password):
        """
        Login user to websit using given mail and password
        :param driver: webdriver instance
        :param user_mail: user mail
        :param user_password: user password
        :return: None
        """
        fill_input(driver, '//*[@id="login-form"]/section/div[1]/div[1]/input', user_mail)
        # login_input_element = driver.find_element(By.XPATH, '//*[@id="login-form"]/section/div[1]/div[1]/input')
        # login_input_element.send.keys(user_mail)

        fill_input(driver, '//*[@id="login-form"]/section/div[2]/div[1]/div/input', user_password)
        # login_input_element = driver.find_element(By.XPATH, '//*[@id="login-form"]/section/div[2]/div[1]/div/input')
        # login_input_element.send.keys(user_password)

        sign_in_button = driver.find_element(By.XPATH, '//*[@id="submit-login"]')
        sign_in_button.click()

    def fill_input(driver, xpath, value, ):
        """
        :param driver: webdriver instance
        :param xpath: xpath to input box
        :param value: mail and password it depends on which box will be used
        """
        input_box = driver.finde_element(By.XPATH, xpath)
        input_box.clear()
        input_box.send_keys(value)

    def assert_element_text(self, driver, xpath, expected_text):
        """Comparing expected text with observed value from web element
           :param driver: webdriver instance
           :param xpath: xpath to element with text to be observed
           :param expected_text: text what we are expecting to be found
           :return: None
        """
        element = driver.find_element(By.XPATH, xpath)
        element_text = element.text
        self.assertEqual(expected_text, element_text,
                         f'Expected text differ from actual on page: {self.url_log_page}')

    def test_correct_login(self):
        config = config_reader.load()
        expected_text = config['correct_user_fullname']
        user_name_xpath = '//a[@class="account"]/*[@class="hidden-sm-down"]'
        user_email = config['correct_user']
        user_pass = config['correct_user_pass']

        driver = self.conf_driver

        driver.get(self.url_log_page)
        fh.user_login(driver, user_email, user_pass)
        self.assert_element_text(driver, user_name_xpath, expected_text)

    def test_incorrect_login(self):
        expected_text = 'Authentication failed.'
        alert_xpath = '//*[@class="alert alert-danger"]'
        user_email = 'invalid@test.test'
        user_pass = 'abc123'
        driver = self.conf_driver

        driver.get(self.url_log_page)
        fh.user_login(driver, user_email, user_pass)
        self.assert_element_text(driver, alert_xpath, expected_text)
