import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select # Dropdown

browser = webdriver.Firefox()
browser.get("https://apps.credence.in/practice")
browser.maximize_window()


# Select Dropdown
dropdown_box = Select(browser.find_element(By.ID, "dropdown-class-example"))
dropdown_box.select_by_visible_text("Option2")

time.sleep(3)
dropdown_box.select_by_index(3)


scrolltothiselement = browser.find_element(By.CLASS_NAME,  "toggle-label")
browser.execute_script("arguments[0].scrollIntoView();", scrolltothiselement)

# Scroll you can give the specific height and weight
# Verify that Dropdown option 2 is selected
assert dropdown_box.first_selected_option.text == "Option2", "Dropdown option 2 is not selected"


time.sleep(3)

browser.close()