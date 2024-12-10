from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time

# Set up WebDriver
driver = webdriver.Chrome()

# Load the target URL
driver.get("https://apps.credence.in/practice")  # Replace with your URL

# Maximize the browser window
driver.maximize_window()

# Locate the slider
slider = driver.find_element(By.ID, "slider")

# Get the slider's dimensions
slider_width = slider.size['width']
slider_location = slider.location['x']  # Starting position of the slider on the X-axis

print(f"Slider Width: {slider_width}")
print(f"Slider Location (X-axis): {slider_location}")

# Function to calculate offset for desired value
def calculate_offset(current_value, target_value, slider_width):
    """
    Calculate the offset needed to move the slider from current_value to target_value.
    """
    max_value = 100  # Slider max value
    min_value = 0    # Slider min value
    value_range = max_value - min_value
    pixels_per_value = slider_width / value_range  # Pixels per unit value
    return (target_value - current_value) * pixels_per_value

# Initialize ActionChains
actions = ActionChains(driver)

# Move to 'Low' position (0%)
time.sleep(2)
actions.click_and_hold(slider).move_by_offset(-slider_width // 2, 0).release().perform()
time.sleep(1)  # Allow time for the slider to update
low_value = slider.get_attribute('value')
print(f"Current Slider Value (Low): {low_value}")

# Calculate offset for 'Medium' (50%)
medium_offset = calculate_offset(int(low_value), 50, slider_width)
actions.click_and_hold(slider).move_by_offset(0, 0).release().perform()
time.sleep(1)
medium_value = slider.get_attribute('value')
print(f"Current Slider Value (Medium): {medium_value}")

# Calculate offset for 'High' (100%)
high_offset = calculate_offset(int(medium_value), 100, slider_width)
actions.click_and_hold(slider).move_by_offset(high_offset, 0).release().perform()
time.sleep(1)
high_value = slider.get_attribute('value')
print(f"Current Slider Value (High): {high_value}")

# Close the browser
driver.quit()
