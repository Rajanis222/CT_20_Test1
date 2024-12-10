import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://apps.credence.in/practice#")
driver.maximize_window()
print("Title of this page is -- > ", driver.title)
time.sleep(1)

driver.implicitly_wait(10)

# Drag and Drop Example
drag = driver.find_element(By.ID, "draggable")
drop = driver.find_element(By.ID, "droppable")
driver.execute_script("arguments[0].scrollIntoView();", drag)

time.sleep(3)
# Perform drag and drop
action = ActionChains(driver)
action.drag_and_drop(drag, drop).perform()
time.sleep(3)

# Verify that the element is dropped

alert = Alert(driver)
print(alert.text)

assert alert.text == "Dropped successfully!", "Element is not dropped successfully"

print("Element is dropped successfully")


# if alert.text == "Dropped successfully!":
#     print("Element is dropped successfully")
#     alert.accept()
# else:
#     print("Element is not dropped successfully")


driver.quit()
