import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://apps.credence.in/practice")
driver.maximize_window()
print("Title of this page is -- > ", driver.title)

# Click on Slider Button
print("Slider")
slider_click = driver.find_element(By.ID, "salaryRange")
driver.execute_script("arguments[0].scrollIntoView();", slider_click)
slider_click.click()


expected_value =49
driver.execute_script(f"arguments[0].value={expected_value};arguments[0].dispatchEvent(new Event('input'))", slider_click)



# Verify that Slider value is 18
print(f"Slider Value -- > {slider_click.get_attribute('value')}")
assert slider_click.get_attribute('value') == str(expected_value), "Slider Value does not match expected value"

time.sleep(5)
driver.close()


# Your task is the execute the same in python code or without using java script
#