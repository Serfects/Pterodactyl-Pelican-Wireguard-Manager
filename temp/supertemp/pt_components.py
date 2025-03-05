"""
Modern prompt_toolkit UI components for PPWM application.

This module provides specialized UI components built with prompt_toolkit
that create a rich, interactive terminal user interface. It includes enhanced input
prompts, dialogs, menus, and formatted text display capabilities optimized
for modern terminal emulators.

Module Dependencies:
- base_utils.py: For logging and constants
- No circular dependencies with other modules
"""
import logging
import os
import sys
import time
from prompt_toolkit import prompt, print_formatted_text, HTML
from prompt_toolkit.styles import Style, merge_styles
from prompt_toolkit.formatted_text import HTML, FormattedText
from prompt_toolkit.shortcuts import (
    clear, input_dialog, message_dialog, yes_no_dialog,
    button_dialog, checkboxlist_dialog, radiolist_dialog, ProgressBar
)
from prompt_toolkit.filters import Condition
from prompt_toolkit.mouse import MouseEventType
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.validation import Validator, ValidationError
from prompt_toolkit.output import ColorDepth
from base_utils import AppError, SCREEN_WIDTH

# Initialize logger for this module
logger = logging.getLogger(__name__)

# ========== Custom Exceptions ==========
class UIComponentError(AppError):
    """Exception raised for prompt_toolkit UI component errors"""
    pass

# ========== Global Styles ==========
# Modern color scheme based on the original application's aesthetic
PPWM_STYLE = Style.from_dict({
    # Dialog styles
    'dialog': 'bg:#171717',
    'dialog frame.label': 'bg:#000000 #3498db bold',
    'dialog.body': 'bg:#171717 #ffffff',
    'dialog shadow': 'bg:#0a0a0a',
    
    # Button styles
    'button': 'bg:#3498db #ffffff',
    'button.focused': 'bg:#2980b9 #ffffff',
    
    # Input field styles
    'text-area': 'bg:#171717 #ffffff',
    'text-area.cursor': '#ffffff bg:#aaaaaa',
    
    # Selection components
    'checkbox': '#3498db',
    'checkbox-list': 'bg:#171717 #ffffff',
    'checkbox-selected': 'bg:#2980b9 #ffffff',
    
    # Radio buttons
    'radio': '#3498db',
    'radio-checked': '#3498db',
    'radio-selected': 'bg:#2980b9 #ffffff',
    
    # Standard color definitions
    'success': '#2ecc71',
    'error': '#e74c3c',
    'warning': '#f39c12',
    'info': '#3498db',
    
    # Prompt components
    'bottom-toolbar': 'bg:#222222 #aaaaaa',
    'prompt': '#3498db',
    'prompt.border': '#444444',
    'status-bar': 'bg:#222222 #aaaaaa',
    'status-bar.key': '#3498db',
    'status-bar.value': '#ffffff',
    'search-toolbar': 'bg:#000000 #ffffff',
    'search-toolbar.text': '#ffffff',
})

# ========== UI Settings ==========
# Settings for the UI components
UI_SETTINGS = {
    'mouse_support': True,      # Enable mouse support by default
    'color_depth': 'DEPTH_24_BIT',  # Use true color if supported
    'min_terminal_width': 80,   # Minimum terminal width for proper display
    'min_terminal_height': 24,  # Minimum terminal height for proper display
}

# ========== System Configuration ==========
def configure_terminal():
    """
    Configure terminal settings for optimal display.
    
    Returns:
        dict: Current terminal configuration
    """
    # Get terminal size
    term_width, term_height = os.get_terminal_size()
    
    # Choose appropriate color depth based on terminal capabilities
    color_depth = ColorDepth.DEPTH_24_BIT
    if 'COLORTERM' in os.environ:
        if os.environ['COLORTERM'] in ('truecolor', '24bit'):
            color_depth = ColorDepth.DEPTH_24_BIT
        else:
            color_depth = ColorDepth.DEPTH_8_BIT
    
    config = {
        'term_width': term_width,
        'term_height': term_height,
        'color_depth': color_depth,
    }
    
    logger.debug(f"Terminal configured: width={term_width}, height={term_height}, color_depth={color_depth}")
    return config

# ========== Basic UI Components ==========
def clear_screen():
    """
    Clear the terminal screen using prompt_toolkit's clear function.
    """
    clear()
    logger.debug("Screen cleared using prompt_toolkit")

def show_message(title, text, style=None):
    """
    Display a message dialog with the given title and text.
    
    Args:
        title (str): Dialog title
        text (str): Message text (can include HTML formatting)
        style (Style, optional): Custom style. Defaults to PPWM_STYLE.
    """
    logger.debug(f"Displaying message: {title}")
    used_style = style if style else PPWM_STYLE
    
    # Ensure text is properly formatted as HTML
    if not text.startswith("<") and not isinstance(text, HTML):
        text = HTML(text)
    
    # Display the message with mouse support
    message_dialog(
        title=title,
        text=text,
        style=used_style,
        mouse_support=UI_SETTINGS['mouse_support']
    ).run()

def show_error_dialog(message, title="Error"):
    """
    Display an error message dialog.
    
    Args:
        message (str): Error message to display
        title (str, optional): Dialog title. Defaults to "Error".
    """
    logger.error(message)
    styled_message = HTML(f"<ansired>⚠ {message}</ansired>")
    show_message(title, styled_message)

def show_success_dialog(message, title="Success"):
    """
    Display a success message dialog.
    
    Args:
        message (str): Success message to display
        title (str, optional): Dialog title. Defaults to "Success".
    """
    logger.info(message)
    styled_message = HTML(f"<ansigreen>✓ {message}</ansigreen>")
    show_message(title, styled_message)

def show_warning_dialog(message, title="Warning"):
    """
    Display a warning message dialog.
    
    Args:
        message (str): Warning message to display
        title (str, optional): Dialog title. Defaults to "Warning".
    """
    logger.warning(message)
    styled_message = HTML(f"<ansiyellow>⚠ {message}</ansiyellow>")
    show_message(title, styled_message)

# ========== Progress Indicators ==========
def show_progress_bar(title, tasks, label_format=None):
    """
    Show a progress bar for a list of tasks.
    
    Args:
        title (str): Title displayed above the progress bar
        tasks (list/iterator): Tasks to iterate through
        label_format (callable, optional): Function to format task labels
    
    Returns:
        Any: Result from the last task
    """
    result = None
    title_html = HTML(f"<b>{title}</b>")
    
    with ProgressBar(title=title_html, style=PPWM_STYLE) as pb:
        for task in pb(tasks):
            # If a label format function was provided, update the label
            if label_format:
                pb.label = label_format(task)
            
            # Process the task (in a real app, this would do something)
            time.sleep(0.05)  # Simulated work
            result = task
            
    return result

def show_indeterminate_progress(message, duration=2.0):
    """
    Show an indeterminate progress indicator for operations with unknown duration.
    
    Args:
        message (str): Message to display
        duration (float, optional): Duration in seconds. Defaults to 2.0.
    """
    # Create a spinner animation
    spinner_chars = "⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏"
    print(HTML(f"<ansicyan>{message}...</ansicyan>"))
    
    try:
        for i in range(int(duration * 10)):
            char = spinner_chars[i % len(spinner_chars)]
            print(HTML(f"\r<ansicyan>{message}...</ansicyan> <ansiblue>{char}</ansiblue>"), end="", flush=True)
            time.sleep(0.1)
        print(HTML("\r<ansigreen>✓</ansigreen> <ansigreen>Complete!</ansigreen>  "))
    except KeyboardInterrupt:
        print(HTML("\r<ansiyellow>✗</ansiyellow> <ansiyellow>Cancelled!</ansiyellow>  "))
        raise

# ========== Enhanced Input Functions ==========
def prompt_input(prompt_text, default="", validator=None, completer=None, style=None, 
                 is_password=False, bottom_toolbar=None, mouse_support=None):
    """
    Get user input with enhanced features from prompt_toolkit.
    
    Args:
        prompt_text (str): The prompt text to display
        default (str, optional): Default value. Defaults to empty string.
        validator (callable, optional): Validation function. Defaults to None.
        completer (Completer, optional): Auto-completion. Defaults to None.
        style (Style, optional): Custom style. Defaults to PPWM_STYLE.
        is_password (bool, optional): Hide input like a password. Defaults to False.
        bottom_toolbar (str/callable, optional): Text for bottom toolbar. Defaults to None.
        mouse_support (bool, optional): Enable mouse support. Default is UI_SETTINGS value.
    
    Returns:
        str: The user's input text
    
    Raises:
        KeyboardInterrupt: If user cancels input with Ctrl+C
    """
    logger.debug(f"Prompting user for input: {prompt_text}")
    used_style = style if style else PPWM_STYLE
    mouse = mouse_support if mouse_support is not None else UI_SETTINGS['mouse_support']
    
    # Ensure prompt text is properly formatted as HTML
    if not isinstance(prompt_text, HTML):
        prompt_text = HTML(prompt_text)
    
    # Create a validator if provided with a validation function
    class InputValidator(Validator):
        def validate(self, document):
            if validator and not validator(document.text):
                raise ValidationError(message="Invalid input")
    
    # Get input from user
    try:
        result = prompt(
            prompt_text,
            default=default,
            validator=InputValidator() if validator else None,
            completer=completer,
            style=used_style,
            is_password=is_password,
            mouse_support=mouse,
            bottom_toolbar=bottom_toolbar
        )
        logger.debug(f"User input received: {'*****' if is_password else result}")
        return result
    except KeyboardInterrupt:
        logger.info("Input prompt interrupted by user")
        raise

def prompt_confirmation_dialog(prompt_text, title="Confirmation", yes_text="Yes", no_text="No", style=None):
    """
    Display a yes/no confirmation dialog.
    
    Args:
        prompt_text (str): The question to ask
        title (str, optional): Dialog title. Defaults to "Confirmation".
        yes_text (str, optional): Text for yes button. Defaults to "Yes".
        no_text (str, optional): Text for no button. Defaults to "No".
        style (Style, optional): Custom style. Defaults to PPWM_STYLE.
    
    Returns:
        bool: True if user confirmed, False otherwise
    """
    logger.debug(f"Requesting confirmation: {prompt_text}")
    used_style = style if style else PPWM_STYLE
    
    # Ensure prompt text is properly formatted as HTML if it's not already
    if not isinstance(prompt_text, HTML) and not prompt_text.startswith("<"):
        prompt_text = HTML(prompt_text)
    
    # Display confirmation dialog with mouse support
    result = yes_no_dialog(
        title=title,
        text=prompt_text,
        yes_text=yes_text,
        no_text=no_text,
        style=used_style,
        mouse_support=UI_SETTINGS['mouse_support']
    ).run()
    
    logger.debug(f"Confirmation result: {result}")
    return result

def prompt_menu_selection(title, options, style=None):
    """
    Display a button menu and return the selected option.
    
    Args:
        title (str): Dialog title
        options (list): List of (button_text, return_value) tuples
        style (Style, optional): Custom style. Defaults to PPWM_STYLE.
    
    Returns:
        Any: Selected value or None if cancelled
    """
    logger.debug(f"Showing menu with {len(options)} options")
    used_style = style if style else PPWM_STYLE
    
    result = button_dialog(
        title=title,
        text="",  # No additional text
        buttons=options,
        style=used_style,
        mouse_support=UI_SETTINGS['mouse_support']
    ).run()
    
    logger.debug(f"Menu selection: {result}")
    return result

def prompt_multi_select(title, text, values, default_values=None, style=None):
    """
    Display a checkbox list for multiple selection.
    
    Args:
        title (str): Dialog title
        text (str): Instruction text
        values (list): List of (value, label) tuples
        default_values (list, optional): List of values to pre-select
        style (Style, optional): Custom style. Defaults to PPWM_STYLE.
    
    Returns:
        list: List of selected values or empty list if cancelled
    """
    logger.debug(f"Showing multi-select with {len(values)} options")
    used_style = style if style else PPWM_STYLE
    defaults = default_values if default_values else []
    
    # If text is not HTML, convert it
    if not isinstance(text, HTML) and not text.startswith("<"):
        text = HTML(text)
    
    result = checkboxlist_dialog(
        title=title,
        text=text,
        values=values,
        default_values=defaults,
        style=used_style,
        mouse_support=UI_SETTINGS['mouse_support']
    ).run()
    
    logger.debug(f"Multi-select result: {result}")
    return result if result else []

# ========== System Information ==========
def get_terminal_capabilities():
    """
    Get information about the terminal's capabilities.
    
    Returns:
        dict: Terminal capability information
    """
    info = {
        'size': os.get_terminal_size(),
        'supports_color': sys.stdout.isatty(),
        'term_type': os.environ.get('TERM', 'unknown'),
        'colorterm': os.environ.get('COLORTERM', 'unknown'),
    }
    
    return info

# Initialize module with terminal configuration
try:
    terminal_config = configure_terminal()
    if terminal_config['term_width'] < UI_SETTINGS['min_terminal_width']:
        logger.warning(f"Terminal width ({terminal_config['term_width']}) below recommended minimum ({UI_SETTINGS['min_terminal_width']})")
    if terminal_config['term_height'] < UI_SETTINGS['min_terminal_height']:
        logger.warning(f"Terminal height ({terminal_config['term_height']}) below recommended minimum ({UI_SETTINGS['min_terminal_height']})")
except Exception as e:
    logger.warning(f"Could not configure terminal: {e}")

logger.debug("pt_components module loaded")
