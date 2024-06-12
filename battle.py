import random

class Battle:
    def __init__(self, player1, player2, terrain):
        self.player1 = player1
        self.player2 = player2
        self.terrain = terrain

    def fight(self):
        print(f"Battle on {self.terrain} terrain!")
        p1_value = sum(unit.value for unit in self.player1.units)
        p2_value = sum(unit.value for unit in self.player2.units)

        if self.terrain == "mountain":
            p1_value *= 1.2
        elif self.terrain == "plain":
            p2_value *= 1.2

        print(f"{self.player1.name} total value: {p1_value}")
        print(f"{self.player2.name} total value: {p2_value}")

        if p1_value > p2_value:
            print(f"{self.player1.name} wins this battle!")
        elif p2_value > p1_value:
            print(f"{self.player2.name} wins this battle!")
        else:
            print("This battle is a draw!")
