import time
from utils import clear_screen, print_header, print_objectives, print_success, generic_cmd_handler, CURRENT_DIR

def run_level():
    title = "LEVEL 3: EXPLOITATION"
    objectives = [
        "Connect to the remote computer.",
        "Syntax: connect [user]@[ip]"
    ]
    hint = "Use the creds from Level 1: admin_root / Winter2025!"
    
    print_header(title)
    print_objectives(objectives, hint)

    while True:
        try:
            prompt = f"{CURRENT_DIR}> "
            user_input = input(prompt).strip()
            parts = user_input.split()
            cmd = parts[0].lower() if parts else ""
            arg = parts[1] if len(parts) > 1 else ""

            common = generic_cmd_handler(cmd, arg)
            if common == "EXIT": return False
            if common: continue

            if cmd == "connect" or cmd == "ssh":
                if "@" in arg:
                    user, ip = arg.split("@")
                    if ip == "192.168.1.105" and user == "admin_root":
                        password = input(f"Enter password for {user}: ")
                        if password == "Winter2025!":
                            print("Verifying credentials...")
                            time.sleep(1)
                            print("Access Granted.")
                            print_success("SYSTEM BREACHED. FLAG: {W1ND0WS_H4CK3D}")
                            return True
                        else:
                            print("Access Denied: Bad Password.")
                    else:
                        print("Connection timed out. Check IP or User.")
                else:
                    print("Usage: connect user@ip")
            else:
                print(f"'{cmd}' is not recognized.")

        except KeyboardInterrupt:
            return False
