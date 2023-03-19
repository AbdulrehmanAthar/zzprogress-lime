from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
# Set the path to the chromedriver executable
chromedriver_path = os.path.join(
    os.getcwd(), 'C:/Users/asadi/Downloads/chromedriver_win32 (1)/chromedriver.exe')

# Start the ChromeDriver service
service = Service(executable_path=chromedriver_path)
service.start()
# Path to chromedriver executable

# Create webdriver instance with path to
driver = webdriver.Chrome(service=service)
# Launch Chrome browser and open the Oodo.com sign-up page
driver = webdriver.Chrome()
driver.get("https://www.odo.com/sign-up")

# Locate the form fields and fill them with valid and invalid credentials
email_input = driver.find_element(By.NAME, "email")
email_input.send_keys("invalidemail")
phone_input = driver.find_element(By.NAME, "phone")
phone_input.send_keys("1234567890")
password_input = driver.find_element(By.NAME, "password")
password_input.send_keys("weakpassword")
confirm_password_input = driver.find_element(By.NAME, "confirm_password")
confirm_password_input.send_keys("weakpassword")
first_name_input = driver.find_element(By.NAME, "first_name")
first_name_input.send_keys("John")
last_name_input = driver.find_element(By.NAME, "last_name")
last_name_input.send_keys("Doe")

# Click the "Create Account" button
create_account_button = driver.find_element(By.CSS_SELECTOR, ".btn-primary[type='submit']")
create_account_button.click()

# Verify that the error message for the invalid phone number is displayed
error_message = driver.find_element(By.CSS_SELECTOR, ".text-danger")
assert "Invalid phone number" in error_message.text

# Close the browser window
driver.quit()
