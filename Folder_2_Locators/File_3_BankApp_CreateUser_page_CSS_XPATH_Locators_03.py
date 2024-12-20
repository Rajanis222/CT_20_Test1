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


# <input id="username" name="username" type="text" class="inputField" required="" maxlength="50">
# input -- > tagname, id --> attribute name, username--> value

"""

# XPATH format --> //tagname[@attribute='value'] # one way to write th e xpath

# XPATH--> XPATH(XML Path Language) is used language to select elements
# or attribute from web pages
# XPATH Format --> //tagname[@attribute='value']
# To check Xpath in browser console --> $x("Xpath")



# CSS_SELECTOR format --> tagname[attribute='value']
# CSS--> CSS(Cascading style sheets) is language used to describe
# presentation of web pages.
# CSS define visual properties of element like front, front size, colour, layout
# CSS format --> tagname[attribute='value']
# password css --> input[id='password']
# To check CSS in browser console --> $$("CSS")




import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome() # chrome
driver.maximize_window()
driver.get("https://apps.credence.in/user.html") # Navigate to login page
print(driver.title)

# Use XPATH locator to find username field and enter the value
username_field = driver.find_element(By.XPATH, "//input[@name='username']") # we have located the field
username_field.send_keys("testuser") # we have entered the value


time.sleep(3)
# Use CLASS_NAME locator to find email field and enter the value
email_field = driver.find_element(By.CSS_SELECTOR, "input[name='email']") # we have located the field
email_field.send_keys("testuser@example.com")

time.sleep(3)
# Use CSS_SELECTOR locator to find password field and enter the value
password_field = driver.find_element(By.CSS_SELECTOR, "input[name='password']")
password_field.send_keys("Test@123")


driver.quit() # close the browser window





