import random
import json
import os
import time

class Battle:
    def __init__(self, player1, player2, terrain):
        """Initialize the Battle with two players and a terrain."""
        self.player1 = player1
        self.player2 = player2
        self.terrain = terrain
        self.city = self.get_random_city()

    def get_random_city(self):
        """Get a random city from the cities.json file."""
        with open('cities.json', 'r') as f:
            cities = json.load(f)
        return random.choice(cities)

    def calculate_casualties(self, unit_count, size_of_battle, attack_modifier, defense_modifier):
        """Calculate the number of casualties based on unit count, battle size, and modifiers."""
        if size_of_battle <= 200:
            return round((unit_count / random.randint(10, 20)) * attack_modifier), round((unit_count / random.randint(10, 20)) * defense_modifier)
        elif size_of_battle <= 400:
            return round((unit_count / random.randint(20, 40)) * attack_modifier), round((unit_count / random.randint(20, 40)) * defense_modifier)
        elif size_of_battle <= 600:
            return round((unit_count / random.randint(40, 60)) * attack_modifier), round((unit_count / random.randint(40, 60)) * defense_modifier)
        elif size_of_battle <= 800:
            return round((unit_count / random.randint(60, 80)) * attack_modifier), round((unit_count / random.randint(60, 80)) * defense_modifier)
        else:
            return round((unit_count / random.randint(80, 100)) * attack_modifier), round((unit_count / random.randint(80, 100)) * defense_modifier)

    def apply_terrain_modifiers(self, attacker, defender):
        """Apply terrain-specific modifiers to attack and defense values."""
        if self.terrain == "mountain":
            attacker['attack'] = 0.7
            defender['defense'] = 1.3
        elif self.terrain == "plains":
            attacker['attack'] = 1.3
            defender['defense'] = 0.8
        elif self.terrain == "forest":
            attacker['attack'] = 0.9
            defender['defense'] = 1.1

    def clear_screen(self):
        """Clear the console screen."""
        os.system("cls" if os.name == "nt" else "clear")

    def slow_print(self, text, delay=0.005):
        """Slowly print out the text with a specified delay."""
        for char in text:
            print(char, end='', flush=True)
            time.sleep(delay)
        print()

    def fight(self):
        """Execute the battle, calculate casualties, and display the results."""
        attacker = self.player1 if random.randint(1, 2) == 1 else self.player2
        defender = self.player2 if attacker == self.player1 else self.player1

        attacker_name = attacker.name
        defender_name = defender.name

        # Default attack and defense values
        attacker_modifiers = {'attack': 1.0}
        defender_modifiers = {'defense': 1.0}

        # Apply terrain-specific modifiers
        self.apply_terrain_modifiers(attacker_modifiers, defender_modifiers)

        attacker_unit_count = attacker.unit_count()
        defender_unit_count = defender.unit_count()

        size_of_battle = random.randint(1, 1000)

        # Calculate casualties for both attacker and defender
        attacker_casualties, defender_casualties = self.calculate_casualties(defender_unit_count, size_of_battle, attacker_modifiers['attack'], defender_modifiers['defense'])

        # Remove units based on calculated casualties
        attacker.remove_units("Troop", attacker_casualties)
        defender.remove_units("Troop", defender_casualties)

        # Update unit counts after battle
        attacker_unit_count = attacker.unit_count()
        defender_unit_count = defender.unit_count()

        # Clear screen and print results slowly
        self.clear_screen()
        self.slow_print(f"\n{'=' * 50}")
        self.slow_print(f"{'BATTLE OF ' + self.city['name'].upper():^50}")
        self.slow_print(f"{'=' * 50}\n")
        self.slow_print(f"{attacker_name} (Attacker) vs {defender_name} (Defender) on {self.terrain.upper()} terrain\n")
        self.slow_print(f"ATTACKER: {attacker_name}")
        self.slow_print(f"DEFENDER: {defender_name}\n")
        self.slow_print(f"{attacker_name} lost {attacker_casualties} units")
        self.slow_print(f"{defender_name} lost {defender_casualties} units\n")
        self.slow_print(f"{attacker_name} has {attacker_unit_count} units left")
        self.slow_print(f"{defender_name} has {defender_unit_count} units left")
        self.slow_print(f"\n{'=' * 50}")

        time.sleep(3)

