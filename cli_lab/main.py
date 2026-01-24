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
        print("1) Level 1 - Recon")
        print("2) Level 2 - Permissions")
        print("3) Level 3 - Searching")
        print("4) Level 4 - Networking")
        print("5) Level 5 - Cryptography_Decoding")
        print("6) Level 6 - Registry")
        print("7) Level 7 - Tasks_services")
        print("8) Level 8 - Event_logs")
        print("0) Back\n")

        choice = input("Select a level: ").strip()

        if choice == "1":
            level1_recon.main()
        elif choice == "2":
            win_level2.main()
        elif choice == "3":
            level3_searching.main()
        elif choice == "4":
            level4_networking.main()
        elif choice == "5":
            level5_cryptography.main()
        elif choice == "6":
            level6_registry.main()
        elif choice == "7":
            level7_tasks_services.main()
        elif choice8 == "8"
            level8_event_logs.main()
        elif choice == "0":
            return
        else:
            print("Invalid choice!\n")


if __name__ == "__main__":
    main()
  

