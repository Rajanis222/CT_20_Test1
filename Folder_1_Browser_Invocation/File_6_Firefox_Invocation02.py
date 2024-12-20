# Serach "firefox geckodriver download" in google
# go to first link


# Link --> https://github.com/mozilla/geckodriver/releases

# Link directly to downland chrome driver
# https://storage.googleapis.com/chrome-for-testing-public/131.0.6778.85/win64/chromedriver-win64.zip
# after download extract zip file
# chromedriver.exe is our file

# create environment variable path for chromedriver.exe
# this is mandatory for all whether you first code is working or not
import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service

# Specify the path to chromedriver
firefox_service = Service(r"C:\geckodriver-v0.35.0-win-aarch64\geckodriver.exe") #() # Setting up the service to local chrome driver

# Initialize the WebDriver with the specified service
driver = webdriver.Firefox(service=firefox_service) # Starting the Chrome browser with the specified driver service
driver.maximize_window() # Maximizing the browser window for a better view
driver.get("https://credence.in/") # Navigating to the specified URL
print(f"Title of the page is -- > {driver.title}") # Print the title of the page -- > driver.title) # Print the title of the page -- >  driver.title
time.sleep(5) # Wait for 5 seconds
driver.close() # Close the browser


