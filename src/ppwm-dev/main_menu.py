from colorama import init
from disp_utils import (
    center_text, ASCII_ART, HistoryBar, 
    display_history, clear_screen, graceful_exit, display_error
)
from general_utils import get_input, confirm_action, MenuExecutionError

# Initialize colorama
init()

# ========== Menu Display Functions ==========
def main_menu():
    """Display the main menu interface and get user selection"""
    # Clear screen and show ASCII art
    clear_screen()
    centered_ascii_art = "\n".join(center_text(line) for line in ASCII_ART.strip().split("\n"))
    print(centered_ascii_art + "\n")  # Added newline back
    
    # Display history navigation
    display_history()
    
    # Define menu options
    menu_options = [
        ("1", "Feature 1", "First feature placeholder"),
        ("2", "Feature 2", "Second feature placeholder"),
        ("x", "Exit", "Exit the application")
    ]
    
    return get_input(
        "Please select an option",
        choices=menu_options
    )

# ========== Menu Action Functions ==========
def run_menu_function(func):
    """Execute menu function with error handling"""
    try:
        func()
    except Exception as e:
        raise MenuExecutionError(f"Error in menu execution: {str(e)}")

# ========== Feature Implementations ==========
def test_feature_1():
    """Placeholder implementation for Feature 1"""
    HistoryBar().push("Feature 1")
    print("\nFeature 1 placeholder")
    input("\nPress Enter to continue...")
    HistoryBar().pop()

def test_feature_2():
    """Placeholder implementation for Feature 2"""
    HistoryBar().push("Feature 2")
    print("\nFeature 2 placeholder")
    input("\nPress Enter to continue...")
    HistoryBar().pop()

# ========== Main Application Loop ==========
def main():
    """Main application entry point and loop"""
    try:
        menu_actions = {
            "1": test_feature_1,
            "2": test_feature_2
        }

        while True:
            choice = main_menu()  # Will handle Ctrl+C through get_input
            if choice.lower() == "x":
                if confirm_action("Are you sure you want to exit?"):
                    break
            
            if choice in menu_actions:
                run_menu_function(menu_actions[choice])
                
    except MenuExecutionError as e:
        display_error(str(e))
        if not confirm_action("Would you like to return to the main menu?"):
            graceful_exit("Exiting due to error", 1)

    except Exception as e:
        display_error(f"Fatal error: {str(e)}")
        graceful_exit("Application terminated due to fatal error", 1)

# ========== Application Entry Point ==========
if __name__ == "__main__":
    main()