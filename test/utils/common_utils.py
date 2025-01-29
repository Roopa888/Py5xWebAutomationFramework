from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.expected_conditions import url_matches
from selenium.webdriver.support.ui import WebDriverWait

from test.constants.constants import Constants


# Method Overloading for webdriver wait function
def webdriver_wait(driver, element_tuple):
    WebDriverWait(driver=driver, timeout=5).until(EC.visibility_of_element_located(element_tuple))


# with timeout specifically mentioned
def webdriver_wait(driver, element_tuple, timeout):
    WebDriverWait(driver=driver, timeout=timeout).until(EC.visibility_of_element_located(element_tuple))

# wait for the url to change
def webdriver_wait_url(driver,timeout):
    WebDriverWait(driver=driver,timeout=timeout).until(EC.url_changes(Constants.app_dashboard_url()))