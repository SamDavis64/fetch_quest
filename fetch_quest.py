import math
from game_map import GameMap
from character import Character

NUM_ITEMS = 5
NUM_LOCATIONS = 5

# ----- Function to calc number of locations and items -----
def calc_num_locations_items(difficulty):
    """set global NUM_LOCATIONS and NUM_ITEMS."""
    global NUM_LOCATIONS, NUM_ITEMS
    NUM_LOCATIONS = difficulty
    NUM_ITEMS = min(int(math.sqrt(difficulty)) + 5, difficulty)


# ----- Initialize Game -----
def initialise_game(difficulty):
    """Initialises the game and returns the game map and player."""
    print("Welcome to Fetch Quest!")
    calc_num_locations_items(difficulty)
    game_map = GameMap(NUM_LOCATIONS, NUM_ITEMS)
    player = Character("Adventurer", game_map.starting_location)
    print(f"Collect {NUM_ITEMS} items and return to {player.location.name} to win!")
    return game_map, player


# ----- Process Player Command -----
def process_command(command, player, game_map):
    """Process the player's input command."""
    if command.startswith("go "):
        direction = command[3:]
        if direction in ["north", "south", "east", "west"]:
            player.move(direction)
        else:
            print("Invalid direction. Use north, south, east, or west.")
    elif command.startswith("take "):
        item_name = command[5:]
        player.take_item(item_name)
    elif command == "inventory":
        player.inventory_list()
    elif command == "look":
        player.location.describe()
    elif command == "map":
        game_map.display_map()
    elif command == "quit":
        print("Thanks for playing!")
        return False
    else:
        print("Unknown command. Try: go <direction>, take <item>, inventory, look, map, quit")
    return True



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
