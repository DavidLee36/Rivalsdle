from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
import json

# Load JSON data
with open("marvel-character-names.json", "r") as file:
    hero_list = json.load(file)

# Set up WebDriver
service = Service("C:\\WebDrivers\\chromedriver.exe")  # Update the path
driver = webdriver.Chrome(service=service)

# Data to store all the heroes lore
heroes_lore = []

try:
    for hero in hero_list:
        hero_lore = {}
        data_to_find = ["gender", "role", "Identity", "Place of Origin", "Group Affiliation", "First Comic Appearance", "Game Release Date"]
        name = hero["lore_name"]
        game_name = hero["game_name"]
        url = f"https://www.marvel.com/characters/{name}/in-comics"
        print(f"Visiting: {url}")

        driver.get(url)
        time.sleep(2)  # Allow the page to load

        for data in data_to_find:
            try:
                # Find the label
                label = driver.find_element(By.XPATH, f"//p[text()='{data}']")

                # Check for sibling type
                sibling = label.find_element(By.XPATH, "following-sibling::*")

                if sibling.tag_name == "p":
                    # For simple text data
                    value = sibling.text
                elif sibling.tag_name == "ul":
                    # For list data
                    items = sibling.find_elements(By.XPATH, ".//li")
                    value = [item.text for item in sibling.find_elements(By.XPATH, ".//li")]
                else:
                    # Default if no match
                    value = "Unknown format"

                hero_lore[data] = value
                print(f"{data}: {value}")

            except Exception as e:
                # If the tag is missing, set value to "None"
                print(f"Missing tag for {data}: {e}")
                hero_lore[data] = "manual" # Note to manually find and input the data

        heroes_lore.append({game_name: hero_lore})
        print()

finally:
    driver.quit()

# Optionally save the results to a file
with open("heroes_lore.json", "w") as file:
    json.dump(heroes_lore, file, indent=4)
