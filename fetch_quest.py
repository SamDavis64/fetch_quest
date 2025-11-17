# BEGIN fetch_quest
def fetch_quest():
    difficulty = int(input("Enter difficulty level (1–100): "))
    game_map, player = initialise_game(difficulty)
    running = True
    won = False
    while running and not won:
#		Print description of players current location
#		Get command
#		running = process_command(command, player, game_map)
#		won = (number of items = NUM_ITEMS) AND (player.location = game_map.starting_location)
#	ENDWHILE
#	IF won THEN
#		Print “Congratulations!”
#	ENDIF
# END fetch_quest

if __name__ == "__main__":
    fetch_quest()
