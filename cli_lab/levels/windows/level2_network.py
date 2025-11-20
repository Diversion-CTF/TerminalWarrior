import time
from .utils import (
    clear_screen,
    print_header,
    print_objectives,
    print_success,
    generic_cmd_handler,
    CURRENT_DIR,
)

def run_level():
    title = "LEVEL 2: NETWORK CONNECTIVITY"
    objectives = [
        "Verify your own IP configuration.",
        "Ping the target server found in notes.txt."
    ]
    hint = "Use 'ipconfig' and 'ping [TARGET_IP]'."
    
    print_header(title)
    print_objectives(objectives, hint)

    while True:
        try:
            user_input = input(f"{CURRENT_DIR}> ").strip().lower()
            parts = user_input.split()
            cmd = parts[0] if parts else ""
            arg = parts[1] if len(parts) > 1 else ""

            common = generic_cmd_handler(cmd, arg)
            if common == "EXIT": return False
            if common: continue

            if cmd == "ipconfig":
                print("\nEthernet adapter Ethernet0:")
                print("   IPv4 Address. . . . . . . . . . . : 75.163.246.128")
                print("   Subnet Mask . . . . . . . . . . . : 255.255.255.0")
                print("   Default Gateway . . . . . . . . . : 75.163.246.1\n")

            elif cmd == "ping":
                if arg == "192.168.1.105":
                    print(f"\nPinging {arg} with 32 bytes of data:")
                    for i in range(4):
                        time.sleep(0.3)
                        print(f"Reply from {arg}: bytes=32 time=1ms TTL=128")
                    
                    # WIN CONDITION
                    print_success("Target Alive! Connectivity Established.")
                    return True
                else:
                    print(f"Ping request could not find host {arg}. Please check the IP.")
            
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