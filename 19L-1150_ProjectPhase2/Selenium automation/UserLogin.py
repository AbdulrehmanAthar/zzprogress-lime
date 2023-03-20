from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# Set the path to the chromedriver executable
chromedriver_path = os.path.join(os.getcwd(), 'H:/Uni/Sem8/ST (1)/chromedriver.exe')
service = Service(executable_path=chromedriver_path)
service.start()
# Create webdriver instance with path to chromedriver
driver = webdriver.Chrome(service=service)
driver.get("http://localhost:8069/web/signup")
username_input = driver.find_element(By.ID, "name")
username_input.send_keys("ABD")
userpassword= driver.find_element(By.ID, "password")
userpassword.send_keys("11223344")
useremail=driver.find_element(By.ID,"login")
useremail.send_keys("1234@gmail.com")
userconfirmpassword=driver.find_element(By.ID,"confirm_password")
userconfirmpassword.send_keys("11223344")
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
success_message = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.o_notification_content")))
assert "Account Created." in success_message.text
driver.quit()
