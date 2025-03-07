# To check if the framework is properly arranged and can be run #initial commit was not successful.So just added thsi new file as copy of first test_sample
import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Install ChromeDriver
chromedriver_path = chromedriver_autoinstaller.install()

# Initialize WebDriver
service = Service(chromedriver_path)
driver = webdriver.Chrome(service=service)
# Your Selenium tests here
driver.get("https://www.w3schools.com/")
print(driver.title)
driver.quit()