# called as Login page class
# has two things
# Page locators
# Page Actions
import time

from selenium.webdriver.common.by import By

from test.utils.common_utils import webdriver_wait


# create a class called Login page and initialise it with a constructor
class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    # Page locators
    # mentioned as tuples
    # all the locators are defined here even if not used

    email = (By.ID, "login-username")
    password = (By.NAME, "password")
    submit_button = (By.ID, "js-login-btn")
    error_message = (By.CLASS_NAME, "notification-box-description")
    # Comment them if any of the locators are not being used now and uncomment when needed .That is how it is maintained
    free_trial = (By.XPATH,"//a[normalize-space()='Start a free trial']")


# forgot_password_button=(By.XPATH,"//button[normalize-space()='Forgot Password?']")
# remember_me_checkbox=(By.XPATH,"//label[normalize-space()='Remember me']/span[@class='checkbox-radio-button ng-scope']")
# sso_login=(By.XPATH,"//button[normalize-space()='Sign in using SSO']")


# Page Actions
# to find each element the id has to be passed to the respective functions below


    def get_email(self):
        return self.driver.find_element(*LoginPage.email)


    def get_password(self):
        return self.driver.find_element(*LoginPage.password)


    def get_submit_button(self):
        return self.driver.find_element(*LoginPage.submit_button)


    def get_error_message(self):
        webdriver_wait(driver=self.driver, element_tuple=self.error_message, timeout=5)
        return self.driver.find_element(*LoginPage.error_message)

    def get_free_trial_button(self):
        return self.driver.find_element(*LoginPage.free_trial)

    # login action function
    def login_to_vwo(self, email, pwd):
        try:
            self.get_email().send_keys(email)
            self.get_password().send_keys(pwd)
            self.get_submit_button().click()
        except Exception as e:
            print(e)
    def get_free_trial_button_click(self):
        try:
            self.get_free_trial_button().click()
        except Exception as e:
            print(e)

    def get_error_message_text(self):
        return self.get_error_message().text


