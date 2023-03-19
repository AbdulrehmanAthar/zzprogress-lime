#Scenario 1: Create Subscription

#python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Start the webdriver
driver = webdriver.Chrome()

# Navigate to the subscription creation page
driver.get("https://example.com/create_subscription")

# Fill out the subscription form
subscription_type = driver.find_element_by_name("subscription_type")
subscription_type.send_keys("Monthly")
# Fill in the rest of the form fields as necessary

# Submit the form
submit_button = driver.find_element_by_css_selector("button[type='submit']")
submit_button.click()

# Wait for the success message to appear
success_message = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, ".success-message"))
)

# Verify that the subscription was created successfully
assert "Subscription created successfully" in success_message.text

# Close the webdriver
driver.quit()