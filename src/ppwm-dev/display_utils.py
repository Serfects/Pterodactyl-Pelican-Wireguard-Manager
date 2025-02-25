"""
Display utilities for the PPWM application.

This module contains utilities for formatting text, creating user interface elements,
and displaying information to the user. It handles all display-related operations
including text formatting, screen clearing, borders, and ASCII art.

Module Dependencies:
- base_utils.py: For logging and basic error handling
- navigation.py: For menu navigation and border constants

This module should be imported after base_utils.py and navigation.py.
"""
import re
import logging
import time
import sys
import os
from colorama import Style, Fore
from base_utils import AppError, SCREEN_WIDTH
from navigation import MenuNavigationTracker, NAV_BORDER_CHAR

# Initialize logger for this module
logger = logging.getLogger(__name__)

# ========== ANSI Escape Code Patterns ==========
ANSI_ESCAPE = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')

# ========== Custom Exceptions ==========
class DisplayError(AppError):
    """Exception raised for display-related errors"""
    pass

# ========== ANSI and Text Formatting Utilities ==========
def strip_ansi(text):
    """
    Remove ANSI escape codes from text for accurate length calculations.
    
    Args:
        text (str): Text containing ANSI escape sequences
        
    Returns:
        str: Text with ANSI escape sequences removed
    """
    return ANSI_ESCAPE.sub('', text)

def split_formatting(text):
    """
    Split text into formatted parts: prefix formatting, main content, and suffix formatting.
    
    Args:
        text (str): Formatted text string
        
    Returns:
        tuple: (prefix_formatting, content, suffix_formatting)
    """
    parts = text.split(Style.RESET_ALL)
    if len(parts) != 2:
        return '', text, ''
    return parts[0], parts[1].strip(), Style.RESET_ALL

def format_error_message(text):
    """
    Add warning symbol and red coloring to error message.
    
    Args:
        text (str): Error message text
        
    Returns:
        str: Formatted error message
    """
    logger.error(text)  # Log error messages when they're formatted
    return f"{Fore.YELLOW}⚠ {Fore.LIGHTRED_EX}{text}{Style.RESET_ALL}"

def format_success(text):
    """
    Add checkmark and green coloring to success message.
    
    Args:
        text (str): Success message text
        
    Returns:
        str: Formatted success message
    """
    logger.info(text)  # Log success messages
    return f"{Fore.LIGHTGREEN_EX}✓ {text}{Style.RESET_ALL}"

# ========== Display Layout Functions ==========
def clear_screen():
    """Clear the terminal screen"""
    logger.debug("Clearing screen")
    os.system('clear' if os.name == 'posix' else 'cls')

def center_text(text, width=None, fill_char=" "):
    """
    Center the given text in available space, accounting for ANSI formatting and truncation.
    
    Args:
        text (str): Text to center
        width (int, optional): Width to center within. Defaults to SCREEN_WIDTH.
        fill_char (str, optional): Character to use for padding. Defaults to space.
        
    Returns:
        str: Centered text string
        
    Raises:
        DisplayError: If fill_char is empty or width is negative
    """
    logger.debug(f"Centering text (width={width}, fill_char='{fill_char}')")
    if not fill_char:
        logger.error("Empty fill character provided")
        raise DisplayError("Fill character cannot be empty")
        
    actual_width = width if width is not None else SCREEN_WIDTH
    if actual_width < 0:
        logger.error(f"Invalid width provided: {actual_width}")
        raise DisplayError("Width cannot be negative")
        
    stripped_text = strip_ansi(text)
    
    # Handle text that's too long by truncating
    if len(stripped_text) > actual_width:
        logger.debug(f"Truncating text: '{stripped_text}' to fit width {actual_width}")
        # Calculate how much text we can keep plus ellipsis
        keep_length = actual_width - 3  # Space for "..."
        
        # Find the ANSI formatting prefix and suffix
        prefix, content, suffix = split_formatting(text)
        
        # Create truncated text with original formatting
        truncated_text = prefix + content[:keep_length] + "..." + suffix
        stripped_text = strip_ansi(truncated_text)
        text = truncated_text
        
    # Center the text (truncated or original)
    padding = (actual_width - len(stripped_text)) // 2
    return (fill_char * padding) + text + (fill_char * (actual_width - len(stripped_text) - padding))

def create_border(char=None, width=None):
    """
    Create a horizontal border using specified character.
    
    Args:
        char (str, optional): Character to use for border. Defaults to NAV_BORDER_CHAR.
        width (int, optional): Width of border. Defaults to SCREEN_WIDTH.
        
    Returns:
        str: Border string
        
    Raises:
        DisplayError: If char is empty or whitespace, or width is negative
    """
    if not char:
        char = NAV_BORDER_CHAR
    if not char.strip():
        logger.error("Empty border character provided")
        raise DisplayError("Border character cannot be empty or whitespace")
        
    actual_width = width if width is not None else SCREEN_WIDTH
    if actual_width < 0:
        logger.error(f"Invalid border width: {actual_width}")
        raise DisplayError("Width cannot be negative")
        
    return char * actual_width

def graceful_exit(message="", exit_code=0):
    """
    Display exit message and terminate application gracefully.
    
    Args:
        message (str, optional): Exit message to display. Defaults to empty string.
        exit_code (int, optional): System exit code. Defaults to 0.
    """
    if exit_code != 0:
        logger.warning(f"Application exiting with non-zero status code: {exit_code}")
    else:
        logger.info("Application exiting normally")
    
    if message:
        logger.info(f"Exit message: {message}")
        print(center_text(f"\n{Fore.YELLOW}{message}{Style.RESET_ALL}"))
    print(center_text(f"\n{Fore.YELLOW}Thank you for using WireGuard Management{Style.RESET_ALL}"))
    print(create_border(NAV_BORDER_CHAR))
    sys.exit(exit_code)

def show_error(message):
    """
    Display error message with consistent formatting.
    
    Args:
        message (str): Error message to display
    """
    logger.error(message)
    print(f"\n{Fore.YELLOW}⚠ {Fore.LIGHTRED_EX}{message}{Style.RESET_ALL}")

# ========== Progress Indicator ==========
def show_progress(message, duration=1.2):
    """
    Show animated progress dots with the given message.
    
    Args:
        message (str): Message to display with progress dots
        duration (float, optional): Duration in seconds. Defaults to 1.2.
        
    Raises:
        DisplayError: If duration is negative
    """
    logger.debug(f"Starting progress indicator: {message}")
    if duration < 0:
        logger.error(f"Invalid progress duration: {duration}")
        raise DisplayError("Progress duration must be non-negative")
        
    try:
        print(f"\n{Fore.LIGHTMAGENTA_EX}{message}...{Style.RESET_ALL}")
        dots = int(duration * 10)  # Calculate number of dots based on duration
        for _ in range(dots):
            sys.stdout.write(f"{Fore.LIGHTCYAN_EX}·{Style.RESET_ALL}")
            sys.stdout.flush()
            time.sleep(duration / dots)
        print(f"\n{Fore.LIGHTGREEN_EX}✓ {Fore.LIGHTGREEN_EX}Complete!{Style.RESET_ALL}")
        logger.debug("Progress indicator completed normally")
    except KeyboardInterrupt:
        logger.warning("Progress indicator interrupted by user")
        show_error("Operation cancelled by user")
        raise
    except Exception as e:
        logger.error(f"Error in progress indicator: {str(e)}")
        show_error(f"Progress indicator error: {str(e)}")
        raise

def display_history():
    """
    Display the current menu name centered in a 70-character wide field.
    It appears one line below the bottom border of the ASCII art.
    A bottom border consisting of the ─ character is printed below.
    """
    history = MenuNavigationTracker().get_history()
    print(center_text(history, width=70))
    print(f"{Fore.LIGHTWHITE_EX}{create_border(NAV_BORDER_CHAR, width=70)}{Style.RESET_ALL}")

# ========== ASCII Art ==========
ASCII_ART = f"""{Fore.LIGHTWHITE_EX}::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::{Style.BRIGHT}{Fore.LIGHTCYAN_EX}        ____      {Style.BRIGHT}{Fore.WHITE} ____  ______        ____  __ {Fore.LIGHTCYAN_EX}      ____        {Style.NORMAL}{Fore.LIGHTWHITE_EX}::
::{Style.BRIGHT}{Fore.LIGHTCYAN_EX}        \ \ \     {Style.BRIGHT}{Fore.WHITE}|  _ \|  _ \ \      / /  \/  |{Fore.LIGHTCYAN_EX}     / / /        {Style.NORMAL}{Fore.LIGHTWHITE_EX}::
::{Style.BRIGHT}{Fore.LIGHTCYAN_EX}         \ \ \    {Style.BRIGHT}{Fore.WHITE}| |_) | |_) \ \ /\ / /| |\/| |{Fore.LIGHTCYAN_EX}    / / /         {Style.NORMAL}{Fore.LIGHTWHITE_EX}::
::{Style.BRIGHT}{Fore.LIGHTCYAN_EX}         / / /    {Style.BRIGHT}{Fore.WHITE}|  __/|  __/ \ V  V / | |  | |{Fore.LIGHTCYAN_EX}    \ \ \         {Style.NORMAL}{Fore.LIGHTWHITE_EX}::
::{Style.BRIGHT}{Fore.LIGHTCYAN_EX}        /_/_/     {Style.BRIGHT}{Fore.WHITE}|_|   |_|     \_/\_/  |_|  |_|{Fore.LIGHTCYAN_EX}     \_\_\        {Style.NORMAL}{Fore.LIGHTWHITE_EX}::
::{Style.BRIGHT}{Fore.LIGHTCYAN_EX}                                                                  {Style.NORMAL}{Fore.LIGHTWHITE_EX}::
::{Fore.LIGHTCYAN_EX}               Pterodactyl-Pelican-Wireguard-Manager              {Style.NORMAL}{Fore.LIGHTWHITE_EX}::
::{Fore.LIGHTCYAN_EX}                           By: Serfects                           {Style.NORMAL}{Fore.LIGHTWHITE_EX}::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::{Style.RESET_ALL}"""

logger.debug("display_utils module loaded")
