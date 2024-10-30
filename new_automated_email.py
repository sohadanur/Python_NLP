#Medium Blog till home of message. 
import json
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

CHROME_WINDOW_SIZE = "1920,1080"
PAGE_LOAD_WAIT_SEC = 30  # Increased wait time for elements
DELAY_SEC = 5

# Load the authentication credentials
def load_credentials(credentials_file):
    try:
        with open(credentials_file) as json_file:
            print("Loading credentials...")
            return json.load(json_file)
    except Exception as e:
        print(f"Error loading credentials: {e}")
        return None

# Initialize the Chrome driver
def init_driver():
    print("Initializing Chrome driver...")
    chrome_options = Options()
    chrome_options.add_argument(f"--window-size={CHROME_WINDOW_SIZE}")
    driver = webdriver.Chrome(options=chrome_options)
    print("Chrome driver initialized.")
    return driver

# Switch to iframe if necessary
def switch_to_iframe(driver):
    try:
        iframe = driver.find_element(By.TAG_NAME, 'iframe')
        driver.switch_to.frame(iframe)
        print("Switched to iframe.")
    except Exception as e:
        print(f"No iframe found: {e}")

# Handle 'Stay signed in?' prompt and click 'Yes'
def handle_stay_signed_in_prompt(driver):
    driver_wait = WebDriverWait(driver, PAGE_LOAD_WAIT_SEC)
    print("Looking for 'Stay signed in?' prompt...")
    
    try:
        stay_signed_in_btn = driver_wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='acceptButton']"))  # Use XPath for the 'Yes' button
        )
        stay_signed_in_btn.click()  # Click the "Yes" button
        print("Clicked 'Yes' on the Stay Signed In prompt.")
    except Exception as e:
        print(f"Could not find or click 'Stay signed in' button: {e}")

# Log into Outlook using Selenium
def login_outlook(driver, credentials):
    driver_wait = WebDriverWait(driver, PAGE_LOAD_WAIT_SEC)

    # Navigate to outlook.office.com/mail
    print("Navigating to Outlook login page...")
    driver.get("https://outlook.office.com/mail/")
    time.sleep(DELAY_SEC)

    # Enter the email address
    try:
        print("Entering email...")
        email_box = driver_wait.until(EC.presence_of_element_located((By.NAME, "loginfmt")))
        email_box.send_keys(credentials["username"])
        email_box.send_keys(Keys.RETURN)
        print("Email entered.")
    except Exception as e:
        print(f"Error entering email: {e}")
    time.sleep(DELAY_SEC)

    # Enter the password
    try:
        print("Entering password...")
        password_box = driver_wait.until(EC.presence_of_element_located((By.NAME, "passwd")))
        password_box.send_keys(credentials["password"])
        password_box.send_keys(Keys.RETURN)
        print("Password entered.")
    except Exception as e:
        print(f"Error entering password: {e}")
    time.sleep(DELAY_SEC)

    # Handle 'Stay signed in?' prompt
    print("Handling 'Stay signed in?' prompt...")
    switch_to_iframe(driver)  # Try switching to iframe if necessary
    handle_stay_signed_in_prompt(driver)  # Handle "Stay signed in?" prompt

    # Wait for the inbox page to load
    try:
        inbox = driver_wait.until(EC.presence_of_element_located((By.ID, "id__7")))
        print("Successfully logged in and inbox loaded.")
    except Exception as e:
        print(f"Could not load inbox: {e}")

# Example usage
if __name__ == "__main__":
    # Load credentials (multiple accounts)
    credentials_file = r'C:\Users\sohad\OneDrive\Desktop\Python\BacBon\codes\authen.json'
    credentials = load_credentials(credentials_file)

    if credentials is None:
        print("Could not load credentials. Exiting.")
        exit()

    # Initialize the driver and login
    driver = init_driver()
    login_outlook(driver, credentials)
