import time

from selenium import  webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://apps.credence.in/practice")
driver.maximize_window()
print("Title of this page is -- > ", driver.title)
time.sleep(1)


# Click on Credence Site Button to open new tab
Open_Windows_Button = driver.find_element(By.ID, "opentab1")
driver.execute_script("arguments[0].scrollIntoView();", Open_Windows_Button)
Open_Windows_Button.click()

time.sleep(1)
# Switch to new tab
print("Switch to new tab")
driver.switch_to.window(driver.window_handles[1])
# to switch to 2nd window[1--> Credence.in (1st window[0] --> practice page)
print("Title of this page is -- > ", driver.title)
time.sleep(3)

time.sleep(3)
#Back to previous tab -- practice page
print("Back to previous tab --practice page")
driver.switch_to.window(driver.window_handles[0])
time.sleep(3)
print("Title of this page is -- > ", driver.title)
Open_Windows_Button = driver.find_element(By.ID, "opentab2")
Open_Windows_Button.click()


driver.quit()
