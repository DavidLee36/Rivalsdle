import json

with open("heroes_lore.json", "r") as file:
    hero_lore = json.load(file)
    print(hero_lore)

for hero in hero_lore:
    print(hero)