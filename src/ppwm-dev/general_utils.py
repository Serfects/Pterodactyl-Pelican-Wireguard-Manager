
from colorama import Fore, Style, Back
from typing import Optional, Union, List, Tuple, Callable, Any, NoReturn
import os
from display_utils import center_text, create_border  # Added for status bar formatting

# Custom exceptions for better error handling and classification
# These help distinguish between different types of errors that can occur
# during input validation and menu execution
class InputValidationError(Exception):
    """Custom exception for input validation errors."""
    pass

class MenuExecutionError(Exception):
    """Custom exception for menu execution errors."""
    pass

# Add new exception for status bar related errors
class StatusBarError(Exception):
    """Custom exception for status bar display errors."""
    pass

# Type definitions for improved code clarity and IDE support
# These types help define the structure of choices that can be passed to get_input:
# - Simple strings: ["option1", "option2"]
# - Tuples with description: [("1", "Option One")]
# - Tuples with description and explanation: [("1", "Option One", "Details")]
ChoiceType = Union[str, Tuple[str, str], Tuple[str, str, str]]
ValidatorType = Callable[[str], bool]
ChoicesType = Optional[List[ChoiceType]]

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

def display_status_bar(path: str, max_length: int = 70) -> None:
    """Display the status bar with the current menu path, truncated if necessary.
    
    Args:
        path (str): The complete navigation path to display.
        max_length (int, optional): Maximum allowed characters before truncation.
            Defaults to 70 characters.
    
    Raises:
        StatusBarError: If the path is empty or contains invalid characters.
        ValueError: If max_length is less than 10 characters (minimum reasonable width).
    """
    if not path:
        raise StatusBarError("Status bar path cannot be empty")
    if max_length < 10:
        raise ValueError("Status bar max_length must be at least 10 characters")

    # Truncate the status path if it is too long to maintain a single line display
    if len(path) > max_length:
        path = "..." + path[-(max_length - 3):]
    status_bar = f"{Fore.LIGHTWHITE_EX}[ {Fore.LIGHTCYAN_EX}{path}{Fore.LIGHTWHITE_EX} ]{Style.RESET_ALL}"
    # Use center_text from displayutil to center the status bar within the terminal width
    print(center_text(status_bar))
    # Print a border below the status bar for visual separation
    print(create_border())

def clear_screen(path: str = "Main Menu") -> None:
    """Clear the terminal screen, display ASCII art, and show status bar."""
    try:
        os.system('clear')  # Linux clear command
        print(ASCII_ART)
        display_status_bar(path)
    except OSError as e:
        raise OSError(f"Failed to clear screen: {str(e)}")  # If 'clear' command fails
    except Exception as e:
        raise StatusBarError(f"Failed to display status bar: {str(e)}")  # Other errors

def get_input(
    prompt: str,
    default: Optional[str] = None,
    validator: Optional[ValidatorType] = None,
    choices: ChoicesType = None,
    required: bool = False
) -> str:
    """
    Enhanced input function with formatted display options and standardized prompting.
    
    Args:
        prompt (str): The main prompt text to display to the user
        default (Optional[str]): Default value if user provides no input
        validator (Optional[Callable[[str], bool]]): Function to validate user input
        choices (Optional[List[Union[str, Tuple[str, str], Tuple[str, str, str]]]]): 
            Available choices in formats:
            - Simple string list ["option1", "option2"]
            - Numbered with description [("1", "Option One")]
            - Numbered with description and explanation [("1", "Option One", "Details")]
        required (bool): Whether empty input is allowed

    Returns:
        str: The validated user input or default value

    Raises:
        InputValidationError: If validation fails and retry is not possible
        KeyboardInterrupt: If user interrupts input (Ctrl+C)
    
    Note:
        This function clears the screen (thus printing the ASCII art and status bar)
        then prints the prompt and available choices. It uses ANSI escape codes to rewrite
        the prompt line with the input for a single-line experience.
    """
    # Clear the screen before displaying the prompt (this also reprints the status bar)
    clear_screen()
    
    # Display Section:
    # The prompt is shown in yellow without bold to be visible but not overwhelming
    # This creates a clear visual hierarchy where the prompt stands out but doesn't dominate
    print(f"\n{Fore.YELLOW}{prompt}{Style.RESET_ALL}")
    
    # Choice Display Logic:
    # If choices are provided, they're displayed in a structured list format
    # - Bullets (•) are dim white to provide subtle separation
    # - Numbers are bright cyan to stand out as interactive elements
    # - Descriptions are white for good readability
    # - Additional explanations are dim gray to provide context without distraction
    if choices:
        print("\nAvailable options:")
        for choice in choices:
            if isinstance(choice, tuple):
                if len(choice) == 3:  # number, description, and explanation
                    number, description, explanation = choice
                    print(f"  {Style.DIM}{Fore.WHITE}•{Style.RESET_ALL} {Fore.LIGHTCYAN_EX}({number}){Style.RESET_ALL} {Fore.WHITE}{description}")
                    print(f"      {Style.DIM}{explanation}{Style.RESET_ALL}")  # Gray explanation
                else:  # just number and description
                    number, description = choice
                    print(f"  {Style.DIM}{Fore.WHITE}•{Style.RESET_ALL} {Fore.LIGHTCYAN_EX}({number}){Style.RESET_ALL} {Fore.WHITE}{description}")
            else:
                print(f"  {Style.DIM}{Fore.WHITE}•{Style.RESET_ALL} {Fore.WHITE}{choice}")
        print()

    # Input Prompt Formatting:
    # Two different prompt styles based on whether a default value exists
    # - Default value prompts show the default in bright blue
    # - Both styles use a cyan arrow (▸) to indicate input location
    # - "Your Entry:" text maintains consistency across both styles
    if default is not None:
        print(f"{Fore.WHITE}(Default: {Fore.LIGHTBLUE_EX}{default}{Fore.WHITE}){Style.RESET_ALL}")
        prompt_text = f"{Fore.WHITE}Your Entry: {Fore.LIGHTCYAN_EX}▸ {Style.RESET_ALL}"
    else:
        prompt_text = f"{Fore.WHITE}Your Entry: {Fore.LIGHTCYAN_EX}▸ {Style.RESET_ALL}"

    # Input Processing Loop:
    # Continuously process input until valid entry is received
    # - Shows user input in bright white for visibility
    # - Uses ANSI codes to create a clean, single-line input experience
    # - Handles empty input with default values or required field validation
    while True:
        user_input = input(prompt_text).strip()
        
        # Show user input in place with bright white text
        print(f"\033[F\033[K{prompt_text}{Style.BRIGHT}{Fore.WHITE}{user_input}{Style.RESET_ALL}")

        # Validation Section:
        # Three levels of validation:
        # 1. Empty input handling (defaults and required fields)
        # 2. Choice validation (if choices are provided)
        # 3. Custom validation (if validator function is provided)
        # Each validation failure shows appropriate error message in red with warning symbol
        # Handle empty input
        if not user_input:
            if default is not None:
                print(f"{Fore.LIGHTGREEN_EX}✓ {Fore.LIGHTBLUE_EX}Default option {Style.BRIGHT}{Fore.WHITE}{default}{Style.RESET_ALL} {Fore.LIGHTBLUE_EX}used{Style.RESET_ALL}")
                return default
            if required:
                print(f"{Fore.YELLOW}⚠ {Fore.LIGHTRED_EX}This field is required.{Style.RESET_ALL}")
                continue

        # Validate choices quietly unless there's an error
        if choices and user_input not in [c[0] if isinstance(c, tuple) else c for c in choices]:
            print(f"{Fore.YELLOW}⚠ {Fore.LIGHTRED_EX}Invalid choice. Please select one of the options above.{Style.RESET_ALL}")
            continue

        # Custom validation quietly unless there's an error
        if validator and not validator(user_input):
            print(f"{Fore.YELLOW}⚠ {Fore.LIGHTRED_EX}Invalid input. Please try again.{Style.RESET_ALL}")
            continue

        return user_input

# Confirmation Function:
# Specialized input handler for yes/no questions
# - Uses custom validator for yes/no/y/n inputs
# - Handles interrupts gracefully
# - Returns boolean for easy conditional handling
def confirm_action(prompt: str) -> bool:
    """
    Get yes/no confirmation from user with standardized formatting.

    Args:
        prompt (str): The confirmation message to display

    Returns:
        bool: True for yes/y, False for no/n

    Raises:
        KeyboardInterrupt: If user interrupts input (Ctrl+C)
    """
    # Clear the screen before displaying the prompt
    clear_screen()
    
    def yes_no_validator(value: str) -> bool:
        return value.lower() in ['yes', 'no', 'y', 'n']
    
    try:
        response = get_input(f"{prompt} {Fore.LIGHTCYAN_EX}(yes/no){Style.RESET_ALL}", 
                           validator=yes_no_validator)
        return response.lower() in ['yes', 'y']
    except KeyboardInterrupt:
        print(f"\n{Fore.YELLOW}Operation cancelled by user{Style.RESET_ALL}")
        return False