# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.inventory = []

    def move(self, direction):
        if getattr(self.current_room, f"{direction}_to") is not None:
            self.current_room = getattr(self.current_room, f"{direction}_to")

    def __str__(self):
        return f"{self.name}'s current location: \n{self.current_room} "

    def take_item(self, item):
        self.inventory.append(item)
