import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
driver=webdriver.Chrome()  # start chrome
driver.maximize_window() #maximize window
driver.get("https://apps.credence.in/practice") # nevigate to given url

# # Radio button 1
# radio_button1=driver.find_element(By.XPATH,"//input[@value='radio1']").click()
# #time.sleep(1)
# # Radio button 2
# radio_button2=driver.find_element(By.CSS_SELECTOR,"input[value='radio2']")
# radio_button2.click()
# #time.sleep(1)
# # Radio button 3
# radio_button3=driver.find_element(By.XPATH, "//input[@value='radio3']")
# radio_button3.click()
# #time.sleep(2)

# Verify that the radio button is selected
#assert radio_button2.is_selected(), "Radio Button 2 is not selected"

# #textbox
# textbox=driver.find_element(By.ID,"autocomplete")
# textbox.send_keys("Credence Testing Academy")
# assert textbox.get_attribute("value")=="Credence Testing Academy"
# time.sleep(2)

# # Dropdown
# dropdown_box=Select(driver.find_element(By.ID,"dropdown-class-example"))
# dropdown_box.select_by_visible_text("Option2")
# time.sleep(2)

# dropdown_box.select_by_index(1)
# time.sleep(2)
#
# # Verify that Dropdown option 2 is selected
# #assert dropdown_box.first_selected_option.text == "Option1", "Dropdown option 1 is not selected"
#
# scrolltothiselement = driver.find_element(By.XPATH,  "/html/body/div[1]/fieldset[4]/legend")
# driver.execute_script("arguments[0].scrollIntoView();", scrolltothiselement)
# time.sleep(2)
#
# #Checkbox
checkbox_1=driver.find_element(By.ID,"checkBoxOption1")
checkbox_1.click()
time.sleep(2)
checkbox_2=driver.find_element(By.ID,"checkBoxOption2")

checkbox_2.click()
time.sleep(1)
checkbox_3=driver.find_element(By.ID,"checkBoxOption3")
checkbox_3.click()
time.sleep(1)
assert checkbox_1.is_selected(),"checkbox 1 is not selected"
#
#Multiselect box
# multiselect_box=Select(driver.find_element(By.XPATH, "//*[@id='multiSelect']"))
# multiselect_box.select_by_visible_text('Item 1')
# multiselect_box.select_by_visible_text('Item 3')
# multiselect_box.select_by_visible_text('Item 4')
#
# print(multiselect_box.all_selected_options[0].text)
# print(multiselect_box.all_selected_options[1].text)
# print(multiselect_box.all_selected_options[2].text)
#
# toggle switch
toggle_switch_male=driver.find_element(By.XPATH,"//label[@for='male']")
toggle_switch_male.click()
time.sleep(3)
# toggle switch-Female
toggle_switch_female=driver.find_element(By.XPATH,"//label[@for='female']")
toggle_switch_female.click()
time.sleep(3)
#verify if toggle switch is selected
#assert  toggle_switch_male.is_selected(),"Male is not selected"