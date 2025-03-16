from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from flask import Flask, request
import threading
import time

app = Flask(__name__)
verification_code = None

@app.route('/receive_code', methods=['POST'])
def receive_code():
    global verification_code
    data = request.json
    verification_code = data.get('code')
    return 'Code received'

def run_selenium():
    global verification_code
    driver = webdriver.Chrome('./chromedriver')
    driver.get("https://example.com")

    # Click the button to send the verification code
    button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#send_code_button"))
    )
    button.click()

    # Wait for the verification code
    while verification_code is None:
        time.sleep(1)

    # Enter the verification code into the form
    code_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#code_input"))
    )
    code_input.send_keys(verification_code)

    # Submit the form
    submit_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#submit_button"))
    )
    submit_button.click()

    driver.quit()

# Run Flask in a separate thread
def run_flask():
    app.run(debug=True)

# Start Flask
flask_thread = threading.Thread(target=run_flask)
flask_thread.daemon = True  # So that it dies when main thread dies
flask_thread.start()

# Run Selenium script
run_selenium()