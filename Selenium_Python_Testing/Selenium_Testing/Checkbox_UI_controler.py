import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver_path = "C:/Development/pythonProject/chromedriver.exe"
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
time.sleep(5)
checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
print(len(checkboxes))
for checkbox in checkboxes:
    if checkbox.get_attribute("value") == "option2":
        checkbox.click()
        assert checkbox.is_selected()
        break
time.sleep(3)
