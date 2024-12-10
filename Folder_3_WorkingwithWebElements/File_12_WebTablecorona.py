import time

from selenium import  webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://www.worldometers.info/coronavirus/#countries")
driver.maximize_window()
print("Title of this page is -- > ", driver.title)

time.sleep(2)
# Web Table Example

table_web = driver.find_elements(By.XPATH, "//table[@id='main_table_countries_today']//tr")
time.sleep(2)
print(len(table_web)) # Output = 19

#$x("//table[@id='product']/tbody/tr[1]/td[1]")

for row in table_web:
    col = row.find_elements(By.TAG_NAME, "td")
    time.sleep(0.3)
    print(f"Row no {table_web.index(row)+1} --> Country: {col[1].text}, Total cases: {col[2].text},Total Death: {col[3].text},Total recovered: {col[3].text }")


driver.quit()



