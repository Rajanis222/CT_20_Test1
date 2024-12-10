import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.alert import Alert
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

#click on checkout
checkout_button=driver.find_element(By.XPATH,"//a[normalize-space()='Proceed to Checkout']").click()
first_name_textbox=driver.find_element(By.ID,"first_name").send_keys("Arjun")
last_name_textbox=driver.find_element(By.ID,"last_name").send_keys("Arjun123")
phone_textbox=driver.find_element(By.ID,"phone")
phone_textbox.clear()
phone_textbox.send_keys("7878787878")
address_texbox=driver.find_element(By.ID,"address").send_keys("Pune,Maharashtra, India")
zip_code=driver.find_element(By.ID,"zip").send_keys("123567")
state_dropdown=Select(driver.find_element(By.ID,"state"))
state_dropdown.select_by_visible_text("Pune")
owner_textbox=driver.find_element(By.ID,"owner").send_keys("Arjun")
cvv_textbox=driver.find_element(By.ID,"cvv").send_keys("257")
time.sleep(2)
#card details 4716 1089 9971 6531
driver.find_element(By.ID,"cardNumber").send_keys("4716")
driver.find_element(By.ID,"cardNumber").send_keys("1089")
driver.find_element(By.ID,"cardNumber").send_keys("9971")
driver.find_element(By.ID,"cardNumber").send_keys("6531")

expiry_dropdown=Select(driver.find_element(By.ID,"exp_month"))
expiry_dropdown.select_by_visible_text("January")
year_dropdown=Select(driver.find_element(By.ID,"exp_year"))
year_dropdown.select_by_value("18")
time.sleep(2)
continue_checkout_button=driver.find_element(By.ID,"confirm-purchase").click()

print(driver.find_element(By.XPATH,"/html/body/div/div[1]/p[1]").text)

driver.close()