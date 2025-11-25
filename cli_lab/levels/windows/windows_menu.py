import sys
import time
from utils import clear_screen, print_header

# Import our modular levels
import level1_recon
import level2_network
import level3_connect
import level4_privesc

def main_menu():
    print_header("THEROOTEXEC CHALLENGE SYSTEM | MAIN CONSOLE")
    print(":: CHALLENGE TRACKS ::")
    print("-" * 35)
    print(" [1] Start Windows Campaign (Levels 1-3)")
    print(" [2] Exit System")
    print("-" * 35)
    
    while True:
        choice = input("Selection: ")
        
        if choice == "1":
            if level1_recon.run_level():
                if level2_network.run_level():
                    if level3_connect.run_level():
                        if level4_privesc.run_level():
                        clear_screen()
                        print("\n\n")
                        print("*" * 50)
                        print("CONGRATULATIONS AGENT. CAMPAIGN COMPLETE.")
                        print("*" * 50)
                        input()
            return 
        elif choice == "2":
            print("System Disconnected.")
            sys.exit(0)

if __name__ == "__main__":
    main_menu()

