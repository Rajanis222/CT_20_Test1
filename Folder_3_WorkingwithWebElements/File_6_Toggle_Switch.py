# this is your Task
# Is_selected()--> Toggle switch
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://apps.credence.in/practice")

# toggle switch-Male
toggle_switch_male=driver.find_element(By.XPATH,"//label[@for='female']")
toggle_switch_male.click()
time.sleep(1)
# toggle switch-Female
toggle_switch_female=driver.find_element(By.XPATH,"//label[@for='female']")
toggle_switch_female.click()
time.sleep(1)
#verify if toggle switch is selected
assert  toggle_switch_male.is_selected(),"Male is not selected"