#Scenario 4: Track Revenue

#python

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver

# Set the path to the chromedriver executable
chromedriver_path = os.path.join(
    os.getcwd(), 'E:\My downloads\chromedriver_win32 (1)/chromedriver.exe')

# Start the ChromeDriver service
service = Service(executable_path=chromedriver_path)
service.start()
# Path to chromedriver executable

# Create webdriver instance with path to
driver = webdriver.Chrome(service=service)
# Navigate to the Odoo login page
driver.get("http://localhost:8069/web/login")

# Enter login credentials and submit the form

username_input = driver.find_element(By.ID, "login")

password_input = driver.find_element(By.ID, "password")
username_input.send_keys("store")
password_input.send_keys("store")
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
app_menu =  WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[title='Home Menu']")))
app_menu.click()
menu_item =  WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.LINK_TEXT, "Apps")))
menu_item.click()
# Go to subscription page
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@name='Q']"))).send_keys("subscription")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,"//button[@type='submit']"))).click()
# WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[text()='Subscriptions']"))).click()

# Select date range
start_date = "2022-01-01"
end_date = "2022-01-31"
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='start_date']"))).clear()
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='start_date']"))).send_keys(start_date)
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='end_date']"))).clear()
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='end_date']"))).send_keys(end_date)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[name='reload']"))).click()

# Verify revenue
expected_revenue = 1000.00
actual_revenue = float(WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "td[name='revenue']"))).text.replace(",", ""))
assert abs(actual_revenue - expected_revenue) < 0.01

try:
    driver.implicitly_wait(10)
finally:
    # Quit the browser
    driver.quit()
