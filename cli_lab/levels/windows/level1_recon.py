import time
# Import our shared tools
from .utils import (
    clear_screen,
    print_header,
    print_objectives,
    print_success,
    generic_cmd_handler,
    CURRENT_DIR
)

def run_level():
    # Setup Level
    title = "LEVEL 1: FILE SYSTEM RECON"
    objectives = [
        "List files in the current directory.",
        "Find and read the 'notes.txt' file."
    ]
    hint = "Use 'dir' to see files and 'type [filename]' to read content."
    
    print_header(title)
    print_objectives(objectives, hint)

    # Game Loop
    while True:
        try:
            user_input = input(f"{CURRENT_DIR}> ").strip().lower()
            parts = user_input.split()
            cmd = parts[0] if parts else ""
            arg = parts[1] if len(parts) > 1 else ""

            # Check common commands first
            common = generic_cmd_handler(cmd, arg)
            if common == "EXIT": return False
            if common: continue

            # Level Specific Commands
            if cmd == "dir" or cmd == "ls":
                print(f"\n Directory of {CURRENT_DIR}\n")
                print("11/10/2025  07:30 AM             1,024 secret.txt")
                print("11/10/2025  07:25 AM               512 notes.txt")
                print("               2 File(s)          1,536 bytes\n")
            
            elif cmd == "type" or cmd == "cat":
                if arg == "notes.txt":
                    print("\n[CONTENT OF NOTES.TXT]")
                    print("-" * 30)
                    print("User: admin_root")
                    print("Pass: Winter2025!")
                    print("Target IP: 192.168.1.105")
                    print("-" * 30)
                    
                    # WIN CONDITION
                    time.sleep(1)
                    print_success("Credentials Found! Level 1 Complete.")
                    return True 
                    
                elif arg == "secret.txt":
                    print("Access Denied. Encrypted file.")
                else:
                    print("File not found.")
            
            else:
                print(f"'{cmd}' is not recognized.")

        except KeyboardInterrupt:
            return False

def main():
    """
    Entry point for TerminalWarrior Windows Level 1
    """
    clear_screen()
    print_header("Windows Level 1 - File System Recon")
    time.sleep(1)

    # Start the challenge loop
    result = run_level()

    # After user exits the level
    return result

