NUM_ITEMS = 5
NUM_LOCATIONS = 5

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

def initialise_game(difficulty):
    pass


def process_command(command, player, game_map):
    pass


def fetch_quest():
    """
    Initialises the game, then runs the Fetch Quest game loop.
    Prompts the user for commands, updates the player state, and checks whether the win condition has been met.
    """
    difficulty = int(input("Enter difficulty level (1–100): ")) # convert text input to integer
    game_map, player = initialise_game(difficulty)
    running = True
    won = False
    while running and not won:
        player.location.describe()
        command = input("What do you want to do? ") # TODO consider sanitising the input
        running = process_command(command, player, game_map)
        # Determine if the player has won:
        # 1. They must collect all required items
        # 2. They must return to the starting location
        won = (len(player.inventory) == NUM_ITEMS) and (player.location == game_map.starting_location)

    if won:
        print('Congratulations')
        # only other option is to quit which is dealt with by process_command and returns False

if __name__ == "__main__":
    fetch_quest()
