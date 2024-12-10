import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Firefox()
driver.maximize_window()

#login

driver.get("https://automation.credence.in/login")
email_add=driver.find_element(By.ID,"email")
email_add.send_keys("credence147@test.com")
time.sleep(3)
password=driver.find_element(By.ID,"password")
password.send_keys("credence147")
login_button=driver.find_element(By.XPATH,"//button[@type='submit']")
login_button.click()

# user login verification
menu_button=driver.find_element(By.CLASS_NAME,"dropdown-toggle")
# logout_button=driver.find_element(By.XPATH,"//a[normalize-space()='Logout']")
try:
    assert menu_button.is_displayed(), "User not logged in"
    print("User is logged in")
except:
    print("User not logged in")
driver.close()

