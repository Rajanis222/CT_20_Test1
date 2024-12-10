# # Firefox invocation 1
# import time
# from selenium import webdriver
# driver = webdriver.Firefox()
#
# driver.get("https://www.google.com")
# driver.maximize_window()
# print(f"Title of the page is -- > {driver.title}")
# time.sleep(5)
# driver.close()

# Firefox Invocation 2

import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service

# Specifying the path to geckodriver
# firefox_service = Service("C:/Drivers/geckodriver-v0.33.0-win64/geckodriver.exe") # Setting up the service to local chrome driver
#
# # Initializing the WebDriver with the specified service
# driver = webdriver.Firefox(service=firefox_service)
# driver.maximize_window()
# driver.get("https://credence.in/")
# print(f"Title of the page is -- > {driver.title}")
# time.sleep(5)
# driver.close()


# # Firefox Invocation 3
# import time
#
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
# from selenium.webdriver.firefox.service import Service
#
# # Automatically download and use the appropriate version of GeckoDriver
# driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
#
# # Example usage
# driver.get("https://credence.in/")
# print(f"Title of the page is -- > {driver.title}") # Print the title of the page -- > driver.title) # Print the title of the page -- >  driver.title
# time.sleep(5) # Wait for 5 seconds
# driver.close() # Close the browser

# Firefox invocation 4
import time

from selenium import webdriver
from selenium.webdriver.firefox.options import Options

firefox_options = Options()
firefox_options.add_argument("--headless") # Run Chrome in headless mode (no visible browser windows)
driver = webdriver.Firefox(options=firefox_options) # Initialize the WebDriver with the specified options and arguments

driver.get("https://credence.in/")
print(f"Title of the page is -- > {driver.title}") # Print the title of the page -- > driver.title) # Print the title of the page -- >  driver.title
time.sleep(5) # Wait for 5 seconds
driver.close() # Close the browser