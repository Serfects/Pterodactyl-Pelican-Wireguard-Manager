import re
from colorama import Style, Fore
import time, sys
import os

# ========== Constants ==========
SCREEN_WIDTH = 70
HISTORYBAR_BORDER_CHAR = "─"
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
    return f"{Fore.YELLOW}⚠ {Fore.LIGHTRED_EX}{text}{Style.RESET_ALL}"

def format_success(text):
    """Add checkmark and green coloring to success message"""
    return f"{Fore.LIGHTGREEN_EX}✓ {text}{Style.RESET_ALL}"

# ========== Display Layout Functions ==========
def clear_screen():
    """Clear the terminal screen"""
    os.system('clear' if os.name == 'posix' else 'cls')

def center_text(text, width=None, fill_char=" "):
    """Center the given text in available space, accounting for ANSI formatting"""
    if not fill_char:
        raise ValueError("Fill character cannot be empty")
    actual_width = width if width is not None else SCREEN_WIDTH
    if actual_width < 0:
        raise ValueError("Width cannot be negative")
    stripped_text = strip_ansi(text)
    if len(stripped_text) > actual_width:
        raise DisplayError(f"Text length ({len(stripped_text)}) exceeds width ({actual_width})")
    padding = (actual_width - len(stripped_text)) // 2
    return (fill_char * padding) + text + (fill_char * (actual_width - len(stripped_text) - padding))

def create_border(char=None, width=None):
    """Create a horizontal border using specified character"""
    if not char:
        char = HISTORYBAR_BORDER_CHAR
    if not char.strip():
        raise ValueError("Border character cannot be empty or whitespace")
    actual_width = width if width is not None else SCREEN_WIDTH
    if actual_width < 0:
        raise ValueError("Width cannot be negative")
    return char * actual_width

def graceful_exit(message="", exit_code=0):
    """Display exit message and terminate application gracefully"""
    if message:
        print(center_text(f"\n{Fore.YELLOW}{message}{Style.RESET_ALL}"))
    print(center_text(f"\n{Fore.YELLOW}Thank you for using WireGuard Management{Style.RESET_ALL}"))
    print(create_border(HISTORYBAR_BORDER_CHAR))
    sys.exit(exit_code)

def display_error(message):
    """Display error message with consistent formatting"""
    print(f"\n{Fore.YELLOW}⚠ {Fore.LIGHTRED_EX}{message}{Style.RESET_ALL}")

# ========== Progress Indicator ==========
def show_progress(message, duration):
    """Show animated progress dots with the given message"""
    if duration < 0:
        raise ValueError("Duration must be non-negative")
    try:
        print(f"\n{Fore.LIGHTMAGENTA_EX}{message}...{Style.RESET_ALL}")
        for _ in range(12):
            sys.stdout.write(f"{Fore.LIGHTCYAN_EX}·{Style.RESET_ALL}")
            sys.stdout.flush()
            time.sleep(0.1)
        print(f"\n{Fore.LIGHTGREEN_EX}✓ {Fore.GREEN}Complete!{Style.RESET_ALL}")
    except KeyboardInterrupt:
        print(f"\n{Fore.YELLOW}Progress interrupted{Style.RESET_ALL}")
        raise

# ========== History Bar Implementation ==========
class HistoryBar:
    """Manages the navigation history display with truncation and formatting"""
    _instance = None
    MAX_WIDTH = 70
    ELLIPSIS = "⋯"
    ARROW = f"{Fore.LIGHTBLUE_EX}▸{Style.RESET_ALL}"
    
    def __new__(cls):
        """Singleton pattern to ensure single history instance"""
        if cls._instance is None:
            cls._instance = super(HistoryBar, cls).__new__(cls)
            cls._instance.path = ["Main Menu"]
        return cls._instance
    
    def _format_menu_name(self, name, is_current=False):
        """Format menu names with appropriate colors"""
        if is_current:
            return f"{Fore.LIGHTCYAN_EX}{name}{Style.RESET_ALL}"
        return f"{Style.DIM}{Fore.WHITE}{name}{Style.RESET_ALL}"
    
    def _calculate_display_length(self, text):
        """Calculate true display length ignoring ANSI codes"""
        return len(strip_ansi(text))
    
    def get_history(self):
        """Generate formatted history bar with proper truncation"""
        if not self.path:
            return ""
            
        # Handle current menu
        current_menu = self._format_menu_name(self.path[-1], True)
        current_length = self._calculate_display_length(current_menu)
        
        # Truncate if current menu is too long
        if current_length > self.MAX_WIDTH:
            truncated = self._format_menu_name(f"{self.path[-1][:self.MAX_WIDTH-3]}...", True)
            return truncated
            
        # Initialize history building
        formatted_menus = [current_menu]
        total_length = current_length
        available_space = self.MAX_WIDTH - current_length
        previous_menus = []
        
        # Calculate ellipsis space
        ellipsis_space = self._calculate_display_length(f"{self.ELLIPSIS} {self.ARROW} ")
        
        # Process previous menus right to left
        for menu in reversed(self.path[:-1]):
            formatted_menu = self._format_menu_name(menu)
            menu_text = f"{formatted_menu} {self.ARROW} "
            menu_length = self._calculate_display_length(menu_text)
            
            # Check space including potential ellipsis
            space_needed = menu_length
            if len(previous_menus) < len(self.path) - 2:
                space_needed += ellipsis_space
                
            if available_space >= menu_length:
                previous_menus.insert(0, (formatted_menu, menu_length))
                available_space -= menu_length
                total_length += menu_length
            else:
                break
        
        # Build final display
        result_parts = []
        
        # Add ellipsis if needed
        if previous_menus and len(previous_menus) < len(self.path) - 1:
            ellipsis = self._format_menu_name(self.ELLIPSIS)
            if available_space >= self._calculate_display_length(f"{ellipsis} {self.ARROW} "):
                result_parts.extend([ellipsis, self.ARROW])
        
        # Add fitting previous menus
        for menu, _ in previous_menus:
            if result_parts:
                result_parts.append(self.ARROW)
            result_parts.append(menu)
        
        # Add current menu
        if result_parts:
            result_parts.append(self.ARROW)
        result_parts.append(current_menu)
        
        return " ".join(result_parts)

def display_history():
    """Display the history bar with proper centering and border"""
    history = HistoryBar().get_history()
    print(center_text(history))
    print(f"{Fore.LIGHTWHITE_EX}{create_border(HISTORYBAR_BORDER_CHAR)}{Style.RESET_ALL}")

# ========== ASCII Art ==========
ASCII_ART = f"""{Fore.LIGHTWHITE_EX}::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::{Fore.LIGHTCYAN_EX}        ____      {Style.BRIGHT}{Fore.WHITE} ____  ______        ____  __ {Fore.LIGHTCYAN_EX}      ____        {Fore.LIGHTWHITE_EX}::
::{Fore.LIGHTCYAN_EX}        \ \ \     {Style.BRIGHT}{Fore.WHITE}|  _ \|  _ \ \      / /  \/  |{Fore.LIGHTCYAN_EX}     / / /        {Fore.LIGHTWHITE_EX}::
::{Fore.LIGHTCYAN_EX}         \ \ \    {Style.BRIGHT}{Fore.WHITE}| |_) | |_) \ \ /\ / /| |\/| |{Fore.LIGHTCYAN_EX}    / / /         {Fore.LIGHTWHITE_EX}::
::{Fore.LIGHTCYAN_EX}         / / /    {Style.BRIGHT}{Fore.WHITE}|  __/|  __/ \ V  V / | |  | |{Fore.LIGHTCYAN_EX}    \ \ \         {Fore.LIGHTWHITE_EX}::
::{Fore.LIGHTCYAN_EX}        /_/_/     {Style.BRIGHT}{Fore.WHITE}|_|   |_|     \_/\_/  |_|  |_|{Fore.LIGHTCYAN_EX}     \_\_\        {Fore.LIGHTWHITE_EX}::
::{Fore.LIGHTCYAN_EX}                                                                  {Fore.LIGHTWHITE_EX}::
::{Fore.LIGHTCYAN_EX}               Pterodactyl-Pelican-Wireguard-Manager              {Fore.LIGHTWHITE_EX}::
::{Fore.LIGHTCYAN_EX}                           By: Serfects                           {Fore.LIGHTWHITE_EX}::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::{Style.RESET_ALL}"""