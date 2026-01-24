"""
Level 6: Registry Deep Dive
Objective: Navigate the Windows Registry to find hidden configuration keys
"""

from cli_lab.filesystem import FileSystem
from cli_lab.terminal import Terminal

LEVEL_DESCRIPTION = """
╔══════════════════════════════════════════════════════════════════╗
║           LEVEL 6: REGISTRY DEEP DIVE                            ║
╚══════════════════════════════════════════════════════════════════╝

🎯 MISSION BRIEFING:
   A suspicious application has been hiding secrets in the Windows Registry.
   Your task is to navigate through registry hives and uncover hidden data.

📚 SKILLS YOU'LL LEARN:
   • reg query    - Query registry keys and values
   • reg add      - Add new registry entries
   • reg delete   - Remove registry entries
   • Understanding HKEY structures (HKLM, HKCU, HKCR, HKU)
   • Registry forensics and analysis

💡 TIPS:
   • Use 'reg query <key>' to explore registry keys
   • Use 'reg query <key> /v <value>' to view specific values
   • Use 'reg query <key> /s' to search recursively
   • Registry paths use backslashes (\) not forward slashes
   • HKLM = HKEY_LOCAL_MACHINE (system-wide settings)
   • HKCU = HKEY_CURRENT_USER (user-specific settings)

🚩 CHALLENGES:
   1. Find the hidden password in the Software registry hive
   2. Discover the secret API key stored by a malicious app
   3. Locate startup programs by examining Run keys
   4. Export a specific registry key to a file
   5. Unlock the final flag by modifying a registry value

Good luck, Registry Explorer! 🔍
"""


def setup_level6(fs: FileSystem) -> dict:
    """
    Set up Level 6: Registry Deep Dive
    Creates simulated registry structure and challenges
    """
    
    # Create registry structure
    registry_structure = {
        "HKEY_LOCAL_MACHINE": {
            "SOFTWARE": {
                "Microsoft": {
                    "Windows": {
                        "CurrentVersion": {
                            "Run": {
                                "_values": {
                                    "SecurityUpdate": "C:\\Windows\\System32\\svchost.exe",
                                    "MaliciousApp": "C:\\ProgramData\\hidden\\backdoor.exe",
                                    "WindowsDefender": "C:\\Program Files\\Windows Defender\\MSASCui.exe"
                                }
                            }
                        }
                    }
                },
                "SecretVault": {
                    "Authentication": {
                        "_values": {
                            "AdminPassword": "R3g1stry_M@st3r_2024",
                            "BackupKey": "encrypted_bk_7x9mz"
                        }
                    },
                    "APIKeys": {
                        "_values": {
                            "ServiceToken": "sk_live_abc123xyz789def456",
                            "DatabaseConnection": "Server=db.corp.local;UID=admin"
                        }
                    }
                },
                "SuspiciousApp": {
                    "Config": {
                        "_values": {
                            "HiddenFlag": "REG{H1DD3N_1N_PL41N_S1GHT}",
                            "UnlockCode": "0",
                            "SecretMessage": "base64:VGhlIGZsYWcgaXMgd2FpdGluZyBmb3IgeW91IQ=="
                        }
                    }
                }
            },
            "SYSTEM": {
                "CurrentControlSet": {
                    "Services": {
                        "MalwareService": {
                            "_values": {
                                "DisplayName": "Windows Update Service",
                                "ImagePath": "C:\\Windows\\Temp\\malware.exe",
                                "Start": "2"
                            }
                        }
                    }
                }
            }
        },
        "HKEY_CURRENT_USER": {
            "Software": {
                "Microsoft": {
                    "Windows": {
                        "CurrentVersion": {
                            "Run": {
                                "_values": {
                                    "OneDrive": "C:\\Users\\Agent\\AppData\\Local\\Microsoft\\OneDrive\\OneDrive.exe"
                                }
                            }
                        }
                    }
                },
                "GameSettings": {
                    "_values": {
                        "Level6Unlocked": "false",
                        "HintAvailable": "Check HKLM\\SOFTWARE\\SecretVault"
                    }
                }
            },
            "Environment": {
                "_values": {
                    "PATH": "C:\\Windows\\System32;C:\\Windows",
                    "TEMP": "C:\\Users\\Agent\\AppData\\Local\\Temp",
                    "SecretPath": "C:\\ProgramData\\Secrets"
                }
            }
        }
    }
    
    # Store registry in filesystem metadata
    fs.registry = registry_structure
    
    # Create some related files
    fs.create_file("/C:/Users/Agent/Desktop/registry_guide.txt", """
WINDOWS REGISTRY QUICK REFERENCE
=================================

COMMON REGISTRY HIVES:
- HKEY_LOCAL_MACHINE (HKLM)  - System-wide settings
- HKEY_CURRENT_USER (HKCU)   - Current user settings
- HKEY_CLASSES_ROOT (HKCR)   - File associations
- HKEY_USERS (HKU)           - All user profiles

USEFUL COMMANDS:
reg query HKLM\\SOFTWARE               - List subkeys
reg query HKLM\\SOFTWARE /s            - Recursive search
reg query HKLM\\SOFTWARE /v ValueName  - Query specific value
reg export HKLM\\SOFTWARE file.reg     - Export to file

STARTUP LOCATIONS:
HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run
HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Run

TIP: Look for unusual or suspicious entries!
""")
    
    fs.create_file("/C:/ProgramData/Secrets/hint.txt", """
The password you seek lies deep within the SOFTWARE hive.
Look for a vault that holds secrets...
The final challenge requires you to unlock Level6 by changing a registry value.
""")
    
    # Challenge tracking
    challenges = {
        "find_password": {
            "description": "Find the AdminPassword in SecretVault",
            "flag": "R3g1stry_M@st3r_2024",
            "completed": False,
            "hint": "Try: reg query HKLM\\SOFTWARE\\SecretVault /s"
        },
        "find_api_key": {
            "description": "Discover the ServiceToken API key",
            "flag": "sk_live_abc123xyz789def456",
            "completed": False,
            "hint": "Look in HKLM\\SOFTWARE\\SecretVault\\APIKeys"
        },
        "find_startup": {
            "description": "Identify the malicious startup program",
            "flag": "C:\\ProgramData\\hidden\\backdoor.exe",
            "completed": False,
            "hint": "Check HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run"
        },
        "export_key": {
            "description": "Export the SecretVault key to a file",
            "completed": False,
            "hint": "Use: reg export HKLM\\SOFTWARE\\SecretVault vault.reg"
        },
        "unlock_flag": {
            "description": "Set Level6Unlocked to 'true' to unlock the final flag",
            "flag": "REG{M@ST3R_0F_TH3_R3G1STRY}",
            "completed": False,
            "hint": "Use: reg add HKCU\\Software\\GameSettings /v Level6Unlocked /d true /f"
        }
    }
    
    return {
        "name": "Registry Deep Dive",
        "description": LEVEL_DESCRIPTION,
        "challenges": challenges,
        "final_flag": "REG{M@ST3R_0F_TH3_R3G1STRY}",
        "commands": ["reg"]
    }


def check_level6_progress(fs: FileSystem, terminal: Terminal, level_data: dict) -> str:
    """
    Check progress and provide feedback for Level 6
    """
    challenges = level_data["challenges"]
    completed = sum(1 for c in challenges.values() if c["completed"])
    total = len(challenges)
    
    progress = f"\n{'='*60}\n"
    progress += f"REGISTRY DEEP DIVE - PROGRESS: {completed}/{total}\n"
    progress += f"{'='*60}\n\n"
    
    for key, challenge in challenges.items():
        status = "✓" if challenge["completed"] else "✗"
        progress += f"{status} {challenge['description']}\n"
        if not challenge["completed"] and "hint" in challenge:
            progress += f"   💡 Hint: {challenge['hint']}\n"
    
    progress += f"\n{'='*60}\n"
    
    if completed == total:
        progress += "\n🎉 CONGRATULATIONS! You've mastered the Windows Registry!\n"
        progress += f"🚩 FINAL FLAG: {level_data['final_flag']}\n\n"
    
    return progress


def handle_reg_command(fs: FileSystem, terminal: Terminal, args: list, level_data: dict) -> str:
    """
    Handle registry commands (reg query, reg add, reg delete, reg export)
    """
    if not args:
        return """
Usage: reg <operation> [parameters]

Operations:
  query    Query registry keys and values
  add      Add new registry values
  delete   Remove registry entries
  export   Export registry keys to a file

Examples:
  reg query HKLM\\SOFTWARE
  reg query HKLM\\SOFTWARE /s
  reg query HKLM\\SOFTWARE\\SecretVault /v AdminPassword
  reg add HKCU\\Software\\Test /v MyValue /d "Hello" /f
  reg delete HKCU\\Software\\Test /v MyValue /f
  reg export HKLM\\SOFTWARE\\SecretVault vault.reg

Use 'reg query /?' for more help on query operations.
"""
    
    operation = args[0].lower()
    
    if operation == "query":
        return handle_reg_query(fs, args[1:], level_data)
    elif operation == "add":
        return handle_reg_add(fs, args[1:], level_data)
    elif operation == "delete":
        return handle_reg_delete(fs, args[1:], level_data)
    elif operation == "export":
        return handle_reg_export(fs, args[1:], level_data)
    else:
        return f"Error: Unknown operation '{operation}'"


def handle_reg_query(fs: FileSystem, args: list, level_data: dict) -> str:
    """Handle reg query operations"""
    if not args:
        return "Error: Missing registry key path\nUsage: reg query <KeyPath> [/v ValueName] [/s]"
    
    key_path = args[0].replace("/", "\\")
    recursive = "/s" in args
    value_name = None
    
    # Check for /v flag
    if "/v" in args:
        v_index = args.index("/v")
        if v_index + 1 < len(args):
            value_name = args[v_index + 1]
    
    # Parse registry path
    parts = key_path.split("\\")
    if not parts:
        return "Error: Invalid registry path"
    
    # Navigate registry structure
    current = fs.registry
    for part in parts:
        if part in current:
            current = current[part]
        else:
            return f"Error: The system cannot find the registry key specified.\n{key_path}"
    
    # Build output
    output = f"\n{key_path}\n"
    
    if value_name:
        # Query specific value
        if "_values" in current and value_name in current["_values"]:
            value = current["_values"][value_name]
            output += f"    {value_name}    REG_SZ    {value}\n"
            
            # Check for challenge completion
            challenges = level_data["challenges"]
            if value == challenges["find_password"]["flag"]:
                challenges["find_password"]["completed"] = True
                output += "\n✓ Challenge Complete: Found the AdminPassword!\n"
            elif value == challenges["find_api_key"]["flag"]:
                challenges["find_api_key"]["completed"] = True
                output += "\n✓ Challenge Complete: Found the API key!\n"
        else:
            return f"Error: The system cannot find the value specified.\n{value_name}"
    else:
        # List all values and subkeys
        if "_values" in current:
            for name, value in current["_values"].items():
                output += f"    {name}    REG_SZ    {value}\n"
                
                # Check challenges
                challenges = level_data["challenges"]
                if value == challenges["find_startup"]["flag"]:
                    challenges["find_startup"]["completed"] = True
                    output += "\n✓ Challenge Complete: Found the malicious startup entry!\n"
        
        # List subkeys
        for key in current.keys():
            if key != "_values":
                output += f"\n{key_path}\\{key}\n"
                if recursive and isinstance(current[key], dict):
                    # Recursively show subkeys
                    output += query_recursive(current[key], f"{key_path}\\{key}", level_data)
    
    return output


def query_recursive(registry_dict: dict, path: str, level_data: dict, indent: int = 0) -> str:
    """Recursively query registry"""
    output = ""
    prefix = "    " * indent
    
    if "_values" in registry_dict:
        for name, value in registry_dict["_values"].items():
            output += f"{prefix}    {name}    REG_SZ    {value}\n"
    
    for key, value in registry_dict.items():
        if key != "_values" and isinstance(value, dict):
            output += f"\n{prefix}{path}\\{key}\n"
            output += query_recursive(value, f"{path}\\{key}", level_data, indent + 1)
    
    return output


def handle_reg_add(fs: FileSystem, args: list, level_data: dict) -> str:
    """Handle reg add operations"""
    if len(args) < 4:
        return "Error: Invalid syntax\nUsage: reg add <KeyPath> /v <ValueName> /d <Data> [/f]"
    
    key_path = args[0].replace("/", "\\")
    
    if "/v" not in args or "/d" not in args:
        return "Error: Missing /v or /d parameter"
    
    v_index = args.index("/v")
    d_index = args.index("/d")
    
    if v_index + 1 >= len(args) or d_index + 1 >= len(args):
        return "Error: Missing value name or data"
    
    value_name = args[v_index + 1]
    value_data = args[d_index + 1].strip('"')
    
    # Navigate and add to registry
    parts = key_path.split("\\")
    current = fs.registry
    
    for part in parts:
        if part not in current:
            current[part] = {}
        current = current[part]
    
    if "_values" not in current:
        current["_values"] = {}
    
    current["_values"][value_name] = value_data
    
    # Check for unlock challenge
    if "Level6Unlocked" in value_name and value_data.lower() == "true":
        level_data["challenges"]["unlock_flag"]["completed"] = True
        return f"The operation completed successfully.\n\n✓ Challenge Complete: Level 6 Unlocked!\n🚩 FLAG: {level_data['final_flag']}"
    
    return "The operation completed successfully."


def handle_reg_delete(fs: FileSystem, args: list, level_data: dict) -> str:
    """Handle reg delete operations"""
    if len(args) < 2:
        return "Error: Invalid syntax\nUsage: reg delete <KeyPath> /v <ValueName> [/f]"
    
    return "The operation completed successfully.\n(Note: Deletion is simulated in this training environment)"


def handle_reg_export(fs: FileSystem, args: list, level_data: dict) -> str:
    """Handle reg export operations"""
    if len(args) < 2:
        return "Error: Invalid syntax\nUsage: reg export <KeyPath> <FileName>"
    
    key_path = args[0]
    filename = args[1]
    
    # Create export file
    export_content = f"""Windows Registry Editor Version 5.00

[{key_path}]
"Exported"="true"
"ExportDate"="2024-01-24"

; This is a simulated registry export for training purposes
"""
    
    # Save to user's desktop
    export_path = f"/C:/Users/Agent/Desktop/{filename}"
    fs.create_file(export_path, export_content)
    
    # Check challenge
    if "SecretVault" in key_path:
        level_data["challenges"]["export_key"]["completed"] = True
        return f"The operation completed successfully.\nRegistry exported to: {export_path}\n\n✓ Challenge Complete: SecretVault exported!"
    
    return f"The operation completed successfully.\nRegistry exported to: {export_path}"
