from colorama import Fore, Style
import time  # Not currently used in this module
import sys   # Only used for potential future error handling

# ========== Custom Exceptions ==========
class InputValidationError(Exception):
    """Raised when input validation fails"""
    pass

class MenuExecutionError(Exception):
    """Raised when a menu action fails to execute"""
    pass

# ========== Input Handling Functions ==========
def get_input(prompt, default=None, validator=None, choices=None, required=False):
    """Get user input with optional validation and choice selection"""
    print(f"\n{Fore.YELLOW}{prompt}{Style.RESET_ALL}")
    
    # Display available choices if provided
    if choices:
        print("\nAvailable options:")
        for choice in choices:
            if isinstance(choice, tuple):
                if len(choice) == 3:
                    # Display choice with explanation
                    number, description, explanation = choice
                    print(f"  {Style.DIM}{Fore.WHITE}•{Style.RESET_ALL} {Fore.LIGHTCYAN_EX}({number}){Style.RESET_ALL} {Fore.WHITE}{description}")
                    print(f"      {Style.DIM}{explanation}{Style.RESET_ALL}")
                else:
                    # Display choice without explanation
                    number, description = choice
                    print(f"  {Style.DIM}{Fore.WHITE}•{Style.RESET_ALL} {Fore.LIGHTCYAN_EX}({number}){Style.RESET_ALL} {Fore.WHITE}{description}")
            else:
                # Display simple choice
                print(f"  {Style.DIM}{Fore.WHITE}•{Style.RESET_ALL} {Fore.WHITE}{choice}")
        print()

    # Show default value if provided
    if default is not None:
        print(f"{Fore.WHITE}(Default: {Fore.LIGHTBLUE_EX}{default}{Fore.WHITE}){Style.RESET_ALL}")
    
    # Prepare input prompt
    prompt_text = f"{Fore.WHITE}Your Entry: {Fore.LIGHTCYAN_EX}▸ {Style.RESET_ALL}"

    # Input loop
    while True:
        # Get and display user input
        user_input = input(prompt_text).strip()
        print(f"\033[F\033[K{prompt_text}{Style.BRIGHT}{Fore.WHITE}{user_input}{Style.RESET_ALL}")

        # Handle empty input
        if not user_input:
            if default is not None:
                print(f"{Fore.LIGHTGREEN_EX}✓ {Fore.LIGHTBLUE_EX}Default option {Style.BRIGHT}{Fore.WHITE}{default}{Style.RESET_ALL} {Fore.LIGHTBLUE_EX}used{Style.RESET_ALL}")
                return default
            if required:
                print(f"{Fore.YELLOW}⚠ {Fore.LIGHTRED_EX}This field is required.{Style.RESET_ALL}")
                continue

        # Validate against choices
        if choices and user_input not in [c[0] if isinstance(c, tuple) else c for c in choices]:
            print(f"{Fore.YELLOW}⚠ {Fore.LIGHTRED_EX}Invalid choice. Please select one of the options above.{Style.RESET_ALL}")
            continue

        # Run custom validation
        if validator and not validator(user_input):
            print(f"{Fore.YELLOW}⚠ {Fore.LIGHTRED_EX}Invalid input. Please try again.{Style.RESET_ALL}")
            continue

        return user_input

def confirm_action(prompt):
    """Request yes/no confirmation from user"""
    def yes_no_validator(value):
        """Validate yes/no input variations"""
        return value.lower() in ['yes', 'no', 'y', 'n']
    
    try:
        response = get_input(
            f"{prompt} {Fore.LIGHTCYAN_EX}(yes/no){Style.RESET_ALL}", 
            validator=yes_no_validator
        )
        return response.lower() in ['yes', 'y']
    except KeyboardInterrupt:
        print(f"\n{Fore.YELLOW}Operation cancelled by user{Style.RESET_ALL}")
        return False