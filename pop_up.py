from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# Set up Chrome options
options = Options()
options.add_argument("--disable-popup-blocking")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
# Initialize WebDriver
driver = webdriver.Chrome(options=options)
driver.get("https://outlook.office.com/mail/")
# Wait and close pop-up by finding its frame or unique element (assumed)
WebDriverWait(driver, 30).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, "iframe.popUpFrame")))
driver.find_element(By.CSS_SELECTOR, "button.closePopUp").click()
# Switch back to the main content after closing the pop-up
driver.switch_to.default_content()