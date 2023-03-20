#Scenario 2: Update Subscription

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
# Wait for the inventory module to load and click on it
app_menu =  WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[title='Home Menu']")))
app_menu.click()
menu_item =  WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.LINK_TEXT, "Apps")))
menu_item.click()
product_button =  WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[title='Apps']")))
product_button.click()
products_menu =  WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.LINK_TEXT, "Main Apps")))
products_menu.click()

prod_search=WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//body/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/input[1]")))
prod_search.send_keys("subscriptions")

new_button =  WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.LINK_TEXT, "Upgrade")))
new_button.click()
# productsalesprice_input = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "name")))
# productsalesprice_input = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "name")))
# productsalesprice_input.send_keys("Burger")
# productsalesprice_input = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "list_price")))
# driver.execute_script('arguments[0].value = "";', productsalesprice_input)
# productsalesprice_input.send_keys("900")
# productcostprice_input = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "standard_price")))
# driver.execute_script('arguments[0].value = "";', productcostprice_input)
# productcostprice_input.send_keys("800")

# productBarcode_input = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "barcode")))
# productBarcode_input.send_keys("100200")

# product_button =  WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[title='Products']")))
# product_button.click()
# products_menu =  WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.LINK_TEXT, "Products")))
# products_menu.click()

try:
    driver.implicitly_wait(0) 
finally:
# Quit the browser
    driver.quit()
