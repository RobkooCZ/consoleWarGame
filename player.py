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
    
    def remove_units(self, unit_type, count):
        """
        Remove a specified number of units of a particular type from the player's collection.
        
        Parameters:
        - unit_type (str): The type of unit to remove (e.g., "Troop", "Artillery", "Tank").
        - count (int): The number of units to remove.
        """
        removed_count = 0
        for unit in self.units:
            if unit.name == unit_type:
                self.units.remove(unit)
                removed_count += 1
                if removed_count == count:
                    break
        return removed_count

