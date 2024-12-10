import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://apps.credence.in/practice#")
driver.maximize_window()
print("Title of this page is -- > ", driver.title)
driver.implicitly_wait(10)

# Click on Double Click Button
double_click_element = driver.find_element(By.ID, "doubleClickBox")
driver.execute_script("arguments[0].scrollIntoView();", double_click_element)
# double_click.click()
# double_click.click()
actions = ActionChains(driver)
actions.double_click(double_click_element).perform()
time.sleep(2)
# Verify that the element is double clicked
alert = Alert(driver)
print(alert.text)
if alert.text == "You double-clicked me!":
    alert.accept()
    print("Element is double clicked successfully")
else:
    print("Element is not double clicked")


driver.quit()