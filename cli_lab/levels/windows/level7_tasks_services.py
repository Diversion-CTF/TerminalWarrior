import subprocess
from .utils import clear_screen, print_header, print_objectives, print_success


FLAG = "TW_TASK_PERSISTENCE_7"


def setup_environment():
    """
    Simulate malicious persistence via scheduled task + service
    """
    # Fake scheduled task
    subprocess.run(
        [
            "schtasks",
            "/create",
            "/tn", "WindowsUpdateCache",
            "/tr", "C:\\ProgramData\\svchost_cache.exe",
            "/sc", "ONLOGON",
            "/f"
        ],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

    # Fake service
    subprocess.run(
        [
            "sc", "create",
            "WinDefendCache",
            "binPath=", "C:\\ProgramData\\defender_cache.exe",
            "start=", "auto"
        ],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )


def cleanup_environment():
    subprocess.run(
        ["schtasks", "/delete", "/tn", "WindowsUpdateCache", "/f"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )
    subprocess.run(
        ["sc", "delete", "WinDefendCache"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )


def run_level():
    clear_screen()
    print_header("LEVEL 7 — TASK SCHEDULER & SERVICES")

    print_objectives([
        "Investigate scheduled tasks for suspicious entries",
        "Inspect system services for malicious persistence",
        "Find the hidden flag"
    ])

    setup_environment()

    print("\nSomething is maintaining persistence on this system.")
    print("It survives reboots.")
    print("Use:")
    print("  schtasks /query")
    print("  sc query\n")

    user_input = input("Enter the flag once you find it: ").strip()

    cleanup_environment()

    if user_input == FLAG:
        print_success("Persistence identified and neutralized.")
        return True
    else:
        print("\n✘ Incorrect.")
        print("Persistence still active.")
        input()
        return False

