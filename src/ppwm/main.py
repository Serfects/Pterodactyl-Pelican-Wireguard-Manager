import os
from port_management import manage_ports
from utilities_module import utilities_menu
from port_summary import port_summary_menu
from backup_restore import backup_restore_menu
from config_generation import get_input, generate_keys, get_network_info, generate_config

def main_menu():
    print("=== WireGuard Management ===\n1. Generate Config\n2. Backup and Restore\n3. Port Management\n4. Utilities\n5. Port Summary\nx. Exit")
    return input("Your choice: ").strip()

def main():
    while (choice := main_menu()) != "x":
        if choice == "1": generate_config()
        elif choice == "2": backup_restore_menu()
        elif choice == "3": manage_ports()
        elif choice == "4": utilities_menu()
        elif choice == "5": port_summary_menu()
        else: print("Invalid choice. Press Enter."); input()
    print("Exiting.")

if __name__ == "__main__": main()