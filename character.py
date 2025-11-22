# ----- Character Class -----
class Character:
    """Characters traverse the locations collecting items."""
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.inventory = []

    def move(self, direction):
        if direction in self.location.neighbors:
            self.location = self.location.neighbors[direction]
            print(f"You move {direction}.")
        else:
            print("You can't go that way.")

    def take_item(self, item_name):
        for item in self.location.items:
            if item.name.lower() == item_name.lower():
                self.inventory.append(item)
                self.location.items.remove(item)
                print(f"You picked up: {item.name}")
                return
        print("That item is not here.")

    def inventory_list(self):
        if self.inventory:
            print("You have collected:")
            for item in self.inventory:
                print(f" - {item}")
        else:
            print("You are carrying nothing.")
