import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Firefox()
driver.maximize_window()

#login

driver.get("https://automation.credence.in/login")
email_add=driver.find_element(By.ID,"email")
email_add.send_keys("credence147@test.com")
time.sleep(3)
password=driver.find_element(By.ID,"password")
password.send_keys("credence147")
login_button=driver.find_element(By.XPATH,"//button[@type='submit']")
login_button.click()

# Add 3 products with different quantities

#select the product 1 	Playstation 4(2)
product_1=driver.find_element(By.XPATH,"//h3[normalize-space()='Playstation 4']")
product_1.click()
#click on add to cart
add_to_cart1=driver.find_element(By.XPATH,"//input[@value='Add to Cart']").click()
#select the quantity
quantity_1=Select(driver.find_element(By.XPATH,"//select[@class='quantity']"))
quantity_1.select_by_index(1)
#click on continue shopping
continue_shopping_1=driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary.btn-lg").click()
time.sleep(4)

# # select product 2 	Xbox One(2)
product_2=driver.find_element(By.XPATH,"//h3[normalize-space()='Xbox One']").click()
# add to cart
add_to_cart2=driver.find_element(By.XPATH,"//input[@value='Add to Cart']").click()
# #Select quantity
quantity_2=Select(driver.find_element(By.XPATH,"//tbody/tr[2]/td[3]/select[1]"))
quantity_2.select_by_index(1)
# #click on continue shopping
continue_shopping_2=driver.find_element(By.XPATH,"//a[normalize-space()='Continue Shopping']")
continue_shopping_2.click()
time.sleep(3)

# select product 3 	Apple Macbook Pro(3)
product_3=driver.find_element(By.XPATH,"//h3[normalize-space()='Apple Macbook Pro']").click()
#add to cart
add_to_cart3=driver.find_element(By.XPATH,"//input[@value='Add to Cart']").click()
time.sleep(2)
#Select quantity
quantity_3=Select(driver.find_element(By.XPATH,"//tbody/tr[3]/td[3]/select[1]"))
quantity_3.select_by_index(2)
#click on continue shopping
continue_shopping=driver.find_element(By.XPATH,"//a[normalize-space()='Continue Shopping']")
continue_shopping.click()
time.sleep(3)

# select product 4
product_4=driver.find_element(By.XPATH,"//h3[normalize-space()='Apple iPad Retina']").click()
#click on add to cart
add_to_cart4=driver.find_element(By.XPATH,"//input[@value='Add to Cart']").click()
#Select quantity

#click on continue shopping
# driver.execute_script("arguments[0].scrollIntoView();", continue_shopping)

# amount verification
# get all the prices in list
num_rows=len(driver.find_elements(By.XPATH,"//table/tbody//tr"))
print(num_rows)
list1=[]
for r in range(num_rows):
    amount=driver.find_element(By.XPATH,"//table/tbody//tr["+str(r+1)+"]/td[4]").text
    print(f"Row no. {r+1})---> amount:{amount}")
    list1.append(amount)

print(list1)

product1_amount=list1[0].replace('$', '').replace("'", '')
print(product1_amount)
product2_amount=list1[1].replace('$', '').replace("'", '')
print(product2_amount)
product3_amount=list1[2].replace('$', '').replace("'", '')
print(product3_amount)
product4_amount=list1[3].replace('$', '').replace("'", '')
print(product4_amount)
Actual_Subtotal=list1[4].replace('$', '').replace("'", '').replace(",","")
print(Actual_Subtotal)
Actual_Tax_Amount=list1[5].replace('$', '').replace("'", '').replace("'","")
print(Actual_Tax_Amount)
Actual_Total_Amount=list1[6].replace('$', '').replace("'", '').replace(",","")
print(Actual_Total_Amount)

Expected_Total_Amount=float(product1_amount)+float(product2_amount)+float(product3_amount)+float(product4_amount)
print(f"Expected subtotal is: {Expected_Total_Amount}")
print(f"Actual subtotal is: {Actual_Subtotal}")
print(type(Actual_Subtotal))

if float(Actual_Subtotal)==Expected_Total_Amount:
    print("Subtotal amount is verified")
else:
    print("Subtotal amount is not verified")

#Tax amount verification
expected_tax_amount=round(float(Expected_Total_Amount) * 0.13,2)
print(f"Expected tax amount is: {expected_tax_amount}")

if float(Actual_Tax_Amount)==float(expected_tax_amount):
    print("Tax amount is verified")
else:
    print("Tax amount not verified")

expected_subtotal=float(Expected_Total_Amount)+float(expected_tax_amount)
print(f"Expected subtotal is: {expected_subtotal}")

if expected_subtotal==Actual_Subtotal:
    print("Subtotal amount is verified")
else:
    print("Subtotal amount not verified")
