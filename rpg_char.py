import math
from enum import Enum

class CharacterClass(Enum):
    WARRIOR = 1
    MAGE = 2
    ROGUE = 3

print("--- RPG Character Creator ---")


char_name = input("Enter your character's name: ").strip().title()

print("Choose a class:")
print("1. Warrior\n2. Mage\n3. Rogue")
class_choice = input("Enter 1, 2, or 3: ")

if class_choice == '1':
    char_class = CharacterClass.WARRIOR
    base_stats = (150, 20, 100) 
elif class_choice == '2':
    char_class = CharacterClass.MAGE
    base_stats = (80, 150, 40)
else:
    char_class = CharacterClass.ROGUE
    base_stats = (100, 50, 120)

hp, mp, stamina = base_stats

character = {
    "name": char_name,
    "class": char_class.name,
    "stats": {
        "hp": hp,
        "mp": mp,
        "stamina": stamina
    },
    "gold": 50
}

inventory = ["Health Potion", "Wooden Sword"]

discovered_locations = {"Starter Village"}

print(f"\nWelcome, {character['name']} the {character['class']}!")


new_item = input("You found a chest! What item did you find? ")
inventory.append(new_item)

character["stats"]["attack"] = 10
character["stats"]["defense"] = 5

new_location = input("You traveled to a new area. Where are you? ")
discovered_locations.add(new_location)


combat_power = math.sqrt(character["stats"]["hp"] * character["stats"]["attack"]) + character["stats"]["stamina"]

character["combat_power"] = round(combat_power, 2)

print("\n--- Character Profile ---")
print(f"Stats: {character['stats']}")
if "Health Potion" in inventory:
    print(f"Inventory: {inventory} (You are safe, you have a potion!)")
else:
    print(f"Inventory: {inventory}")
    
print(f"Locations Discovered: {discovered_locations}")
print(f"Combat Power: {character['combat_power']}")

is_strong = True if character["combat_power"] > 120 else False

print("\nIs " + character['name'] + " ready for the boss? " + ("Yes!" if is_strong else "Not yet, keep training."))
