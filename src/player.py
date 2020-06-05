# Write a class to hold player information, e.g. what room they are in
# currently.

class Player():
    def __init__(self, name, current_room, items):
        self.name = name
        self.current_room = current_room
        self.items = items
        
    # def print_items(self):
    #     if len(self.inventory) > 0:
    #         print("There are the following items before you:")
    #         for item in self.inventory:
    #             print(item)
    #     else: print("There's nothing in your inventory")
        
    # def grab(self, ind):
    #     grabbed = self.current_room.pop(ind)
    #     self.inventory.append(grabbed)

            
        