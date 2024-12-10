
# 1.Chrome Invocation 1
# import time
# from selenium import webdriver
#
# driver=webdriver.Chrome()
# driver.get("https://www.google.com/")
# driver.maximize_window()
# print(f"Title of the page: {driver.title}")
# time.sleep(5)
# driver.close()

# 2.Chrome Invocation 2
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

#specify the path to chrome driver
chrome_service=Service("C:/Drivers/chromedriver-win64/chromedriver-win64/chromedriver.exe")

#Initialize the WebDriver with specified service
driver=webdriver.Chrome(service=chrome_service)
driver.get("https://www.google.com")
driver.maximize_window()
print(f"Title of the page is: {driver.title}")
time.sleep(5)
driver.close()

# # 3.Automatically download and use the appropriate version of chromedriver
# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.service import Service
#
# driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#
# driver.get("https://www.google.com")
# driver.maximize_window()
# print(f"Title of the page is: {driver.title}")
# time.sleep(5)
# driver.close()

# # 4. Chrome invocation headless.

# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
#
# chrome_options=Options()
# chrome_options.add_argument("--headless")
# driver=webdriver.Chrome(options=chrome_options)
#
# driver.get("https://www.google.com")
# driver.maximize_window()
# print(f"Title of this page is: {driver.title}")
# time.sleep(3)
# driver.close()
