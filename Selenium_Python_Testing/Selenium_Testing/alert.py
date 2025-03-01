import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

name = "Harshil"
driver_path = "C:/Development/pythonProject/chromedriver.exe"
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
time.sleep(5)
driver.find_element(By.ID, "name").send_keys(name)
time.sleep(2)
driver.find_element(By.ID, "alertbtn").click()
time.sleep(2)
alert = driver.switch_to.alert
alert_text = alert.text
print(alert_text)
assert "Harshil" in alert_text
alert.accept()
time.sleep(2)
