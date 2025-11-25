# FILE: level4_privesc.py
import time
from utils import clear_screen, print_header, print_objectives, print_success, generic_cmd_handler

# New Level 4 Prompt (Simulating a shell on the remote box)
REMOTE_PROMPT = "C:\\admin_root\\Desktop> "

def run_level():
    title = "LEVEL 4: PRIVILEGE ESCALATION"
    objectives = [
        "You are connected to the target server.",
        "Execute the hidden 'get-flag' script to complete the mission."
    ]
    hint = "Type the command 'get-flag' and hit Enter."
    
    print_header(title)
    print_objectives(objectives, hint)

    while True:
        try:
            user_input = input(REMOTE_PROMPT).strip().lower()
            parts = user_input.split()
            cmd = parts[0] if parts else ""
            arg = parts[1] if len(parts) > 1 else ""

            # Check shared commands (help, exit, etc.)
            # Note: We use generic_cmd_handler, but some commands (like PING) won't make sense here.
            common = generic_cmd_handler(cmd, arg)
            if common == "EXIT": return False
            if common: continue

            # Level 4 Specific Logic
            if cmd == "get-flag":
                print("\nRunning exploit script...")
                time.sleep(2)
                print("Exploit successful. Accessing protected data...")
                time.sleep(1)
                
                # WIN CONDITION
                print_success("PRIVILEGES ELEVATED. FINAL FLAG: {P45SW0RD_G0LD3N}")
                return True
            
            elif cmd == "dir":
                print("\n 11/25/2025  08:00 AM             2,048 logs.txt")
                print(" 11/25/2025  08:15 AM                 1 get-flag.exe (hidden)")
                print("                2 File(s)          2,049 bytes\n")

            else:
                print(f"'{cmd}' is not recognized on the remote shell.")

        except KeyboardInterrupt:
            return False