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
player = Player(new_input, room["outside"])
movement_options = ["n", "e", "w", "s"]
item_options = ["g", "t", "d"]

# change room function
def change_room(direction):

    player.move(direction)
    if hasattr(player.current_room, f"{direction}_to") == False:
        print(
            """
            ========================================\n
            That's a dead end, you can't move that way\n
            ========================================
            """
        )
    else:
        pass


def item_action(input, item):
    if input == "t":
        player_take = player.take_item(item)
        if player_take:
            player.current_room.remove_item(item)
            return print(
                f"\n===========================\nYou put {item} into your bag \n===========================\n "
            )
        elif player_take == False:
            return print("\n==== Item not found ====")


def display_items():
    if len(player.current_room.items) > 0:
        item_store = []
        for item in player.current_room.items:
            item_store.append(item.name)
        return f" {', '.join(item_store)}"


def show_inventory():
    item_bag = []
    if len(player.inventory) > 0:
        for item in player.inventory:
            item_bag.append(item.name)
        return print(
            f"\n==============================\nInventory: {', '.join(item_bag)}\n==============================\n"
        )
    else:
        return print(
            f"\n===========================\n     Nothing in your bag     \n===========================\n"
        )


def instructions():
    return """\n ---------------------- \n Press [N] for NORTH \n Press [S] for SOUTH \n Press [W] for WEST \n Press [E] for EAST \n Press [I] Shows Inventory \n Press [Q] to quit \n """


while True:
    selection = input(
        (
            f"\n {instructions()} \n ---------------------- \n {player} \n items: {display_items()} \n What do you do? "
        )
    ).split(" ")
    if selection[0] == "q":
        print(
            "\n===========================\n     See you next time     \n===========================\n"
        )
        break
    try:
        if len(selection) == 1:
            if selection[0] == "i":
                show_inventory()

            elif selection[0] in movement_options:
                change_room(selection[0])
            else:
                print(
                    "\n===========================\n     Invalid input     \n===========================\n"
                )
        elif len(selection) == 2:
            if selection[0] in item_options:
                item_action(selection[0], selection[1])
    except AttributeError:
        print(
            "\n===========================\n     Invalid option, please try again     \n===========================\n"
        )
