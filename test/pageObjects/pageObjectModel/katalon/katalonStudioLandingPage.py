# Katalon Page class
# Page locators inside the Katalon Studio page
# Page actions

from selenium.webdriver.common.by import By
from test.utils.common_utils import WebDriverWait, webdriver_wait


class LandingPage:
    def __init__(self,driver):
        self.driver=driver
    # page locators
    make_appointment_btn=(By.ID,"btn-make-appointment")
    # function to find the above locators
    def get_make_appointment(self):
        return self.driver.find_element(*LandingPage.make_appointment_btn)
    #function to click on the element and navigate to the next page

    def click_make_appointment(self):
        try:
            webdriver_wait(driver=self.driver,element_tuple=self.make_appointment_btn,timeout=5)
            self.get_make_appointment().click()
        except Exception as e:
            print("Make Appointment button could not be clicked/n",e)

