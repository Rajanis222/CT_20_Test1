import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://apps.credence.in/practice")
print("title of this page is :", driver.title)
time.sleep(2)
# click on new window
open_window_button=driver.find_element(By.ID,"openwindow")
open_window_button.click()
print("title of this page is:",driver.title)
time.sleep(2)
# Switch to new window
print("switch to new window")
driver.switch_to.window(driver.window_handles[1])
print("title of this page is :", driver.title)
time.sleep(2)
message=driver.find_element(By.XPATH,"//*[@id='main-home-content']/div/section[1]/div/div/div/div[1]/div/h3")
print(message.text)