
rooms = {
    "forest": {
        "description": "You stand among towering pines. A path leads north and east.",
        "exits": {"north": "cave", "east": "village"},
        "items": ["map"]
    },
    "cave": {
        "description": "The cave is cold and damp. Shadows dance on the walls.",
        "exits": {"south": "forest"},
        "items": ["sword"]
    },
    "village": {
        "description": "The village is eerily quiet. You hear a stream to the west.",
        "exits": {"west": "forest"},
        "items": []
    }
}

current_room = "forest"
inventory = []

def print_welcome():
    print("====================================")
    print("   Welcome to the Forest of Secrets")
    print("====================================")
    print("Type 'go [direction]' to move, 'quit' to exit.")
    print("Available directions: north, south, east, west.")
    print("Type 'take [item]' to pick up items, 'inventory' to check your items.")
    print("Your adventure begins now!")

def display_help():
    print("Available commands:")
    print("  go [direction] - Move in a direction (north, south, east, west)")
    print("  take [item] - Pick up an item")
    print("  inventory - Check your items")
    print("  quit - Exit the game")

print_welcome()

while True:
    print("\n" + rooms[current_room]["description"])
    
    # Show items in the room
    if rooms[current_room]["items"]:
        print("You see:", ", ".join(rooms[current_room]["items"]))
    
    command = input("> ").strip().lower()
    
    if command in ["quit", "exit"]:
        print("Thanks for playing Forest of Secrets!")
        break

    elif command.startswith("go "):
        direction = command.split(" ")[1]
        if direction in rooms[current_room]["exits"]:
            current_room = rooms[current_room]["exits"][direction]
        else:
            print("You can't go that way.")

    elif command.startswith("take "):
        item = command.split(" ", 1)[1]
        if item in rooms[current_room]["items"]:
            inventory.append(item)
            rooms[current_room]["items"].remove(item)
            print(f"You picked up the {item}.")
        else:
            print("That item isn't here.")

    elif command == "inventory":
        if inventory:
            print("You have:", ", ".join(inventory))
        else:
            print("Your inventory is empty.")

    elif command == "help":
        display_help()

    else:
        print("I don't understand that command.")