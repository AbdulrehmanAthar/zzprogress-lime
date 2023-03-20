#Scenario 1: Create Subscription

# This script navigates to the Odoo login page
 # and logs in with the specified credentials. 
 # It then navigates to the Subscription page,
 # clicks the Create button, and fills out 
 # the subscription form with test data. 
 # Finally, it verifies that the subscription 
 # was created successfully and closes the browser.
#python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set the path to the chromedriver executable
chromedriver_path = os.path.join(os.getcwd(), 'E:\My downloads\chromedriver_win32 (1)\chromedriver.exe')

# Start the ChromeDriver service
service = Service(executable_path=chromedriver_path)
service.start()

# Create webdriver instance with path to chromedriver
driver = webdriver.Chrome(service=service)

# Navigate to the Odoo login page
driver.get("http://localhost:8069/web/login")

# Enter login credentials and submit the form
username_input = driver.find_element(By.ID, "login")
password_input = driver.find_element(By.ID, "password")
username_input.send_keys("store")
password_input.send_keys("store")
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

# Navigate to the subscriptions page
app_menu = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[aria-expanded='false']")))
app_menu.click()
menu_item = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.LINK_TEXT, "Subscriptions")))
menu_item.click()
# Navigate to the subscription page
app_menu = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[title='Home Menu']")))
app_menu.click()
menu_item =  WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.LINK_TEXT, "Subscription")))
menu_item.click()

# Click the Create button
create_button = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[class='btn btn-primary btn-sm o-kanban-button-new']")))
create_button.click()

# Fill out the subscription form
name_input = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='name']")))
name_input.send_keys("Test Subscription")
recurring_input = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='recurring_interval']")))
recurring_input.send_keys("1")
period_input = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "select[name='recurring_rule_type']")))
period_input.click()
period_option = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//option[@value='monthly']")))
period_option.click()
price_input = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='list_price']")))
price_input.send_keys("10")
description_input = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "textarea[name='description']")))
description_input.send_keys("This is a test subscription")
save_button = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[name='save']")))
save_button.click()

# Verify that the subscription was created successfully
success_message = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.o_notification_content")))
assert "Subscription Test Subscription has been created." in success_message.text

# Close the browser
driver.quit()
