import allure
import pytest
import time
from selenium import webdriver
# 3 things we need to do here
# Assertions and use the Page object class
# Webdriver start
# User interactions + assertions
# Close webdriver
from test.constants.constants import Constants
from test.pageObjects.pageObjectModel.vwo import loginPage
from test.pageObjects.pageObjectModel.vwo import dashboardPage
from test.pageObjects.pageObjectModel.vwo.dashboardPage import DashboardPage
from test.pageObjects.pageObjectModel.vwo.loginPage import LoginPage
from test.utils.Utils import *
from dotenv import load_dotenv
import os
# the below code sets up an env before running any tests .So no need to call this inside any test case function again
@pytest.fixture()
def setup():
    load_dotenv()
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(Constants.app_url())
    return driver

@allure.title("VWO login test")
@allure.description("TC#0-Verify the login with invalid crdentials")
@allure.feature("Feature|VWO app negative test case")
@pytest.mark.negative
def test_vwo_login_negative(setup):
    driver=setup
    login_page=LoginPage(driver=driver)
    login_page.login_to_vwo(email=os.getenv("INVALID_USERNAME"),pwd=os.getenv("INVALID_PASSWORD"))
    error_msg_element=login_page.get_error_message_text()
    take_screen_shot(driver=driver,name="VWO_app_test_negative")
    assert error_msg_element==os.getenv("error_message_expected")

@allure.title("VWO Login Test")
@allure.feature("TC#1 - VWO App Positive Test")
@pytest.mark.positive
def test_vwo_login_positive(setup):
    driver=setup
    loginPage=LoginPage(driver=driver)
    loginPage.login_to_vwo(email=os.getenv("USER_NAME"),pwd=os.getenv("PASSWORD"))
    dashboard_page=DashboardPage(driver=driver)
    take_screen_shot(driver=driver, name="VWO_app_test_positive")
    assert os.getenv("USERNAME_LOGGED_IN") in dashboard_page.get_user_logged_in_text()
