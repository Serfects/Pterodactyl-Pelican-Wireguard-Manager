# ========== Imports ==========
import re
import logging
from colorama import Style, Fore
import time, sys
import os

# Initialize logger for this module
logger = logging.getLogger(__name__)

# ========== General Constants ==========
SCREEN_WIDTH = 70
ANSI_ESCAPE = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')

# ========== Custom Exceptions ==========
class DisplayError(Exception):
    pass

# ========== ANSI and Text Formatting Utilities ==========
def strip_ansi(text):
    """Remove ANSI escape codes from text for accurate length calculations"""
    return ANSI_ESCAPE.sub('', text)

def split_formatting(text):
    """Split text into formatted parts: prefix formatting, main content, and suffix formatting"""
    parts = text.split(Style.RESET_ALL)
    if len(parts) != 2:
        return '', text, ''
    return parts[0], parts[1].strip(), Style.RESET_ALL

def format_error(text):
    """Add warning symbol and red coloring to error message"""
    logger.error(text)  # Log error messages when they're formatted
    return f"{Fore.YELLOW}⚠ {Fore.LIGHTRED_EX}{text}{Style.RESET_ALL}"

def format_success(text):
    """Add checkmark and green coloring to success message"""
    logger.info(text)  # Log success messages
    return f"{Fore.LIGHTGREEN_EX}✓ {text}{Style.RESET_ALL}"

# ========== Display Layout Functions ==========
def clear_screen():
    """Clear the terminal screen"""
    logger.debug("Clearing screen")
    os.system('clear' if os.name == 'posix' else 'cls')

def center_text(text, width=None, fill_char=" "):
    """Center the given text in available space, accounting for ANSI formatting and truncation"""
    logger.debug(f"Centering text (width={width}, fill_char='{fill_char}')")
    if not fill_char:
        logger.error("Empty fill character provided")
        display_error("Invalid formatting: Empty fill character")
        raise ValueError("Fill character cannot be empty")
    actual_width = width if width is not None else SCREEN_WIDTH
    if actual_width < 0:
        logger.error(f"Invalid width provided: {actual_width}")
        display_error("Invalid formatting: Negative width value")
        raise ValueError("Width cannot be negative")
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
    """Create a horizontal border using specified character"""
    if not char:
        char = HISTORYBAR_BORDER_CHAR
    if not char.strip():
        logger.error("Empty border character provided")
        display_error("Invalid formatting: Empty border character")
        raise ValueError("Border character cannot be empty or whitespace")
    actual_width = width if width is not None else SCREEN_WIDTH
    if actual_width < 0:
        logger.error(f"Invalid border width: {actual_width}")
        display_error("Invalid formatting: Negative border width")
        raise ValueError("Width cannot be negative")
    return char * actual_width

def graceful_exit(message="", exit_code=0):
    """Display exit message and terminate application gracefully"""
    if exit_code != 0:
        logger.warning(f"Application exiting with non-zero status code: {exit_code}")
    else:
        logger.info("Application exiting normally")
    
    if message:
        logger.info(f"Exit message: {message}")
        print(center_text(f"\n{Fore.YELLOW}{message}{Style.RESET_ALL}"))
    print(center_text(f"\n{Fore.YELLOW}Thank you for using WireGuard Management{Style.RESET_ALL}"))
    print(create_border(HISTORYBAR_BORDER_CHAR))
    sys.exit(exit_code)

def display_error(message):
    """Display error message with consistent formatting"""
    logger.error(message)
    print(f"\n{Fore.YELLOW}⚠ {Fore.LIGHTRED_EX}{message}{Style.RESET_ALL}")

# ========== Progress Indicator ==========
def show_progress(message, duration):
    """Show animated progress dots with the given message"""
    logger.debug(f"Starting progress indicator: {message}")
    if duration < 0:
        logger.error(f"Invalid progress duration: {duration}")
        display_error("Invalid progress duration: Must be non-negative")
        raise ValueError("Duration must be non-negative")
    try:
        print(f"\n{Fore.LIGHTMAGENTA_EX}{message}...{Style.RESET_ALL}")
        for _ in range(12):
            sys.stdout.write(f"{Fore.LIGHTCYAN_EX}·{Style.RESET_ALL}")
            sys.stdout.flush()
            time.sleep(0.1)
        print(f"\n{Fore.LIGHTGREEN_EX}✓ {Fore.LIGHTGREEN_EX}Complete!{Style.RESET_ALL}")
        logger.debug("Progress indicator completed normally")
    except KeyboardInterrupt:
        logger.warning("Progress indicator interrupted by user")
        display_error("Operation cancelled by user")
        raise
    except Exception as e:
        logger.error(f"Error in progress indicator: {str(e)}")
        display_error(f"Progress indicator error: {str(e)}")
        raise

# ========== History Bar Section ==========
# History Bar-specific constant
HISTORYBAR_BORDER_CHAR = "─"

class HistoryBar:
    """Manages the one-line navigation history display within a 70-character limit.
    Displays only the current menu name centered. If the menu name exceeds a visible
    length of 66 characters, it is truncated to 64 characters plus a space and
    a dim white '⋯' marker.
    """
    _instance = None
    MAX_WIDTH = 70
    TRUNCATION_THRESHOLD = 66  # Maximum visible length for menu name before truncation

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(HistoryBar, cls).__new__(cls)
            cls._instance.stack = ["Main Menu"]
            logger.debug("HistoryBar singleton initialized")
        return cls._instance

    def push(self, menu_name):
        """Push a new menu name onto the history stack."""
        if not menu_name or not menu_name.strip():
            logger.error("Attempted to push empty menu name to history")
            display_error("Invalid menu name: Cannot be empty")
            raise DisplayError("Menu name cannot be empty or whitespace")
        logger.debug(f"Pushing to history stack: {menu_name}")
        self.stack.append(menu_name.strip())

    def pop(self):
        """Pop the current menu name off the history stack"""
        if len(self.stack) > 1:
            popped = self.stack.pop()
            logger.debug(f"Popped from history stack: {popped}")
            return popped
        logger.debug("Attempted to pop base menu - ignored")
        return None

    def clear(self):
        """Reset the history bar to only contain the base menu"""
        logger.debug("Clearing history stack")
        self.stack = ["Main Menu"]

    def get_history(self):
        """
        Return the current menu name formatted for the history bar.
        Applies light cyan color to the menu name. If its visible length (ignoring ANSI codes)
        exceeds 66 characters, it will be truncated to 64 characters followed by a space and a
        dim white '⋯'. The resulting text is meant to fit within a 70-character limit.
        """
        current = self.stack[-1]
        visible_len = len(current)
        if visible_len > self.TRUNCATION_THRESHOLD:
            formatted = f"{Style.BRIGHT}{Fore.LIGHTCYAN_EX}{current[:64]}{Style.RESET_ALL}" + " " + f"{Style.DIM}{Fore.WHITE}⋯{Style.RESET_ALL}"
        else:
            formatted = f"{Style.BRIGHT}{Fore.LIGHTCYAN_EX}{current}{Style.RESET_ALL}"
        return formatted

def display_history():
    """
    Display the current menu name centered in a 70-character wide field.
    It appears one line below the bottom border of the ASCII art.
    A bottom border consisting of the ─ character is printed below.
    """
    history = HistoryBar().get_history()
    print(center_text(history, width=70))
    print(f"{Fore.LIGHTWHITE_EX}{create_border(HISTORYBAR_BORDER_CHAR, width=70)}{Style.RESET_ALL}")

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