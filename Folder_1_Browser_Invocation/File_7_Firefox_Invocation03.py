# pip install webdriver-manager # automatically download Firefox driver which is compatible with you system firefox browser
import time

from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service

# Automatically download and use the appropriate version of GeckoDriver
driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

# Example usage
driver.get("https://credence.in/")
print(f"Title of the page is -- > {driver.title}") # Print the title of the page -- > driver.title) # Print the title of the page -- >  driver.title
time.sleep(5) # Wait for 5 seconds
driver.close() # Close the browser