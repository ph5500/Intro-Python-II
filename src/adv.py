from room import Room
from player import Player
from item import Item
import textwrap

# Declare all the rooms

room = {
    "outside": Room(
        "Outside Cave Entrance",
        "North of you, the cave mount beckons",
        [Item("Rock", "Just a rock")],
    ),
    "foyer": Room(
        "Foyer",
        """Dim light filters in from the south. Dusty
passages run north and east.""",
        [Item("Stick", "A long stick"), Item("Bag", "Just an empty bag")],
    ),
    "overlook": Room(
        "Grand Overlook",
        """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",
        [Item("Knife", "An old rusty knife")],
    ),
    "narrow": Room(
        "Narrow Passage",
        """The narrow passage bends here from west
to north. The smell of gold permeates the air.""",
        [Item("Sand", "Just sand")],
    ),
    "treasure": Room(
        "Treasure Chamber",
        """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south....but the smell of rot creeps into your nose from the west...""",
        [Item("Shield", "Round shield")],
    ),
    "stench": Room(
        "Graveyard of Bones",
        """You enter a cavern with a giant pit filled with rotting flesh and bones. Could this be a lair of a dragon? Possibly filled with
        treasure or sneak out before whatever is living here finds you.""",
        [Item("Sword", "Long sword"), Item("Coins", "A handful of silver coins")],
    ),
}


# Link rooms together
# change W
room["outside"].n_to = room["foyer"]
room["foyer"].s_to = room["outside"]
room["foyer"].n_to = room["overlook"]
room["foyer"].e_to = room["narrow"]
room["overlook"].s_to = room["foyer"]
room["narrow"].w_to = room["foyer"]
room["narrow"].n_to = room["treasure"]
room["treasure"].s_to = room["narrow"]
room["treasure"].w_to = room["stench"]
room["stench"].e_to = room["treasure"]

new_input = input("Hello adventurer, please tell me your name \n")
new_player = Player(new_input, room["outside"])


# welcome the user and let them know where they are
# print(
#     f"Welcome {new_player.name}, you are currently {new_player.current_room.name}, {new_player.current_room.description}"
# )

# change room function
def change_room(direction):
    new_player.move(direction)
    if getattr(new_player.current_room, f"{selection}_to") is None:
        print(
            """
            ========================================\n
            That's a dead end, you can't move that way \n
            ========================================
            """
        )


while True:
    selection = input(
        (
            f"""
            \n ---------------------- \n 
            {new_player} \n 
            ---------------------- \n 
            Press [N] for NORTH \n 
            Press [S] for SOUTH \n 
            Press [W] for WEST \n 
            Press [E] for EAST \n 
            Press [Q] to quit \n 
            What do you do? """
        )
    ).split(" ")

    if selection[0] == "q":
        print("See you next time")
        break
    # elif new_player.current_room.name == "Treasure Chamber":
    #     print("You left the cave empty handed. Try again in version 2")
    #     break
    try:
        if selection[0] == "n" or "s" or "w" or "e":
            change_room(selection[0])
    except AttributeError:
        print("Invalid option, please try again")
