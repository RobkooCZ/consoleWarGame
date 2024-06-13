from player import Player
from units import UnitFactory
from battle import Battle
from terrain import Terrain
import os
import math

class Game:
    def __init__(self):
        self.players = [Player(input("Please enter the first player's name: ")), Player(input("Please enter the second player's name: "))]
        self.terrain = Terrain()

    def start(self):
        self.setup_game()
        self.play_game()

    def setup_game(self):
        initial_cash = 1000
        for player in self.players:
            player.add_money(initial_cash)
            self.setup_units(player)

    def setup_units(self, player):
        os.system("cls" if os.name == "nt" else "clear")
        print(f"\n{player.name}, purchase your units. Your budget: {player.money}$")
        while player.money > 0:
            unit = input("\nWhat type of unit would you like?\n1) Troop (5$)\n2) Artillery (20$)\n3) Tank (100$)\nInput: ").lower()
            unit_obj = UnitFactory.create_unit(unit)
            if unit in ["troop", "artillery", "tank"]:
                while True:
                    max_units = int(player.money / unit_obj.cost)
                    if unit == "artillery":
                        unit_count = input(f"\nHow many {unit} would you like to buy for {unit_obj.cost}$ each?\nMaximum amount of {unit} with your budget of {player.money}$ is {max_units} {unit}.\nInput: ")
                    else:
                        unit_count = input(f"\nHow many {unit}s would you like to buy for {unit_obj.cost}$ each?\nMaximum amount of {unit}s with your budget of {player.money}$ is {max_units} {unit}s.\nInput: ")

                    if unit_count.isdigit():
                        total_units_cost = int(unit_count) * unit_obj.cost
                        money_left = player.money - total_units_cost

                        if total_units_cost > player.money:
                            print(f"\nYou can't afford that. It is {abs(money_left)}$ over your budget of {player.money}$")
                            break
                        else:
                            if unit == "artillery":
                                print(f"\nAfter buying {unit_count} {unit}, you would be left with {money_left}$")
                            else:
                                print(f"\nAfter buying {unit_count} {unit}s, you would be left with {money_left}$")

                            confirm_purchase = input(f"\nDo you want to purchase {unit_count} {unit}(s) for {total_units_cost}$?\n1) Yes\n2) No\nInput: ").lower()
                            if confirm_purchase in ["1", "yes"]:
                                for _ in range(int(unit_count)):
                                    if unit_obj and player.can_afford(unit_obj.cost):
                                        player.purchase_unit(unit_obj)
                                break
                            elif confirm_purchase in ["2", "no"]:
                                break
                            else:
                                print("=" * 30)
                                print("Please enter 'yes' or 'no'")
                                print("=" * 30)
                    else:
                        print("\n")
                        print("=" * 30)
                        print("Please enter a number.")
                        print("=" * 30)
            else:
                print("\n")
                print("=" * 40)
                print("Incorrect unit type. Please try again.")
                print("=" * 40)

    def play_game(self):
        while True:
            battle = Battle(self.players[0], self.players[1], self.terrain.get_random_terrain())
            battle.fight()
            if self.players[0].unit_count() <= 0 or self.players[1].unit_count() <= 0:
                if self.players[0].unit_count() <= 0:
                    print("=" * 40)
                    print(f"\nTHE WAR HAS BEEN WON BY {self.players[1].name}!\n")
                    print("=" * 40)
                else:
                    print("=" * 40)
                    print(f"\nTHE WAR HAS BEEN WON BY {self.players[0].name}!\n")
                    print("=" * 40)
                break