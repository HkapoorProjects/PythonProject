import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver_path = "C:/Development/pythonProject/chromedriver.exe"
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.get("https://rahulshettyacademy.com/client")
driver.maximize_window()
time.sleep(5)
driver.find_element(By.LINK_TEXT, "Forgot password?").click()
driver.find_element(By.CSS_SELECTOR, "form div:nth-child(1) input").send_keys(
    "abc@gmail.com"
)
driver.find_element(By.CSS_SELECTOR, "form div:nth-child(2) input").send_keys(
    "Harsh@12"
)
driver.find_element(By.CSS_SELECTOR, "form div:nth-child(3) input").send_keys(
    "Harsh@12"
)
time.sleep(5)
driver.find_element(By.CSS_SELECTOR, "form div:nth-child(4) button").click()
time.sleep(10)
