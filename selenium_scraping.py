from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize the Selenium WebDriver (Chrome in this case)
driver = webdriver.Chrome()  # Make sure the path to chromedriver is in your PATH

try:
    # Step 1: Go to Telegram website
    driver.get("https://my.telegram.org")
    
    # Step 2: Click on 'API Development Tools'
    # WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "API development tools"))).click()

    # Step 3: Enter your phone number and submit
    phone_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "my_login_phone")))
    phone_input.send_keys("+12394527521")  # Enter your phone number here
    driver.find_element(By.CSS_SELECTOR, "div.support_submit button[type='submit']").click()

    # Wait for the code to arrive (you must enter this manually)
    code = input("Enter the code you received: ")

    # Step 4: Enter the received code
    code_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "my_password")))
    code_input.send_keys(code)
    driver.find_element(By.CSS_SELECTOR, "div.support_submit button[type='submit']").click()

    # Step 5: Wait for login and get api_id and api_hash
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "API development tools"))).click()
    api_id = driver.find_element(By.XPATH, "//span[contains(text(), 'api_id')]/following-sibling::span").text
    api_hash = driver.find_element(By.XPATH, "//span[contains(text(), 'api_hash')]/following-sibling::span").text

    print(f"API ID: {api_id}")
    print(f"API Hash: {api_hash}")

finally:
    # Close the browser
    driver.quit()
