import time

from selenium import  webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://apps.credence.in/practice")
driver.maximize_window()
print("Title of this page is -- > ", driver.title)

time.sleep(1)
# Click on mouse hover button
mouseHover_button = driver.find_element(By.ID, "mousehover")
driver.execute_script("arguments[0].scrollIntoView();", mouseHover_button)

# Initialize ActionChains
actions = ActionChains(driver)

# Perform mouse hover action
actions.move_to_element(mouseHover_button).perform()


# Click on Top
top_button = driver.find_element(By.LINK_TEXT, "Top")
top_button.click()
time.sleep(5)
