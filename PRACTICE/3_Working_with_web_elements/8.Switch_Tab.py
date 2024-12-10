from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://apps.credence.in/practice")
print("Title of this page is:", driver.title)
# click on credence site tab
credence_site_tab=driver.find_element(By.ID,"opentab1")
credence_site_tab.click()
#switch to new tab
driver.switch_to.window(driver.window_handles[1])
print("Title of this page is: ", driver.title)
