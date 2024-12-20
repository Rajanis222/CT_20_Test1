

import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
driver.implicitly_wait(5)


username_list = ["Admin", "admin@yourstore.com" , "admin1@yourstore.com","Admin", "admin2", "admin3", "admin4"]
Password_list = ["admin123", "admin", "admin1", "admin123", "admin2", "admin3", "admin4"]

for i in range(len(username_list)):
    username = driver.find_element(By.XPATH, "//input[@placeholder='Username']")
    #username.clear()
    username.send_keys(username_list[i])
    password = driver.find_element(By.XPATH, "//input[@placeholder='Password']")
    #password.clear()
    password.send_keys(Password_list[i])
    login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    login_button.click()
    try:
        menu_button = driver.find_element(By.XPATH, "//p[@class='oxd-userdropdown-name']")
        menu_button.click()
        logout_button = driver.find_element(By.XPATH, "//a[normalize-space()='Logout']")
        logout_button.click()
        print(f"Successfully logged in as {username_list[i]}")
    except:
        print(f"Failed to log in as {username_list[i]}")
        driver.refresh()

