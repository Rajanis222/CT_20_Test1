import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()

# register

driver.get("https://automation.credence.in/shop")
register=driver.find_element(By.XPATH,"//a[normalize-space()='Register']")
register.click()
name=driver.find_element(By.XPATH,"//input[@id='name']")
name.send_keys("credence147")
email=driver.find_element(By.XPATH,"//input[@id='email']")
email.send_keys("credence147@test.com")
password=driver.find_element(By.XPATH,"//input[@id='password']")
password.send_keys("credence147")
confirm_password=driver.find_element(By.XPATH,"//input[@id='password-confirm']")
confirm_password.send_keys("credence147")
register_button=driver.find_element(By.XPATH,"//button[@type='submit']")
register_button.click()
time.sleep(3)
