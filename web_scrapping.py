# Importing necessary packages
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time  # for adding delay

# Create a Service object using the ChromeDriver executable path
service = Service(ChromeDriverManager().install())

# Initialize the Chrome driver
driver = webdriver.Chrome(service=service)

# For holding the resultant list
element_list = []

# Loop through the pages
for page in range(1, 3):
    page_url = "https://webscraper.io/test-sites/e-commerce/static/computers/laptops?page=" + str(page)
    try:
        driver.get(page_url)
        # Adding a delay to ensure elements are loaded
        time.sleep(2)
        
        # Finding elements
        titles = driver.find_elements(By.CLASS_NAME, "title")
        prices = driver.find_elements(By.CLASS_NAME, "price")
        descriptions = driver.find_elements(By.CLASS_NAME, "description")
        ratings = driver.find_elements(By.CLASS_NAME, "ratings")

        # Loop to collect data
        for i in range(len(titles)):
            element_list.append([titles[i].text, prices[i].text, descriptions[i].text, ratings[i].text])

    except Exception as e:
        print(f"An error occurred while processing the page {page}: {e}")

# Close the driver after scraping
driver.quit()

# Print the scraped data
print(element_list)
