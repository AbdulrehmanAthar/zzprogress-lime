#Scenario 7: Generate Monthly Report

#This test case logs into the Odoo system, 
# navigates to the Subscriptions page, 
# selects the monthly report view, 
# sets the date range and applies 
# the filter, and then verifies the 
# revenue total for the month matches 
# the expected value.
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

# Select monthly report view
view_select = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".o_view_controller .o_cp_switch_buttons .o_switch_view.o_switch_list")))
view_select.click()
monthly_report = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".o_cp_switch_buttons .o_switch_view.o_switch_kanban")))
monthly_report.click()

# Set date range and apply filter
start_date = "2022-01-01"
end_date = "2022-01-31"
start_date_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".o_searchview .o_datepicker input.o_datepicker_input.o_input[name='start_date']")))
end_date_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".o_searchview .o_datepicker input.o_datepicker_input.o_input[name='end_date']")))
start_date_input.clear()
start_date_input.send_keys(start_date)
end_date_input.clear()
end_date_input.send_keys(end_date)
apply_filter = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".o_searchview .o_facet_values button.o_apply_filter")))
apply_filter.click()

# Verify revenue total for the month
expected_revenue = 1000.00
actual_revenue = float(WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".o_kanban_view .o_kanban_record:first-child .o_kanban_footer .o_stat_value")).text.replace(",", "")))
assert abs(actual_revenue - expected_revenue) < 0.01

# Quit the browser
driver.quit()
