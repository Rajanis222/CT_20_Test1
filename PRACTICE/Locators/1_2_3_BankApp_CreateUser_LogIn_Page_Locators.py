import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://apps.credence.in/user.html")
print(driver.title)

#ID locator
username_field=driver.find_element(By.ID, "username") #located the field
username_field.send_keys("testuser123") #entered the value

#NAME locator
password_field=driver.find_element(By.NAME, "password").send_keys("Test@123")

#CLASS_NAME locator
email_field=driver.find_element(By.CLASS_NAME, "email").send_keys("testuser123@example.com")

#Tag_NAME locator
# input_fields = driver.find_element(By.TAG_NAME, "input")
# phone_field=input_fields[3]

phone_field=driver.find_element(By.ID, "phone").send_keys("526212342")

create_user_button=driver.find_element(By.ID, "createUserButton")
driver.execute_script("arguments[0].scrollIntoView();", create_user_button)
create_user_button.click()

# LINK TEXT
login_link=driver.find_element(By.LINK_TEXT,"Go to Login")
driver.execute_script("arguments[0].scrollIntoView();", login_link)
login_link.click()

# XPATH locator
username_field_1=driver.find_element(By.XPATH,"//input[@name='username']").send_keys("testuser123")
password_field_1=driver.find_element(By.CSS_SELECTOR, "input[name='password']").send_keys("Test@123")
login_button=driver.find_element(By.NAME,"loginButtonTag").click()
time.sleep(5)
driver.close()



