import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver_path = "C:/Development/pythonProject/chromedriver.exe"
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.get("https://www.rahulshettyacademy.com/dropdownsPractise/")
driver.maximize_window()
driver.find_element(By.ID, "autosuggest").send_keys("Us")
time.sleep(5)
countries = driver.find_elements(By.CSS_SELECTOR, "li[class='ui-menu-item'] a")
print(len(countries))
for country in countries:
    if country.text == "Cyprus":
        country.click()
        break
time.sleep(3)
assert driver.find_element(By.ID, "autosuggest").get_attribute("value") == "Cyprus"
