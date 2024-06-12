from player import Player
from units import UnitFactory
from battle import Battle
from terrain import Terrain

import math

class Game:
    def __init__(self):
        self.players = [Player("Player 1"), Player("Player 2")]
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
        print(f"{player.name}, purchase your units.")
        while player.money > 0:
            unit = input("What type of unit would you like?\n1) Troop\n2) Artillery\n3) Tank\nInput: ").lower()
            while True:
                if unit == "artillery":
                    unitCount = input(f"\nHow much {unit} would you like to buy?\nInput: ")
                else:
                    unitCount = input(f"\nHow many {unit}s would you like to buy?\nInput: ")
                
                if unitCount.isdigit():
                    break
                else:
                    print("\nPlease enter a number.")
            unit_obj = UnitFactory.create_unit(unit)

            for _ in range(int(unitCount)):
                if unit_obj and player.can_afford(unit_obj.cost):
                    player.purchase_unit(unit_obj)
                else:
                    if player.money < unit_obj.cost:
                        print(f"\nYou don't have enough money to purchase {unit}.")
                    else:
                        print("\nInvalid unit.")

    def play_game(self):
        for _ in range(3):
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