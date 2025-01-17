from colorama import Fore, Style, Back
from typing import Optional, Union, List, Tuple, Callable, Any
import time
import sys

# Custom exceptions for better error handling and classification
# These help distinguish between different types of errors that can occur
# during input validation and menu execution
class InputValidationError(Exception):
    """Custom exception for input validation errors."""
    pass

class MenuExecutionError(Exception):
    """Custom exception for menu execution errors."""
    pass

# Type definitions for improved code clarity and IDE support
# These types help define the structure of choices that can be passed to get_input:
# - Simple strings: ["option1", "option2"]
# - Tuples with description: [("1", "Option One")]
# - Tuples with description and explanation: [("1", "Option One", "Details")]
ChoiceType = Union[str, Tuple[str, str], Tuple[str, str, str]]
ValidatorType = Callable[[str], bool]
ChoicesType = Optional[List[ChoiceType]]

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
    """
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
    def yes_no_validator(value: str) -> bool:
        return value.lower() in ['yes', 'no', 'y', 'n']
    
    try:
        response = get_input(f"{prompt} {Fore.LIGHTCYAN_EX}(yes/no){Style.RESET_ALL}", 
                           validator=yes_no_validator)
        return response.lower() in ['yes', 'y']
    except KeyboardInterrupt:
        print(f"\n{Fore.YELLOW}Operation cancelled by user{Style.RESET_ALL}")
        return False

# Progress Indicator:
# Visual feedback for operations that take time
# - Shows message in bright magenta for visibility
# - Displays cyan dots at regular intervals
# - Completes with green checkmark and message
# - Handles interrupts gracefully with cleanup
def show_progress(message: str, duration: Union[int, float]) -> None:
    """
    Show a simple progress indicator with formatted output.

    Args:
        message (str): The message to display during progress
        duration (Union[int, float]): Duration in seconds for the progress indication

    Raises:
        ValueError: If duration is negative
        KeyboardInterrupt: If user interrupts progress (Ctrl+C)
    """
    if duration < 0:
        raise ValueError("Duration must be non-negative")

    try:
        print(f"\n{Fore.LIGHTMAGENTA_EX}{message}...{Style.RESET_ALL}")
        dots = int(duration * 6)
        for _ in range(dots):
            sys.stdout.write(f"{Fore.LIGHTCYAN_EX}·{Style.RESET_ALL}")
            sys.stdout.flush()
            time.sleep(0.167)
        print(f"\n{Fore.LIGHTGREEN_EX}✓ {Fore.GREEN}Complete!{Style.RESET_ALL}")
    except KeyboardInterrupt:
        print(f"\n{Fore.YELLOW}Progress interrupted{Style.RESET_ALL}")
        raise