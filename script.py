from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Set Chrome options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")  # Run Chrome in headless mode (no GUI)

# Set the path to chromedriver
chrome_driver_path = "/usr/bin/chromedriver"

# Initialize the Chrome driver
driver = webdriver.Chrome(executable_path=chrome_driver_path, options=chrome_options)

# Navigate to a website
driver.get("https://www.google.com")

# Perform some actions (e.g., search on Google)
search_box = driver.find_element("name", "q")
search_box.send_keys("Docker Selenium example")
search_box.send_keys(Keys.RETURN)

# Wait for a while to see the results
time.sleep(5)

# Print the title of the page
print("Page title:", driver.title)

# Quit the browser
driver.quit()
