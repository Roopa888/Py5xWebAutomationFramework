# Free Trial page class
# Page locators inside the Free Trial page
#  actions
from selenium.webdriver.common.by import By

from test.utils.common_utils import webdriver_wait


class FreeTrialPage:
    def __init__(self, driver):
        self.driver = driver

    # page locators
    # user_name_email_ft = (By.ID,"page-v1-step1-email")
    username_email_ft= (By.XPATH, "//input[@id='page-v1-step1-email']")
    checkbox_terms = (By.XPATH, "//form[@id='page-free-trial-signup-form-step1']//input[@name='gdpr_consent_checkbox']")
    button_click_ft = (By.XPATH, "//button[normalize-space()='Create a Free Trial Account']")
    error_msg_invalid_email = (By.XPATH, "//div[normalize-space()='The email address you entered is incorrect.']")

    # function to find the above element
    def get_user_name_email_ft(self):
        webdriver_wait(driver=self.driver, element_tuple=self.username_email_ft, timeout=10)
        return self.driver.find_element(*FreeTrialPage.username_email_ft)

    def get_checkbox_terms(self):
        webdriver_wait(driver=self.driver, element_tuple=self.username_email_ft, timeout=10)
        return self.driver.find_element(*FreeTrialPage.checkbox_terms)

    def get_button_click_ft(self):
        return self.driver.find_element(*FreeTrialPage.button_click_ft)

    def get_error_msg_invalid_email(self):
        return self.driver.find_element(*FreeTrialPage.error_msg_invalid_email)

    # To get the text of the error msg element
    def get_error_msg_invalid_email_text(self):
        webdriver_wait(driver=self.driver, element_tuple=self.error_msg_invalid_email, timeout=5)
        return self.get_error_msg_invalid_email().text

    def enter_free_trial_details_invalid(self, invalid_email):
        try:
            self.get_user_name_email_ft().send_keys(invalid_email)
            self.get_checkbox_terms().click()
            webdriver_wait(driver=self.driver, element_tuple=self.button_click_ft, timeout=5)
            self.get_button_click_ft().click()
        except Exception as e:
            print(e)
