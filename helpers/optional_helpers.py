import time
from selenium.webdriver.common.by import By



def wait_for_elements(driver, xpath, max_seconds_to_wait=5, number_of_expected_elements=1):
    """ Checking every second if list of elements under specified xpath was found.
    :param driver: webdriver instance
    :param xpath: xpath of web element
    :param max_seconds_to_wait: maximum waiting for element (default:5)
    :param number_of_expected_elements: specifies of minimum number of elements to be found
    :return: list of found elements.
    """
    for seconds in range(max_seconds_to_wait):
        elements = driver.find_elements(By.XPATH, xpath)
        print(f'Total waiting {seconds}s')

        if len(elements) >= number_of_expected_elements:
            return elements

        if seconds == (max_seconds_to_wait - 1):
            print('End of wait')
            assert len(elements) > number_of_expected_elements, f'Expected {number_of_expected_elements} elements but found {len(elements)} for xpath {xpath} in time of {max_seconds_to_wait}s.'

        time.sleep(2)