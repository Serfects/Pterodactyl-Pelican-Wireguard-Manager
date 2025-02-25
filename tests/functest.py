#!/usr/bin/env python3
"""
PPWM Test Script (functest.py)

This script is used to test various components and features of the 
Pterodactyl-Pelican-Wireguard-Manager application in isolation.
It provides a menu-driven interface to test specific functionality
without affecting the actual system configuration.

The script mimics the look and feel of the real application to provide
an authentic testing experience, while focusing purely on functionality tests.
"""

import os
import sys
import time
import signal
import logging
from datetime import datetime

# Set Python path to include the parent directory
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src/ppwm-dev')))

# Import application modules
try:
    from base_utils import AppError, setup_logging, check_root, SCREEN_WIDTH
    from display_utils import (ASCII_ART, clear_screen, center_text, create_border, 
                              show_error, format_error_message, format_success, 
                              show_progress, graceful_exit, NAV_BORDER_CHAR)
    from navigation import MenuNavigationTracker
    from input_utils import get_input, confirm_action
except ImportError as e:
    print(f"Error importing module: {e}")
    print("Please make sure you're running the script from the correct directory")
    print("and that all required modules are present.")
    sys.exit(1)

# Set up logging for test script
logger = setup_logging()
logger.info("Test script started")

# Initialize the menu navigation tracker
menu_tracker = MenuNavigationTracker()

def handle_sigint(sig, frame):
    """Handle CTRL+C gracefully"""
    logger.info("SIGINT received, exiting gracefully")
    graceful_exit("\nExiting test script...", 0)

# Register signal handler
signal.signal(signal.SIGINT, handle_sigint)

# ========== Test Functions ==========

def test_display_utilities():
    """Test various display utility functions"""
    clear_screen()
    menu_tracker.push("Display Utilities Test")
    
    print(ASCII_ART)
    print(create_border(NAV_BORDER_CHAR))
    print(menu_tracker.display())
    print(create_border(NAV_BORDER_CHAR))
    
    print("\n1. Testing text centering")
    print("-------------------------")
    print(center_text("This is centered text"))
    print(center_text("This is centered colored " + "\033[92mGREEN\033[0m text"))
    print(center_text("This is a really long text that should get truncated because it exceeds the screen width", SCREEN_WIDTH))
    
    print("\n2. Testing borders")
    print("----------------")
    print(create_border("="))
    print(create_border("-"))
    print(create_border("~"))
    
    print("\n3. Testing error formatting")
    print("------------------------")
    print(format_error_message("This is a test error message"))
    print(format_success("This is a test success message"))
    
    print("\n4. Testing progress indicator")
    show_progress("Testing progress indicator", 2)
    print(format_success("Progress completed successfully"))
    
    choice = get_input("\nPress 'B' to go back or 'X' to exit: ", ["B", "X"], case_insensitive=True)
    if choice.upper() == "X":
        graceful_exit("Exiting test script...", 0)
    
    menu_tracker.pop()
    return main_menu()

def test_navigation_tracker():
    """Test the MenuNavigationTracker functionality"""
    clear_screen()
    menu_tracker.push("Navigation Tracker Test")
    
    print(ASCII_ART)
    print(create_border(NAV_BORDER_CHAR))
    print(menu_tracker.display())
    print(create_border(NAV_BORDER_CHAR))
    
    print("\n1. Testing menu navigation")
    print("-----------------------")
    print(f"Current menu: {menu_tracker.current_menu()}")
    
    print("\n2. Testing menu history")
    print("--------------------")
    print("Let's navigate through a simulated menu hierarchy:")
    
    test_menus = ["Server Setup", "Network Configuration", "WireGuard Setup", "Advanced Settings"]
    
    for menu in test_menus:
        print(f"\nPushing '{menu}' to navigation stack...")
        menu_tracker.push(menu)
        print("Current navigation display:")
        print(create_border(NAV_BORDER_CHAR))
        print(menu_tracker.display())
        print(create_border(NAV_BORDER_CHAR))
        time.sleep(1)
    
    print("\nNow let's go back through the menus:")
    
    while len(test_menus) > 0:
        print("\nPopping from navigation stack...")
        menu_tracker.pop()
        test_menus.pop()
        print("Current navigation display:")
        print(create_border(NAV_BORDER_CHAR))
        print(menu_tracker.display())
        print(create_border(NAV_BORDER_CHAR))
        time.sleep(1)
    
    choice = get_input("\nPress 'B' to go back or 'X' to exit: ", ["B", "X"], case_insensitive=True)
    if choice.upper() == "X":
        graceful_exit("Exiting test script...", 0)
    
    menu_tracker.pop()
    return main_menu()

def test_input_utilities():
    """Test input validation and handling functions"""
    clear_screen()
    menu_tracker.push("Input Utilities Test")
    
    print(ASCII_ART)
    print(create_border(NAV_BORDER_CHAR))
    print(menu_tracker.display())
    print(create_border(NAV_BORDER_CHAR))
    
    print("\n1. Testing basic input with validation")
    print("---------------------------------")
    choice = get_input("Enter a number between 1 and 5: ", 
                      valid_options=["1", "2", "3", "4", "5"],
                      error_message="Invalid input. Please enter a number between 1 and 5.")
    print(format_success(f"You entered: {choice}"))
    
    print("\n2. Testing confirmed actions")
    print("-------------------------")
    confirmed = confirm_action("Do you want to simulate a dangerous action?")
    if confirmed:
        show_progress("Simulating action", 1.5)
        print(format_success("Action completed successfully"))
    else:
        print(format_error_message("Action cancelled"))
    
    print("\n3. Testing case-insensitive input")
    print("-----------------------------")
    choice = get_input("Enter 'YES' or 'NO' (case insensitive): ", 
                      valid_options=["YES", "NO"],
                      case_insensitive=True,
                      error_message="Please enter either 'YES' or 'NO'.")
    print(format_success(f"You entered: {choice}"))
    
    print("\n4. Testing input with default value")
    print("-------------------------------")
    choice = get_input("Enter your name (default: 'User'): ",
                      default="User")
    print(format_success(f"Hello, {choice}!"))
    
    choice = get_input("\nPress 'B' to go back or 'X' to exit: ", ["B", "X"], case_insensitive=True)
    if choice.upper() == "X":
        graceful_exit("Exiting test script...", 0)
    
    menu_tracker.pop()
    return main_menu()

def test_error_handling():
    """Test error handling and logging functionality"""
    clear_screen()
    menu_tracker.push("Error Handling Test")
    
    print(ASCII_ART)
    print(create_border(NAV_BORDER_CHAR))
    print(menu_tracker.display())
    print(create_border(NAV_BORDER_CHAR))
    
    print("\n1. Testing basic error display")
    print("--------------------------")
    show_error("This is a test error message")
    
    print("\n2. Testing exception handling")
    print("--------------------------")
    try:
        # Intentionally cause an error
        print("Dividing by zero...")
        result = 1 / 0
    except Exception as e:
        logger.error(f"Caught exception: {str(e)}")
        show_error(f"Caught exception: {str(e)}")
    
    print("\n3. Testing AppError custom exceptions")
    print("---------------------------------")
    try:
        # Simulate a custom error
        print("Raising AppError...")
        raise AppError("This is a custom application error")
    except AppError as e:
        logger.error(f"Caught AppError: {str(e)}")
        show_error(f"Caught AppError: {str(e)}")
    
    print("\n4. Testing error message formatting")
    print("-------------------------------")
    error_message = format_error_message("Cannot access required file")
    print(error_message)
    
    choice = get_input("\nPress 'B' to go back or 'X' to exit: ", ["B", "X"], case_insensitive=True)
    if choice.upper() == "X":
        graceful_exit("Exiting test script...", 0)
    
    menu_tracker.pop()
    return main_menu()

def test_root_check():
    """Test the root check functionality"""
    clear_screen()
    menu_tracker.push("Root Check Test")
    
    print(ASCII_ART)
    print(create_border(NAV_BORDER_CHAR))
    print(menu_tracker.display())
    print(create_border(NAV_BORDER_CHAR))
    
    print("\n1. Simulating root check")
    print("---------------------")
    print("This will simulate both a successful and failed root check.")
    
    # Test successful root check
    print("\nSimulating successful root check (user is root):")
    
    try:
        # Mock the os.geteuid function temporarily to simulate root access
        original_geteuid = os.geteuid
        os.geteuid = lambda: 0
        
        result = check_root()
        print(format_success("Root check passed: User appears to be root"))
        
        # Restore the original function
        os.geteuid = original_geteuid
    except Exception as e:
        logger.error(f"Error during root check test: {str(e)}")
        show_error(f"Error during root check test: {str(e)}")
    
    # Test failed root check
    print("\nSimulating failed root check (user is not root):")
    
    try:
        # Mock the os.geteuid function temporarily to simulate non-root access
        original_geteuid = os.geteuid
        os.geteuid = lambda: 1000
        
        result = check_root()
        print(format_error_message("This should not be displayed because check_root should exit"))
        
        # Restore the original function
        os.geteuid = original_geteuid
    except SystemExit:
        print(format_success("Root check correctly attempted to exit when not root"))
    except Exception as e:
        logger.error(f"Unexpected error during root check test: {str(e)}")
        show_error(f"Unexpected error during root check test: {str(e)}")
    finally:
        # Make sure we restore the original function even if there's an error
        os.geteuid = original_geteuid
    
    choice = get_input("\nPress 'B' to go back or 'X' to exit: ", ["B", "X"], case_insensitive=True)
    if choice.upper() == "X":
        graceful_exit("Exiting test script...", 0)
    
    menu_tracker.pop()
    return main_menu()

def test_logging():
    """Test the logging functionality"""
    clear_screen()
    menu_tracker.push("Logging Test")
    
    print(ASCII_ART)
    print(create_border(NAV_BORDER_CHAR))
    print(menu_tracker.display())
    print(create_border(NAV_BORDER_CHAR))
    
    print("\n1. Testing logging at different levels")
    print("---------------------------------")
    
    logger.debug("This is a DEBUG level test message")
    print(format_success("Debug message logged"))
    
    logger.info("This is an INFO level test message")
    print(format_success("Info message logged"))
    
    logger.warning("This is a WARNING level test message")
    print(format_success("Warning message logged"))
    
    logger.error("This is an ERROR level test message")
    print(format_success("Error message logged"))
    
    logger.critical("This is a CRITICAL level test message")
    print(format_success("Critical message logged"))
    
    print("\n2. Testing exception logging")
    print("------------------------")
    try:
        # Cause an exception
        x = 1 / 0
    except Exception as e:
        logger.exception("Exception occurred during division")
        print(format_success("Exception logged with traceback"))
    
    print("\n3. Log file location")
    print("----------------")
    log_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'logs')
    print(f"Logs are being stored in: {log_dir}")
    
    if os.path.exists(log_dir):
        log_files = [f for f in os.listdir(log_dir) if f.endswith('.log')]
        if log_files:
            print(format_success(f"Found {len(log_files)} log file(s):"))
            for log_file in log_files:
                print(f" - {log_file}")
        else:
            print(format_error_message("No log files found in the log directory"))
    else:
        print(format_error_message(f"Log directory {log_dir} does not exist"))
    
    choice = get_input("\nPress 'B' to go back or 'X' to exit: ", ["B", "X"], case_insensitive=True)
    if choice.upper() == "X":
        graceful_exit("Exiting test script...", 0)
    
    menu_tracker.pop()
    return main_menu()

def main_menu():
    """Display the main test menu and handle user input"""
    clear_screen()
    menu_tracker.reset()
    menu_tracker.push("Test Menu")
    
    print(ASCII_ART)
    print(create_border(NAV_BORDER_CHAR))
    print(menu_tracker.display())
    print(create_border(NAV_BORDER_CHAR))
    
    print("\nPterodactyl-Pelican-Wireguard-Manager Test Script")
    print("===============================================")
    print("\nSelect a test to run:")
    print("1. Display Utilities")
    print("2. Navigation Tracker")
    print("3. Input Utilities")
    print("4. Error Handling")
    print("5. Root Check")
    print("6. Logging")
    print("X. Exit")
    
    choice = get_input("\nEnter your choice: ", ["1", "2", "3", "4", "5", "6", "X"], case_insensitive=True)
    
    if choice == "1":
        return test_display_utilities()
    elif choice == "2":
        return test_navigation_tracker()
    elif choice == "3":
        return test_input_utilities()
    elif choice == "4":
        return test_error_handling()
    elif choice == "5":
        return test_root_check()
    elif choice == "6":
        return test_logging()
    elif choice.upper() == "X":
        graceful_exit("Exiting test script...", 0)
    else:
        show_error("Invalid selection")
        return main_menu()

if __name__ == "__main__":
    # Disable root check for testing purposes
    # check_root()  # Uncomment to enforce root check in tests
    
    try:
        main_menu()
    except KeyboardInterrupt:
        logger.info("KeyboardInterrupt received")
        graceful_exit("\nTest script terminated by user", 0)
    except AppError as e:
        logger.error(f"Application error: {str(e)}")
        show_error(f"Application error: {str(e)}")
        sys.exit(1)
    except Exception as e:
        logger.exception("Unhandled exception")
        show_error(f"Unhandled exception: {str(e)}")
        sys.exit(1)
