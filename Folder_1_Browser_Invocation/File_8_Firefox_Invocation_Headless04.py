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