from player import Player
from units import UnitFactory
from battle import Battle
from terrain import Terrain

import math

class Game:
    def __init__(self):
        self.players = [Player(input("Please enter the first player's name: ")), Player(input("Please enter the second player's name: "))]
        self.terrain = Terrain()

    def start(self):
        self.setup_game()
        self.play_game()
        self.end_game()

    def setup_game(self):
        initial_cash = 1000
        for player in self.players:
            player.add_money(initial_cash)
            self.setup_units(player)

    def setup_units(self, player):
        print(f"\n{player.name}, purchase your units. Your budget: {player.money}$")
        while player.money > 0:
            unit = input("\nWhat type of unit would you like?\n1) Troop (5$)\n2) Artillery (20$)\n3) Tank (100$)\nInput: ").lower()
            unit_obj = UnitFactory.create_unit(unit)
            if unit == "troop" or unit == "artillery" or unit == "tank":
                while True:
                    maxUnits = player.money / unit_obj.cost
                    if unit == "artillery":
                        unitCount = input(f"\nHow much {unit} would you like to buy for {unit_obj.cost}$ each?\nMaximum amount of {unit} with your budget of {player.money}$ is {maxUnits} {unit}.\nInput: ")
                    else:
                        unitCount = input(f"\nHow many {unit}s would you like to buy for {unit_obj.cost}$ each?\nMaximum amount of {unit}s with your budget of {player.money}$ is {maxUnits} {unit}s.\nInput: ")
                    
                    if unitCount.isdigit():
                        totalUnitsCost = int(unitCount) * unit_obj.cost
                        while True:
                            moneyLeft = player.money - totalUnitsCost
                            if moneyLeft < 0:
                                moneyLeft = moneyLeft * -1
                            if totalUnitsCost > player.money:
                                print(f"\nYou can't afford that. It is {moneyLeft}$ over your budget of {player.money}$")
                                deniedPurchase = True
                                break
                            else:
                                if unit == "artillery":
                                    print(f"\nAfter buying {unitCount} {unit}, you would be left with {moneyLeft}$")
                                else:
                                    print(f"\nAfter buying {unitCount} {unit}s, you would be left with {moneyLeft}$")
                                if unit == "artillery":
                                    confirmPurchase = input(f"\nDo you want to purchase {unitCount} {unit} for {totalUnitsCost}$?\n1) Yes\n2) No\nInput: ").lower()
                                else:
                                    confirmPurchase = input(f"\nDo you want to purchase {unitCount} {unit}s for {totalUnitsCost}$?\n1) Yes\n2) No\nInput: ").lower()
                                if confirmPurchase == "yes" or confirmPurchase == "no":
                                    if confirmPurchase == "yes":
                                        deniedPurchase = False
                                        break
                                    if confirmPurchase == "no":
                                        deniedPurchase = True
                                        break
                                else:
                                    print("=" * 30)
                                    print("Please enter 'yes' or 'no'")
                                    print("=" * 30)
                        break
                    else:
                        print("\n")
                        print("=" * 30)
                        print("Please enter a number.")
                        print("=" * 30)
                if not deniedPurchase:
                    for _ in range(int(unitCount)):
                        if unit_obj and player.can_afford(unit_obj.cost):
                            player.purchase_unit(unit_obj)
            else:
                print("\n")
                print("=" * 40)
                print("Incorrect unit type. Please try again.")
                print("=" * 40)

    def play_game(self):
        for _ in range(30):
            battle = Battle(self.players[0], self.players[1], self.terrain.get_random_terrain())
            battle.fight()

    def end_game(self):
        print("Game Over")
        winner = self.determine_winner()
        if winner:
            print(f"{winner.name} wins!")
        else:
            print("It's a draw!")

    def determine_winner(self):
        if self.players[0].unit_count() > self.players[1].unit_count():
            return self.players[0]
        elif self.players[0].unit_count() < self.players[1].unit_count():
            return self.players[1]
        else:
            return None