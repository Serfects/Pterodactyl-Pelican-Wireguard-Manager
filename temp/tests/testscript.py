import os
import sys
from colorama import init, Fore, Style

from disp_utils import (
    DisplayConfig,
    display_screen,
    show_progress,
    center_text,
    create_border,
    BreadcrumbTracker,
    format_error,
    format_success
)
from general_utils import get_input, confirm_action, MenuExecutionError

init()

# Keep original utility testing but integrate with new display system
def test_utils_features():
    breadcrumb = BreadcrumbTracker.get_instance()
    breadcrumb.push("Utils Testing")
    
    def run_tests():
        # Original input testing
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
        
        # Display results using centered text
        print(f"\n{Fore.CYAN}=== Input Summary ==={Style.RESET_ALL}")
        print(center_text(f"Name: {name}"))
        print(center_text(f"Port: {port}"))
        print(center_text(f"Color: {color}"))
        print(center_text(f"Role: {role}"))
        print(center_text(f"Score: {score}"))

    display_screen("Utils Testing", run_tests)
    input("\nPress Enter to continue...")
    breadcrumb.pop()

# Keep mock config generator but use new display features
def mock_generate_config():
    breadcrumb = BreadcrumbTracker.get_instance()
    breadcrumb.push("Config Generator")
    
    def run_generator():
        show_progress("Checking system requirements", 1.5)
        
        server_type = get_input("Select server type", choices=[
            ("1", "Standalone Server", "Single server configuration"),
            ("2", "Multi-Server", "Multiple server setup"),
            ("3", "Custom", "Advanced configuration options")
        ])
        
        if confirm_action("Generate server keys?"):
            show_progress("Generating server keys", 3)
            show_progress("Creating configuration files", 1.5)
            print(center_text(format_success("Configuration generated successfully!")))
    
    display_screen("Config Generator", run_generator)
    breadcrumb.pop()
    input("\nPress Enter to continue...")

# Keep backup/restore testing with new display integration
def mock_backup_restore():
    breadcrumb = BreadcrumbTracker.get_instance()
    breadcrumb.push("Backup and Restore")
    
    while True:
        def show_menu():
            return get_input("Select operation", choices=[
                ("1", "Create Backup", "Save current configuration"),
                ("2", "Restore Backup", "Load previous configuration"),
                ("3", "View Backups", "List existing backups"),
                ("4", "Return to Main Menu")
            ])
            
        display_screen("Backup and Restore", None)
        choice = show_menu()
        
        if choice == "4":
            break
            
        if choice == "1":
            breadcrumb.push("Create Backup")
            if confirm_action("Create new backup?"):
                show_progress("Creating backup", 2)
                print(center_text(format_success("Backup created successfully!")))
            breadcrumb.pop()
        elif choice == "2":
            breadcrumb.push("Restore Backup")
            if confirm_action("Restore from backup?"):
                show_progress("Restoring configuration", 2)
                print(center_text(format_success("Configuration restored!")))
            breadcrumb.pop()
        elif choice == "3":
            breadcrumb.push("View Backups")
            show_progress("Loading backup list", 1.5)
            print("\nAvailable Backups:")
            print(center_text("backup_20240101_120000.tar.gz"))
            print(center_text("backup_20240102_153000.tar.gz"))
            breadcrumb.pop()
        
        input("\nPress Enter to continue...")
    
    breadcrumb.pop()

# Add new display testing while keeping original tests
def test_display_features():
    """Test DisplayConfig and display formatting features"""
    breadcrumb = BreadcrumbTracker.get_instance()
    breadcrumb.push("Display Tests")

    def display_content():
        # Test all border styles
        print(f"{Fore.CYAN}Testing border styles:{Style.RESET_ALL}")
        print(create_border(char=DisplayConfig.Header.ASCII_BORDER))
        print(create_border(char=DisplayConfig.Header.BREADCRUMB_BORDER))
        print(create_border(char=DisplayConfig.Title.BORDER_CHAR))
        
        # Test text formatting
        print(f"\n{Fore.CYAN}Testing text formatting:{Style.RESET_ALL}")
        print(center_text("Centered Text"))
        print(center_text("1: Option One"))
        print(format_error("Test Error Message"))
        print(format_success("Test Success Message"))

    display_screen("Display Tests", display_content)
    input("\nPress Enter to continue...")
    breadcrumb.pop()

def test_breadcrumb_navigation():
    """Test breadcrumb functionality with deep navigation"""
    breadcrumb = BreadcrumbTracker.get_instance()
    breadcrumb.push("Navigation Test")

    def nav_test():
        # Push many items to test truncation
        print(f"{Fore.CYAN}Testing breadcrumb navigation and truncation:{Style.RESET_ALL}\n")
        paths = ["Settings", "Network", "Advanced", "Security", "Certificates", "Import"]
        for path in paths:
            breadcrumb.push(path)
            display_screen("Navigation Depth Test", lambda: None)
            input(f"\nPress Enter to add {path}...")

        # Pop back one by one
        while len(paths):
            path = paths.pop()
            breadcrumb.pop()
            display_screen("Navigation Depth Test", lambda: None)
            if paths:
                input(f"\nPress Enter to remove {path}...")

    display_screen("Navigation Test", nav_test)
    breadcrumb.pop()

def main():
    try:
        breadcrumb = BreadcrumbTracker.get_instance()
        breadcrumb.reset()

        menu_actions = {
            "1": (test_utils_features, "Testing utility functions"),
            "2": (mock_generate_config, "Testing config generator"),
            "3": (mock_backup_restore, "Testing backup system"),
            "4": (test_display_features, "Testing display features"),
            "5": (test_breadcrumb_navigation, "Testing breadcrumb navigation")
        }

        while True:
            try:
                display_screen("Test Script", lambda: None)
                choice = get_input("Select test to run", choices=[
                    ("1", "Utils Test", "Test input and display utilities"),
                    ("2", "Config Test", "Test configuration generator"),
                    ("3", "Backup Test", "Test backup and restore functions"),
                    ("4", "Display Test", "Test display formatting"),
                    ("5", "Navigation Test", "Test breadcrumb navigation"),
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
                print(format_error(str(e)))
                if not confirm_action("Return to test menu?"):
                    break

            except KeyboardInterrupt:
                if confirm_action("\nExit test script?"):
                    break
                print(f"\n{Fore.YELLOW}Returning to test menu...{Style.RESET_ALL}")

    except Exception as e:
        print(format_error(f"Fatal error: {str(e)}"))
    finally:
        print(center_text(f"\n{Fore.YELLOW}Test script completed{Style.RESET_ALL}"))
        print(create_border(char=DisplayConfig.Header.BREADCRUMB_BORDER))

if __name__ == "__main__":
    main()
