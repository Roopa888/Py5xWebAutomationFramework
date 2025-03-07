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
import urllib.request
htmlfile = urllib.request.urlopen("http://google.com")
htmltext = htmlfile.read()
print(htmltext)