from colorama import Fore, Style

# ========== Custom Exceptions ==========
class InputValidationError(Exception):
    """Raised when input validation fails"""
    pass

class MenuExecutionError(Exception):
    """Raised when a menu action fails to execute"""
    pass

# ========== Input Handling Functions ==========
def handle_interrupt():
    """Handle Ctrl+C interrupt with clean exit"""
    print()  # Add newline after ^C
    from disp_utils import graceful_exit
    graceful_exit("Received interrupt signal, shutting down...", 0)

def get_input(prompt, default=None, validator=None, choices=None, required=False):
    """Get user input with optional validation and choice selection"""
    try:
        print(f"\n{Fore.LIGHTYELLOW_EX}{prompt}{Style.RESET_ALL}")
        
        # Display available choices if provided
        if choices:
            print("\nAvailable options:")
            for choice in choices:
                if isinstance(choice, tuple):
                    if len(choice) == 3:
                        # Display choice with explanation
                        number, description, explanation = choice
                        print(f"  {Style.DIM}{Fore.LIGHTWHITE_EX}•{Style.RESET_ALL} {Fore.LIGHTCYAN_EX}({number}){Style.RESET_ALL} {Fore.LIGHTWHITE_EX}{description}")
                        print(f"      {Style.DIM}{explanation}{Style.RESET_ALL}")
                    else:
                        # Display choice without explanation
                        number, description = choice
                        print(f"  {Style.DIM}{Fore.LIGHTWHITE_EX}•{Style.RESET_ALL} {Fore.LIGHTCYAN_EX}({number}){Style.RESET_ALL} {Fore.LIGHTWHITE_EX}{description}")
                else:
                    # Display simple choice
                    print(f"  {Style.DIM}{Fore.LIGHTWHITE_EX}•{Style.RESET_ALL} {Fore.LIGHTWHITE_EX}{choice}")
            print()

        # Show default value if provided
        if default is not None:
            print(f"{Fore.LIGHTWHITE_EX}(Default: {Fore.LIGHTBLUE_EX}{default}{Fore.LIGHTWHITE_EX}){Style.RESET_ALL}")
        
        # Prepare input prompt
        prompt_text = f"{Fore.LIGHTWHITE_EX}Your Entry: {Fore.LIGHTCYAN_EX}▸ {Style.RESET_ALL}"

        # Input loop
        while True:
            # Get and display user input
            user_input = input(prompt_text).strip()
            print(f"\033[F\033[K{prompt_text}{Style.BRIGHT}{Fore.LIGHTWHITE_EX}{user_input}{Style.RESET_ALL}")

            # Handle empty input
            if not user_input:
                if default is not None:
                    print(f"{Fore.LIGHTGREEN_EX}✓ {Fore.LIGHTBLUE_EX}Default option {Style.BRIGHT}{Fore.LIGHTWHITE_EX}{default}{Style.RESET_ALL} {Fore.LIGHTBLUE_EX}used{Style.RESET_ALL}")
                    return default
                if required:
                    print(f"{Fore.LIGHTYELLOW_EX}⚠ {Fore.LIGHTRED_EX}This field is required.{Style.RESET_ALL}")
                    continue

            # Validate against choices
            if choices and user_input not in [c[0] if isinstance(c, tuple) else c for c in choices]:
                print(f"{Fore.LIGHTYELLOW_EX}⚠ {Fore.LIGHTRED_EX}Invalid choice. Please select one of the options above.{Style.RESET_ALL}")
                continue

            # Run custom validation
            if validator and not validator(user_input):
                print(f"{Fore.LIGHTYELLOW_EX}⚠ {Fore.LIGHTRED_EX}Invalid input. Please try again.{Style.RESET_ALL}")
                continue

            return user_input
    except KeyboardInterrupt:
        handle_interrupt()

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
        print(f"\n{Fore.LIGHTYELLOW_EX}Operation cancelled by user{Style.RESET_ALL}")
        return False