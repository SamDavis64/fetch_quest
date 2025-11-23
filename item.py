# ----- Item Class -----
class Item:
    """
    Items are collected as the game is played.
    """
    def __init__(self, name, description=""):
        self.name = name
        self.description = description  # not used currently

    def __str__(self):
        return self.name

