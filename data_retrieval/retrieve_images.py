import requests
from bs4 import BeautifulSoup
import os

# Step 1: Fetch the webpage
url = "https://marvelrivals.fandom.com/wiki/Heroes"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}
response = requests.get(url, headers=headers)

save_path = "C:/Users/david/Desktop/Programs/MarvelRivalsdle/Rivalsdle/src/assets/hero_icons/"

# Ensure the save path exists
os.makedirs(save_path, exist_ok=True)

# Check if the request was successful
if response.status_code == 200:
    # Step 2: Parse the HTML
    soup = BeautifulSoup(response.text, "html.parser")

    # Step 3: Find the `ul` with class `select-list`
    tbody = soup.find("tbody")
    trows = tbody.find_all("tr")
    rows = trows[1:len(trows)-2]  # Remove the top row, and the last two
    for row in rows:
        tdata = row.find_all("td")
        img_cell = tdata[1]

        src = img_cell.find("img")['data-src']
        src = src[0:src.find("png")+3]  # Remove 'revisions' from url to get og image
        name_idx = src.find("images") + 12

        # Name to save the image as
        name = src[name_idx:len(src)-9].replace("_", " ")

        response = requests.get(src, stream=True)
        response.raise_for_status()

        save = os.path.join(save_path, f"{name}.png")

        with open(save, "wb") as file:
            for chunk in response.iter_content(1024):
                file.write(chunk)
        print(f"Image downloaded: {save}")

else:
    print(f"Failed to fetch the webpage. Status code: {response.status_code}")
