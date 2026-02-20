import os
import sys

# Allow running as a script: python .\cli_lab\main.py
if __name__ == "__main__" and __package__ is None:
    repo_root = os.path.dirname(os.path.dirname(__file__))
    if repo_root not in sys.path:
        sys.path.insert(0, repo_root)

from cli_lab.levels.linux import (
    level1_intro,
    level2_permissions as linux_level2,
)

from cli_lab.levels.windows import (
    level1_recon,
    level2_permissions as win_level2,
    level3_searching,
    level4_networking,
    level5_cryptography,
    level6_registry,
    level7_tasks_services,
    level8_event_logs,
    level9_disk_forensics,
    level10_powershell,
)


def main():
    while True:
        print("=== TerminalWarrior ===\n")
        print("1) Linux Challenges")
        print("2) Windows Challenges")
        print("0) Exit\n")

        terminal_choice = input("Select a Terminal: ").strip()

        if terminal_choice == "1":
            linux_menu()
        elif terminal_choice == "2":
            windows_menu()
        elif terminal_choice == "0":
            print("Goodbye")
            break
        else:
            print("Invalid choice!\n")


def linux_menu():
    while True:
        print("\n=== Linux Levels ===")
        print("1) Level 1 - Intro Challenge")
        print("2) Level 2 - Permissions")
        print("3) Level 3 - COMING SOON")
        print("4) Level 4 - COMING SOON")
        print("5) Level 5 - COMING SOON")
        print("0) Back\n")

        choice = input("Select a level: ").strip()

        if choice == "1":
            level1_intro.main()
        elif choice == "2":
            linux_level2.main()
        elif choice == "3":
            print("COMING SOON!")
        elif choice == "4":
            print("COMING SOON!")
        elif choice == "5":
            print("COMING SOON!")
        elif choice == "0":
            return
        else:
            print("Invalid choice!\n")


def windows_menu():
    while True:
        print("\n=== Windows Levels ===")
        print("1) Level 1 - Intro Challenge")
        print("2) Level 2 - Permissions & Ownership")
        print("3) Level 3 - Searching the System")
        print("4) Level 4 - Networking Challenge")
        print("5) Level 5 - Cryptography & Decoding")
        print("6) Level 6 - Registry Deep Dive")
        print("7) Level 7 - Task Scheduler & Services")
        print("8) Level 8 - Event Log Forensics")
        print("9) Level 9 - Disk Forensics & File Recovery")
        print("10) Level 10 - PowerShell Scripting Challenge")
        print("0) Back\n")

        choice = input("Select a level: ").strip()

        if choice == "1":
            level1_recon.run_level()
        elif choice == "2":
            win_level2.run_level()
        elif choice == "3":
            level3_searching.run_level()
        elif choice == "4":
            level4_networking.run_level()
        elif choice == "5":
            level5_cryptography.run_level()
        elif choice == "6":
            level6_registry.run_level()
        elif choice == "7":
            level7_tasks_services.run_level()
        elif choice == "8":
            level8_event_logs.run_level()
        elif choice == "9":
            level9_disk_forensics.run_level()
        elif choice == "10":
            level10_powershell.run_level()
        elif choice == "0":
            return
        else:
            print("Invalid choice!\n")


if __name__ == "__main__":
    main()
  
  

