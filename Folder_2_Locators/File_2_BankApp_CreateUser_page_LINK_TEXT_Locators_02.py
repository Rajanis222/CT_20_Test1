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
print(driver.title)

# Use LINK_TEXT locator to find Login link
#login_link = driver.find_element(By.LINK_TEXT, "Go to Login") # we have to give full text which is given for link
#login_link.click()
#
# time.sleep(3)

# Use LINK_TEXT locator to find Login link


login_link = driver.find_element(By.PARTIAL_LINK_TEXT, "Login") # we have to give partial text which is given for link
driver.execute_script("arguments[0].scrollIntoView();", login_link) # scroll into view
login_link.click()

time.sleep(3)
driver.back()

time.sleep(5)
driver.quit() # close the browser window





