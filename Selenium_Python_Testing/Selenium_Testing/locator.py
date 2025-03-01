import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver_path = "C:/Development/pythonProject/chromedriver.exe"
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
driver.find_element(By.NAME, "name").send_keys("Harshil Kapoor")
driver.find_element(By.NAME, "email").send_keys("abc@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("12345")
driver.find_element(By.ID, "exampleCheck1").click()
dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
dropdown.select_by_index(0)
time.sleep(5)
dropdown.select_by_visible_text("Female")
driver.find_element(By.XPATH, "//*[@class = 'btn btn-success']").click()
message = driver.find_element(By.CLASS_NAME, "alert-success").text
assert "Success!" in message
driver.find_element(By.XPATH, "(//input[@type='text'])[3]").clear()
driver.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys("HarshilKapoor")
driver.find_element(By.XPATH, "(//input[@type='text'])[3]").clear()
time.sleep(20)
# driver.close()
