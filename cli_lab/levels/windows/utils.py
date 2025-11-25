import os

# Shared Game State
CURRENT_DIR = "C:\\Users\\User"

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header(title):
    clear_screen()
    banner_width = 70
    print("*" * banner_width)
    print(f"** {title} **".center(banner_width))
    print("*" * banner_width)
    print("| PLATFORM: Windows CTF by Therootexec")
    print("| STATUS:   System Status Nominal.")
    print("+" + "-" * banner_width + "+")
    print()

def print_objectives(objectives, hint):
    print(":: CURRENT MISSION OBJECTIVES ::")
    for obj in objectives:
        print(f" [!] {obj}")
    print(f"\n >> HINT: {hint}")
    print("-" * 50)
    print()

def print_success(message):
    print("\n" + "="*60)
    print(f" SUCCESS: {message}")
    print("="*60)
    input(" Press ENTER to proceed...")

def generic_cmd_handler(cmd, args):
    if cmd in ["cls", "clear"]:
        clear_screen()
        return True
    elif cmd == "help" or cmd == "?":
        print("\n CORE:      HELP      CLS       EXIT")
        print(" NETWORK:   IPCONFIG  PING      CONNECT")
        print(" FILE:      DIR       TYPE      PWD")
        return True
    elif cmd == "whoami":
        print("user\\desktop-pc234")
        return True
    elif cmd == "pwd":
        print(CURRENT_DIR)
        return True
    elif cmd == "exit" or cmd == "quit":
        return "EXIT"
    return False
