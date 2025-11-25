import time
from utils import clear_screen, print_header, print_objectives, print_success, generic_cmd_handler, CURRENT_DIR

def run_level():
    title = "LEVEL 2: NETWORK ENUMERATION"
    objectives = [
        "Check your IP address configuration.",
        "Ping the remote server (found in notes)."
    ]
    hint = "Use 'ipconfig' and 'ping [IP_ADDRESS]'."
    
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

            if cmd == "ipconfig":
                print("\nWindows IP Configuration")
                print("Ethernet adapter Ethernet0:")
                print("   IPv4 Address. . . . . . . . . . . : 75.163.246.128")
                print("   Subnet Mask . . . . . . . . . . . : 255.255.255.0")
                print("   Default Gateway . . . . . . . . . : 75.163.246.1")

            elif cmd == "ping":
                if arg == "192.168.1.105":
                    print(f"\nPinging 192.168.1.105 with 32 bytes of data:")
                    for i in range(4):
                        time.sleep(0.3)
                        print("Reply from 192.168.1.105: bytes=32 time=1ms TTL=128")
                    print("Ping statistics: Sent = 4, Received = 4, Lost = 0 (0% loss)")
                    print_success("Target Reachable! Level 2 Complete.")
                    return True
                else:
                    print(f"Ping request could not find host {arg}. Please check the name.")
            else:
                print(f"'{cmd}' is not recognized.")

        except KeyboardInterrupt:
            return False
