from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
import json

# Load hero IDs from the JSON file
with open("hero-ids.json", "r") as file:
    hero_ids = json.load(file)

# Set up WebDriver (update the path to your ChromeDriver)
service = Service("C:\\WebDrivers\\chromedriver.exe")  # Update the path here
driver = webdriver.Chrome(service=service)

# Button image sources
l_click_src = "https://www.marvelrivals.com/pc/gw/20241128194803/img/sbzj_5901af42.png"
r_click_src = "https://www.marvelrivals.com/pc/gw/20241128194803/img/sbyj_ec1b2d5e.png"

# Data to store all heroes and their abilities
heroes_data = []

try:
    base_url = "https://www.marvelrivals.com/heroes/?id="

    for hero_id in hero_ids:
        # Build the hero's page URL
        url = f"{base_url}{hero_id}"
        print(f"Visiting: {url}")

        # Open the hero's page
        driver.get(url)

        # Allow time for the page to load
        time.sleep(2)

        # Get hero name
        character_name = driver.find_element(By.CLASS_NAME, "hero-nick").text
        print(character_name)

        # Store abilities data
        abilities = []

        # Find all `div` elements with class `skill-info`
        skill_info_divs = driver.find_elements(By.CLASS_NAME, "skill-info")

        if skill_info_divs:
            # Only process the first two divs
            for skill_div in skill_info_divs[:2]:
                # Extract and process all `li` elements within this div
                li_elements = skill_div.find_elements(By.TAG_NAME, "li")
                for li in li_elements:
                    button_element = li.find_element(By.CLASS_NAME, "tag1")
                    try:
                        # Check if the button contains an image
                        button_img = button_element.find_element(By.TAG_NAME, "img")
                        button_img_src = button_img.get_attribute("src")  # Get image source if it's an image
                        if button_img_src == l_click_src:
                            button = "L CLICK"
                        elif button_img_src == r_click_src:
                            button = "R CLICK"
                        else:
                            button = "UNKNOWN BUTTON"
                    except:
                        # Otherwise, assume it's plain text
                        button = button_element.text

                    # Get ability name and image source
                    name = li.find_element(By.CLASS_NAME, "tag2").text
                    img = li.find_element(By.CLASS_NAME, "img")
                    img_src = img.find_element(By.TAG_NAME, "img").get_attribute("src")

                    # Add ability data to the list
                    abilities.append({
                        "button": button,
                        "name": name,
                        "img_src": img_src
                    })

        # Add hero data to the main list
        heroes_data.append({
            "hero_name": character_name,
            "abilities": abilities
        })

finally:
    # Close the WebDriver
    driver.quit()

# Save all hero data to a JSON file
with open("heroes-abilities.json", "w") as file:
    json.dump(heroes_data, file, indent=4)

print("All hero data has been saved to heroes-abilities.json.")
