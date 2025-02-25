"""
Input handling utilities for the PPWM application.

This module provides common utility functions used throughout the application,
including input handling, validation, and action confirmation. It contains
functions for getting user input, validating data, and handling common
interaction patterns.

Module Dependencies:
- base_utils.py: For logging and error base classes
- display_utils.py: For display formatting and error visualization 

This module should be imported after base_utils.py and display_utils.py.
"""
import logging
from colorama import Fore, Style
from base_utils import AppError
from display_utils import show_error, graceful_exit

# Initialize logger for this module
logger = logging.getLogger(__name__)

# ========== Custom Exceptions ==========
class InputValidationError(AppError):
    """Exception raised when input validation fails"""
    pass

class MenuExecutionError(AppError):
    """Exception raised when a menu action fails to execute"""
    pass

# ========== Input Handling Functions ==========
def handle_interrupt():
    """
    Handle Ctrl+C interrupt with clean exit.
    
    Provides a graceful shutdown when the user interrupts the application
    with Ctrl+C by displaying a message and exiting with success code.
    """
    print()  # Add newline after ^C
    graceful_exit("Received interrupt signal, shutting down...", 0)

def prompt_user(prompt, default=None, validator=None, choices=None, required=False):
    """
    Get user input with optional validation and choice selection.
    
    Presents a formatted prompt to the user, handles validation against
    available choices or custom validators, and supports default values.
    
    Args:
        prompt (str): The message to display to the user
        default (str, optional): Default value if user provides no input
        validator (function, optional): Custom validation function
        choices (list, optional): List of valid choices
        required (bool, optional): Whether empty input is allowed
        
    Returns:
        str: The validated user input or default value
        
    Raises:
        KeyboardInterrupt: If user cancels input with Ctrl+C
        Exception: For other input processing errors
    """
    logger.debug(f"Input prompt: '{prompt}', Default: {default}, Required: {required}")
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
            logger.debug(f"Received input: '{user_input}'")
            print(f"\033[F\033[K{prompt_text}{Style.BRIGHT}{Fore.LIGHTWHITE_EX}{user_input}{Style.RESET_ALL}")

            # Handle empty input
            if not user_input:
                if default is not None:
                    logger.debug(f"Using default value: {default}")
                    print(f"{Fore.LIGHTGREEN_EX}✓ {Fore.LIGHTBLUE_EX}Default option {Style.BRIGHT}{Fore.LIGHTWHITE_EX}{default}{Style.RESET_ALL} {Fore.LIGHTBLUE_EX}used{Style.RESET_ALL}")
                    return default
                if required:
                    logger.debug("Required field left empty")
                    show_error("This field cannot be empty")
                    continue

            # Validate against choices
            if choices and user_input not in [c[0] if isinstance(c, tuple) else c for c in choices]:
                logger.debug(f"Invalid choice entered: {user_input}")
                show_error("Invalid selection: Please choose from the available options")
                continue

            # Run custom validation
            if validator and not validator(user_input):
                logger.debug(f"Custom validation failed for input: {user_input}")
                show_error("Invalid input: Please check your entry and try again")
                continue

            logger.debug(f"Valid input received: {user_input}")
            return user_input
    except KeyboardInterrupt:
        logger.info("Input interrupted by user")
        handle_interrupt()
    except Exception as e:
        logger.error(f"Input error: {str(e)}")
        show_error(f"Input error: {str(e)}")
        raise

def prompt_confirmation(prompt):
    """
    Request yes/no confirmation from user.
    
    Asks the user a yes/no question and returns a boolean result.
    
    Args:
        prompt (str): The confirmation question to ask
        
    Returns:
        bool: True if user confirmed, False otherwise
    """
    logger.debug(f"Requesting confirmation: {prompt}")
    def yes_no_validator(value):
        """Validate yes/no input variations"""
        return value.lower() in ['yes', 'no', 'y', 'n']
    
    try:
        response = prompt_user(
            f"{prompt} {Fore.LIGHTCYAN_EX}(yes/no){Style.RESET_ALL}", 
            validator=yes_no_validator
        )
        result = response.lower() in ['yes', 'y']
        logger.debug(f"User confirmed: {result}")
        return result
    except KeyboardInterrupt:
        logger.info("User interrupted confirmation prompt")
        print(f"\n{Fore.LIGHTYELLOW_EX}Operation cancelled by user{Style.RESET_ALL}")
        return False

logger.debug("input_utils module loaded")
