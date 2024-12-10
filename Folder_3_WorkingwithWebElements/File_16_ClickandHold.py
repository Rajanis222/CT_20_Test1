import time

from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://apps.credence.in/practice#")
driver.maximize_window()
print("Title of this page is -- > ", driver.title)
driver.implicitly_wait(10)

# Click on Click and Hold Button
click_and_hold_element = driver.find_element(By.ID, "clickHoldBox")
driver.execute_script("arguments[0].scrollIntoView();", click_and_hold_element)


# Perform click and hold action
actions = ActionChains(driver)
actions.click_and_hold(click_and_hold_element).perform()
time.sleep(2)


# Verify that the element is clicked and held
alert = Alert(driver)
print(alert.text)
if alert.text == "You clicked and held me!":
    time.sleep(2)
    alert.accept()
    print("Element is clicked and held successfully")
else:
    print("Element is not clicked and held")

