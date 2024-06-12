class Player:
    def __init__(self, name):
        self.name = name
        self.money = 0
        self.units = []

    def add_money(self, amount):
        self.money += amount

    def can_afford(self, cost):
        return self.money >= cost

    def purchase_unit(self, unit):
        if self.can_afford(unit.cost):
            self.units.append(unit)
            self.money -= unit.cost

    def unit_count(self):
        return len(self.units)
