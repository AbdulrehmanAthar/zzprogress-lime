from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Launch the Chrome browser and navigate to the sign-up page
driver = webdriver.Chrome()
driver.get("https://www.odo.com/signup")

# Enter valid credentials in the input fields
first_name_input = driver.find_element_by_name("first_name")
first_name_input.send_keys("John")

last_name_input = driver.find_element_by_name("last_name")
last_name_input.send_keys("Doe")

email_input = driver.find_element_by_name("email")
email_input.send_keys("johndoe@example.com")

# Enter a weak password
password_input = driver.find_element_by_name("password")
password_input.send_keys("password")

# Click the "Create Account" button
create_account_button = driver.find_element_by_xpath("//button[contains(text(),'Create Account')]")
create_account_button.click()

# Verify that an error message is displayed for the weak password
error_message = driver.find_element_by_xpath("//div[contains(text(),'Password strength is too weak')]")
assert error_message.is_displayed()

# Close the
