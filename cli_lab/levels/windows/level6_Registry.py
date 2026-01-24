import subprocess
from levels.base_level import BaseLevel


class Level(BaseLevel):
    name = "Level 6 - Registry Deep Dive"
    description = (
        "Navigate the Windows Registry to uncover a hidden configuration key.\n"
        "A secret password is stored somewhere in the registry.\n\n"
        "Hints:\n"
        "- Use reg query\n"
        "- Think user-level, not system-level\n"
        "- HKCU is your friend\n"
    )

    expected_password = "terminal_warrior_6"

    def setup(self):
        # Create a hidden registry key with a value
        subprocess.run(
            [
                "reg", "add",
                r"HKCU\\Software\\TerminalWarrior\\Hidden",
                "/v", "Secret",
                "/t", "REG_SZ",
                "/d", self.expected_password,
                "/f"
            ],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )

    def run(self):
        print("A secret is hidden somewhere in the Windows Registry.")
        print("Find the password and enter it below.")
        print("You may need: reg query")

        user_input = input("\nEnter the password you found: ").strip()
        return user_input

    def check(self, user_input):
        if user_input == self.expected_password:
            print("\n✔ Correct!")
            print("You successfully navigated the registry.")
            return True
        else:
            print("\n✘ Incorrect.")
            print("The registry still holds its secrets.")
            return False

    def cleanup(self):
        subprocess.run(
            [
                "reg", "delete",
                r"HKCU\\Software\\TerminalWarrior",
                "/f"
            ],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
