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
password.send_keys("Credence@123")

# Click the login button
driver.find_element(By.CLASS_NAME, "btn").click()


# Click on Apple mac book protection
driver.find_element(By.XPATH, "//h3[normalize-space()='Apple Macbook Pro']").click()

# Click on add to cart
driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/form[1]/input[5]").click()

# Select Quantity
quantity = Select(driver.find_element(By.XPATH, "//select[@class='quantity']"))
quantity.select_by_index(1)



# Add more 3 products
# take diffrentr quantitties of each product
# and Check every product's price
# Check Subtotal
#  Check tax verofy that 13% tax
# Check Total
time.sleep(6)