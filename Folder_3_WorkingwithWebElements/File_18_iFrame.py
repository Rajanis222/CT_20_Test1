import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://apps.credence.in/practice#")
driver.maximize_window()
print(driver.title)
driver.implicitly_wait(10)

# Click on Credence Site Button to open new tab
iframe_element = driver.find_element(By.ID, "courses-iframe")
driver.execute_script("arguments[0].scrollIntoView();", iframe_element)
driver.switch_to.frame(iframe_element)
#
time.sleep(3)
print("Title of this page is -- > ", driver.title)
message = driver.find_element(By.XPATH, "//span[@class='text-white b label']")
print(message.text)
print(driver.title)

# verify that the driver is switched to i frame

if driver.title == "Credence":
  print("Driver is switched to iFrame")
else:
  print("Driver is not switched to iFrame")
