from selenium.webdriver.support.events import AbstractEventListener
import time
import allure
from allure_commons.types import AttachmentType

class ScreenshotListener(AbstractEventListener):

   def on_exception(self, exception, driver):
       # PyCharm debugger cause exception so we need to ignore it
       pycharm_debugger_exceptions = [
           "'WebElement' object has no attribute '__len__'",
           "'WebDriver' object has no attribute '__len__'",
           "'WebDriver' object has no attribute 'shape'",
           "'WebElement' object has no attribute 'shape'"
       ]
       if str(exception) not in pycharm_debugger_exceptions:
           make_screenshot(driver, 'driver')



def make_screenshot(driver, producer):
    screenshot_path = rf"testResults\{producer}_exception_{time.time()}.png"
    driver.get_screenshot_as_file(screenshot_path)
    allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
    print(f"Screenshot saved as {screenshot_path}")

""" Stary kod (ponizej), nowy znajduje sie pod komenatrzem!  
class ScreenshotListener(AbstractEventListener):
    def on_exception(self, exception, driver):
        make_screenshot(driver, 'driver')

def make_screenshot(driver, producer):
    screenshot_path = rf"testResultss/{producer}_exception_{time.time()}.png"
    driver.get_screenshot_as_file(screenshot_path)
    allure.attach(driver.get_screenshot_as_png(), name= "Screnshoot", attachment_type= AttachmentType.PNG)
    print(f"Screenshot saved as {screenshot_path}")
    
"""