from utils import color_print

def print_welcome():
    color_print("====================================", "cyan")
    color_print("   Welcome to the Forest of Secrets", "cyan")
    color_print("====================================", "cyan")
    color_print("Type 'go [direction]' to move, 'quit' to exit.", "cyan")
    color_print("Available directions: north, south, east, west.", "cyan")
    color_print("Type 'take [item]' to pick up items, 'inventory' to check your items.", "cyan")
    color_print("Your adventure begins now!", "cyan")

def display_help():
    color_print("Available commands:", "cyan")
    color_print("  go [direction] - Move in a direction (north, south, east, west)", "cyan")
    color_print("  take [item] - Pick up an item", "cyan")
    color_print("  inventory - Check your items", "cyan")
    color_print("  quit - Exit the game", "cyan")
