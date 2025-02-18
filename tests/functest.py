import os
import sys
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
    show_progress
)
from general_utils import get_input, confirm_action, MenuExecutionError
from main_menu import graceful_exit

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

def main():
    """Main test execution function"""
    try:
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
                ("5", "ASCII Styles", "Compare ASCII art border styles"),
                ("x", "Exit", "Exit test script")
            ]
            
            choice = get_input("Select Test Suite", choices=main_options)
            
            if choice.lower() == "x":
                if confirm_action("Are you sure you want to exit testing?"):
                    break
                continue
                
            try:
                if choice == "1":
                    test_utils_features()
                elif choice == "2":
                    test_display_features()
                elif choice == "3":
                    test_menu_system()
                elif choice == "4":
                    test_history_bar()
                elif choice == "5":
                    test_ascii_art_styles()
                    
            except MenuExecutionError as e:
                display_error(str(e))
                if not confirm_action("Continue testing?"):
                    break
                    
    except Exception as e:
        display_error(f"Fatal error in test script: {str(e)}")
        graceful_exit("Test script terminated due to error", 1)
        
    graceful_exit("Test script completed", 0)

if __name__ == "__main__":
    main()
