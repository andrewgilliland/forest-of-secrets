from data import ROOMS
from ui import display_help
from utils import color_print

def game_loop():
    current_room = "forest"
    inventory = []

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
                next_room = ROOMS[current_room]["exits"][direction]
                
                # Win/lose conditions when entering the village
                if next_room == "village":
                    if "sword" in inventory and "map" in inventory:
                        color_print("\n🏆 You enter the village, sword at your side and map in hand. You have survived the Forest of Secrets!", "green")
                        break
                    else:
                        color_print("\n💀 You enter the village unprepared. Bandits ambush you, and your adventure ends here.", "red")
                        break

                current_room = next_room
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