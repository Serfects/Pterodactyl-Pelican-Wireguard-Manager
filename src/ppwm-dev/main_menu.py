import os
import sys
import logging
from colorama import init
from disp_utils import (
    center_text, ASCII_ART, HistoryBar, 
    display_history, clear_screen, graceful_exit,
    display_error, format_error
)
from general_utils import (
    get_input, confirm_action, MenuExecutionError, check_root,
    add_navigation_options, process_menu_choice  # Added missing imports
)

# Initialize logger for this module
logger = logging.getLogger(__name__)

# Initialize colorama
init()

# ========== Menu Display Functions ==========
def main_menu():
    """Display the main menu interface and get user selection"""
    logger.debug("Initializing main menu display")
    clear_screen()
    
    # Display ASCII art
    centered_ascii_art = "\n".join(center_text(line) for line in ASCII_ART.strip().split("\n"))
    print(centered_ascii_art + "\n")
    logger.debug("ASCII art displayed")
    
    # Display history navigation
    display_history()
    logger.debug("History bar displayed")
    
    # Define menu options (removed VPS Setup Wizard)
    menu_options = [
        ("1", "Feature 1", "First feature placeholder"),
        ("2", "Feature 2", "Second feature placeholder")
    ]
    
    # Add navigation options (back/exit)
    menu_options = add_navigation_options(menu_options)
    logger.debug("Menu options prepared")
    
    return get_input(
        "Please select an option",
        choices=menu_options
    )

# ========== Menu Action Functions ==========
def run_menu_function(func):
    """Execute menu function with error handling"""
    logger.info(f"Executing menu function: {func.__name__}")
    try:
        func()
    except Exception as e:
        logger.error(f"Error in menu function {func.__name__}: {str(e)}", exc_info=True)
        display_error(f"Failed to execute {func.__name__}: {str(e)}")
        raise MenuExecutionError(f"Error in menu execution: {str(e)}")

# ========== Feature Implementations ==========
def test_feature_1():
    """Placeholder implementation for Feature 1"""
    logger.debug("Entering Feature 1")
    HistoryBar().push("Feature 1")
    print("\nFeature 1 placeholder")
    input("\nPress Enter to continue...")
    HistoryBar().pop()
    logger.debug("Exiting Feature 1")

def test_feature_2():
    """Placeholder implementation for Feature 2"""
    logger.debug("Entering Feature 2")
    HistoryBar().push("Feature 2")
    print("\nFeature 2 placeholder")
    input("\nPress Enter to continue...")
    HistoryBar().pop()
    logger.debug("Exiting Feature 2")

# ========== Main Application Loop ==========
def main():
    """Main application entry point and loop"""
    logger.info("Application initialization started")
    try:
        menu_actions = {
            "1": test_feature_1,
            "2": test_feature_2
        }
        logger.debug("Menu actions configured")

        while True:
            choice = main_menu()
            logger.info(f"Menu selection: {choice}")
            
            should_exit, was_handled = process_menu_choice(choice, menu_actions)
            
            if should_exit:
                break
            elif was_handled and choice in menu_actions:
                logger.debug(f"Executing menu action for choice: {choice}")
                run_menu_function(menu_actions[choice])
            else:
                logger.warning(f"Invalid menu selection: {choice}")
                
    except MenuExecutionError as e:
        logger.error(f"Menu execution error: {str(e)}")
        display_error(f"Menu operation failed: {str(e)}")
        if not confirm_action("Would you like to return to the main menu?"):
            logger.info("User chose to exit after error")
            graceful_exit("Exiting due to error", 1)
        logger.info("User chose to continue after error")

    except KeyboardInterrupt:
        logger.info("Application interrupted by user")
        display_error("Operation cancelled by user")
        graceful_exit("Application terminated by user", 1)

    except Exception as e:
        logger.critical(f"Fatal error occurred: {str(e)}", exc_info=True)
        display_error(f"Critical error: {str(e)}")
        graceful_exit("Application terminated due to fatal error", 1)

    logger.info("Application shutdown initiated")

# ========== Application Entry Point ==========
if __name__ == "__main__":
    check_root()  # Using the centralized root check from general_utils
    main()