from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import json

# Set up WebDriver (update the path to your ChromeDriver)
service = Service("C:\\WebDrivers\\chromedriver.exe")
driver = webdriver.Chrome(service=service)

try:
    # Open the target URL
    driver.get("https://www.marvelrivals.com/heroes")

    # Allow time for the page to fully load
    time.sleep(5)

    # Find the `ul` element with class `select-list` inside `select-box`
    select_list = driver.find_element(By.CSS_SELECTOR, ".select-box .select-list")

    # Extract `data-id` attributes from all `li` elements
    hero_ids = [li.get_attribute("data-id") for li in select_list.find_elements(By.TAG_NAME, "li")]

    print(f"Hero IDs: {hero_ids}")

    # Save hero IDs to `hero-ids.json`
    with open("hero-ids.json", "w") as file:
        json.dump(hero_ids, file, indent=4)

    print("Hero IDs saved successfully!")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    # Close the WebDriver
    driver.quit()
