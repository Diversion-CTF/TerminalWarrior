# Made by Diversion-CTF
import random

# ----------------------------------------------------------------------
# HELP MENU
# ----------------------------------------------------------------------
def print_help():
    print("Available commands:")
    print("  help                         - Show this help menu")
    print("  ls / ls -a                   - List files (include hidden with -a)")
    print("  cd <dir>                     - Change directory")
    print("  pwd                          - Print current directory")
    print("  whoami                       - Show current user")
    print("  cat <file>                   - Read file contents")
    print("  find <path> -name <pattern>  - Search for files by name")
    print("  grep <pattern> <file>        - Search inside files")
    print("  head <file>                  - View beginning of a file")
    print("  tail <file>                  - View end of a file")
    print("  less <file>                  - View large files interactively")
    print("  challenge                    - Show challenge progress")
    print("  exit                         - Exit level 3\n")

# ----------------------------------------------------------------------
# CHALLENGES
# ----------------------------------------------------------------------
def build_challenge_list(state):
    return [
        "",
        f"{'✅' if state[1] else '◻️'} 1) Find the hidden file in /home/user/logs.",
        "",
        f"{'✅' if state[2] else '◻️'} 2) Analyze auth.log to find an error.",
        "",
        f"{'✅' if state[3] else '◻️'} 3) Locate the suspicious backup file.",
        "",
        f"{'✅' if state[4] else '◻️'} 4) Extract leaked credentials from logs.",
        "",
        f"{'✅' if state[5] else '◻️'} 5) Read the final system flag.",
        "",
    ]

def print_challenges(state):
    for line in build_challenge_list(state):
        print(line)

# ----------------------------------------------------------------------
# MAIN
# ----------------------------------------------------------------------
def main():
    challenge_state = {i: False for i in range(1, 6)}

    print("Type command 'challenge' to see your progress.\n")
    input("Press Enter to start...")

    # MOTD randomness
    processes = random.randint(90, 220)
    memoryusage = random.randint(200, 900)
    day = random.randint(1, 28)
    hour = random.randint(0, 23)
    minute = random.randint(10, 59)
    second = random.randint(10, 59)

    print("\nWelcome to the Linux CLI Flag Challenge LEVEL 3 (SEARCHING) made by (Diversion-CTF)\n")
    input("Press Enter to continue...")
    print()

    print_challenges(challenge_state)
    print("\nWelcome to Ubuntu 20.04.6 LTS (GNU/Linux 5.15.0-91-generic x86_64)\n")
    print(f"System information as of [Thu Oct {day} {hour:02d}:{minute:02d}:{second:02d} UTC 2025]\n")
    print(f"System load: 0.01               Processes:          {processes}")
    print("Usage of /:   22.10% of 49.11GB  Users logged in:     1")
    print(f"Memory usage: {memoryusage}MB")
    print("Swap usage:   0%\n")

    # ------------------------------------------------------------------
    # PLAYER GUIDANCE (COMMAND USAGE)
    # ------------------------------------------------------------------
    print("TIP: This system contains large logs and hidden files.")
    print("Manually reading everything is inefficient.")
    print("Recommended tools for this level:")
    print("  - find   (locate files)")
    print("  - grep   (search inside files)")
    print("  - head   (view beginning of logs)")
    print("  - tail   (view recent log entries)")
    print("  - less   (navigate large files)\n")

    current_directory = "/home/user"

    hidden_found = False
    error_found = False
    backup_found = False
    credential_found = False
    flag_read = False

    # ------------------------------------------------------------------
    # FILESYSTEM
    # ------------------------------------------------------------------
    def print_ls(directory, all_files=False):
        if directory == "/home/user":
            print("logs  backups  notes.txt")
        elif directory == "/home/user/logs":
            if all_files:
                print(".  ..  auth.log  system.log  .hidden_log  .final.flag")
            else:
                print("auth.log  system.log")
        elif directory == "/home/user/backups":
            print("backup_old.tar.gz  system.bak")
        else:
            print("")

    # ------------------------------------------------------------------
    # COMMAND LOOP
    # ------------------------------------------------------------------
    while True:
        prompt = f"user@linux:{current_directory}$ "
        command = input(prompt).strip()

        if command == "":
            continue

        if command == "exit":
            print("logout")
            break

        if command == "challenge":
            print()
            print_challenges(challenge_state)
            print()
            continue

        if command == "help":
            print_help()
            continue

        if command == "pwd":
            print(current_directory)
            continue

        if command == "whoami":
            print("user")
            continue

        # --------------------------------------------------------------
        # CD
        # --------------------------------------------------------------
        if command.startswith("cd "):
            target = command[3:].strip()
            if target in ("~", "/home/user"):
                current_directory = "/home/user"
            elif target == "logs" and current_directory == "/home/user":
                current_directory = "/home/user/logs"
            elif target == "backups" and current_directory == "/home/user":
                current_directory = "/home/user/backups"
            elif target == "..":
                current_directory = "/home/user"
            else:
                print(f"cd: no such file or directory: {target}")
            continue

        # --------------------------------------------------------------
        # LS
        # --------------------------------------------------------------
        if command == "ls":
            print_ls(current_directory, all_files=False)
            continue

        if command == "ls -a":
            print_ls(current_directory, all_files=True)
            if current_directory == "/home/user/logs" and not hidden_found:
                hidden_found = True
                challenge_state[1] = True
                print("\nHidden file discovered!")
                print("You completed challenge 1!")
            continue

        # --------------------------------------------------------------
        # CAT / HEAD / TAIL / LESS
        # --------------------------------------------------------------
        if command.startswith(("cat ", "head ", "tail ", "less ")):
            file = command.split(" ", 1)[1]

            if current_directory == "/home/user":
                if file == "notes.txt":
                    print("Sysadmin note:")
                    print("Logs can be massive — avoid reading them line by line.")
                    print("Use grep to search for keywords.")
                    print("Use find to locate misplaced or hidden files.")
                    print("head, tail, and less make log analysis easier.")
                else:
                    print(f"{file}: No such file")

            elif current_directory == "/home/user/logs":
                if file == "auth.log":
                    print("auth.log is a large file.")
                    print("Hint: use head, tail, or less to inspect it efficiently.")
                    print("...")
                    print("ERROR: invalid password for user admin")
                    if not error_found:
                        error_found = True
                        challenge_state[2] = True
                        print("\nYou completed challenge 2!")
                elif file == ".hidden_log":
                    print("Hidden log entry:")
                    print("WARNING: Suspicious activity detected in auth.log")
                elif file in (".final.flag", "final.flag"):
                    if credential_found:
                        print("FINAL FLAG: SEARCH-LEVEL3-COMPLETE")
                        if not flag_read:
                            flag_read = True
                            challenge_state[5] = True
                            print("You completed challenge 5!")
                    else:
                        print("cat: final.flag: Permission denied")
                elif file == "system.log":
                    print("System boot completed successfully.")
                else:
                    print(f"{file}: No such file")

            elif current_directory == "/home/user/backups":
                if file == "system.bak":
                    print("Old system backup detected.")
                    if not backup_found:
                        backup_found = True
                        challenge_state[3] = True
                        print("You completed challenge 3!")
                else:
                    print(f"{file}: No such file")
            continue

        # --------------------------------------------------------------
        # FIND
        # --------------------------------------------------------------
        if command.startswith("find "):
            if "hidden" in command:
                print("/home/user/logs/.hidden_log")
            elif "bak" in command:
                print("/home/user/backups/system.bak")
            elif "flag" in command:
                print("/home/user/logs/.final.flag")
            else:
                print("find: no results")
            continue

        # --------------------------------------------------------------
        # GREP
        # --------------------------------------------------------------
        if command.startswith("grep "):
            if "password" in command and "auth.log" in command:
                print("admin:SuperSecretPassword123")
                if not credential_found:
                    credential_found = True
                    challenge_state[4] = True
                    print("\nCredential leak found.")
                    print("You completed challenge 4!")
            else:
                print("grep: no matches found")
            continue

        print(f"{command}: command not found")

if __name__ == "__main__":
    main()
