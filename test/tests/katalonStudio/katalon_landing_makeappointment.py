import pytest
import allure
from selenium import webdriver
from test.pageObjects.pageObjectModel.katalon.katalonStudioLandingPage import LandingPage
from test.pageObjects.pageObjectModel.katalon.katalon_make_appointment_page import LoginAppointmentpage
from test.constants.constants_katalon import ConstantsKatalon
from test.tests.vwoLogin.conftest import driver
from test.utils.Utils import *
import os
from dotenv import load_dotenv

from test.utils.common_utils import webdriver_wait_url


# the below code sets up an env before running any tests .So no need to call this inside any test case function again
@pytest.fixture
def setup_katalon():
    load_dotenv()
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.get(ConstantsKatalon.katalon_app_url())
    return driver
def test_katalon_landing_page(setup_katalon):
    driver=setup_katalon
    landing_page=LandingPage(driver=driver)
    take_screen_shot(driver=driver,name="Landing Page")
    landing_page.click_make_appointment()
    webdriver_wait_url(driver=driver,timeout=6)
    assert driver.current_url=="https://katalon-demo-cura.herokuapp.com/profile.php#login"
    take_screen_shot(driver=driver,name="Appointment page")
#def test_login_make_appointment_page():
    login_appointmentpage=LoginAppointmentpage(driver=driver)
    take_screen_shot(driver=driver,name="Login  Appointment Page")
    login_appointmentpage.login_to_make_appointment("John Doe","ThisIsNotAPassword")
    webdriver_wait_url(driver=driver, timeout=6)
    assert driver.current_url=="https://katalon-demo-cura.herokuapp.com/#appointment"
    take_screen_shot(driver=driver,name="Appointment page")


