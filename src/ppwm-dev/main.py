import os
from displayutil import center_text, create_border, format_option
from port_management import manage_ports
from utilities_module import utilities_menu
from port_summary import port_summary_menu
from backup_restore import backup_restore_menu
from config_generation import get_input, generate_keys, get_network_info, generate_config

ASCII_ART = """
::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::             ____  ______        ______             ::
::            |  _ \|  _ \ \      / / ___|            ::
::            | |_) | |_) \ \ /\ / / |  _             ::
::            |  __/|  __/ \ V  V /| |_| |            ::
::            |_|   |_|     \_/\_/  \____|            ::
::                                                    ::
::        Pterodactyl-Pelican-Wireguard-Manager       ::
::                    By: Serfects                    ::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::
"""

def main_menu():
    """Display main menu and return user choice."""
    os.system('clear')  # Clear screen before showing menu
    
    # Center each line of the ASCII art
    centered_ascii_art = "\n".join(center_text(line) for line in ASCII_ART.strip().split("\n"))
    print(centered_ascii_art)
    
    print("\n" + create_border())
    print(center_text("Main Menu"))
    print(create_border() + "\n")
    
    menu_options = [
        ("1", "Generate Config"),
        ("2", "Backup and Restore"),
        ("3", "Port Management"),
        ("4", "Utilities"),
        ("5", "Port Summary"),
        ("x", "Exit")
    ]
    
    for key, description in menu_options:
        print(format_option(key, description))
    
    print("\n" + create_border())
    return input("\nYour choice: ").strip().lower()

def main():
    """Main program loop."""
    while (choice := main_menu()) != "x":
        if choice == "1":
            generate_config()
        elif choice == "2":
            backup_restore_menu()
        elif choice == "3":
            manage_ports()
        elif choice == "4":
            utilities_menu()
        elif choice == "5":
            port_summary_menu()
        else:
            print("Invalid choice. Press Enter to continue...")
            input()
    
    print(center_text("Thank you for using WireGuard Management"))
    print(create_border())

if __name__ == "__main__":
    main()