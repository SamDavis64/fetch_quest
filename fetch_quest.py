NUM_ITEMS = 5
NUM_LOCATIONS = 5


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
