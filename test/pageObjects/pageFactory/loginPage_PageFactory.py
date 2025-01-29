# Page locators
# Page actions
from seleniumpagefactory.Pagefactory import PageFactory
from test.utils.common_utils import *
from selenium.webdriver.common.by import By


# inherits from Pagefactory available in selenium Pagefactory
class LoginPage(PageFactory):
    def __init__(self, driver):
        self.driver = driver
        self.highlight = True  # To highlight every webElement in PageClass

    locators = {
        'username': ("CSS", "#login-username"),
        'password': ("NAME", "password"),
        'submit_button': ("ID", "js-login-btn"),
        'error_message': ("CLASS_NAME", "notification-box-description")
    }

    def login_to_vwo(self, usr, pwd):
        self.username.set_text(usr)
        self.password.set_text(pwd)
        self.submit_button.click_button()

    def error_msg(self):
        return self.error_message.get_text()
