import os
import sys
import time
from datetime import datetime

# --- All complex colors and borders have been removed ---

# Global State for the Windows Challenge
current_dir = "C:\\Users\\User" 

# --------------------------------------------------------------------------
# --- STYLIZED UTILITY FUNCTIONS (Simplified) ---
# --------------------------------------------------------------------------

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header(title="HACKER TERMINAL SIMULATOR"):
    clear_screen()
    
    banner_width = 77
    print("*" * banner_width)
    print(f"** {title} **".center(banner_width))
    print("*" * banner_width)
    
    print("|")
    print(f"| PLATFORM: Windows CTF by Therootexec")
    print(f"| GOAL: Navigate the system and solve the challenge objectives.")
    print(f"| STATUS: System Status Nominal. Ready for Challenge.")
    print("|")
    print("+" + "-" * banner_width + "+")
    print()

def print_system_info():
    now = datetime.now()
    
    print(":: SYSTEM BASELINE ::")
    print("-" * 25)

    def print_info_line(key, value):
        print(f" {key.ljust(18)}: {value}")

    print_info_line("OS Version", "Microsoft Windows 10.0.19045")
    print_info_line("Host User", "user\\desktop-pc234")
    print_info_line("Runtime", f"[{now.strftime('%H:%M:%S')}] {now.strftime('%m/%d/%Y')}")
    print_info_line("IP Address", "75.163.246.128 (eth0)")
    
    print("-" * 25)
    print()


def print_challenge_progress(level_num):
    box_width = 65
    
    print("+" + "-" * box_width + "+")
    print(f"| MISSION OBJECTIVES: LEVEL {level_num} |".center(box_width))
    print("+" + "-" * box_width + "+")
    
    print(f"| {'Welcome, Agent. Your target objectives are:'.ljust(box_width - 2)} |")
    
    print(f"| {'1. Read the secret.txt file.'.ljust(box_width - 2)} |")
    print(f"| {'2. Find the administrator username.'.ljust(box_width - 2)} |")
    print(f"| {'3. Find the administrator password.'.ljust(box_width - 2)} |")
    print(f"| {'4. Find the remote computer IP address.'.ljust(box_width - 2)} |")
    print(f"| {'5. Successfully connect to remote computer.'.ljust(box_width - 2)} |")
    print(f"| {'6. Find FLAG.txt on remote computer.'.ljust(box_width - 2)} |")
    print(f"| {' ' * (box_width - 2)} |") 
    
    print("+" + "-" * box_width + "+")

    print(f"| {'Type \'help\' for command list or \'status\' for progress.'.ljust(box_width - 2)} |")
    print("\\" + "-" * box_width + "/")
    print()

def print_help():
    print(":: COMMAND SYNTAX HELP ::")
    print("-" * 30)
    
    print(" CORE:      HELP/?    STATUS        CLEAR/CLS   EXIT/QUIT")
    print(" FILE SYS:  DIR/LS    TYPE/CAT [FILE] PWD")
    print(" NETWORK:   WHOAMI    IPCONFIG      PING [IP]")
    
    print("-" * 30)
    print()

# --------------------------------------------------------------------------
# --- COMMAND SIMULATION AND FLOW FUNCTIONS ---
# --------------------------------------------------------------------------

def simulate_command(command, level_num):
    global current_dir 
    
    command_lower = command.lower().strip()
    parts = command_lower.split()
    cmd = parts[0] if parts else ""
    arg = parts[1] if len(parts) > 1 else ""
    
    print() 

    if cmd == "help" or cmd == "?":
        print_help()
    
    elif cmd == "clear" or cmd == "cls":
        windows_challenge_start_sequence(level_num, re_run=True)
        return False

    elif cmd == "status" or cmd == "progress":
        print_challenge_progress(level_num)
    
    elif cmd == "dir" or cmd == "ls":
        print(" Volume in drive C has no label.")
        print(" Volume Serial Number is A1B2-C3D4")
        print()
        print(f" Directory of {current_dir}")
        print()
        print("11/10/2025  07:42 AM    <DIR>          .")
        print("11/10/2025  07:42 AM    <DIR>          ..")
        print("11/10/2025  07:30 AM             1,024 secret.txt")
        print("11/10/2025  07:25 AM               512 notes.txt")
        print("11/10/2025  07:20 AM    <DIR>          Documents")
        print("11/10/2025  07:20 AM    <DIR>          Downloads")
        print("11/10/2025  07:20 AM    <DIR>          Desktop")
        print("               2 File(s)          1,536 bytes")
        print("               5 Dir(s)  12,345,678,901 bytes free")
    
    elif cmd == "pwd":
        print(current_dir)
        
    elif cmd == "type" or cmd == "cat":
        if arg == "secret.txt":
            print("Access Denied: You do not have permission to view this file.")
        elif arg == "notes.txt":
            print("System Administrator Notes:")
            print("Username: admin_root")
            print("Temporary password: Winter2025!")
            print("Remote server IP: 192.168.1.105")
        else:
             print(f"The system cannot find the file specified: {arg}")

    elif cmd == "whoami":
        print("user\\desktop-pc234")
    
    elif cmd == "ipconfig":
        print("Windows IP Configuration")
        print()
        print("Ethernet adapter Ethernet0:")
        print("   IPv4 Address. . . . . . . . . . . : 75.163.246.128")
        print("   Subnet Mask . . . . . . . . . . . : 255.255.255.0")
        print("   Default Gateway . . . . . . . . . : 75.163.246.1")
    
    elif cmd == "ping":
        if arg == "192.168.1.105":
            print(f"Pinging 192.168.1.105 with 32 bytes of data:")
            print("Reply from 192.168.1.105: bytes=32 time=1ms TTL=128")
            print("    Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),")
        else:
            print(f"Ping request could not find host {arg}. Please check the name and try again.")
    
    elif cmd == "exit" or cmd == "quit":
        print("Thank you for using Therootexec Challenge System!")
        return True
    
    elif command_lower:
        print(f"'{command}' is not recognized as an internal or external command,")
        print("operable program or batch file.")
    
    return False

# --- Start Sequence Helper ---

def windows_challenge_start_sequence(level_num, re_run=False):
    print_header(f"HACKER TERMINAL SIMULATOR // WINDOWS CTF - LEVEL {level_num}")
    
    if not re_run:
        input("Agent authorized. Press ENTER to connect to the challenge system...")
        print()
    
    print_system_info()
    print_challenge_progress(level_num)


def windows_challenge(level_num):
    global current_dir
    current_dir = "C:\\Users\\User" 

    windows_challenge_start_sequence(level_num)
    
    while True:
        try:
            prompt = f"{current_dir}> "
            command = input(prompt)
            if simulate_command(command, level_num):
                break
            
        except KeyboardInterrupt:
            print("\n\nUse 'exit' or 'quit' to leave the challenge.")
            print()
            
    level_selection("windows") 


def level_selection(challenge_type):
    print_header(f"{challenge_type.upper()} LEVEL SELECTION | THERESEC")
    
    levels = {
        1: "File System Recon (Initial Access)",
        2: "Network Enumeration (Pivot Point)",
        3: "Privilege Escalation (Rooted!)",
        4: "Back to Main Menu"
    }
    
    print(":: AVAILABLE MISSIONS ::")
    print("-" * 30)
    for num, desc in levels.items():
        if challenge_type == "linux" and num < 4:
            print(f" [{num}] {desc} (LOCKED)")
        elif num < 4:
            print(f" [{num}] Level {num}: {desc}")
        else:
            print(f" [{num}] {desc}")
    print("-" * 30)
    print()

    while True:
        choice = input(f"Select MISSION {challenge_type} level (1-{len(levels)}): ")
        
        if choice.isdigit():
            level_num = int(choice)
            if level_num in levels:
                if level_num == 4:
                    main_menu()
                    return
                elif challenge_type == "windows":
                    print(f"Deploying Windows Level {level_num}: {levels[level_num]}...")
                    time.sleep(1)
                    windows_challenge(level_num)
                    return
                else: # Linux
                    print(f"Linux Level {level_num} - Target currently offline.")
                    input("Press Enter to return to level selection...")
                    level_selection("linux")
                    return
            else:
                print("Invalid selection. Please choose from the list.")
        else:
            print("Invalid input. Please enter a number.")
        print()

def main_menu():
    print_header("THEROOTEXEC CHALLENGE SYSTEM | MAIN CONSOLE")
    
    print(":: CHALLENGE TRACK SELECTION ::")
    print("-" * 35)
    print(" [1] Linux Challenges (Targets: Offline)")
    print(" [2] Windows Challenges (Targets: Active)")
    print(" [3] Exit System")
    print("-" * 35)
    print()
    
    while True:
        choice = input("Select TRACK number (1-3): ")
        
        if choice == "1":
            level_selection("linux")
            return
        elif choice == "2":
            level_selection("windows")
            return
        elif choice == "3":
            print("System Disconnected.")
            sys.exit(0)
        else:
            print("Invalid TRACK selection.")
            print()

if __name__ == "__main__":
    try:
        main_menu()
    except Exception as e:
        print(f"\nAn unexpected system error occurred: {e}")