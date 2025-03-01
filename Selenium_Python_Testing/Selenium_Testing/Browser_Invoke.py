import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Path to ChromeDriver
driver_path = "C:/Development/pythonProject/chromedriver.exe"

# Set up the ChromeDriver service
service = Service(driver_path)

# Launch Chrome browser
driver = webdriver.Chrome(service=service)

# Open a webpage
driver.get("https://www.google.com")
driver.maximize_window()
print(driver.title)
print(driver.current_url)
driver.get("https://www.facebook.com")
driver.back()
driver.refresh()
driver.forward()
time.sleep(10)
# Close the browser
driver.close()

variable_1 = 10
