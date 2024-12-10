# This is your task

"""
1.

search selectorshub extension firefox in google
go to first link
or you can to got below link
https://addons.mozilla.org/en-US/firefox/addon/selectorshub/

click on add to firefox button

similar for chrome, edge



2.

test case studio extension firefox

go to this link

https://addons.mozilla.org/en-US/firefox/addon/testcase-studio/


click on add to firefox




"""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://automation.credence.in/login")
driver.maximize_window()


# Enter the username
username = driver.find_element(By.ID,"email")
username.send_keys("Credencetest@test.com")

# Enter the password
password = driver.find_element(By.ID, "password")
password.send_keys("Credence@1234")

# Click the login button
driver.find_element(By.CLASS_NAME, "btn").click()


# Verify that the user is logged in
try:
    MenuButton = driver.find_element(By.CLASS_NAME, "dropdown-toggle")
    assert MenuButton.is_displayed(), "User is not logged in"
    print("User is logged in")
except:
    print("User is not logged in")

finally:
    driver.quit()