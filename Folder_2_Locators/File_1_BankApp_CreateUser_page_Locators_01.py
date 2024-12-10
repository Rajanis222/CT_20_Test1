"""
List of Locators available in selenium:
ID
NAME
CLASS_NAME
TAG_NAME
LINK_TEXT
PARTIAL_LINK_TEXT
CSS_SELECTOR
XPATH

# input -- > tagname, id --> attribute name, username--> value
"""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome() # chrome
driver.maximize_window()
driver.get("https://apps.credence.in/user.html") # Navigate to login page
print(f"(Title of the page is -- > {driver.title}") # Print the title of the page -- > driver.title) # Print the title of the page -- > driver.title)

# Use ID locator to find username field and enter the value
username_field = driver.find_element(By.ID, "username") # we have located the field
username_field.send_keys("testuser") # we have entered the value # operation send_keys

# Use NAME locator to find password field and enter the value
password_field = driver.find_element(By.NAME, "password")
password_field.send_keys("Test@123")

# Use CLASS_NAME locator to find email field and enter the value
email_field = driver.find_element(By.CLASS_NAME, "email")
email_field.send_keys("testuser@example.com")


# Use Tag_NAME locator to find Phone field and enter the value
input_fields = driver.find_elements(By.TAG_NAME, "input") # we have located all the input fields
phone_field = input_fields[3]  # assuming this is the fourth input field
phone_field.send_keys("123487986787")

# Use ID Locator to find createUser Button
create_user_button = driver.find_element(By.ID, "createUserButton")
create_user_button.click() # we have clicked on the button


time.sleep(5) # wait for 5 seconds
driver.quit() # Quit the browser window