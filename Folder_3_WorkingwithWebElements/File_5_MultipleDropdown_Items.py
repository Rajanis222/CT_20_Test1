import time

from numpy.testing.print_coercion_tables import print_cancast_table
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://apps.credence.in/practice")
driver.maximize_window()

Dropdown_list = Select(driver.find_element(By.ID, 'multiSelect'))
time.sleep(2)
Dropdown_list.select_by_visible_text("Item 1")
time.sleep(2)
Dropdown_list.select_by_visible_text("Item 3")
time.sleep(2)
Dropdown_list.select_by_visible_text("Item 4")
time.sleep(2)
Dropdown_list.select_by_visible_text("Item 5")
time.sleep(2)


print(Dropdown_list.all_selected_options[0].text) # Output Item 1
print(Dropdown_list.all_selected_options[1].text) # Output Item 3
print(Dropdown_list.all_selected_options[2].text) # Output Item 4