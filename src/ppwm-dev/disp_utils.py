import re
from colorama import Style, Fore
import time, sys

SCREEN_WIDTH = 70
BORDER_CHAR = "─"  # Changed to single horizontal line

ANSI_ESCAPE = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')

class DisplayError(Exception):
    pass

class BreadcrumbManager:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(BreadcrumbManager, cls).__new__(cls)
            cls._instance.path = ["Main Menu"]
        return cls._instance
    
    def push(self, menu_name):
        self.path.append(menu_name)
    
    def pop(self):
        if len(self.path) > 1:  # Keep at least "Main Menu"
            return self.path.pop()
        return None
    
    def clear(self):
        self.path = ["Main Menu"]
    
    def get_breadcrumb(self):
        return f"{Fore.LIGHTBLUE_EX}{' → '.join(self.path)}{Style.RESET_ALL}"

def display_breadcrumb():
    breadcrumb = BreadcrumbManager().get_breadcrumb()
    print(center_text(breadcrumb))       # Display breadcrumb text
    print(create_border(BORDER_CHAR))    # Only bottom border with dotted line

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
    actual_width = width if width is not None else SCREEN_WIDTH
    if actual_width < 0:
        raise ValueError("Width cannot be negative")
    stripped_text = strip_ansi(text)
    if len(stripped_text) > actual_width:
        raise DisplayError(f"Text length ({len(stripped_text)}) exceeds width ({actual_width})")
    padding = (actual_width - len(stripped_text)) // 2
    return (fill_char * padding) + text + (fill_char * (actual_width - len(stripped_text) - padding))

def create_border(char=None, width=None):
    if not char:
        char = BORDER_CHAR
    if not char.strip():
        raise ValueError("Border character cannot be empty or whitespace")
    actual_width = width if width is not None else SCREEN_WIDTH
    if actual_width < 0:
        raise ValueError("Width cannot be negative")
    return char * actual_width

def format_error(text):
    return f"{Fore.YELLOW}⚠ {Fore.LIGHTRED_EX}{text}{Style.RESET_ALL}"

def format_success(text):
    return f"{Fore.LIGHTGREEN_EX}✓ {text}{Style.RESET_ALL}"

def show_progress(message, duration):
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