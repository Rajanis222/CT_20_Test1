# pip install webdriver-manager # automatically download chrome driver which is compatible with you system chrome browser
import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

# Automatically download and use the appropriate version of chromedriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Example usage
driver.get("https://credence.in/")
print(f"Title of the page is -- > {driver.title}") # Print the title of the page -- > driver.title) # Print the title of the page -- >  driver.title
time.sleep(5) # Wait for 5 seconds
driver.close() # Close the browser