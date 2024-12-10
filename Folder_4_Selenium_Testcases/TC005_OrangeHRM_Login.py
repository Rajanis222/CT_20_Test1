import time

from selenium import webdriver
from selenium.webdriver.common.by import By

################################################################
driver = webdriver.Chrome()
################################################################
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
driver.implicitly_wait(10) # Wait for 10 seconds for all elements to

username = driver.find_element(By.XPATH, "//input[@placeholder='Username']")
username.send_keys("Admin")
password = driver.find_element(By.XPATH, "//input[@placeholder='Password']")
password.send_keys("admin123")

login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
login_button.click()

# Verify that the user is logged in

try:
    menu_button = driver.find_element(By.XPATH, "//p[@class='oxd-userdropdown-name']")
    assert menu_button.is_displayed(), "User is not logged in"
    print("User is logged in")
    menu_button.click()
    logout_button = driver.find_element(By.XPATH, "//a[normalize-space()='Logout']")
    logout_button.click()
except:
    print("User is not logged in")

time.sleep(10)
driver.quit()


# https://phptravels.net/
# https://parabank.parasoft.com/
# https://iemodemoindia.meditab.com/#/app/patient/create
# https://demoq.eu/en/
#