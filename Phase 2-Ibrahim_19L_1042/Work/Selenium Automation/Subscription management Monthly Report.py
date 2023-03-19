#Scenario 7: Generate Monthly Report

from selenium import webdriver

# Launch the browser and navigate to the monthly report page
driver = webdriver.Chrome()
driver.get("https://example.com/monthly-report")

# Select the customer's subscription and generate the report
subscription_select = driver.find_element_by_xpath("//select[@name='subscription']")
subscription_select.select_by_value("12345")
generate_button = driver.find_element_by_xpath("//button[@type='submit']")
generate_button.click()

# Verify that the report was generated and sent to the customer
assert driver.current_url == "https://example.com/monthly-report/success"
assert "Monthly report generated successfully" in driver.page_source

# Close the browser
driver.quit()
