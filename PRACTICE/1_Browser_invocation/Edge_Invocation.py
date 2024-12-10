# # Edge Invocation 1
#
# import time
# from selenium import webdriver
# driver=webdriver.Edge()
# driver.get("https://www.google.com")
# driver.maximize_window()
# print(f"Title of the page is: {driver.title}")
# time.sleep(3)
# driver.close()
import time

# # Edge Invocation 2
# from selenium import webdriver
# from selenium.webdriver.edge.service import Service
#
# # specifying the path to edge driver
# edge_service=Service("C:/Drivers/edgedriver_win64/msedgedriver.exe")
#
# #Initializing the webdriver with specified service
# driver=webdriver.Edge(service=edge_service)
# driver.get("https://www.google.com")
# driver.maximize_window()
# print(f"Title of the page is: {driver.title}")
# time.sleep(2)
# driver.close()

# # Edge invocation 3
# from selenium import webdriver
# from webdriver_manager.microsoft import EdgeChromiumDriverManager
# from selenium.webdriver.edge.service import Service
#
# driver=webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
#
# driver.get("https://www.google.com")
# print(f"Title of the page is -- > {driver.title}")
# time.sleep(2)
# driver.close()

#Edge Invocation 4

import time
from selenium import webdriver
from selenium.webdriver.edge.options import Options

edge_options=Options()
edge_options.add_argument("--headless")
driver = webdriver.Edge(options=edge_options)
driver.get("https://credence.in/")
print(f"Title of the page is -- > {driver.title}")
time.sleep(2)
driver.close()

