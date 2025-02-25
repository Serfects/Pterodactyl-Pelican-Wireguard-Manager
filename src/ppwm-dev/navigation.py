"""
Navigation and history management for the PPWM application.

This module contains utilities for managing navigation history, menu transitions,
and user interface state tracking. It provides a singleton MenuNavigationTracker class
that maintains a stack of menu names for proper back-navigation.

Module Dependencies:
- base_utils.py: For logging and basic utility functions
- No circular dependencies with other modules

Other modules should import this after base_utils.py but before display or interactive modules.
"""
import logging
from colorama import Style, Fore
from base_utils import AppError, SCREEN_WIDTH

# Initialize logger for this module
logger = logging.getLogger(__name__)

# ========== Navigation Constants ==========
NAV_BORDER_CHAR = "─"

# ========== Custom Exceptions ==========
class NavigationError(AppError):
    """Exception raised for errors in the navigation system"""
    pass

# ========== History Management ==========
class MenuNavigationTracker:
    """
    Manages the menu navigation history with a stack-based approach.
    
    This singleton class tracks the user's location in the menu hierarchy
    and provides functionality for navigating forward and backward.
    It maintains a stack of menu names and displays the current menu name
    in the UI header.
    
    The display is limited to a 70-character limit with proper truncation
    for longer menu names.
    """
    _instance = None
    MAX_WIDTH = 70
    TRUNCATION_THRESHOLD = 66  # Maximum visible length for menu name before truncation

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(MenuNavigationTracker, cls).__new__(cls)
            cls._instance.stack = ["Main Menu"]
            logger.debug("MenuNavigationTracker singleton initialized")
        return cls._instance

    def push(self, menu_name):
        """
        Push a new menu name onto the history stack.
        
        Args:
            menu_name (str): The name of the menu to add to history
            
        Raises:
            NavigationError: If menu_name is empty or only whitespace
        """
        if not menu_name or not menu_name.strip():
            logger.error("Attempted to push empty menu name to history")
            raise NavigationError("Menu name cannot be empty or whitespace")
        logger.debug(f"Pushing to history stack: {menu_name}")
        self.stack.append(menu_name.strip())

    def pop(self):
        """
        Pop the current menu name off the history stack.
        
        Returns:
            str or None: The popped menu name, or None if at the base menu
        """
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
        dim white '⋯' marker.
        
        Returns:
            str: Formatted menu name for display
        """
        current = self.stack[-1]
        visible_len = len(current)
        if visible_len > self.TRUNCATION_THRESHOLD:
            formatted = f"{Style.BRIGHT}{Fore.LIGHTCYAN_EX}{current[:64]}{Style.RESET_ALL}" + " " + f"{Style.DIM}{Fore.WHITE}⋯{Style.RESET_ALL}"
        else:
            formatted = f"{Style.BRIGHT}{Fore.LIGHTCYAN_EX}{current}{Style.RESET_ALL}"
        return formatted

    def get_current(self):
        """
        Get the name of the current menu (unformatted).
        
        Returns:
            str: Current menu name without formatting
        """
        return self.stack[-1]
    
    def get_previous(self):
        """
        Get the name of the previous menu (unformatted).
        
        Returns:
            str or None: Previous menu name, or None if at the base menu
        """
        if len(self.stack) > 1:
            return self.stack[-2]
        return None

# ========== Navigation Processing ==========
def process_menu_choice(choice, menu_actions):
    """
    Process menu selection including navigation options.
    
    Args:
        choice (str): User's menu selection
        menu_actions (dict): Dictionary of menu actions
    
    Returns:
        tuple: (should_exit, was_handled) - Flags for menu flow control
    """
    logger.debug(f"Processing menu choice: {choice}")
    history = MenuNavigationTracker()
    
    if choice.lower() == "x":
        logger.info("Exit requested")
        from input_utils import prompt_confirmation  # Correct import, good!
        if prompt_confirmation("Are you sure you want to exit?"):
            logger.info("User confirmed exit")
            return True, True
        logger.info("User cancelled exit")
        return False, True
        
    if choice.lower() == "b" and len(history.stack) > 1:
        logger.info("Back navigation requested")
        history.pop()
        return False, True
        
    return False, choice in menu_actions

def add_navigation_options(menu_options):
    """
    Add navigation options (back/exit) to menu choices with a subtle separator.
    Exit option appears first, followed by back option (when available).
    
    Args:
        menu_options (list): List of menu option tuples
    
    Returns:
        list: Updated menu options with navigation options
    """
    logger.debug("Processing navigation options")
    history = MenuNavigationTracker()
    
    # Add double spacing before navigation options
    menu_options.append(("", "", ""))
    menu_options.append(("", "", ""))
    
    # Add subtle separator line (slightly brighter than the navigation text)
    menu_options.append(
        ("", f"{Style.DIM}{Fore.LIGHTBLACK_EX}────────────────────────{Style.RESET_ALL}", "")
    )
    
    # Add exit option with subtle coloring but no explanation (always first)
    menu_options.append(
        ("x", f"{Style.DIM}{Fore.BLACK}Exit application{Style.RESET_ALL}", "")
    )
    
    if len(history.stack) > 1:  # Add back option if not on main menu
        menu_options.append(
            ("b", f"{Style.DIM}{Fore.BLACK}Return to previous menu{Style.RESET_ALL}", 
             f"{Style.DIM}{Fore.BLACK}Go back to {history.stack[-2]}{Style.RESET_ALL}")
        )
    
    return menu_options

logger.debug("navigation module loaded")
