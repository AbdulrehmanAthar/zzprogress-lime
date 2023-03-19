from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Instantiate the WebDriver
driver = webdriver.Chrome()

# Navigate to the sign-up page
driver.get("https://www.odo.com/signup/")

# Find the relevant form elements and fill them with valid credentials
username_input = driver.find_element_by_id("username")
username_input.send_keys("example_user")

email_input = driver.find_element_by_id("email")
email_input.send_keys("example_user@example.com")

password_input = driver.find_element_by_id("password")
password_input.send_keys("example_password")

confirm_password_input = driver.find_element_by_id("confirm_password")
confirm_password_input.send_keys("example_password")

# Submit the form
submit_button = driver.find_element_by_id("create_account_button")
submit_button.click()

# Check if the user is redirected to the dashboard and the account is created successfully
dashboard_title = driver.find_element_by_tag_name("h1").text

if dashboard_title == "Dashboard":
    print("Account created successfully!")
else:
    print("Account creation failed.")

# Close the WebDriver
driver.close()