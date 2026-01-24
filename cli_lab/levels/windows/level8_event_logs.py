import subprocess
from .utils import clear_screen, print_header, print_objectives, print_success


FLAG = "TW_EVENT_TRACE_8"


def setup_environment():
    """
    Inject a fake suspicious event into the Windows Event Log (simulated via message)
    """
    subprocess.run(
        [
            "wevtutil", "im",
            "Microsoft-Windows-Security-Auditing"
        ],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )


def run_level():
    clear_screen()
    print_header("LEVEL 8 — EVENT LOG FORENSICS")

    print_objectives([
        "Analyze Windows Event Logs",
        "Identify suspicious authentication activity",
        "Trace the security incident"
    ])

    setup_environment()

    print("\nA security incident occurred on this system.")
    print("The traces were left behind in the Windows Event Logs.\n")
    print("Useful commands:")
    print("  wevtutil qe Security /c:10 /rd:true")
    print("  wevtutil qe System /c:10 /rd:true\n")
    print("Focus on failed logons and unusual activity.\n")

    user_input = input("Enter the flag once you trace the incident: ").strip()

    if user_input == FLAG:
        print_success("Incident successfully traced through event logs.")
        return True
    else:
        print("\n✘ Incorrect.")
        print("The logs still hide the truth.")
        input()
        return False
