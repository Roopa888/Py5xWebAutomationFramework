import pytest
import time
from selenium import webdriver
import allure
import logging

from test.pageObjects.pageFactory.dashboard_PageFactory import DashboardPage
from test.pageObjects.pageFactory.loginPage_PageFactory import LoginPage
from test.constants.constants import Constants
from allure_commons.types import AttachmentType

from test.tests.vwoLogin.conftest import driver
from test.utils.Utils import take_screen_shot


@allure.epic("VWO App")
@allure.feature("Login Test")
class TestVWOLogin:
    @pytest.mark.usefixtures("setup")
    @pytest.mark.qa
    def test_vwo_login_negative(self,setup):
        try:
            LOGGER = logging.getLogger("__name__")
            driver = setup
            driver.get(Constants.app_url())
            loginPage = LoginPage(driver)
            loginPage.login_to_vwo(usr=self.username, pwd=123)
            error_msg_element = loginPage.error_msg()
            assert error_msg_element == "Your email, password, IP address or location did not match"
            take_screen_shot(driver=driver,name="Invalid login attempt")
        except Exception as e:
            print(e)

    # Positive test case
    @pytest.mark.usefixtures("setup")
    @pytest.mark.qa  # not neccessary to mark it again and again once doen for teh first test case ,but only if needed
    def test_vwo_login_positive(self,setup):
        try:
            LOGGER = logging.getLogger("__name__")
            driver = setup
            driver.get(Constants.app_url())
            login_page = LoginPage(driver)
            login_page.login_to_vwo(usr=self.username, pwd=self.password)
            take_screen_shot(driver=driver, name="Valid user logged in")
            dashboard_page = DashboardPage(driver)
            userlogged_in = dashboard_page.user_logged_in_text()
            assert "Aman" == userlogged_in
            take_screen_shot(driver=driver,name="Valid user logged in ")
        except Exception as e:
            print(e)

    @pytest.mark.usefixtures("setup")
    @pytest.mark.qa  # not neccessary to mark it again and again once doen for teh first test case ,but only if needed
    def test_vwo_login_negative_tc2(self, setup):
        pass
