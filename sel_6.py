import json
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

CHROME_WINDOW_SIZE = "1920,1080"
PAGE_LOAD_WAIT_SEC = 60
DELAY_SEC = 3

#Function to load authentication credentials
def load_credentials(credentials_file):
    with open(credentials_file) as json_file:
        return json.load(json_file)
    
# Initialize Chrome driver
def init_driver():
    chrome_options = Options()
    chrome_options.add_argument(f"--window-size={CHROME_WINDOW_SIZE}")
    chrome_options.add_argument("--disable-popup-blocking")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)
    driver = webdriver.Chrome(options=chrome_options)
    return driver    
   
# Function to handle 'Stay signed in?' prompt and click 'Yes'
def handle_stay_signed_in_prompt(driver):
    driver_wait = WebDriverWait(driver, 60)
    try:
        print("Looking for 'Stay signed in?' prompt...")
        stay_signed_in_btn = driver_wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@id='acceptButton']")))
        stay_signed_in_btn.click()  # Click the "Yes" button
        print("Clicked 'Yes' on the Stay Signed In prompt.")
    except Exception as e:
        print(f"Could not find or click 'Stay signed in?' button: {e}")
          
# Log in to Outlook using Selenium
def login_outlook(driver, credentials):
    driver_wait = WebDriverWait(driver, PAGE_LOAD_WAIT_SEC)

    # Navigate to outlook.office.com/mail
    print("Navigating to Outlook login page...")
    driver.get("https://outlook.office.com/mail/")
    time.sleep(DELAY_SEC)

    # Input email address
    print("Entering email...")
    login_box = driver_wait.until(EC.presence_of_element_located((By.NAME, "loginfmt")))
    login_box.send_keys(credentials["username"])
    login_box.send_keys(Keys.RETURN)
    time.sleep(DELAY_SEC)

    # Input password
    print("Entering password...")
    password_box = driver_wait.until(EC.presence_of_element_located((By.NAME, "passwd")))
    password_box.send_keys(credentials["password"])
    password_box.send_keys(Keys.RETURN)
    time.sleep(DELAY_SEC)
     
    # Handle the 'Stay signed in?' prompt
    print("Handling 'Stay signed in?' prompt...")
    handle_stay_signed_in_prompt(driver)

# Block email pop-ups
    try:
         WebDriverWait(driver, 20).until(
             EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, "iframe.popUpFrame"))
         )
         driver.find_element(By.CSS_SELECTOR, "button.closePopUp").click()
         driver.switch_to.default_content()
         print("Closed the email pop-up successfully.")
    except Exception as e:
         print(f"No pop-up found or failed to close pop-up: {e}")
    #Confirm if logged in by checking if the "New message" button is loaded
    try:
        inbox = driver_wait.until(EC.presence_of_element_located((By.XPATH, '//button[@aria-label="New mail"]')))
        print("Successfully logged in.")
    except Exception as e:
        print(f"Could not log in: {e}")

# Function to send email using Selenium
def send_email_selenium(driver, subject, body_content, recipient_list):
    driver_wait = WebDriverWait(driver, 60)
    
    #Click "New message" button
    print("Clicking 'New mail' button...")
    try:
        new_message_btn = driver_wait.until(EC.presence_of_element_located((By.XPATH, '//button[@aria-label="New mail"]')))
        new_message_btn.click()
    except Exception as e:
        print(f"Failed to click 'New mail' button: {e}")
        return
    time.sleep(2)
    print("Filling in the 'To' field...")
    try:
        to_field = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, '//div[contains(text(), "To")]'))
    )
        #to_field = driver_wait.until(EC.presence_of_element_located((By.XPATH, '//input[contains(@aria-label, "To")]')))
        driver.execute_script("arguments[0].scrollIntoView(true);", to_field)
        driver.execute_script("arguments[0].focus();", to_field)
        to_field.send_keys(", ".join(recipient_list))  # Add recipients
        to_field.send_keys(Keys.RETURN)
    except Exception as e:
        print(f"Failed to fill 'To' field: {e}")
        return
    time.sleep(5)  

#Fill in the subject
    print("Filling in the subject...")
    try:
        subject_field = driver_wait.until(EC.presence_of_element_located((By.XPATH, '//input[@aria-label="Add a subject"]')))
        driver.execute_script("arguments[0].scrollIntoView(true);", subject_field)
        driver.execute_script("arguments[0].focus();", subject_field)
        subject_field.send_keys(subject)
    except Exception as e:
        print(f"Failed to fill 'Subject' field: {e}")
        return
    time.sleep(2)    
# Fill in the email body content
    print("Filling in the body content...")
    try:
        body_field = driver_wait.until(EC.presence_of_element_located((By.XPATH, '//div[@aria-label="Message body"]')))
        driver.execute_script("arguments[0].scrollIntoView(true);", body_field)
        driver.execute_script("arguments[0].focus();", body_field)
        body_field.send_keys(body_content)
    except Exception as e:
        print(f"Failed to fill 'Message body': {e}")
        return
    time.sleep(2)        
# Click the Send button using JavaScript if needed
    print("Clicking the 'Send' button...")
    try:
        send_btn = driver_wait.until(EC.presence_of_element_located((By.XPATH, '//button[@aria-label="Send"]')))
        driver.execute_script("arguments[0].scrollIntoView(true);", send_btn)
        driver.execute_script("arguments[0].focus();", send_btn)
        send_btn.click()
    except Exception as e:
        print(f"Failed to click 'Send' button: {e}")
        return
    time.sleep(3)
    print("Email sent successfully.")    
    
    # Example usage
if __name__ == "__main__":
    # Load credentials (multiple accounts)
    credentials_file = r'C:\Users\sohad\OneDrive\Desktop\Python\BacBon\codes\authen.json'
    credentials = load_credentials(credentials_file)

    # Initialize the Chrome driver
    driver = init_driver()

    # Log in to Outlook using credentials
    login_outlook(driver, credentials)

    # Create the email content
    subject = "Your Dynamic HTML Email"
    body_content = "This is a test email sent using Selenium!"
    recipient_list = ['humayra.bacbon@gmail.com']

    # Send the email
    send_email_selenium(driver, subject, body_content, recipient_list)

    driver.switch_to.default_content()
    # Close the driver after sending
    driver.quit()
    
    