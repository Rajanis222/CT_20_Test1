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

driver = webdriver.Firefox()
driver.implicitly_wait(10)
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
add_to_cart = driver.find_element(By.XPATH, "//input[@value='Add to Cart']")
add_to_cart.click()
# Select Quantity
quantity = Select(driver.find_element(By.XPATH, "//select[@class='quantity']"))
quantity.select_by_index(1)

#time.sleep(2)
# Click Continue Shopping
driver.find_element(By.XPATH, "//a[normalize-space()='Continue Shopping']").click()

# ContinueShopping = driver.find_element(By.XPATH, "//a[normalize-space()='Continue Shopping']")
# print(ContinueShopping.is_displayed())
# driver.execute_script("arguments[0].scrollIntoView();", ContinueShopping)
# time.sleep(2)
# ContinueShopping.click()


#time.sleep(3)
# Click on PlayStation 4
product_Playstation = driver.find_element(By.XPATH, "//h3[normalize-space()='Playstation 4']")
product_Playstation.click()


#time.sleep(3)
# Click on add to cart
add_to_cart = driver.find_element(By.XPATH, "//input[@value='Add to Cart']")
add_to_cart.click()



# Select Quantity PlayStation 4
quantity = Select(driver.find_element(By.XPATH, "/html/body/div/table/tbody/tr[2]/td[3]/select"))
quantity.select_by_index(2)
#time.sleep(2)
# Click Continue Shopping
driver.find_element(By.XPATH, "//a[normalize-space()='Continue Shopping']").click()

#time.sleep(4)
# Click on Xbox
product_Xbox = driver.find_element(By.XPATH, "//h3[normalize-space()='Xbox One']")
product_Xbox.click()


# Click on add to cart
add_to_cart = driver.find_element(By.XPATH, "//input[@value='Add to Cart']")
add_to_cart.click()

# Select Quantity PlayStation 4
quantity = Select(driver.find_element(By.XPATH, "/html/body/div/table/tbody/tr[3]/td[3]/select"))
quantity.select_by_index(3)


num_rows = len(driver.find_elements(By.XPATH, "//tbody/tr"))
print(num_rows) # output = 6

#time.sleep(3)
list1 = []
for r in range(num_rows):
        time.sleep(2)
        amount = driver.find_element(By.XPATH, "//tbody[1]/tr[" + str(r+1) + "]/td[4]").text
        print(f"Row no {r+1} --> Amount: {amount}")
        list1.append(amount)

print(list1) # output = ['$4599.98', '$1199.97', '$1799.96', '$7,599.91', '$987.99', '$8,587.90']

product1_amount = list1[0].replace('$', '').replace("'", "")
print(product1_amount) # output = 0

product2_amount = list1[1].replace('$', '').replace("'", "")
print(product2_amount) # output = 1

product3_amount = list1[2].replace('$', '').replace("'", "")
print(product3_amount) # output = 2

Actual_Subtotal = list1[3].replace('$', '').replace("'", "").replace(",", "")
print(f"Actual Subtotal: {Actual_Subtotal}") # output = 3 Actual_Subtotal) # output = 3

Actual_Tax_Amount = list1[4].replace('$', '').replace("'", "")
print(f"Actual Tax Amount: {Actual_Tax_Amount}") # output = 4 Actual_Tax_Amount) # output = 4

Actual_Total_Amount = list1[5].replace('$', '').replace("'", "").replace(",", "")
print(f"Actual Total Amount: {Actual_Total_Amount}") # output = 5 Actual_Total_Amount) # output = 5Actual_Total_Amount) # output = 5

# this value we have calculated by adding the amount of all 3 product
Expected_Subtotal = float(product1_amount) + float(product2_amount) + float(product3_amount)
print(f"Expected Subtotal: {Expected_Subtotal}") # output = 6 Expected Subtotal: 6Expected_Subtotal) # output = 6


if float(Actual_Subtotal) == Expected_Subtotal:
    print("Subtotal Amount is verified")
else:
    print("Subtotal Amount is not verified")


Expected_Tax_Amount = round(float(Expected_Subtotal) * 0.13, 2)
print(f"Expected Tax Amount: {Expected_Tax_Amount}") # output = 7 Expected Tax Amount: 0.91Expected_Tax_Amount) # output = 7

if float(Actual_Tax_Amount) == float(Expected_Tax_Amount):
    print("Tax Amount is verified")
else:
    print("Tax Amount is not verified")

Expected_Total_Amount = float(Expected_Subtotal) + float(Expected_Tax_Amount)
print(f"Expected Total Amount: {Expected_Total_Amount}") # output = 8 Expected Total Amount: 6.91Expected_Total_Amount) # output = 8
time.sleep(3)
if float(Actual_Total_Amount) == Expected_Total_Amount:
    print("Total Amount is verified")
else:
    print("Total Amount is not verified")



driver.quit()


# Add more 3 products
# take diffrentr quantitties of each product
# and Check every product's price
# Check Subtotal
#  Check tax verofy that 13% tax
# Check Total


# apps.credence.in
# Bank -login
# bank app -signup
# bank app create user
# bank app edit user
# bank app user search
#time.sleep(6)

# sunday 7 to 9: 30 session 1
# 9:30 to 10 break
# 10 :to 12 session 1