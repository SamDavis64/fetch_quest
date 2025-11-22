# ----- GameMap Class -----
class GameMap:
    def __init__(self, num_locations, num_items):
        self.locations = []
        self.item_names = []

        self.locations = self.create_locations(num_locations)
        self.connect_locations()
        self.starting_location = self.locations[0]
        self.item_names = self.generate_item_names(num_items)
        self.distribute_items()


    def create_locations1(self, num):
        prefixes = [
            "Whispering", "Crimson", "Foggy", "Azure", "Twilight",
            "Echoing", "Glowing", "Howling", "Sunken", "Obsidian",
            "Silver", "Ember", "Frosted", "Verdant", "Hidden"
        ]

        suffixes = [
            "Hollow", "Tower", "Dunes", "Pass", "Keep",
            "Caverns", "Marsh", "Ridge", "Vale", "Point",
            "Spire", "Forest", "Glade", "Sanctum", "Reach"
        ]

        names = set()
        while len(names) < num:
            names.add(random.choice(prefixes) + " " + random.choice(suffixes))

        names = list(names) # Convert set to a list

        locations = []
        for name in names:  # Loop through each name in the 'names' collection
            location = Location(name)
            locations.append(location)
        return locations

    def create_locations(self, num):
        """Create and return a list of unique Location objects."""
        prefixes = [
            "Whispering", "Crimson", "Foggy", "Azure", "Twilight",
            "Echoing", "Glowing", "Howling", "Sunken", "Obsidian",
            "Silver", "Ember", "Frosted", "Verdant", "Hidden"
        ]

        suffixes = [
            "Hollow", "Tower", "Dunes", "Pass", "Keep",
            "Caverns", "Marsh", "Ridge", "Vale", "Point",
            "Spire", "Forest", "Glade", "Sanctum", "Reach"
        ]

        # ----- Generate all possible prefix-suffix combinations -----
        all_names = []
        for p in prefixes:
            for s in suffixes:
                name = p + " " + s
                all_names.append(name)

        # Shuffle the full list of names
        random.shuffle(all_names)

        # Select only as many as needed for this game
        selected_names = all_names[:num]

        # Create Location objects
        locations = []
        for name in selected_names:
            location = Location(name)
            locations.append(location)

        return locations
