import os
import sys
from typing import Tuple, Dict, Callable, NoReturn, Optional
from colorama import init, Fore, Style
from display_utils import center_text, create_border
from port_management import manage_ports
from utilities_module import utilities_menu
from port_summary import port_summary_menu
from backup_restore import backup_restore_menu
from general_utils import get_input, confirm_action, MenuExecutionError, clear_screen

# Initialize colorama
init()

# Type Definitions:
# Custom types to improve code clarity and maintainability
# MenuFunction: Represents any function that can be called from the menu
# MenuActions: Dictionary mapping menu choices to their actions
MenuFunction = Callable[[], None]
MenuActions = Dict[str, MenuFunction]

def main_menu() -> str:
    """
    Display main menu and handle user input.
    
    Returns:
        str: Selected menu option identifier (1-5 or 'x')
    
    Raises:
        KeyboardInterrupt: If user interrupts menu (Ctrl+C)
        MenuExecutionError: If menu display or input handling fails
        StatusBarError: If status bar cannot be displayed
    """
    try:
        clear_screen("Main Menu")
        
        print("\n" + create_border())
        print(center_text(f"{Fore.YELLOW}Main Menu{Style.RESET_ALL}"))
        print(create_border() + "\n")
        
        # Menu Options:
        # Each option includes:
        # - Number/letter for selection
        # - Short description
        # - Detailed explanation
        menu_options = [
            ("1", "Generate Config", "Create a new WireGuard configuration"),
            ("2", "Backup and Restore", "Manage configuration backups"),
            ("3", "Port Management", "Configure and manage port settings"),
            ("4", "Utilities", "Additional tools and settings"),
            ("5", "Port Summary", "View current port configurations"),
            ("x", "Exit", "Exit the application")
        ]
        
        return get_input(
            "Please select an option",
            choices=menu_options
        )
    except Exception as e:
        raise MenuExecutionError(f"Failed to display main menu: {str(e)}")

# Menu Function Executor:
# Wrapper for menu function execution with error handling
# - Catches and wraps exceptions in MenuExecutionError
# - Provides consistent error handling across all menu options
def run_menu_function(func: MenuFunction, path: str) -> None:
    """
    Execute a provided menu function with error handling.
    
    Args:
        func (MenuFunction): The menu function to execute.
        path (str): Current menu navigation path for status bar.
    
    Raises:
        MenuExecutionError: If function execution fails.
        StatusBarError: If status bar cannot be displayed.
        KeyboardInterrupt: If user interrupts execution.
    
    Note:
        This function handles both the execution and any cleanup needed
        if the function fails or is interrupted.
    """
    clear_screen(path)
    try:
        func()
    except Exception as e:
        raise MenuExecutionError(f"Error in menu execution: {str(e)}")

# Graceful Exit Handler:
# Ensures consistent shutdown behavior
# - Displays optional exit message
# - Shows thank you message
# - Creates clean visual border
# - Returns appropriate system exit code
def graceful_exit(message: str = "", exit_code: int = 0) -> NoReturn:
    """
    Perform a graceful shutdown of the application.
    
    Args:
        message (str): Optional message to display before exiting.
        exit_code (int): System exit code.
    
    Note:
        The function prints a thank-you note, a final border, and then exits.
    """
    if message:
        print(center_text(f"\n{Fore.YELLOW}{message}{Style.RESET_ALL}"))
    print(center_text(f"\n{Fore.YELLOW}Thank you for using WireGuard Management{Style.RESET_ALL}"))
    print(create_border())
    sys.exit(exit_code)

# Main Application Loop:
# Primary control flow of the application
# - Maintains menu state
# - Handles all error conditions
# - Provides graceful shutdown
def main() -> None:
    """
    Main application loop with comprehensive error handling.
    
    This function serves as the primary entry point and controller for the application,
    handling menu navigation, user input, and error conditions.
    
    Error Handling Levels:
      - Recoverable MenuExecutionError: Provides the option to return to the main menu.
      - KeyboardInterrupt: Catches user-initiated interruptions, allowing graceful exit.
      - Fatal Exceptions: All other exceptions trigger a fatal error shutdown.
    """
    clear_screen("Main Menu")
    try:
        # Menu Action Mapping:
        # Dictionary of all available menu options
        # Each option maps to a function
        menu_actions: MenuActions = {
            "1": generate_config,
            "2": backup_restore_menu,
            "3": manage_ports,
            "4": utilities_menu,
            "5": port_summary_menu
        }

        # Main Program Loop:
        # Continues until explicit exit
        # - Handles menu selection
        # - Processes user choices
        # - Manages errors and interrupts
        while True:
            try:
                # Menu Navigation:
                # Get and process user choice
                # Handle exit condition
                choice = main_menu()
                if choice.lower() == "x":
                    if confirm_action("Are you sure you want to exit?"):
                        break
                
                if choice in menu_actions:
                    func = menu_actions[choice]
                    # Construct the dynamic path for the status bar using the chosen option's description.
                    run_menu_function(func, f"Main Menu -> {menu_options[int(choice)-1][1]}")
                    
            # Error Handling:
            # Three levels of error handling:
            # 1. Menu execution errors (recoverable)
            # 2. Keyboard interrupts (user-initiated)
            # 3. Unexpected errors (fatal)
            except MenuExecutionError as e:
                print(f"\n{Fore.YELLOW}⚠ {Fore.LIGHTRED_EX}{str(e)}{Style.RESET_ALL}")
                if not confirm_action("Would you like to return to the main menu?"):
                    graceful_exit("Exiting due to error", 1)
                    
            except KeyboardInterrupt:
                if confirm_action("\nDo you want to exit?"):
                    graceful_exit("Received interrupt signal, shutting down...", 0)
                print(f"\n{Fore.YELLOW}Returning to main menu...{Style.RESET_ALL}")

    except Exception as e:
        # Fatal Error Handling:
        # Last resort for unexpected errors
        # Ensures user sees error before exit
        print(f"\n{Fore.YELLOW}⚠ {Fore.LIGHTRED_EX}Fatal error: {str(e)}{Style.RESET_ALL}")
        graceful_exit("Application terminated due to fatal error", 1)

# Application Entry Point:
# Standard Python idiom for script execution
if __name__ == "__main__":
    main()