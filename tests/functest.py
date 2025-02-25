import os
import sys
import logging
from pathlib import Path
from colorama import init, Fore, Style

# Initialize colorama
init()

# Add the src directory to Python path for imports
src_path = Path(__file__).parent.parent / "src" / "ppwm-dev"
sys.path.append(str(src_path))

from disp_utils import (
    center_text, ASCII_ART, HistoryBar,
    display_history, clear_screen, display_error,
    show_progress, format_error, format_success
)
from general_utils import (
    get_input, confirm_action, MenuExecutionError,
    check_root, setup_logging, add_navigation_options, process_menu_choice
)
from main_menu import graceful_exit

# Initialize logger for test script
logger = logging.getLogger(__name__)

def test_utils_features():
    """Test various input and validation features"""
    HistoryBar().push("Utils Testing")
    
    test_results = []
    
    # Test basic input
    name = get_input("Enter your name", required=True)
    test_results.append(("Basic Required Input", bool(name)))
    
    # Test default value
    port = get_input("Enter port number", default="51820")
    test_results.append(("Default Value Input", port == "51820" if not port else True))
    
    # Test simple choices
    color = get_input("Select a color", choices=["red", "blue", "green"])
    test_results.append(("Simple Choices", color in ["red", "blue", "green"]))
    
    # Test tuple choices with descriptions
    role = get_input("Select your role", choices=[
        ("1", "Administrator", "Full system access"),
        ("2", "User", "Limited access"),
        ("3", "Guest", "View only access")
    ])
    test_results.append(("Complex Choices", role in ["1", "2", "3"]))
    
    # Test number validation
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
    test_results.append(("Input Validation", bool(score)))
    
    # Display test results
    print("\n=== Utils Testing Results ===")
    for test_name, result in test_results:
        status = "✓" if result else "✗"
        color = Fore.LIGHTGREEN_EX if result else Fore.LIGHTRED_EX
        print(f"{color}{status} {test_name}{Style.RESET_ALL}")
    
    input("\nPress Enter to continue...")
    HistoryBar().pop()

def test_display_features():
    """Test various display and formatting features"""
    HistoryBar().push("Display Testing")
    
    # Test screen clearing
    clear_screen()
    print("Testing screen clear... (cleared above)")
    
    # Test ASCII art display
    print("\nTesting ASCII art display:")
    centered_ascii = "\n".join(center_text(line) for line in ASCII_ART.strip().split("\n"))
    print(centered_ascii)
    
    # Test history bar
    print("\nTesting history bar display:")
    display_history()
    
    # Test progress indicator
    if confirm_action("Would you like to test the progress indicator?"):
        show_progress("Testing progress display", 1)
    
    # Test error display
    print("\nTesting error display:")
    display_error("This is a test error message")
    
    input("\nPress Enter to continue...")
    HistoryBar().pop()

def test_menu_system():
    """Test the menu system functionality"""
    HistoryBar().push("Menu Testing")
    
    menu_options = [
        ("1", "Option One", "First test option"),
        ("2", "Option Two", "Second test option"),
        ("3", "Return", "Go back to main menu")
    ]
    
    while True:
        choice = get_input("Test Menu", choices=menu_options)
        if choice == "3":
            break
        elif choice in ["1", "2"]:
            show_progress(f"Testing Option {choice}", 1)
    
    HistoryBar().pop()

def test_history_bar():
    """Test the updated history bar functionality (displays only the current menu)."""
    # Reset history bar to initial state.
    HistoryBar().clear()
    clear_screen()
    print("\n".join(center_text(line) for line in ASCII_ART.strip().split("\n")) + "\n")
    display_history()
    get_input("Press Enter to begin the updated history bar test...", choices=[""])
    
    # Push new menus and display updated history after each push.
    new_menus = [
        "Settings",
        "Network Configuration",
        "WireGuard Settings",
        "Peer Management",
        "Add New Peer",
        "Advanced Options with a very long description that might be truncated if it exceeds sixty-six characters"
    ]
    
    for menu in new_menus:
        HistoryBar().push(menu)
        clear_screen()
        print("\n".join(center_text(line) for line in ASCII_ART.strip().split("\n")) + "\n")
        display_history()
        print(f"\nCurrent menu: {menu}")
        get_input("Press Enter to continue...", choices=[""])
    
    # Pop menus one by one and display the updated history bar.
    while HistoryBar().pop() is not None:
        clear_screen()
        print("\n".join(center_text(line) for line in ASCII_ART.strip().split("\n")) + "\n")
        display_history()
        get_input("Press Enter to pop the current menu...", choices=[""])
        
    print(f"\n{Fore.LIGHTGREEN_EX}✓ History bar test complete!{Style.RESET_ALL}")
    get_input("Press Enter to return to main menu...", choices=[""])

def test_ascii_art_styles():
    """Test different styles of ASCII art border characters"""
    HistoryBar().push("ASCII Art Comparison")
    
    # Regular version (unbold border and specific text)
    print("\nRegular Version (Unbold Border and Title Text):")
    print("-" * 70)
    unbold_art = (ASCII_ART
        # Keep text in the art bold except for specific lines
        .replace(
            '::{Style.BRIGHT}{Fore.LIGHTCYAN_EX}               Pterodactyl-Pelican-Wireguard-Manager',
            '::{Style.NORMAL}{Fore.LIGHTCYAN_EX}               Pterodactyl-Pelican-Wireguard-Manager'
        )
        .replace(
            '::{Style.BRIGHT}{Fore.LIGHTCYAN_EX}                           By: Serfects',
            '::{Style.NORMAL}{Fore.LIGHTCYAN_EX}                           By: Serfects'
        )
    )
    centered_unbold = "\n".join(center_text(line) for line in unbold_art.strip().split("\n"))
    print(centered_unbold)
    
    # Create bold version (everything bold)
    print("\nBold Version (Bold Border and Text):")
    print("-" * 70)
    bold_border_art = ASCII_ART.replace(
        f"{Fore.LIGHTWHITE_EX}::", 
        f"{Style.BRIGHT}{Fore.LIGHTWHITE_EX}::"
    )
    centered_bold = "\n".join(center_text(line) for line in bold_border_art.strip().split("\n"))
    print(centered_bold)
    
    input("\nPress Enter to continue...")
    HistoryBar().pop()

def test_logging_system():
    """Test the logging system configuration and functionality"""
    HistoryBar().push("Logging System Test")
    
    test_results = []
    
    try:
        # Test log file creation
        logger.info("Testing logging system")
        test_results.append(("Log File Creation", True))
        
        # Test different log levels
        logger.debug("Test debug message")
        logger.info("Test info message")
        logger.warning("Test warning message")
        logger.error("Test error message")
        test_results.append(("Log Levels", True))
        
        # Test error formatting
        error_msg = "Test error formatting"
        formatted_error = format_error(error_msg)
        print(f"\nTesting error formatting:\n{formatted_error}")
        test_results.append(("Error Formatting", True))
        
        # Test success formatting
        success_msg = "Test success formatting"
        formatted_success = format_success(success_msg)
        print(f"\nTesting success formatting:\n{formatted_success}")
        test_results.append(("Success Formatting", True))
        
    except Exception as e:
        display_error(f"Logging test failed: {str(e)}")
        test_results.append(("Logging System", False))
    
    # Display test results
    print("\n=== Logging System Test Results ===")
    for test_name, result in test_results:
        status = format_success("PASS") if result else format_error("FAIL")
        print(f"{test_name}: {status}")
    
    input("\nPress Enter to continue...")
    HistoryBar().pop()

def test_root_check():
    """Test the root privilege checking functionality"""
    HistoryBar().push("Root Check Test")
    
    print("\nTesting root privilege check...")
    try:
        current_euid = os.geteuid()
        is_root = current_euid == 0
        
        print(f"\nCurrent effective UID: {current_euid}")
        print(f"Running as root: {format_success('Yes') if is_root else format_error('No')}")
        
        if not is_root:
            print("\nNote: Some features may be limited without root privileges")
            print("Try running the script with 'sudo' for full functionality")
    except Exception as e:
        display_error(f"Root check test failed: {str(e)}")
    
    input("\nPress Enter to continue...")
    HistoryBar().pop()

def test_error_handling():
    """Test various error handling scenarios"""
    HistoryBar().push("Error Handling Test")
    
    test_scenarios = [
        ("Invalid Input", lambda: get_input("Test input", validator=lambda x: False)),
        ("Empty Required Field", lambda: get_input("Test input", required=True)),
        ("Invalid Choice", lambda: get_input("Test input", choices=["1", "2"]))
    ]
    
    print("\nTesting error handling scenarios...")
    for scenario, test_func in test_scenarios:
        print(f"\nTesting: {scenario}")
        try:
            test_func()
        except Exception as e:
            print(format_error(f"Expected error occurred: {str(e)}"))
    
    input("\nPress Enter to continue...")
    HistoryBar().pop()

def test_navigation_options():
    """Test the new navigation options functionality"""
    HistoryBar().push("Navigation Options Test")
    
    print("\nTesting navigation options in different menu depths:")
    
    # Test main menu (should only show exit)
    clear_screen()
    print("\n=== Main Menu Test ===")
    main_options = [
        ("1", "Test Option 1", "First test option"),
        ("2", "Test Option 2", "Second test option")
    ]
    main_options = add_navigation_options(main_options)
    get_input("Press Enter to continue to submenu test...", choices=main_options)
    
    # Test first submenu (should show both back and exit)
    HistoryBar().push("Submenu Level 1")
    clear_screen()
    print("\n=== Submenu Level 1 Test ===")
    submenu_options = [
        ("1", "Sub Option 1", "First sub option"),
        ("2", "Sub Option 2", "Second sub option")
    ]
    submenu_options = add_navigation_options(submenu_options)
    get_input("Press Enter to continue to deep submenu test...", choices=submenu_options)
    
    # Test deep submenu (should show both back and exit)
    HistoryBar().push("Deep Submenu")
    clear_screen()
    print("\n=== Deep Submenu Test ===")
    deep_options = [
        ("1", "Deep Option 1", "First deep option"),
        ("2", "Deep Option 2", "Second deep option")
    ]
    deep_options = add_navigation_options(deep_options)
    get_input("Press Enter to test navigation...", choices=deep_options)
    
    # Test navigation
    while len(HistoryBar().stack) > 1:
        clear_screen()
        print(f"\nCurrent menu: {HistoryBar().stack[-1]}")
        nav_options = [("1", "Test Option", "Test option")]
        nav_options = add_navigation_options(nav_options)
        choice = get_input("Select an option (use 'b' to go back)", choices=nav_options)
        
        should_exit, was_handled = process_menu_choice(choice, {"1": lambda: None})
        if should_exit:
            break
    
    HistoryBar().pop()  # Clean up any remaining history
    print(f"\n{Fore.LIGHTGREEN_EX}✓ Navigation options test complete!{Style.RESET_ALL}")
    input("\nPress Enter to continue...")

def main():
    """Main test execution function"""
    logger.info("Starting test script")
    try:
        test_functions = {  # Define test_functions before using it
            "1": test_utils_features,
            "2": test_display_features,
            "3": test_menu_system,
            "4": test_history_bar,
            "5": test_root_check,
            "6": test_logging_system,
            "7": test_error_handling,
            "8": test_navigation_options
        }
        
        while True:
            clear_screen()
            centered_ascii = "\n".join(center_text(line) for line in ASCII_ART.strip().split("\n"))
            print(centered_ascii + "\n")
            display_history()
            
            main_options = [
                ("1", "Utils Tests", "Test input and validation features"),
                ("2", "Display Tests", "Test display and formatting features"),
                ("3", "Menu Tests", "Test menu system functionality"),
                ("4", "History Bar", "Test history bar features"),
                ("5", "Root Check", "Test root privilege checking"),
                ("6", "Logging", "Test logging system"),
                ("7", "Error Handling", "Test error handling scenarios"),
                ("8", "Navigation Options", "Test new navigation options"),
            ]
            
            # Add navigation options to main menu
            main_options = add_navigation_options(main_options)
            
            choice = get_input("Select Test Suite", choices=main_options)
            
            should_exit, was_handled = process_menu_choice(choice, test_functions)
            
            if should_exit:
                break
            elif was_handled and choice in test_functions:
                test_functions[choice]()

    except KeyboardInterrupt:
        logger.info("Test script interrupted by user")
        print("\nTest script interrupted by user")
    except Exception as e:
        logger.error(f"Fatal error in test script: {str(e)}", exc_info=True)
        display_error(f"Fatal error in test script: {str(e)}")
    
    logger.info("Test script completed")
    print("\nTest script completed")
    input("\nPress Enter to exit...")

if __name__ == "__main__":
    # Initialize logging for test script
    setup_logging()
    main()
