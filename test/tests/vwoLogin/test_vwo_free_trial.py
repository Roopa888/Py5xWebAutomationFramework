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

from test.pageObjects.pageObjectModel.vwo.loginPage import LoginPage
from test.pageObjects.pageObjectModel.vwo.freeTrialPage import FreeTrialPage
from dotenv import load_dotenv
import os

from test.utils.Utils import *


# the below code sets up an env before running any tests .So no need to call this inside any test case function again
@pytest.fixture()
def setup():
    load_dotenv()
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(Constants.app_url())
    return driver


@allure.title("VWO Free Trial")
@allure.description("TC#0-Verify the VWo Free Trial page")
@allure.feature("Feature|VWO Free Trial Page")
@pytest.mark.negative
def test_vwo_ft_negative(setup):
    driver = setup
    login_page = LoginPage(driver=driver)
    login_page.get_free_trial_button_click()
    take_screen_shot(driver=driver, name="VWO_free_trial_negative")
    free_trial_page = FreeTrialPage(driver=driver)
    free_trial_page.enter_free_trial_details_invalid("admin")
    error_msg_text = free_trial_page.get_error_msg_invalid_email_text()
    assert error_msg_text == "The email address you entered is incorrect."
