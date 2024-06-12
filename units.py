class Unit:
    def __init__(self, name, cost, value):
        self.name = name
        self.cost = cost
        self.value = value

class Troop(Unit):
    def __init__(self):
        super().__init__("Troop", 5, 1)

class Artillery(Unit):
    def __init__(self):
        super().__init__("Artillery", 20, 3)

class Tank(Unit):
    def __init__(self):
        super().__init__("Tank", 100, 5)

class UnitFactory:
    @staticmethod
    def create_unit(unit_type):
        if unit_type == "troop":
            return Troop()
        elif unit_type == "artillery":
            return Artillery()
        elif unit_type == "tank":
            return Tank()
        return None
