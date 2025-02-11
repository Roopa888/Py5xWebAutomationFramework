
from selenium import webdriver
import pytest
from selenium.webdriver import Chrome
import os
from dotenv import load_dotenv
load_dotenv()
edge_options = webdriver.EdgeOptions()
edge_options.add_argument("no-sandbox")
edge_options.add_argument("disable-dev-shm-usage")
driver = webdriver.Edge(options = edge_options)
#driver=webdriver.Edge()
print("driver got")
@pytest.fixture(scope='class') #it is available to all classes
def setup(request):
    #driver = webdriver.Edge()
    driver.maximize_window()
    username=os.getenv("USER_NAME")
    password=os.getenv("PASSWORD")
    request.cls.driver=driver
    request.cls.username=username
    request.cls.password=password
    yield driver# return driver
    driver.quit()