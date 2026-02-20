import sys
from .utils import clear_screen, print_header

from . import (
    level1_recon,
    level2_permissions,
    level3_searching,
    level4_networking,
    level5_cryptography,
    level6_registry,
    level7_tasks_services,
    level8_event_logs,
    level9_disk_forensics,
    level10_powershell,
)


LEVELS = [
    ("Level 1 - Intro Challenge", level1_recon.run_level),
    ("Level 2 - Permissions & Ownership", level2_permissions.run_level),
    ("Level 3 - Searching the System", level3_searching.run_level),
    ("Level 4 - Networking Challenge", level4_networking.run_level),
    ("Level 5 - Cryptography & Decoding", level5_cryptography.run_level),
    ("Level 6 - Registry Deep Dive", level6_registry.run_level),
    ("Level 7 - Task Scheduler & Services", level7_tasks_services.run_level),
    ("Level 8 - Event Log Forensics", level8_event_logs.run_level),
    ("Level 9 - Disk Forensics & File Recovery", level9_disk_forensics.run_level),
    ("Level 10 - PowerShell Scripting", level10_powershell.run_level),
]


def run_campaign():
    for _, runner in LEVELS:
        if not runner():
            return
    clear_screen()
    print("\n" + "*" * 60)
    print("MISSION COMPLETE! WINDOWS CAMPAIGN ACHIEVED")
    print("*" * 60)
    input()


def main_menu():
    while True:
        print_header("WINDOWS TERMINAL WARRIOR | MAIN CONSOLE")
        print(":: CHALLENGE TRACKS ::")
        print("-" * 45)
        print(" [1] Start Windows Campaign (Levels 1-10)")
        print(" [2] Select Individual Level")
        print(" [3] Exit System")
        print("-" * 45)

        choice = input("Selection: ").strip()

        if choice == "1":
            run_campaign()
        elif choice == "2":
            select_level_menu()
        elif choice == "3":
            print("System Disconnected.")
            sys.exit(0)


def select_level_menu():
    while True:
        print("\n=== Windows Levels ===")
        for idx, (name, _) in enumerate(LEVELS, start=1):
            print(f"{idx}) {name}")
        print("0) Back\n")

        choice = input("Select a level: ").strip()
        if choice == "0":
            return
        if choice.isdigit():
            idx = int(choice) - 1
            if 0 <= idx < len(LEVELS):
                LEVELS[idx][1]()
                continue
        print("Invalid choice!\n")


if __name__ == "__main__":
    main_menu()
