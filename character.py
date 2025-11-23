# ----- Character Class -----
from location import Location
from item import Item

class Character:
    """
    Characters traverse locations collecting items
    """
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


if __name__ == "__main__":
    test_location = Location("Test location")
    test_location.items = [Item("Item1"), Item("Item2"), Item("Item3")]
    player = Character("Fred", test_location)
    player.take_item("item1")
    player.take_item("item2")
    player.inventory_list()
