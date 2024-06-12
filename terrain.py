import random

class Terrain:
    def __init__(self):
        self.terrains = ["forest", "plains", "mountain"]

    def get_random_terrain(self):
        return random.choice(self.terrains)