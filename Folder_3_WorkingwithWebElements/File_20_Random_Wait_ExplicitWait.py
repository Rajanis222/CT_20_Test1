import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver = webdriver.Chrome()

wait = WebDriverWait(driver, 10)

# Open the given URL
driver.get("https://apps.credence.in/practice")
driver.maximize_window()


# Print the title of the webpage
print("Title of this page is -- > ", driver.title)



# Click on Random Wait Button
print("Random Wait")
random_wait_click = driver.find_element(By.ID, "RandomWaitBtn")
driver.execute_script("arguments[0].scrollIntoView();", random_wait_click)
random_wait_click.click()


#time.sleep(5) # Hard time in python # this is not suggest when the time is random
# this is suggested only when the time is fixed

# Driver will wait for exact seconds for the next command to be executed
# Get Level 1 Text
print("Level 1 Text")

# Explicit wait


# WebDriverWait(driver, 10) --> Driver will wait for 10 seconds for the next command to be executed
# if element will visible in 3 sec then it will not wait complete 10 secs
# until(expected_conditions.visibility_of_element_located --> we have given the condition that
# wait for the element to be visible on the page
WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.ID, "level1Text")))
level_1_text = driver.find_element(By.ID, "level1Text").text

print(level_1_text)

#time.sleep(10)
# Get Level 2 Text
# poll_frequency=1 is by default

WebDriverWait(driver, 10, poll_frequency=0.1).until(expected_conditions.visibility_of_element_located((By.ID, "level2Text")))
print("Level 2 Text")
level_2_text = driver.find_element(By.ID, "level2Text").text
print(level_2_text)


# Fluent wait
# Get Level 3 Text
print("Level 3 Text")
wait.until(expected_conditions.visibility_of_element_located((By.ID, "level3Text")))
level_3_text = driver.find_element(By.ID, "level3Text").text
driver.quit()


# https://fast.com/#
# internet speed test search on google