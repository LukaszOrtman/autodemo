from selenium.webdriver.common.by import By


def user_login(driver, user_mail, user_pass):
    """
    Login user to websit using given mail and password
    :param driver: webdriver instance
    :param user_mail: user mail
    :param user_password: user password
    :return: None
    """

    # finding login input box and sending value
    fill_input(driver, '//*[@id="login-form"]/section/div[1]/div[1]/input', user_mail)
    #login_input_element = driver.find_element(By.XPATH, '//*[@id="login-form"]/section/div[1]/div[1]/input')
    #login_input_element.send.keys(user_mail)

    #finding password input box and sending value
    fill_input(driver, '//*[@id="login-form"]/section/div[2]/div[1]/div/input', user_pass)
    #login_input_element = driver.find_element(By.XPATH, '//*[@id="login-form"]/section/div[2]/div[1]/div/input')
    #login_input_element.send.keys(user_password)

    # finding button "SIGN IN"
    sign_in_button = driver.find_element(By.XPATH, '//*[@id="submit-login"]')
    sign_in_button.click()


def fill_input(driver, xpath, value, ):
    """


    :param driver: webdriver instance
    :param xpath: xpath to input box
    :param value: mail and password it depends on which box will be used
    """
    input_box = driver.find_element(By.XPATH, xpath)
    input_box.clear()
    input_box.send_keys(value)

