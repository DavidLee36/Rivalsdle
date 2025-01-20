from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
import json

with open("marvel-character-names.json", "r") as file:
    hero_list = json.load(file)

# Set up WebDriver (update the path to your ChromeDriver)
service = Service("C:\\WebDrivers\\chromedriver.exe")  # Update the path here
driver = webdriver.Chrome(service=service)

# Data to store all the heroes lore
hero_lore = []

try:
    for hero in hero_list:
        url = f"https://www.marvel.com/characters/{hero["lore_name"]}/in-comics"
        print(f"Visiting: {url}")

        driver.get(url)
finally:
    driver.quit()