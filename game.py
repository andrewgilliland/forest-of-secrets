
rooms = {
    "forest": {
        "description": "You stand among towering pines. A path leads north and east.",
        "exits": {"north": "cave", "east": "village"}
    },
    "cave": {
        "description": "The cave is cold and damp. Shadows dance on the walls.",
        "exits": {"south": "forest"}
    },
    "village": {
        "description": "The village is eerily quiet. You hear a stream to the west.",
        "exits": {"west": "forest"}
    }
}

current_room = "forest"
inventory = []

print("Welcome to the Forest of Secrets!")
print("Type 'go [direction]' to move, 'quit' to exit.")
print("Available directions: north, south, east, west.")
print("Your adventure begins now!")

while True:
    print("\n" + rooms[current_room]["description"])
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

    else:
        print("I don't understand that command.")