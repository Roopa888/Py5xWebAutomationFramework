# Dashboard page class
# Page locators inside the dashboard page
# Page actions
from selenium.webdriver.common.by import By

from test.utils.common_utils import webdriver_wait


class DashboardPage:
    def __init__(self, driver):
        self.driver = driver

    # page locators
    user_logged_in = (By.XPATH, "//span[@data-qa='lufexuloga']")

    # function to find the above element
    def get_user_logged_in(self):
        return self.driver.find_element(*DashboardPage.user_logged_in)

    def get_user_logged_in_text(self):
        webdriver_wait(driver=self.driver, element_tuple=self.user_logged_in, timeout=15)
        print(self.get_user_logged_in().text)
        return self.get_user_logged_in().text
