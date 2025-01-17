import os
import sys
from typing import Tuple, Dict, Callable, NoReturn
from colorama import init, Fore, Style
from displayutil import center_text, create_border
from port_management import manage_ports
from utilities_module import utilities_menu
from port_summary import port_summary_menu
from backup_restore import backup_restore_menu
from utils import get_input, confirm_action, show_progress, MenuExecutionError
from config_generation import generate_keys, get_network_info, generate_config

# Initialize colorama
init()

# Type Definitions:
# Custom types to improve code clarity and maintainability
# MenuFunction: Represents any function that can be called from the menu
# MenuAction: Tuple of (function, loading message) for menu items
# MenuActions: Dictionary mapping menu choices to their actions
MenuFunction = Callable[[], None]
MenuAction = Tuple[MenuFunction, str]
MenuActions = Dict[str, MenuAction]

# ASCII Art Banner:
# Decorative header using box-drawing characters and the application name
# - Uses white borders for clean appearance
# - Cyan text for the logo and title
# - Maintains symmetry for professional appearance
ASCII_ART = f"""{Fore.LIGHTWHITE_EX}::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::{Fore.LIGHTCYAN_EX}             ____  ______        ______             {Fore.LIGHTWHITE_EX}::
::{Fore.LIGHTCYAN_EX}            |  _ \|  _ \ \      / / ___|            {Fore.LIGHTWHITE_EX}::
::{Fore.LIGHTCYAN_EX}            | |_) | |_) \ \ /\ / / |  _             {Fore.LIGHTWHITE_EX}::
::{Fore.LIGHTCYAN_EX}            |  __/|  __/ \ V  V /| |_| |            {Fore.LIGHTWHITE_EX}::
::{Fore.LIGHTCYAN_EX}            |_|   |_|     \_/\_/  \____|            {Fore.LIGHTWHITE_EX}::
::{Fore.LIGHTCYAN_EX}                                                    {Fore.LIGHTWHITE_EX}::
::{Fore.LIGHTCYAN_EX}        Pterodactyl-Pelican-Wireguard-Manager       {Fore.LIGHTWHITE_EX}::
::{Fore.LIGHTCYAN_EX}                    By: Serfects                    {Fore.LIGHTWHITE_EX}::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::${Style.RESET_ALL}"""

# Main Menu Function:
# Handles the display and interaction of the main menu
# - Clears screen for clean presentation
# - Centers ASCII art and menu title
# - Displays options with descriptions
# - Returns user selection with built-in validation
def main_menu() -> str:
    """
    Display main menu and handle user input.

    Returns:
        str: Selected menu option

    Raises:
        KeyboardInterrupt: If user interrupts menu (Ctrl+C)
    """
    # Screen Clearing:
    # Uses appropriate clear command based on operating system
    os.system('clear' if os.name == 'posix' else 'cls')
    
    # Banner Display:
    # Centers each line of ASCII art individually
    # Adds borders above and below menu title
    centered_ascii_art = "\n".join(center_text(line) for line in ASCII_ART.strip().split("\n"))
    print(centered_ascii_art)
    
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
    
    # Input Handling:
    # Uses get_input with validation and default option
    return get_input(
        "Please select an option",
        choices=menu_options
    )

# Menu Function Executor:
# Wrapper for menu function execution with error handling
# - Shows progress indicator during loading
# - Catches and wraps exceptions in MenuExecutionError
# - Provides consistent error handling across all menu options
def run_menu_function(func: MenuFunction, loading_message: str) -> None:
    """
    Execute menu function with error handling and progress indication.

    Args:
        func (Callable[[], None]): The menu function to execute
        loading_message (str): Progress message to display

    Raises:
        MenuExecutionError: If menu function execution fails
    """
    try:
        show_progress(loading_message, 1)
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
        message (str): Optional message to display before exiting
        exit_code (int): Exit code to return to the system
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
    """
    try:
        # Menu Action Mapping:
        # Dictionary of all available menu options
        # Each option maps to a function and loading message
        menu_actions: MenuActions = {
            "1": (generate_config, "Preparing config generator"),
            "2": (backup_restore_menu, "Loading backup menu"),
            "3": (manage_ports, "Loading port management"),
            "4": (utilities_menu, "Loading utilities"),
            "5": (port_summary_menu, "Loading port summary")
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
                    func, message = menu_actions[choice]
                    run_menu_function(func, message)
                    
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