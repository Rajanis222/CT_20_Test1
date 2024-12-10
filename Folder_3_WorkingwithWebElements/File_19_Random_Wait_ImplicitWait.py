import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()


# Open the given URL
driver.get("https://apps.credence.in/practice")
driver.maximize_window()
# implicitly_wait is a global wait used by all element
# Here Driver will wait implicitly for 10 seconds
# that means if the element is present in 3 secs
# then driver will not wait for complete 10 sec like hard time time.sleep(10)
driver.implicitly_wait(10) # condition for wait , always wait for element to be present on page


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
level_1_text = driver.find_element(By.ID, "level1Text").text
print(level_1_text)

time.sleep(10)
# Get Level 2 Text
print("Level 2 Text")
level_2_text = driver.find_element(By.ID, "level2Text").text
print(level_2_text)

# Get Level 3 Text
print("Level 3 Text")
level_3_text = driver.find_element(By.ID, "level3Text").text
print(level_3_text)

# Get Level 4 Text
print("Level 4 Text")
level_4_text = driver.find_element(By.ID, "level4Text").text
print(level_4_text)


# Get Level 5 Text
print("Level 5 Text")
level_5_text = driver.find_element(By.ID, "level5Text").text
print(level_5_text)


# Get level 6 Text
print("Level 6 Text")
level_6_text = driver.find_element(By.ID, "level6Text").text
print(level_6_text)


driver.quit()

#driver.quit()
