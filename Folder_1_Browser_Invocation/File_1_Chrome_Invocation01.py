# you need to install the selenium library
# How to install it
# command -- > pip install selenium

# Pip --> pip install package -- > package manager in python used to install and manage  additional libraries
# Make your terminal is in cmd
# If it is showing power shell then change it to cmd
# From setting--Tools--> Terminal--> shell path -- > "C:\WINDOWS\system32\cmd.exe"
import time
from selenium import webdriver
driver = webdriver.Chrome() # start the chrome

driver.get("https://credence.in/") # Navigate to given url
driver.maximize_window() # Maximum the window
print(f"Title of the page is -- > {driver.title}") # Print the title of the page -- > driver.title) # Print the title of the page -- >  driver.title
time.sleep(5) # Wait for 5 seconds
driver.close() # Close the browser