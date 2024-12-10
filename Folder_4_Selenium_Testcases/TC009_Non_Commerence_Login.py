
"""
In Real time testing,
OTPs, capcha, any other verification pages are excluded.

example credit card data use automation.credence.in
fix type of data for OTPs, capcha, any other verification pages


in real time, automation tester never deal with these kind of validation.

Most of the sites automation is restricted
to avoid being detected as a bot.

Try to create, login the gmail account

Reward--> rs 1500 amazon gift card





"""



"""



import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://admin-demo.nopcommerce.com/")
driver.maximize_window()
driver.implicitly_wait(10)


username_list = ["admin@yourstore.com" , "admin1@yourstore.com", "admin2", "admin3", "admin4"]
Password_list = ["admin", "admin1", "admin2", "admin3", "admin4"]

for i in range(len(username_list)):
    username = driver.find_element(By.ID, "Email")
    username.clear()
    username.send_keys(username_list[i])
    password = driver.find_element(By.ID, "Password")
    password.clear()
    password.send_keys(Password_list[i])
    login_button = driver.find_element(By.XPATH, "//button[normalize-space()='Log in']")
    login_button.click()
    try:
        Logout_button = driver.find_element(By.XPATH, "//a[normalize-space()='Logout']")
        Logout_button.click()
        print(f"Successfully logged in as {username_list[i]}")
    except:
        username.clear()
        password.clear()
        print(f"Failed to log in as {username_list[i]}")

"""