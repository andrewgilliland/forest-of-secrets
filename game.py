from data import ROOMS
from ui import print_welcome, display_help

current_room = "forest"
inventory = []

print_welcome()

while True:
    print("\n" + ROOMS[current_room]["description"])
    
    # Show items in the room
    if ROOMS[current_room]["items"]:
        print("You see:", ", ".join(ROOMS[current_room]["items"]))
    
    command = input("> ").strip().lower()
    
    if command in ["quit", "exit"]:
        print("Thanks for playing Forest of Secrets!")
        break

    elif command.startswith("go "):
        direction = command.split(" ")[1]
        if direction in ROOMS[current_room]["exits"]:
            current_room = ROOMS[current_room]["exits"][direction]
        else:
            print("You can't go that way.")

    elif command.startswith("take "):
        item = command.split(" ", 1)[1]
        if item in ROOMS[current_room]["items"]:
            inventory.append(item)
            ROOMS[current_room]["items"].remove(item)
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