#Scenario 6: Track Retention Rate

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

# Create webdriver instance with path to chromedriver executable
driver = webdriver.Chrome(service=service)

# Navigate to the Odoo login page
driver.get("http://localhost:8069/web/login")

# Enter login credentials and submit the form
username_input = driver.find_element(By.ID, "login")
password_input = driver.find_element(By.ID, "password")
username_input.send_keys("store")
password_input.send_keys("store")
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

# Go to Apps menu and select Subscriptions
app_menu = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[title='Home Menu']")))
app_menu.click()
menu_item = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.LINK_TEXT, "Apps")))
menu_item.click()
search_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@name='Q']")))
search_input.send_keys("subscriptions")
search_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
search_button.click()
subscriptions_link = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[text()='Subscriptions']")))
subscriptions_link.click()

# Select date range and click Reload button
start_date = "2022-01-01"
end_date = "2022-01-31"
start_date_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='start_date']")))
start_date_input.clear()
start_date_input.send_keys(start_date)
end_date_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='end_date']")))
end_date_input.clear()
end_date_input.send_keys(end_date)
reload_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[name='reload']")))
reload_button.click()

# Verify retention rate
expected_retention_rate = 75.00
actual_retention_rate = float(WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "td[name='retention_rate']"))).text.replace("%", ""))
assert abs(actual_retention_rate - expected_retention_rate) < 0.01

# Quit the browser
driver.quit()
