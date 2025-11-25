import time
from utils import clear_screen, print_header, print_objectives, print_success, generic_cmd_handler, CURRENT_DIR

def run_level():
    title = "LEVEL 3: REMOTE EXPLOITATION"
    objectives = [
        "Connect to the target server.",
        "Syntax: connect [username]@[ip_address]"
    ]
    hint = "Recall the credentials found in notes.txt (admin_root / Winter2025!)"
    
    print_header(title)
    print_objectives(objectives, hint)

    while True:
        try:
            user_input = input(f"{CURRENT_DIR}> ").strip() # Don't lower() immediately to preserve password case
            parts = user_input.split()
            cmd = parts[0].lower() if parts else ""
            arg = parts[1] if len(parts) > 1 else ""

            # Standard commands
            common = generic_cmd_handler(cmd, arg)
            if common == "EXIT": return False
            if common: continue

            # --- LEVEL 3 SPECIFIC COMMANDS ---
            if cmd == "connect" or cmd == "ssh":
                # Check format: connect user@ip
                if "@" in arg:
                    target_user, target_ip = arg.split("@")
                    
                    if target_ip == "192.168.1.105" and target_user == "admin_root":
                        # Password Prompt
                        print(f"Connecting to {target_ip}...")
                        time.sleep(1)
                        password = input(f"root@{target_ip}'s password: ")
                        
                        if password == "Winter2025!":
                            print("\nAuthenticating...")
                            time.sleep(1.5)
                            print("Access Granted.")
                            
                            # WIN CONDITION
                            print_success("SYSTEM BREACHED! Root access obtained.")
                            return True
                        else:
                            print("Access Denied: Incorrect Password.")
                    else:
                        print("Connection timed out. Check Username or IP.")
                else:
                    print("Usage: connect username@ip_address")

            elif cmd == "help":
                 print("\n COMMANDS: CONNECT, HELP, CLS, EXIT")
            
            else:
                print(f"'{cmd}' is not recognized.")

        except KeyboardInterrupt:
            return False