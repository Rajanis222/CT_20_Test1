import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
driver.implicitly_wait(10)

# Enter credentials
username = driver.find_element(By.XPATH, "//input[@placeholder='Username']")
username.send_keys("Admin")
password = driver.find_element(By.XPATH, "//input[@placeholder='Password']")
password.send_keys("admin123")

# Click on login button
login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
login_button.click()

# Click on PIM Link
pim_link = driver.find_element(By.XPATH, "//span[normalize-space()='PIM']")
pim_link.click()

# Click on Add Employee button
add_emp_button = driver.find_element(By.XPATH, "//button[normalize-space()='Add']")
add_emp_button.click()
time.sleep(1)
# Fill out the form
first_name = driver.find_element(By.XPATH, "//input[@placeholder='First Name']")
first_name.send_keys("John")
time.sleep(2)
middle_name = driver.find_element(By.XPATH, "//input[@placeholder='Middle Name']")
middle_name.send_keys("martin")
time.sleep(2)
last_name = driver.find_element(By.XPATH, "//input[@placeholder='Last Name']")
last_name.send_keys("Doe")
time.sleep(3)
# Upload the image
image_input = driver.find_element(By.XPATH, "//input[@type='file']")
image_input.send_keys(r"D:\Flowers\Night-Jasmine.jpg")

# Click on Save button
save_button = driver.find_element(By.XPATH, "//button[@type='submit']")
save_button.click()
time.sleep(3)
# Verify that the employee is added

try:
    message = driver.find_element(By.XPATH, "//p[@class='oxd-text oxd-text--p oxd-text--toast-message oxd-toast-content-text']")
    print(message.text)
    print("Employee is added")
except:
    print("Employee is not added")

finally:
    # Close the browser
    driver.quit()
