# DnD 5e API Data Fetcher

This is a simple Python application that fetches and displays data from the Dungeons and Dragons 5th Edition API. The program allows users to choose between different categories such as spells, monsters, equipment, and classes, and randomly select an item from each category for detailed information.

## Features

- **Spells:** Fetches and displays spell information such as name, description, higher levels, range, components, casting time, etc.
- **Monsters:** Fetches and displays monster information including size, type, armor class, hit points, abilities, and actions.
- **Equipment:** Fetches and displays equipment details like name, category, cost, weight, damage, and properties.
- **Classes:** Fetches and displays class information such as name, hit die, saving throws, proficiencies, starting equipment, and subclasses.

## How to Use

1. Clone or download this repository.
2. Install the required dependency:
   ```bash
   pip install requests
   ```
3. Run the Python script:
   ```bash
   Lab3.py
   ```
4. The program will prompt you to select one of the following categories:
   - **1:** Spells
   - **2:** Monsters
   - **3:** Equipment
   - **4:** Classes

5. After selecting a category, the program will ask you to choose a random number from the available list of items.
6. The selected item's details will be displayed on the screen.

7. Once you finish, you will be asked to run the program again. Type "yes" to restart or "no" to exit.

## Example

```
Pick a category:
1: Spells
2: Monsters
3: Equipment
4: Classes
Enter your choice: 1
There are 319 spells available.
Pick a number between 1 and 319: 45
Here is all the information about your selected spell:
Spell Name: Fireball
Description: A bright streak flashes from your pointing finger to a point you choose within range and then blossoms with a low roar into an explosion of flame.
Range: 150 feet
Components: V, S, M
Material: A tiny ball of bat guano and sulfur
Duration: Instantaneous
Casting Time: 1 action
Level: 3
School: Evocation
Attack Type: Ranged
Damage: {'damage_dice': '8d6', 'damage_type': {'name': 'fire'}}
```

## API Source

This script fetches data from the [DnD 5e API](https://www.dnd5eapi.co/). It is a free, community-powered API providing information on various Dungeons and Dragons 5th Edition aspects.

## Requirements

- Python 3.x
- `requests` library

You can install the `requests` library using:

```bash
pip install requests
```
