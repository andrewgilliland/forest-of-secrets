
ANSI_COLORS = {
    "red": "\033[91m",
    "green": "\033[92m",
    "yellow": "\033[93m",
    "blue": "\033[94m",
    "magenta": "\033[95m",
    "cyan": "\033[96m",
    "reset": "\033[0m"
}

def color_print(text, color):
    print(f"{ANSI_COLORS[color]}{text}{ANSI_COLORS['reset']}")