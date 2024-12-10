import time

from selenium import  webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://apps.credence.in/practice")
driver.maximize_window()
print("Title of this page is -- > ", driver.title)
time.sleep(1)


# Click on Simple Alert" Button
print("Simple Alert")
alert_button = driver.find_element(By.ID, "simpleAlert")
driver.execute_script("arguments[0].scrollIntoView();", alert_button)
alert_button.click()
time.sleep(3)

alert = Alert(driver)
print(alert.text)
alert.accept()

time.sleep(3)

################################################################
# Click on Confirm Alert" Button
print("Confirm Alert")
confirmAlert_button = driver.find_element(By.ID, "confirmAlert")      # Click on Confirm Alert" Button
driver.execute_script("arguments[0].scrollIntoView();", alert_button)
confirmAlert_button.click()
time.sleep(3)

alert = Alert(driver)
print(f" Confirm Alert Message -- > {alert.text}") # print( alert.text)
alert.accept()
print(f"Confirm Alert Message after accept -- > {alert.text}") # print( alert.text))
alert.accept()

time.sleep(3)
confirmAlert_button.click()
time.sleep(3)

alert = Alert(driver)
print(f" Confirm Alert Message -- > {alert.text}") # print( alert.text)
alert.dismiss() # dismiss the alert
print(f"Confirm Alert Message after dismiss -- > {alert.text}") # print( alert.text))
alert.accept()
time.sleep(3)





################################################################
# Click on Prompt Alert" Button
print("Prompt Alert")
promptAlert_button = driver.find_element(By.ID, "promptAlert")      # Click on Prompt Alert" Button
driver.execute_script("arguments[0].scrollIntoView();", promptAlert_button)
promptAlert_button.click()
time.sleep(3)

alert = Alert(driver)
# first message click prompt alter
print(alert.text)
# Enter value in prompt alert
alert.send_keys("Credence")
# After Entering the value click on Ok button
alert.accept()
# print message after accepting
print(alert.text)
# accepting last prompt alter message
alert.accept()


time.sleep(3)

