from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.implicitly_wait(10)


username=driver.find_element(By.XPATH,"//input[@placeholder='Username']")
username.clear()
username.send_keys("Admin")
password=driver.find_element(By.XPATH,"//input[@placeholder='Password']")
password.clear()
password.send_keys("admin")
login_button=driver.find_element(By.XPATH,"//button[normalize-space()='Login']")
login_button.click()

try:
    menu_button=driver.find_element(By.XPATH,"//p[@class='oxd-userdropdown-name']")
    assert menu_button.is_displayed(),"User not logged in(try)"
    print("user is logged in")
    menu_button.click()
    logout_button=driver.find_element(By.XPATH,"//a[normalize-space()='Logout']")
    logout_button.click()
except:
    print("User not logged in(except)")

# driver.quit()