#Scenario 6: Track Retention Rate

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Start the webdriver
driver = webdriver.Chrome()

# Navigate to the retention rate page
driver.get("https://example.com/retention_rate")

# Track the retention rate
track_retention_rate_button = driver.find_element_by_css_selector("button[name='track_retention_rate']")
track_retention_rate_button.click()

# Wait for the retention rate to be calculated and displayed
retention_rate = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, ".retention-rate"))
)

# Verify that the retention rate was calculated and displayed successfully
assert retention_rate.text != ""

# Close the webdriver
driver.quit()