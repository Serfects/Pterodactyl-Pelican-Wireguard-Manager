import os
import sys
from colorama import init, Fore, Style

# Import from main modules (these work because PYTHONPATH includes src/ppwm-dev)
from disp_utils import display_screen, show_progress, center_text, create_border
from general_utils import get_input, confirm_action, MenuExecutionError

# Initialize colorama for cross-platform color support
init()

def test_utils_features():
    # Test general utility functions with various input types
    display_screen("Utils Testing", lambda: None)
    
    name = get_input("Enter your name", required=True)
    port = get_input("Enter port number", default="51820")
    color = get_input("Select a color", choices=["red", "blue", "green"])
    
    role = get_input("Select your role", choices=[
        ("1", "Administrator", "Full system access"),
        ("2", "User", "Limited access"),
        ("3", "Guest", "View only")
    ])
    
    def number_validator(value):
        try:
            num = int(value)
            return 1 <= num <= 100
        except ValueError:
            return False
            
    score = get_input(
        "Enter a number between 1-100",
        validator=number_validator
    )
    
    # Display results
    display_screen("Test Results", lambda: print_test_results(name, port, color, role, score))
    input("\nPress Enter to continue...")

def print_test_results(name, port, color, role, score):
    print(f"{Fore.CYAN}=== Input Summary ==={Style.RESET_ALL}")
    print(f"Name: {Fore.WHITE}{name}{Style.RESET_ALL}")
    print(f"Port: {Fore.WHITE}{port}{Style.RESET_ALL}")
    print(f"Color: {Fore.WHITE}{color}{Style.RESET_ALL}")
    print(f"Role: {Fore.WHITE}{role}{Style.RESET_ALL}")
    print(f"Score: {Fore.WHITE}{score}{Style.RESET_ALL}")

def mock_generate_config():
    display_screen("Config Generator", lambda: None)
    show_progress("Checking system requirements", 1.5)
    
    server_type = get_input("Select server type", choices=[
        ("1", "Standalone Server", "Single server configuration"),
        ("2", "Multi-Server", "Multiple server setup"),
        ("3", "Custom", "Advanced configuration options")
    ])
    
    if confirm_action("Generate server keys?"):
        show_progress("Generating server keys", 3)
        show_progress("Creating configuration files", 1.5)
        print(center_text(f"\n{Fore.GREEN}Configuration generated successfully!{Style.RESET_ALL}"))
    
    input("\nPress Enter to continue...")

def mock_backup_restore():
    while True:
        display_screen("Backup and Restore", lambda: None)
        choice = get_input("Select operation", choices=[
            ("1", "Create Backup", "Save current configuration"),
            ("2", "Restore Backup", "Load previous configuration"),
            ("3", "View Backups", "List existing backups"),
            ("4", "Return to Main Menu")
        ])
        
        if choice == "4":
            break
            
        if choice == "1":
            if confirm_action("Create new backup?"):
                show_progress("Creating backup", 2)
                print(center_text(f"\n{Fore.GREEN}Backup created successfully!{Style.RESET_ALL}"))
        elif choice == "2":
            if confirm_action("Restore from backup?"):
                show_progress("Restoring configuration", 2)
                print(center_text(f"\n{Fore.GREEN}Configuration restored!{Style.RESET_ALL}"))
        elif choice == "3":
            show_progress("Loading backup list", 1.5)
            print("\nAvailable Backups:")
            print(f"  {Style.DIM}•{Style.RESET_ALL} backup_20240101_120000.tar.gz")
            print(f"  {Style.DIM}•{Style.RESET_ALL} backup_20240102_153000.tar.gz")
        
        input("\nPress Enter to continue...")

def main():
    # Verify we're running in test environment
    if not os.getenv('TESTING'):
        print(f"{Fore.YELLOW}Warning: Not running in test environment{Style.RESET_ALL}")
        print("Please run: source test_environment/activate_env.sh")
        sys.exit(1)

    try:
        menu_actions = {
            "1": (test_utils_features, "Testing utility functions"),
            "2": (mock_generate_config, "Testing config generator"),
            "3": (mock_backup_restore, "Testing backup system")
        }

        while True:
            try:
                display_screen("Test Script Menu", lambda: None)
                choice = get_input("Select test to run", choices=[
                    ("1", "Test Utils", "Test input and display utilities"),
                    ("2", "Test Config", "Test configuration generator"),
                    ("3", "Test Backup", "Test backup and restore functions"),
                    ("x", "Exit", "Exit test script")
                ])
                
                if choice.lower() == "x":
                    if confirm_action("Exit test script?"):
                        break
                
                if choice in menu_actions:
                    func, message = menu_actions[choice]
                    show_progress(message, 1.5)
                    func()
                    
            except MenuExecutionError as e:
                print(f"\n{Fore.YELLOW}⚠ {Fore.LIGHTRED_EX}{str(e)}{Style.RESET_ALL}")
                if not confirm_action("Return to test menu?"):
                    break
                    
            except KeyboardInterrupt:
                if confirm_action("\nExit test script?"):
                    break
                print(f"\n{Fore.YELLOW}Returning to test menu...{Style.RESET_ALL}")

    except Exception as e:
        print(f"\n{Fore.YELLOW}⚠ {Fore.LIGHTRED_EX}Fatal error: {str(e)}{Style.RESET_ALL}")
    finally:
        print(center_text(f"\n{Fore.YELLOW}Test script completed{Style.RESET_ALL}"))
        print(create_border())

if __name__ == "__main__":
    main()
