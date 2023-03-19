#Scenario 2: Update Subscription

#python

from selenium import webdriver

# Start the webdriver
driver = webdriver.Chrome()

# Navigate to the subscription update page
driver.get("https://example.com/update_subscription")

# Select the new subscription plan
new_plan = driver.find_element_by_name("new_plan")
new_plan.send_keys("Annual")

# Submit the form
submit_button = driver.find_element_by_css_selector("button[type='submit']")
submit_button.click()

# Verify that the subscription was updated successfully
assert "Subscription updated successfully" in driver.page_source

# Close the webdriver
driver.quit()