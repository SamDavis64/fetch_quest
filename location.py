# ----- Location Class -----
class Location:
    """Each location has its own items and connected neighbours"""
    def __init__(self, name):
        self.name = name
        self.items = []
        self.neighbors = {}

    def connect(self, other, direction):
        opposites = {'north': 'south', 'south': 'north',
                     'east': 'west', 'west': 'east'}
        self.neighbors[direction] = other
        other.neighbors[opposites[direction]] = self

    def describe(self):
        print(f"\nYou are at {self.name}.")
        if self.items:
            print("You see the following items:")
            for item in self.items:
                print(f" - {item}")
        else:
            print("There is nothing of interest here.")
        if self.neighbors:
            print("Exits:", ", ".join(self.neighbors.keys()))
        else:
            print("There are no visible exits.")  # Should never occur

