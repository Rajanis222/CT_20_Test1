import time

from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("headless")
#
# driver = webdriver.Chrome(options=chrome_options)
# Open browser
driver = webdriver.Firefox()
driver.maximize_window()
# Go to Url
driver.get("https://automation.credence.in/login")
driver.find_element(By.XPATH, "//input[@name='email']").send_keys("Credencetest@test.com")
driver.find_element(By.CSS_SELECTOR, "input[id='password']").send_keys("Credence@123")
# Click Login button
driver.find_element(By.XPATH, "//button[@type='submit']").click()

# Click on Product--Macbook
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[3]/div/div/a[2]/h3").click()
# Click on add to cart
driver.find_element(By.XPATH, "//input[@value='Add to Cart']").click()
#Procedd to Checkout
driver.find_element(By.XPATH, "//a[@class='btn btn-success btn-lg']").click()
time.sleep(3)
# Enter First_Name
driver.find_element(By.XPATH, "//input[@id='first_name']").send_keys("Credence")
# Enter Last_Name
driver.find_element(By.XPATH, "//input[@id='last_name']").send_keys("Pune")
# Enter Phone
driver.find_element(By.XPATH, "//input[@id='phone']").send_keys("9091929355")
# Enter Address
driver.find_element(By.XPATH, "//textarea[@id='address']").send_keys("Dhankawdi, Pune")
# Enter Zip
driver.find_element(By.XPATH, "//input[@id='zip']").send_keys("411013")
# Select state
state = Select(driver.find_element(By.XPATH, "//select[@id='state']"))
state.select_by_visible_text("Pune")
# Enter  Owner name
driver.find_element(By.XPATH, "//input[@id='owner']").send_keys("Tushar")
# Enter CVV
driver.find_element(By.XPATH, "//input[@id='cvv']").send_keys("043")

# Select Year
year = Select(driver.find_element(By.XPATH, "//select[@id='exp_year']"))
year.select_by_index(2)

# Select Month
month = Select(driver.find_element(By.XPATH, "//select[@id='exp_month']"))
month.select_by_index(2)

# Enter card number\
# 5281 0370 4891 6168
driver.find_element(By.XPATH, "//input[@id='cardNumber']").send_keys("5281")
driver.find_element(By.XPATH, "//input[@id='cardNumber']").send_keys("0370")
driver.find_element(By.XPATH, "//input[@id='cardNumber']").send_keys("4891")
driver.find_element(By.XPATH, "//input[@id='cardNumber']").send_keys("6168")
# Click on Checkout button
driver.find_element(By.XPATH,"//button[@id='confirm-purchase']").click()


print(driver.find_element(By.XPATH, "/html/body/div/div[1]/p[1]").text)

driver.close()