# Katalon Page class
# Page locators inside the Katalon make appointment page
# Page actions
from selenium.webdriver.common.by import By
from test.utils.common_utils import WebDriverWait,webdriver_wait
class LoginAppointmentpage:
    def __init__(self,driver):
        self.driver=driver
    user_name_txt=(By.ID,"txt-username")
    password_txt=(By.ID,"txt-password")
    login_btn=(By.ID,"btn-login")
    def get_user_name(self):
        return self.driver.find_element(*LoginAppointmentpage.user_name_txt)
    def get_password(self):
        return self.driver.find_element(*LoginAppointmentpage.password_txt)
    def get_login_btn(self):
        return self.driver.find_element(*LoginAppointmentpage.login_btn)
    def click_login_btn(self):
        try:
            webdriver_wait(driver=self.driver,element_tuple=self.login_btn,timeout=5)
            self.get_login_btn().click()
        except Exception as e:
            print("Login to  Appointment button could not be clicked/n", e)


    def login_to_make_appointment(self, user_name_txt, password_txt):
        try:
            self.get_user_name().send_keys(user_name_txt)
            self.get_password().send_keys(password_txt)
            self.click_login_btn()
        except Exception as e:
            print(e)