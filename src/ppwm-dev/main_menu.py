import os
import sys
from colorama import init, Fore, Style
from disp_utils import center_text, create_border
from general_utils import get_input, confirm_action, show_progress, MenuExecutionError

init()

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

def main_menu():
    os.system('clear' if os.name == 'posix' else 'cls')
    centered_ascii_art = "\n".join(center_text(line) for line in ASCII_ART.strip().split("\n"))
    print(centered_ascii_art)
    
    print("\n" + create_border())
    print(center_text(f"{Fore.YELLOW}Main Menu{Style.RESET_ALL}"))
    print(create_border() + "\n")
    
    menu_options = [
        ("1", "Feature 1", "First feature placeholder"),
        ("2", "Feature 2", "Second feature placeholder"),
        ("x", "Exit", "Exit the application")
    ]
    
    return get_input(
        "Please select an option",
        choices=menu_options
    )

def run_menu_function(func, loading_message):
    try:
        func()
    except Exception as e:
        raise MenuExecutionError(f"Error in menu execution: {str(e)}")

def graceful_exit(message="", exit_code=0):
    if message:
        print(center_text(f"\n{Fore.YELLOW}{message}{Style.RESET_ALL}"))
    print(center_text(f"\n{Fore.YELLOW}Thank you for using WireGuard Management{Style.RESET_ALL}"))
    print(create_border())
    sys.exit(exit_code)

def test_feature_1():
    print("\nFeature 1 placeholder")
    input("\nPress Enter to continue...")

def test_feature_2():
    print("\nFeature 2 placeholder")
    input("\nPress Enter to continue...")

def main():
    try:
        menu_actions = {
            "1": (test_feature_1, "Loading feature 1"),
            "2": (test_feature_2, "Loading feature 2")
        }

        while True:
            try:
                choice = main_menu()
                if choice.lower() == "x":
                    if confirm_action("Are you sure you want to exit?"):
                        break
                
                if choice in menu_actions:
                    func, message = menu_actions[choice]
                    run_menu_function(func, message)
                    
            except MenuExecutionError as e:
                print(f"\n{Fore.YELLOW}⚠ {Fore.LIGHTRED_EX}{str(e)}{Style.RESET_ALL}")
                if not confirm_action("Would you like to return to the main menu?"):
                    graceful_exit("Exiting due to error", 1)
                    
            except KeyboardInterrupt:
                if confirm_action("\nDo you want to exit?"):
                    graceful_exit("Received interrupt signal, shutting down...", 0)
                print(f"\n{Fore.YELLOW}Returning to main menu...{Style.RESET_ALL}")

    except Exception as e:
        print(f"\n{Fore.YELLOW}⚠ {Fore.LIGHTRED_EX}Fatal error: {str(e)}{Style.RESET_ALL}")
        graceful_exit("Application terminated due to fatal error", 1)

if __name__ == "__main__":
    main()