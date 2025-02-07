import re
import sys
import os
import time
from colorama import Style, Fore

#######################
# Global Configuration
#######################

class DisplayConfig:
    # Global display configuration
    SCREEN_WIDTH = 64
    PADDING = 2
    
    class Header:
        # Header-specific display settings
        ASCII_BORDER = "═"
        SIDE_BORDER = "::"
        BREADCRUMB_BORDER = "─"
        BREADCRUMB_COLOR = Fore.LIGHTCYAN_EX
        ASCII_COLOR = Fore.LIGHTCYAN_EX
        BORDER_COLOR = Fore.LIGHTWHITE_EX
    
    class Title:
        # Title section display settings
        BORDER_CHAR = "="
        COLOR = Fore.YELLOW

ANSI_ESCAPE = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')

class DisplayError(Exception):
    pass

#################################
# Header Components (ASCII & Breadcrumb)
#################################

# ASCII Art Definition
ASCII_ART = f"""{DisplayConfig.Header.BORDER_COLOR}{DisplayConfig.Header.ASCII_BORDER * DisplayConfig.SCREEN_WIDTH}
{DisplayConfig.Header.SIDE_BORDER}{DisplayConfig.Header.ASCII_COLOR}       ____       ____  ______        ____  __       ____       {DisplayConfig.Header.BORDER_COLOR}{DisplayConfig.Header.SIDE_BORDER}
{DisplayConfig.Header.SIDE_BORDER}{DisplayConfig.Header.ASCII_COLOR}       \ \ \     |  _ \|  _ \ \      / /  \/  |     / / /       {DisplayConfig.Header.BORDER_COLOR}{DisplayConfig.Header.SIDE_BORDER}
{DisplayConfig.Header.SIDE_BORDER}{DisplayConfig.Header.ASCII_COLOR}        \ \ \    | |_) | |_) \ \ /\ / /| |\/| |    / / /        {DisplayConfig.Header.BORDER_COLOR}{DisplayConfig.Header.SIDE_BORDER}
{DisplayConfig.Header.SIDE_BORDER}{DisplayConfig.Header.ASCII_COLOR}        / / /    |  __/|  __/ \ V  V / | |  | |    \ \ \        {DisplayConfig.Header.BORDER_COLOR}{DisplayConfig.Header.SIDE_BORDER}
{DisplayConfig.Header.SIDE_BORDER}{DisplayConfig.Header.ASCII_COLOR}       /_/_/     |_|   |_|     \_/\_/  |_|  |_|     \_\_\       {DisplayConfig.Header.BORDER_COLOR}{DisplayConfig.Header.SIDE_BORDER}
{DisplayConfig.Header.SIDE_BORDER}{DisplayConfig.Header.ASCII_COLOR}                                                                {DisplayConfig.Header.BORDER_COLOR}{DisplayConfig.Header.SIDE_BORDER}
{DisplayConfig.Header.SIDE_BORDER}{DisplayConfig.Header.ASCII_COLOR}             Pterodactyl-Pelican-Wireguard-Manager              {DisplayConfig.Header.BORDER_COLOR}{DisplayConfig.Header.SIDE_BORDER}
{DisplayConfig.Header.ASCII_BORDER * DisplayConfig.SCREEN_WIDTH}${Style.RESET_ALL}"""

class BreadcrumbTracker:
    _instance = None
    _path = ["Main Menu"]
    
    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance
    
    def push(self, menu_name):
        self._path.append(menu_name)
    
    def pop(self):
        if len(self._path) > 1:
            return self._path.pop()
        return None
    
    def reset(self):
        self._path = ["Main Menu"]
    
    def get_path(self, max_width=64):
        if not self._path:
            return ""
        separator = f" {Fore.LIGHTBLACK_EX}>{Style.RESET_ALL} "
        full_path = separator.join(self._path)
        stripped_len = len(strip_ansi(full_path))
        
        if stripped_len <= max_width:
            return full_path
        
        visible_width = max_width - 3
        current = self._path[-1]
        previous = self._path[-2] if len(self._path) > 1 else ""
        
        if len(strip_ansi(current)) + len(strip_ansi(previous)) + len(separator) + 3 <= visible_width:
            return f"...{separator}{previous}{separator}{current}"
        return f"...{separator}{current}"

def display_ascii_header():
    # Handles ASCII art display with consistent spacing
    try:
        centered_ascii = "\n".join(center_text(line) for line in ASCII_ART.strip().split("\n"))
        print(centered_ascii.rstrip())
    except DisplayError as e:
        print(format_error(f"ASCII Header Error: {e}"))
        return False
    return True

def display_breadcrumb():
    # Handles breadcrumb display with consistent spacing
    try:
        breadcrumb = BreadcrumbTracker.get_instance()
        path = breadcrumb.get_path(DisplayConfig.SCREEN_WIDTH)
        print(center_text(
            f"{DisplayConfig.Header.BREADCRUMB_COLOR}{path}{Style.RESET_ALL}"
        ))
        print(create_border(char=DisplayConfig.Header.BREADCRUMB_BORDER))
    except DisplayError as e:
        print(format_error(f"Breadcrumb Error: {e}"))
        return False
    return True

#################################
# Display Utilities
#################################

def strip_ansi(text):
    return ANSI_ESCAPE.sub('', text)

def split_formatting(text):
    parts = text.split(Style.RESET_ALL)
    if len(parts) != 2:
        return '', text, ''
    return parts[0], parts[1].strip(), Style.RESET_ALL

def center_text(text, width=None, fill_char=" "):
    if not fill_char:
        raise ValueError("Fill character cannot be empty")
    actual_width = width if width is not None else DisplayConfig.SCREEN_WIDTH
    if actual_width < 0:
        raise ValueError("Width cannot be negative")
    stripped_text = strip_ansi(text)
    if len(stripped_text) > actual_width:
        raise DisplayError(f"Text length ({len(stripped_text)}) exceeds width ({actual_width})")
    padding = (actual_width - len(stripped_text)) // 2
    return (fill_char * padding) + text + (fill_char * (actual_width - len(stripped_text) - padding))

def create_border(char=None, width=None):
    if not char:
        char = DisplayConfig.Title.BORDER_CHAR
    if not char.strip():
        raise ValueError("Border character cannot be empty or whitespace")
    actual_width = width if width is not None else DisplayConfig.SCREEN_WIDTH
    if actual_width < 0:
        raise ValueError("Width cannot be negative")
    return char * actual_width

def format_option(key, text, padding=None):
    if not key or not text:
        raise ValueError("Key and text must not be empty")
    actual_padding = padding if padding is not None else DisplayConfig.PADDING
    if actual_padding < 0:
        raise ValueError("Padding cannot be negative")
    return " " * actual_padding + f"{key}. {text}"

def format_error(text):
    return f"{Fore.YELLOW}⚠ {Fore.LIGHTRED_EX}{text}{Style.RESET_ALL}"

def format_success(text):
    return f"{Fore.LIGHTGREEN_EX}✓ {text}{Style.RESET_ALL}"

def show_progress(message, duration=1.5):
    if duration < 0:
        raise ValueError("Duration must be non-negative")

    try:
        print(f"\n{Fore.LIGHTMAGENTA_EX}{message}...{Style.RESET_ALL}")
        dots = 20
        delay = duration / dots
        for _ in range(dots):
            sys.stdout.write(f"{Fore.LIGHTCYAN_EX}·{Style.RESET_ALL}")
            sys.stdout.flush()
            time.sleep(delay)
        print(f"\n{Fore.LIGHTGREEN_EX}✓ {Fore.GREEN}Complete!{Style.RESET_ALL}")
    except KeyboardInterrupt:
        print(f"\n{Fore.YELLOW}Progress interrupted{Style.RESET_ALL}")
        raise

#################################
# Screen Management
#################################

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def display_screen(title, content_func=None):
    # Main display coordinator
    clear_screen()
    
    if not display_ascii_header() or not display_breadcrumb():
        return False
    
    print("\n" + create_border())
    print(center_text(f"{DisplayConfig.Title.COLOR}{title}{Style.RESET_ALL}"))
    print(create_border() + "\n")
    
    if content_func:
        content_func()
    
    return True