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
radio_list = driver.find_elements(By.XPATH, "//input[@type='radio']")
# Below is the case when we don't know the place exactly or it is dynamically changes
# for radio in radio_list:
#     if radio.get_attribute("value") == "radio2":
#         radio.click()
#         assert radio.is_selected()
#         break

# Below is the code when we know it is not going to change
radio_list[1].click()
assert radio_list[1].is_selected()
time.sleep(5)

# Now we are going to check is displayed function
assert driver.find_element(By.ID, "displayed-text").is_displayed()
time.sleep(5)
driver.find_element(By.ID, "hide-textbox").click()
time.sleep(2)
assert not driver.find_element(By.ID, "displayed-text").is_displayed()
