import time

from selenium import  webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://apps.credence.in/practice")
driver.maximize_window()
print("Title of this page is -- > ", driver.title)

time.sleep(2)
# Web Table Example

webTable_scroll = driver.find_element(By.XPATH, "//legend[normalize-space()='Web Table Example']")      # Click on Prompt Alert" Button
driver.execute_script("arguments[0].scrollIntoView();", webTable_scroll)

table_web = driver.find_elements(By.XPATH, "//table[@id='product']/tbody/tr")
time.sleep(2)
print(len(table_web)) # Output = 19

#$x("//table[@id='product']/tbody/tr[1]/td[1]")

for row in table_web:
    col = row.find_elements(By.TAG_NAME, "td")
    print(f"Row no {table_web.index(row)+1} --> Instructor: {col[0].text}, Course: {col[1].text},Price: {col[2].text}")


driver.quit()



