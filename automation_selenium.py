import json
import time
import smtplib
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formataddr

CHROME_WINDOW_SIZE = "1920,1080"
DOWNLOAD_DIR = r"/path/to/your/folder"
PAGE_LOAD_WAIT_SEC = 60
DELAY_SEC = 3
BCC_BATCH_LIMIT = 10  # Sending limit for BCC recipients
SENDING_DELAY_SEC = 5  # Delay between sending batches
EMAIL_SEND_LIMIT = 50  # Number of emails that can be sent per session (adjust as needed)

# Function to load authentication credentials
def load_credentials(credentials_file):
    with open(credentials_file) as json_file:
        return json.load(json_file)

# Initialize Chrome driver
def init_driver():
    chrome_options = Options()
    chrome_options.add_argument(f"--window-size={CHROME_WINDOW_SIZE}")
    chrome_options.add_experimental_option("prefs", {
        "download.default_directory": DOWNLOAD_DIR,
        "download.prompt_for_download": False,
    })
    driver = webdriver.Chrome(options=chrome_options)
    return driver

# Log in to Outlook using Selenium
def login_outlook(driver, credentials):
    driver_wait = WebDriverWait(driver, PAGE_LOAD_WAIT_SEC)

    # Navigate to outlook.office.com/mail
    driver.get("https://outlook.office.com/mail/")
    time.sleep(DELAY_SEC)

    # Input email address
    login_box = driver_wait.until(EC.presence_of_element_located((By.NAME, "loginfmt")))
    login_box.send_keys(credentials["username"])
    login_box.send_keys(Keys.RETURN)

    time.sleep(DELAY_SEC)

    # Input password
    password_box = driver_wait.until(EC.presence_of_element_located((By.NAME, "passwd")))
    password_box.send_keys(credentials["password"])
    password_box.send_keys(Keys.ENTER)
    
    # Confirm my stay signed-in option
    stay_sign_in = (By.XPATH, "//button[@id='acceptButton']")
    stay_sign_in = driver_wait.until(EC.presence_of_element_located(stay_sign_in))
    stay_sign_in.click() 

# Function to create an HTML email
def create_email(subject, sender_name, sender_email, recipient_list, content_html):
    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = formataddr((sender_name, sender_email))
    msg['To'] = ', '.join(recipient_list)  # Just to display in the email header

    # Attach the HTML content
    msg.attach(MIMEText(content_html, 'html'))
    return msg

# Function to send an email batch via SMTP (you can customize to use selenium for Outlook web app)
def send_email_batch(smtp_server, smtp_port, sender_email, sender_password, email_batches):
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(sender_email, sender_password)
    
    for batch in email_batches:
        try:
            for msg in batch:
                server.sendmail(sender_email, msg['To'].split(', '), msg.as_string())
            print(f"Batch of {len(batch)} emails sent successfully!")
            time.sleep(SENDING_DELAY_SEC)  # Add delay between batches
        except Exception as e:
            print(f"Error sending batch: {e}")

    server.quit()

# Function to manage sending emails in batches
def send_emails_in_batches(email_list, subject, content_html, sender_name, sender_email, sender_password, smtp_server, smtp_port):
    email_batches = [email_list[i:i + BCC_BATCH_LIMIT] for i in range(0, len(email_list), BCC_BATCH_LIMIT)]
    
    messages = []
    for batch in email_batches:
        msg = create_email(subject, sender_name, sender_email, batch, content_html)
        messages.append(msg)

    # Send the email batches
    send_email_batch(smtp_server, smtp_port, sender_email, sender_password, [messages[i:i+BCC_BATCH_LIMIT] for i in range(0, len(messages), BCC_BATCH_LIMIT)])

# Function to handle multiple accounts and emails
def handle_multiple_accounts(account_list, email_list, subject, content_html):
    for account in account_list:
        print(f"Logging in and sending emails from account: {account['username']}")
        driver = init_driver()
        try:
            login_outlook(driver, account)
            
            # Send emails in batches for the current account
            send_emails_in_batches(
                email_list=email_list,
                subject=subject,
                content_html=content_html,
                sender_name=account['sender_name'],
                sender_email=account['username'],
                sender_password=account['password'],
                smtp_server='smtp.office365.com',  # Adjust for your SMTP server
                smtp_port=587
            )
        except Exception as e:
            print(f"Error with account {account['username']}: {e}")
        finally:
            driver.quit()

        print(f"Finished sending emails for account: {account['username']}")

# Example usage
if __name__ == "__main__":
    # Load credentials (multiple accounts)
    credentials_file = r'C:\Users\sohad\OneDrive\Desktop\Python\BacBon\codes\authen.json'
    credentials = load_credentials(credentials_file)

    # Create the HTML content for the email
    html_content = """
    <html>
        <body>
            <h1>Hi there!</h1>
            <p>This is a dynamically generated email with selenium. Do not reply. <b>HTML formatting</b>.</p>
        </body>
    </html>
    """

    # Example list of recipients
    recipient_list = ['humayra.bacbon@gmail.com', 'nourinhaqueridi@gmail.com', 'bushra70100@gmail.com']  # Extend as necessary

    # Handle multiple accounts for sending
    handle_multiple_accounts(
        account_list=credentials,  # List of accounts from the JSON file
        email_list=recipient_list,
        subject="Your Dynamic HTML Email",
        content_html=html_content
    )
