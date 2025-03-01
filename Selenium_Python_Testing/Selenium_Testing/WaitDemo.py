import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver_path = "C:/Development/pythonProject/chromedriver.exe"
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.implicitly_wait(7)
driver.get("https://www.rahulshettyacademy.com/seleniumPractise/")
driver.maximize_window()
time.sleep(5)
driver.find_element(By.XPATH, "//input[@type='search']").send_keys("ber")
time.sleep(5)
results = driver.find_elements(By.XPATH, "//*[@class='products']/div")
count = len(results)
assert count > 0
# time.sleep(2)
for result in results:
    result.find_element(By.XPATH, "div/button").click()
# time.sleep(2)
driver.find_element(By.XPATH, "//*[@alt='Cart']").click()
# time.sleep(2)
driver.find_element(By.XPATH, "//*[text()= 'PROCEED TO CHECKOUT']").click()
# time.sleep(2)
driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
# time.sleep(2)
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()
# time.sleep(5)
