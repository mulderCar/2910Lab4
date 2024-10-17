import requests

run = True

# Function to format and display spell data
def display_spell_info(spell):
    if spell.get('name'):
        print(f"Spell Name: {spell.get('name')}")
    if spell.get('desc'):
        print(f"Description: {' '.join(spell.get('desc', []))}")
    if spell.get('higher_level'):
        print(f"Higher Levels: {' '.join(spell.get('higher_level', []))}")
    if spell.get('range'):
        print(f"Range: {spell.get('range')}")
    if spell.get('components'):
        print(f"Components: {', '.join(spell.get('components', []))}")
    if spell.get('material'):
        print(f"Material: {spell.get('material')}")
    if spell.get('duration'):
        print(f"Duration: {spell.get('duration')}")
    if spell.get('casting_time'):
        print(f"Casting Time: {spell.get('casting_time')}")
    if spell.get('level') is not None:
        print(f"Level: {spell.get('level')}")
    if spell.get('school'):
        print(f"School: {spell.get('school', {}).get('name')}")
    if spell.get('attack_type'):
        print(f"Attack Type: {spell.get('attack_type')}")
    if spell.get('damage'):
        print(f"Damage: {spell.get('damage')}")
    print()

# Function to format and display monster data
def display_monster_info(monster):
    if monster.get('name'):
        print(f"Monster Name: {monster.get('name')}")
    if monster.get('size'):
        print(f"Size: {monster.get('size')}")
    if monster.get('type'):
        print(f"Type: {monster.get('type')}")
    if monster.get('alignment'):
        print(f"Alignment: {monster.get('alignment')}")
    if monster.get('armor_class') is not None:
        print(f"Armor Class: {monster.get('armor_class')}")
    if monster.get('hit_points'):
        print(f"Hit Points: {monster.get('hit_points')} (Hit Dice: {monster.get('hit_dice')})")
    if monster.get('speed') and monster.get('speed').get('walk'):
        print(f"Speed: {monster.get('speed').get('walk')}")

    # Display monster stats if they exist
    print("Ability Scores:")
    if monster.get('strength'):
        print(f"  Strength: {monster.get('strength')}")
    if monster.get('dexterity'):
        print(f"  Dexterity: {monster.get('dexterity')}")
    if monster.get('constitution'):
        print(f"  Constitution: {monster.get('constitution')}")
    if monster.get('intelligence'):
        print(f"  Intelligence: {monster.get('intelligence')}")
    if monster.get('wisdom'):
        print(f"  Wisdom: {monster.get('wisdom')}")
    if monster.get('charisma'):
        print(f"  Charisma: {monster.get('charisma')}")

    # Display actions if they exist
    if monster.get('actions'):
        print("Actions:")
        for action in monster.get('actions', []):
            if action.get('name'):
                print(f"  {action['name']}: {action.get('desc', '')}")
    print()

# Function to format and display equipment data
def display_equipment_info(equipment):
    if equipment.get('name'):
        print(f"Equipment Name: {equipment.get('name')}")
    if equipment.get('equipment_category'):
        print(f"Category: {equipment.get('equipment_category', {}).get('name')}")
    if equipment.get('cost') and equipment.get('cost').get('quantity') and equipment.get('cost').get('unit'):
        print(f"Cost: {equipment.get('cost').get('quantity')} {equipment.get('cost').get('unit')}")
    if equipment.get('weight'):
        print(f"Weight: {equipment.get('weight')} lbs")
    if equipment.get('damage'):
        print(f"Damage: {equipment.get('damage', {}).get('damage_dice')} {equipment.get('damage', {}).get('damage_type', {}).get('name')}")
    if equipment.get('armor_class'):
        print(f"Armor Class: {equipment.get('armor_class', {}).get('base')}")
    if equipment.get('properties'):
        print(f"Properties: {', '.join([prop['name'] for prop in equipment.get('properties', [])])}")
    print()

# Function to format and display class data
def display_class_info(class_data):
    if class_data.get('name'):
        print(f"Class Name: {class_data.get('name')}")
    if class_data.get('hit_die'):
        print(f"Hit Die: {class_data.get('hit_die')}")
    if class_data.get('saving_throws'):
        print(f"Saving Throws: {', '.join([save['name'] for save in class_data.get('saving_throws', [])])}")
    if class_data.get('proficiencies'):
        print(f"Proficiencies: {', '.join([prof['name'] for prof in class_data.get('proficiencies', [])])}")
    if class_data.get('starting_equipment'):
        print(f"Starting Equipment: {', '.join([eq['equipment']['name'] for eq in class_data.get('starting_equipment', [])])}")
    if class_data.get('subclasses'):
        print(f"Subclasses: {', '.join([subclass['name'] for subclass in class_data.get('subclasses', [])])}")
    print()

# Function to ask for category selection
def get_category_choice():
    while True:
        try:
            print("Pick a category:")
            print("1: Spells")
            print("2: Monsters")
            print("3: Equipment")
            print("4: Classes")
            choice = int(input("Enter your choice: "))
            if choice in [1, 2, 3, 4]:
                return choice
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Function to ask for a random number choice
def get_random_choice(max_number):
    while True:
        try:
            choice = int(input(f"Pick a number between 1 and {max_number}: "))
            if 1 <= choice <= max_number:
                return choice - 1
            else:
                print(f"Invalid choice. Please enter a number between 1 and {max_number}.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Function to make API calls and handle errors
def fetch_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP errors
        return response.json()  # Parse JSON response
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

# Main function to handle the API calls and category-based formatting
def main():
    base_url = "https://www.dnd5eapi.co/api/"
    category_choice = get_category_choice()

    if category_choice == 1:
        spells_data = fetch_data(base_url + "spells")
        if spells_data:
            spells = spells_data['results']
            max_spells = len(spells)
            print(f"There are {max_spells} spells available.")
            random_choice = get_random_choice(max_spells)
            selected_spell = spells[random_choice]
            spell_details = fetch_data(base_url + f"spells/{selected_spell['index']}")
            if spell_details:
                print("Here is all the information about your selected spell:")
                display_spell_info(spell_details)

    elif category_choice == 2:
        monsters_data = fetch_data(base_url + "monsters")
        if monsters_data:
            monsters = monsters_data['results']
            max_monsters = len(monsters)
            print(f"There are {max_monsters} monsters available.")
            random_choice = get_random_choice(max_monsters)
            selected_monster = monsters[random_choice]
            monster_details = fetch_data(base_url + f"monsters/{selected_monster['index']}")
            if monster_details:
                print("Here is all the information about your selected monster:")
                display_monster_info(monster_details)

    elif category_choice == 3:
        equipment_data = fetch_data(base_url + "equipment")
        if equipment_data:
            equipment_list = equipment_data['results']
            max_equipment = len(equipment_list)
            print(f"There are {max_equipment} equipment items available.")
            random_choice = get_random_choice(max_equipment)
            selected_equipment = equipment_list[random_choice]
            equipment_details = fetch_data(base_url + f"equipment/{selected_equipment['index']}")
            if equipment_details:
                print("Here is all the information about your selected equipment:")
                display_equipment_info(equipment_details)

    elif category_choice == 4:
        classes_data = fetch_data(base_url + "classes")
        if classes_data:
            classes = classes_data['results']
            max_classes = len(classes)
            print(f"There are {max_classes} classes available.")
            random_choice = get_random_choice(max_classes)
            selected_class = classes[random_choice]
            class_details = fetch_data(base_url + f"classes/{selected_class['index']}")
            if class_details:
                print("Here is all the information about your selected class:")
                display_class_info(class_details)

while run:
    if __name__ == "__main__":
        main()
        run = input("Would you like to run the program again? (yes/no) ") == "yes"