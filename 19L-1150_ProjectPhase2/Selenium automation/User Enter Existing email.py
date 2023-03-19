from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Initialize the browser and open the sign-up page
driver = webdriver.Chrome()
driver.get("https://www.odoo.com/signup")

# Enter the existing email address and other valid credentials
email = driver.find_element_by_name("login")
email.send_keys("existinguser@example.com")
first_name = driver.find_element_by_name("firstname")
first_name.send_keys("John")
last_name = driver.find_element_by_name("lastname")
last_name.send_keys("Doe")
password = driver.find_element_by_name("password")
password.send_keys("password123")

# Click the "Create Account" button
create_account_button = driver.find_element_by_css_selector("button[type='submit']")
create_account_button.click()

# Verify that the error message is displayed
error_message = driver.find_element_by_css_selector(".alert-danger")
assert error_message.is_displayed() and "already exists" in error_message.text

# Close the browser
driver.quit()
