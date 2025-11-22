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

    def connect_locations(self):
        # Connect all locations into a simple tree structure
        directions = ['north', 'south', 'east', 'west']

        unconnected = self.locations[:]
        connected = [unconnected.pop(0)]

        while unconnected:
            # Pick a connected location that still has available exits
            available = [loc for loc in connected if len(loc.neighbors) < len(directions)]
            if not available:
                # all connected locations are full; stop connecting
                break

            loc1 = random.choice(available)
            loc2 = unconnected.pop(0)

            # choose a direction that is still free
            free_dirs = [d for d in directions if d not in loc1.neighbors]
            if not free_dirs:
                continue  # just in case, skip if somehow no free directions

            dir = random.choice(free_dirs)
            loc1.connect(loc2, dir)
            connected.append(loc2)


    def generate_item_names(self, num):
        adjectives = [
            "Glowing", "Ancient", "Silver", "Mystic", "Cracked",
            "Golden", "Dark", "Frozen", "Burning", "Silent",
            "Cursed", "Radiant", "Enchanted", "Shadowed", "Blessed"
        ]
        nouns = [
            "Orb", "Key", "Crystal", "Ring", "Tome",
            "Stone", "Amulet", "Lantern", "Scroll", "Gem",
            "Blade", "Crown", "Mask", "Chalice", "Feather"
        ]
        names = set()
        while len(names) < num:
            names.add(random.choice(adjectives) + " " + random.choice(nouns))
        return list(names)

    def distribute_items(self):
        items = [Item(name) for name in self.item_names]
        for item in items:
            location = random.choice(self.locations)
            location.items.append(item)

    def display_map(self):
        """Display a readable table of all locations, their items, and directions."""
        print("\n=== GAME MAP ===")
        print(f"{'Location':30} | {'Items':35} | {'N':^3} | {'S':^3} | {'E':^3} | {'W':^3}")
        print("-" * 85)
        for loc in self.locations:
            items_str = ", ".join([item.name for item in loc.items]) if loc.items else "-"
            dirs = {d: "✓" if d in loc.neighbors else " " for d in ['north', 'south', 'east', 'west']}
            print(f"{loc.name:30} | {items_str:35} | {dirs['north']:^3} | {dirs['south']:^3} | {dirs['east']:^3} | {dirs['west']:^3}")
        print("-" * 85)

