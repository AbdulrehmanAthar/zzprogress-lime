from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# set up the webdriver
driver = webdriver.Chrome()

# navigate to the sign-up page
driver.get("https://www.odoo.com/page/sign-up")

# enter invalid email address
email_field = driver.find_element(By.NAME, "email")
email_field.send_keys("invalid_email_address")

# enter valid credentials for other fields
first_name_field = driver.find_element(By.NAME, "firstname")
first_name_field.send_keys("John")

last_name_field = driver.find_element(By.NAME, "lastname")
last_name_field.send_keys("Doe")

company_field = driver.find_element(By.NAME, "company_name")
company_field.send_keys("ABC Inc.")

phone_field = driver.find_element(By.NAME, "phone")
phone_field.send_keys("1234567890")

password_field = driver.find_element(By.NAME, "password")
password_field.send_keys("password123")

# click the "Create Account" button
create_account_button = driver.find_element(By.XPATH, "//button[text()='Create Account']")
create_account_button.click()

# verify that the error message is displayed
try:
    error_message = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'Invalid email address')]"))
    )
    print("Error message displayed: ", error_message.text)
except:
    print("Error message not displayed")

# close the browser
driver.quit()