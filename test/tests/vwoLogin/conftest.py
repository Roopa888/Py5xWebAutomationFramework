
from selenium import webdriver
import pytest
from selenium.webdriver import Edge
from selenium.webdriver.edge.options import Options as EdgeOptions, Options
import os
from dotenv import load_dotenv
load_dotenv()
# edge_options = webdriver.EdgeOptions()
# edge_options.add_argument("no-sandbox")
# edge_options.add_argument("disable-dev-shm-usage")
# edge_options.add_argument("--remote-debugging-port=9222")
#driver = webdriver.Edge(executable_path=r"C:\Users\aslog\Downloads\edgedriver_win64 (1)\msedgedriver.exe")
# options = EdgeOptions()
# options.add_argument("--no-sandbox")
# options.add_argument("--disable-dev-shm-usage")
# options.add_argument("--remote-debugging-port=9222")
# driver = webdriver.Edge(options =options)
options = Options()
options.headless = False  # Set to True if you want headless
driver = webdriver.Chrome(options=options)
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