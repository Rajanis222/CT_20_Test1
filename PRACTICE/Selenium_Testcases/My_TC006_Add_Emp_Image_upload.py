import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.implicitly_wait(10)

# Enter username and password
username=driver.find_element(By.XPATH,"//input[@placeholder='Username']")
username.clear()
username.send_keys("Admin")
password=driver.find_element(By.XPATH,"//input[@placeholder='Password']")
password.clear()
password.send_keys("admin123")
# click login
login_button=driver.find_element(By.XPATH,"//button[normalize-space()='Login']")
login_button.click()
#click on pim link
PIM_Tab=driver.find_element(By.XPATH,"//span[normalize-space()='PIM']")
PIM_Tab.click()
# click on add button
add_button=driver.find_element(By.XPATH,"//button[normalize-space()='Add']").click()
# Fill the information form
first_name=driver.find_element(By.XPATH,"//input[@placeholder='First Name']")
first_name.send_keys("john")
middle_name=driver.find_element(By.XPATH,"//input[@placeholder='Middle Name']")
middle_name.send_keys("martin")
last_name=driver.find_element(By.XPATH, "//input[@placeholder='Last Name']")
last_name.send_keys("cooper")
add_image=driver.find_element(By.XPATH,"//input[@type='file']")
add_image.send_keys(r"D:\Flowers\Night-Jasmine.jpg")
save_button=driver.find_element(By.XPATH,"//button[@type='submit']")
time.sleep(2)
save_button.click()
# verify employee if employee is added
try:
    message=driver.find_element(By.XPATH,"//p[@class='oxd-text oxd-text--p oxd-text--toast-message oxd-toast-content-text']")
    print(message.text)
    print("employee is added")
except:
    print("employee is not added")