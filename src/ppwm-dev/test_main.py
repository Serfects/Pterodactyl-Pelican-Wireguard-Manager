import os
import sys
from typing import Tuple, Dict, Callable, NoReturn
from colorama import init, Fore, Style
from displayutil import center_text, create_border
from utils import get_input, confirm_action, show_progress, MenuExecutionError

# Initialize colorama
init()

# Custom types for menu handling
MenuFunction = Callable[[], None]
MenuAction = Tuple[MenuFunction, str]
MenuActions = Dict[str, MenuAction]

# Use the actual ASCII art and formatting from main.py
ASCII_ART = f"""{Fore.WHITE}::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::{Fore.CYAN}             ____  ______        ______             {Fore.WHITE}::
::{Fore.CYAN}            |  _ \|  _ \ \      / / ___|            {Fore.WHITE}::
::{Fore.CYAN}            | |_) | |_) \ \ /\ / / |  _             {Fore.WHITE}::
::{Fore.CYAN}            |  __/|  __/ \ V  V /| |_| |            {Fore.WHITE}::
::{Fore.CYAN}            |_|   |_|     \_/\_/  \____|            {Fore.WHITE}::
::{Fore.CYAN}                                                    {Fore.WHITE}::
::{Fore.CYAN}        Pterodactyl-Pelican-Wireguard-Manager       {Fore.WHITE}::
::{Fore.CYAN}                    By: Serfects                    {Fore.WHITE}::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::{Style.RESET_ALL}
"""

# Mock functions for features not yet implemented
def mock_generate_config():
    """Mock config generation with realistic UI flow"""
    show_progress("Checking system requirements", 1)
    
    server_type = get_input("Select server type", choices=[
        ("1", "Standalone Server", "Single server configuration"),
        ("2", "Multi-Server", "Multiple server setup"),
        ("3", "Custom", "Advanced configuration options")
    ])
    
    port = get_input("Enter WireGuard port", default="51820")
    
    if confirm_action("Generate server keys?"):
        show_progress("Generating server keys", 2)
        show_progress("Creating configuration files", 1)
        print(f"\n{Fore.GREEN}Configuration generated successfully!{Style.RESET_ALL}")
    
    input("\nPress Enter to continue...")

def mock_backup_restore():
    """Mock backup/restore with realistic UI flow"""
    choices = [
        ("1", "Create Backup", "Save current configuration"),
        ("2", "Restore Backup", "Load previous configuration"),
        ("3", "View Backups", "List existing backups"),
        ("4", "Return to Main Menu")
    ]
    
    while True:
        choice = get_input("Backup and Restore Menu", choices=choices)
        if choice == "4":
            break
        
        if choice == "1":
            if confirm_action("Create new backup?"):
                show_progress("Creating backup", 2)
                print(f"\n{Fore.GREEN}Backup created successfully!{Style.RESET_ALL}")
        elif choice == "2":
            if confirm_action("Restore from backup?"):
                show_progress("Restoring configuration", 2)
                print(f"\n{Fore.GREEN}Configuration restored!{Style.RESET_ALL}")
        elif choice == "3":
            show_progress("Loading backup list", 1)
            print("\nAvailable Backups:")
            print("  • backup_20240101_120000.tar.gz")
            print("  • backup_20240102_153000.tar.gz")
        
        input("\nPress Enter to continue...")

def mock_port_management():
    """Mock port management functionality"""
    choices = [
        ("1", "Add Port", "Configure new port forwarding"),
        ("2", "Remove Port", "Delete existing port configuration"),
        ("3", "Return to Main Menu")
    ]
    choice = get_input("Select port operation", choices=choices)
    if choice != "3":
        show_progress("Updating port configuration", 2)

def mock_utilities():
    """Mock utilities functionality"""
    show_progress("Running system check", 2)
    print(f"\n{Fore.GREEN}All systems operational{Style.RESET_ALL}")
    input("\nPress Enter to continue...")

def mock_port_summary():
    """Mock port summary display"""
    show_progress("Loading port configurations", 1)
    print("\nActive Ports:")
    print("  • 51820/udp - WireGuard")
    print("  • 22/tcp - SSH")
    input("\nPress Enter to continue...")

def test_border_alignment():
    """Test border alignment with colored text"""
    os.system('clear' if os.name == 'posix' else 'cls')
    
    # Test centered ASCII art with borders
    centered_ascii_art = "\n".join(center_text(line) for line in ASCII_ART.strip().split("\n"))
    print(centered_ascii_art)
    
    # Test various colored text with borders
    print("\n" + create_border())
    print(center_text(f"{Fore.YELLOW}Testing Border Alignment{Style.RESET_ALL}"))
    print(create_border())
    
    # Test mixed colored text
    mixed_text = f"{Fore.CYAN}Cyan{Style.RESET_ALL} and {Fore.MAGENTA}Magenta{Style.RESET_ALL} text"
    print("\n" + create_border())
    print(center_text(mixed_text))
    print(create_border())
    
    input("\nPress Enter to continue to main menu...")

def main() -> None:
    """Main application loop using actual utils.py functionality"""
    try:
        # Add border alignment test to menu
        menu_actions: MenuActions = {
            "1": (test_border_alignment, "Testing border alignment"),
            "2": (mock_generate_config, "Preparing config generator"),
            "3": (mock_backup_restore, "Loading backup menu"),
            "4": (mock_port_management, "Loading port management"),
            "5": (mock_utilities, "Loading utilities"),
            "6": (mock_port_summary, "Loading port summary")
        }

        while True:
            try:
                # Use actual main_menu functionality from main.py
                os.system('clear' if os.name == 'posix' else 'cls')
                
                centered_ascii_art = "\n".join(center_text(line) for line in ASCII_ART.strip().split("\n"))
                print(centered_ascii_art)
                
                print("\n" + create_border())
                print(center_text(f"{Fore.YELLOW}Main Menu{Style.RESET_ALL}"))
                print(create_border() + "\n")
                
                menu_options = [
                    ("1", "Test Border Alignment", "Test border alignment with colored text"),
                    ("2", "Generate Config", "Create a new WireGuard configuration"),
                    ("3", "Backup and Restore", "Manage configuration backups"),
                    ("4", "Port Management", "Configure and manage port settings"),
                    ("5", "Utilities", "Additional tools and settings"),
                    ("6", "Port Summary", "View current port configurations"),
                    ("x", "Exit", "Exit the application")
                ]
                
                choice = get_input("Please select an option", choices=menu_options, default="1")
                
                if choice.lower() == "x":
                    if confirm_action("Are you sure you want to exit?"):
                        break
                
                if choice in menu_actions:
                    func, message = menu_actions[choice]
                    show_progress(message, 1)
                    func()
                    
            except MenuExecutionError as e:
                print(f"\n{Fore.YELLOW}⚠ {Fore.LIGHTRED_EX}{str(e)}{Style.RESET_ALL}")
                if not confirm_action("Would you like to return to the main menu?"):
                    break
                    
            except KeyboardInterrupt:
                if confirm_action("\nDo you want to exit?"):
                    break
                print(f"\n{Fore.YELLOW}Returning to main menu...{Style.RESET_ALL}")

    except Exception as e:
        print(f"\n{Fore.YELLOW}⚠ {Fore.LIGHTRED_EX}Fatal error: {str(e)}{Style.RESET_ALL}")
    finally:
        print(center_text(f"\n{Fore.YELLOW}Thank you for using WireGuard Management{Style.RESET_ALL}"))
        print(create_border())

if __name__ == "__main__":
    main()
