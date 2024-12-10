import time

from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://apps.credence.in/practice#")
driver.maximize_window()
print("Title of this page is -- > ", driver.title)
driver.implicitly_wait(10)

# Click on Right Click Button
right_click_element = driver.find_element(By.ID, "rightClickBox")
driver.execute_script("arguments[0].scrollIntoView();", right_click_element)

# Initialize ActionChains
actions = webdriver.ActionChains(driver)

# Right click on the element
actions.context_click(right_click_element).perform()
time.sleep(2)

# Verify that the element is right clicked
alert = Alert(driver)
print(alert.text)
if alert.text == "You right-clicked me!":
    time.sleep(4)
    alert.accept()
    print("Element is right clicked successfully")
else:
    print("Element is not right clicked")
