import time

from selenium import  webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://apps.credence.in/practice")
driver.maximize_window()
print("Title of this page is -- > ", driver.title)
time.sleep(1)
# Click on Open Windows Button to open new window
Open_Windows_Button = driver.find_element(By.ID, "openwindow")
Open_Windows_Button.click()
driver.execute_script("arguments[0].scrollIntoView();", Open_Windows_Button)
time.sleep(1)
print("Title of this page is -- > ", driver.title)

# Switch to new window
print("Switch to new window")
driver.switch_to.window(driver.window_handles[1]) # to switch to 2nd window[1--> Credence.in (1st window[0] --> practice page)
print("Title of this page is -- > ", driver.title)
time.sleep(3)
message = driver.find_element(By.CLASS_NAME,  "text-white")
print(message.text)


time.sleep(3)
# Back to previous window -- practice page
print("Back to previous window --practice page")
driver.switch_to.window(driver.window_handles[0])
print("Title of this page is -- > ", driver.title)

driver.quit()
