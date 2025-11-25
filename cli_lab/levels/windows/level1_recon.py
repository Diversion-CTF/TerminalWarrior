import time
from utils import clear_screen, print_header, print_objectives, print_success, generic_cmd_handler, CURRENT_DIR

def run_level():
    title = "LEVEL 1: FILE SYSTEM RECON"
    objectives = [
        "List files in the current directory.",
        "Read 'notes.txt' to find credentials."
    ]
    hint = "Use 'dir' to look around and 'type [filename]' to read."
    
    print_header(title)
    print_objectives(objectives, hint)

    while True:
        try:
            prompt = f"{CURRENT_DIR}> "
            user_input = input(prompt).strip().lower()
            parts = user_input.split()
            cmd = parts[0] if parts else ""
            arg = parts[1] if len(parts) > 1 else ""

            common = generic_cmd_handler(cmd, arg)
            if common == "EXIT": return False
            if common: continue

            if cmd == "dir" or cmd == "ls":
                print(f" Directory of {CURRENT_DIR}")
                print()
                print("11/10/2025  07:42 AM    <DIR>          .")
                print("11/10/2025  07:42 AM    <DIR>          ..")
                print("11/10/2025  07:30 AM             1,024 secret.txt")
                print("11/10/2025  07:25 AM               512 notes.txt")
                print("               2 File(s)          1,536 bytes")
                print("               2 Dir(s)   12,345,678,901 bytes free")
            
            elif cmd == "type" or cmd == "cat":
                if arg == "secret.txt":
                    print("Access Denied: You do not have permission to view this file.")
                elif arg == "notes.txt":
                    print("\nSystem Administrator Notes:")
                    print("-" * 25)
                    print("Username: admin_root")
                    print("Temporary password: Winter2025!")
                    print("Remote server IP: 192.168.1.105")
                    print("-" * 25)
                    time.sleep(1)
                    print_success("Credentials & IP Found! Level 1 Complete.")
                    return True
                else:
                    print(f"The system cannot find the file specified: {arg}")
            else:
                print(f"'{cmd}' is not recognized.")

        except KeyboardInterrupt:
            return False
