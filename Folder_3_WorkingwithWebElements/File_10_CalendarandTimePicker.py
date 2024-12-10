import time

from selenium import  webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://apps.credence.in/practice")
driver.maximize_window()
print("Title of this page is -- > ", driver.title)
time.sleep(1)


# Enter value in calender box
calender_box = driver.find_element(By.ID, "datePicker")
calender_box.send_keys("28-11-2024")

# Enter value time picker box
time_picker_box = driver.find_element(By.ID, "timePicker")
time_picker_box.send_keys("12:30AM")
time.sleep(8)
driver.quit()