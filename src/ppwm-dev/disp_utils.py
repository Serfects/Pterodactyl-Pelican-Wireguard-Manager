import re
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