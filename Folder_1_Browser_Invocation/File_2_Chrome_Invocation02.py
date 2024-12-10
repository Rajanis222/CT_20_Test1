# Serach "chromedriver download" in google
# go to first link
import time

# Link --> https://googlechromelabs.github.io/chrome-for-testing/

# Link directly to downland chrome driver
# https://storage.googleapis.com/chrome-for-testing-public/131.0.6778.85/win64/chromedriver-win64.zip
# after download extract zip file
# chromedriver.exe is our file

# create environment variable path for chromedriver.exe
# this is mandatory for all whether you first code is working or not

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Specify the path to chromedriver
chrome_service = Service("C:/chromedriver-win64/chromedriver.exe") # Setting up the service to local chrome driver

# Initialize the WebDriver with the specified service
driver = webdriver.Chrome(service=chrome_service) # Starting the Chrome browser with the specified driver service
driver.maximize_window() # Maximizing the browser window for a better view
driver.get("https://credence.in/") # Navigating to the specified URL
print(f"Title of the page is -- > {driver.title}") # Print the title of the page -- > driver.title) # Print the title of the page -- >  driver.title
time.sleep(5) # Wait for 5 seconds
driver.close() # Close the browser


