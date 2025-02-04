
"""
Display utilities for consistent terminal output formatting.

This module provides utilities for formatting text output in the terminal,
including centering text, creating borders, and formatting menu options.
All functions maintain consistent styling across the application.
"""

import re
from typing import Union, Optional, Tuple
from colorama import Style, Fore

# Display Constants:
# These define the basic parameters for text formatting
# - SCREEN_WIDTH: Standard width for all formatted output
# - BORDER_CHAR: Character used for horizontal borders
# - PADDING: Space before and after menu options
SCREEN_WIDTH: int = 80
BORDER_CHAR: str = "="
PADDING: int = 2

# ANSI escape code pattern for stripping color codes when calculating lengths
ANSI_ESCAPE = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')

class DisplayError(Exception):
    """Custom exception for display-related errors."""
    pass

def strip_ansi(text: str) -> str:
    """
    Remove ANSI escape codes from text for length calculations.
    
    Args:
        text: Text containing ANSI escape codes

    Returns:
        str: Text with ANSI codes removed
    """
    return ANSI_ESCAPE.sub('', text)

def split_formatting(text: str) -> Tuple[str, str, str]:
    """
    Split text into prefix formatting, content, and suffix formatting.
    Returns tuple of (prefix_format, clean_text, suffix_format)
    """
    parts = text.split(Style.RESET_ALL)
    if len(parts) != 2:
        return '', text, ''
    
    return parts[0], parts[1].strip(), Style.RESET_ALL

def center_text(
    text: str,
    width: Optional[int] = None,
    fill_char: str = " "
) -> str:
    """
    Center text while preserving ANSI color codes.

    Args:
        text: Text to be centered (may contain ANSI codes)
        width: Width to center within (defaults to SCREEN_WIDTH)
        fill_char: Character to use for padding (default space)

    Returns:
        str: Centered text with preserved ANSI formatting

    Raises:
        DisplayError: If text is longer than specified width
        ValueError: If width is negative or fill_char is empty
    """
    if not fill_char:
        raise ValueError("Fill character cannot be empty")
    
    actual_width = width if width is not None else SCREEN_WIDTH
    
    if actual_width < 0:
        raise ValueError("Width cannot be negative")
    
    # Strip ANSI codes for length calculation
    stripped_text = strip_ansi(text)
    
    if len(stripped_text) > actual_width:
        raise DisplayError(f"Text length ({len(stripped_text)}) exceeds width ({actual_width})")
    
    # Calculate padding needed
    padding = (actual_width - len(stripped_text)) // 2
    return (fill_char * padding) + text + (fill_char * (actual_width - len(stripped_text) - padding))

def create_border(
    char: Optional[str] = None,
    width: Optional[int] = None
) -> str:
    """
    Create a horizontal border line.

    Args:
        char: Character to use for border (defaults to BORDER_CHAR)
        width: Width of border (defaults to SCREEN_WIDTH)

    Returns:
        str: Border string of specified width

    Raises:
        ValueError: If border character is empty or width is negative
    """
    if not char:
        char = BORDER_CHAR
    
    if not char.strip():
        raise ValueError("Border character cannot be empty or whitespace")
    
    actual_width = width if width is not None else SCREEN_WIDTH
    
    if actual_width < 0:
        raise ValueError("Width cannot be negative")
        
    return char * actual_width

def format_option(
    key: str,
    text: str,
    padding: Optional[int] = None
) -> str:
    """
    Format a menu option with consistent styling.

    Args:
        key: Option identifier (number or letter)
        text: Option description
        padding: Space before option (defaults to PADDING)

    Returns:
        str: Formatted menu option string

    Raises:
        ValueError: If key or text is empty
    """
    if not key or not text:
        raise ValueError("Key and text must not be empty")
    
    actual_padding = padding if padding is not None else PADDING
    
    if actual_padding < 0:
        raise ValueError("Padding cannot be negative")
        
    return " " * actual_padding + f"{key}. {text}"
    return " " * actual_padding + f"{key}. {text}"

# Optional: Add utility functions for colored text
def format_error(text: str) -> str:
    """Format error message with consistent styling."""
    return f"{Fore.YELLOW}⚠ {Fore.LIGHTRED_EX}{text}{Style.RESET_ALL}"

def format_success(text: str) -> str:
    """Format success message with consistent styling."""
    return f"{Fore.LIGHTGREEN_EX}✓ {text}{Style.RESET_ALL}"

# Optional: Add utility functions for colored text
def format_error(text: str) -> str:
    """Format error message with consistent styling."""
    return f"{Fore.YELLOW}⚠ {Fore.LIGHTRED_EX}{text}{Style.RESET_ALL}"

def format_success(text: str) -> str:
    """Format success message with consistent styling."""
    return f"{Fore.LIGHTGREEN_EX}✓ {text}{Style.RESET_ALL}"