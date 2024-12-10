import time

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Firefox()
browser.get("https://apps.credence.in/practice")
browser.maximize_window()

#time.sleep(3)
# Select Radio Button 1
radio_button1 = browser.find_element(By.XPATH, "//input[@value='radio1']")
radio_button1.click()


#time.sleep(3)
# Select Radio Button 1
radio_button2 = browser.find_element(By.XPATH, "//input[@value='radio2']")
radio_button2.click()


#time.sleep(3)
# Select Radio Button 1
radio_button3 = browser.find_element(By.XPATH, "//input[@value='radio3']")
radio_button3.click()

# Verify that the radio button is selected
#print(radio_button3.is_selected())


assert radio_button2.is_selected(), "Radio Button 2 is not selected"

browser.close()

