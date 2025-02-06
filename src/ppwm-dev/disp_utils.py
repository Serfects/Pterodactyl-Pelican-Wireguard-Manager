import re
import sys
import os
import time
from colorama import Style, Fore

SCREEN_WIDTH = 80
BORDER_CHAR = "="
PADDING = 2

ANSI_ESCAPE = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')

class DisplayError(Exception):
    pass

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

def format_option(key, text, padding=None):
    if not key or not text:
        raise ValueError("Key and text must not be empty")
    actual_padding = padding if padding is not None else PADDING
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
        # Always show 20 dots with delay calculated from duration
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

# ASCII art for consistent header display across all screens
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

def clear_screen():
    # Clear terminal screen based on OS
    os.system('clear' if os.name == 'posix' else 'cls')

def display_screen(title, content_func=None):
    # Clear screen and display ASCII header
    clear_screen()
    centered_ascii = "\n".join(center_text(line) for line in ASCII_ART.strip().split("\n"))
    print(centered_ascii)
    
    # Display title section with borders
    print("\n" + create_border())
    print(center_text(f"{Fore.YELLOW}{title}{Style.RESET_ALL}"))
    print(create_border() + "\n")
    
    # Run the content function if provided
    if content_func:
        content_func()