import random
import json

class Battle:
    def __init__(self, player1, player2, terrain):
        self.player1 = player1
        self.player2 = player2
        self.terrain = terrain
        self.city = self.get_random_city()

    def get_random_city(self):
        with open('cities.json', 'r') as f:
            cities = json.load(f)
        return random.choice(cities)

    def fight(self):
        # print(f"Battle on {self.terrain} terrain!") # will be redone to be made like "battle of [city]"
        # p1_value = sum(unit.value for unit in self.player1.units)
        # p2_value = sum(unit.value for unit in self.player2.units)

        # decide whos the attacker and whos the defender, and assign attack and defender debuff/buff
        attacker = random.randint(1,2)
        p1_attack = 0
        p2_attack = 0
        p1_defence = 0
        p2_defence = 0
        p1_unit_count = self.player1.unit_count()
        p2_unit_count = self.player2.unit_count()

        print(f"\n===== Battle of {self.city['name']} =====")

        if attacker == 1:
            print(f"\n{self.player1.name} is attacking {self.player2.name}'s position.")

            # terrain modifiers
            if self.terrain == "mountain":
                p1_attack = 0.7
                p2_defence = 1.3
            elif self.terrain == "plains":
                p1_attack = 1.3
                p2_defence = 0.8
            elif self.terrain == "forest":
                p1_attack = 0.9
                p2_defence = 1.1

            p1_casualties = round((p1_unit_count / random.randint(10,20)) * p1_attack)
            p2_casualties = round((p2_unit_count / random.randint(10,20)) * p2_defence)

            self.player1.remove_units("Troop", p1_casualties)
            self.player2.remove_units("Troop", p2_casualties)

            p1_unit_count = self.player1.unit_count()
            p2_unit_count = self.player2.unit_count()

            print(f"\n{self.player1.name} lost {p1_casualties} units while {self.player2.name} lost {p2_casualties} units.\n{self.player1.name} has {p1_unit_count} units left while {self.player2.name} has {p2_unit_count} units left.")
        else:
            print(f"\n{self.player2.name} is attacking {self.player1.name}'s position.")

            # terrain modifiers
            if self.terrain == "mountain":
                p2_attack = 0.7
                p1_defence = 1.3
            elif self.terrain == "plains":
                p2_attack = 1.3
                p1_defence = 0.8
            elif self.terrain == "forest":
                p2_attack = 0.9
                p1_defence = 1.1

            # fighting mechanics

            p1_casualties = round((p1_unit_count / random.randint(10,20)) * p2_attack)
            p2_casualties = round((p2_unit_count / random.randint(10,20)) * p1_defence)

            self.player1.remove_units("Troop", p1_casualties)
            self.player2.remove_units("Troop", p2_casualties)

            p1_unit_count = self.player1.unit_count()
            p2_unit_count = self.player2.unit_count()

            print(f"\n{self.player1.name} lost {p1_casualties} units while {self.player2.name} lost {p2_casualties} units.\n{self.player1.name} has {p1_unit_count} units left while {self.player2.name} has {p2_unit_count} units left.")