from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://automation.credence.in/register")
driver.maximize_window()
driver.implicitly_wait(2)


# Fill the registration form
# Enter Usename
name = driver.find_element(By.ID, "name")
name.send_keys("credencetest@test.com")

# @Gmail.com

# asjhcb@gmail.com
# sdkjvb.gmail.com
# akhfdb123@gmail.com

# Enter Email
email = driver.find_element(By.ID, "email")
email.send_keys("credencetest2134567@test.com")

# Enter Password
password = driver.find_element(By.ID, "password")
password.send_keys("Test@123")

# Enter Confirm Password
confirm_password = driver.find_element(By.ID, "password-confirm")
confirm_password.send_keys("Test@123")

# Click on Submit button
submit_button = driver.find_element(By.CLASS_NAME, "btn")
submit_button.click()

# Verify the user registration
try:
    MenuButton = driver.find_element(By.CLASS_NAME, "dropdown-toggle")
    assert MenuButton.is_displayed(), "User is not logged in"
    print("User is logged in")
except:
    print("User is not logged in")

finally:
    driver.quit()