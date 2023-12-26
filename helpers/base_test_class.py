import unittest
from selenium import webdriver
from selenium.webdriver.support.events import EventFiringWebDriver
from helpers.screenshot_listener import ScreenshotListener
import config_reader
import json



class BaseTestClass(unittest.TestCase):

  @classmethod
  def setUp(self):
     config = config_reader.load()
     self.base_url = config["base_url"]
     self.url_log_page = 'https://autodemo.testoneo.com/en/login?back=my-account'
     self.url_log_page = 'https://autodemo.testoneo.com/en/login?back=my-account'
     self.url = 'https://autodemo.testoneo.com/en/men/1-1-hummingbird-printed-t-shirt.html'
     self.sample_product_url = self.base_url + 'men/1-1-hummingbird-printed-t-shirt.html'
     self.man_t_shirt_url = self.base_url + 'men/1-4-hummingbird-printed-t-shirt.html'
     self.subpage_art_url = self.base_url + '9-art'

     self.product_details_url = 'https://autodemo.testoneo.com/en/men/1-4-hummingbird-printed-t-shirt.html#/2-size-m/11-color-black'

     options = webdriver.ChromeOptions()
     self.driver = webdriver.Chrome(options=options)

     self.driver.implicitly_wait(10)

     self.user_mail = 'ortman@opp.pl'
     self.user_password = 'hiphop00'

     self.fail_email = 'ortma@op.pl'
     self.fail_password = 'hipho00'

     self.fail_alert = 'Authentication failed.'

     if config['event_firing_driver']:
        self.conf_driver = EventFiringWebDriver(self.driver, ScreenshotListener())
     else:
        self.conf_driver = self.driver

  @classmethod
  def tearDown(self):
     self.conf_driver.quit()