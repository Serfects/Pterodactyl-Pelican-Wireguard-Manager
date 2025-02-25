import os
import sys
import logging
from logging.handlers import RotatingFileHandler
from datetime import datetime
from colorama import Fore, Style
from disp_utils import display_error, graceful_exit, HistoryBar  # Added missing import

# ========== System Check Functions ==========
def check_root():
    """Check if the script is running with root privileges"""
    logger.debug("Checking for root privileges")
    if os.geteuid() != 0:
        logger.error("Script not running with root privileges")
        display_error("This application requires root privileges")
        input("\nPress Enter to exit...")
        sys.exit(1)
    logger.debug("Root privilege check passed")

# ========== Logging Setup ==========
def setup_logging():
    """Configure and initialize the logging system"""
    # Constants for log rotation
    MAX_LOG_SIZE = 5 * 1024 * 1024  # 5 MB in bytes
    BACKUP_COUNT = 4  # Keep 4 backups (total of 5 files including current)

    # Determine appropriate log directory based on environment
    if os.geteuid() == 0:  # Running as root
        log_dir = '/var/log/ppwm'
    else:  # Running as normal user
        log_dir = os.path.expanduser('~/.local/share/ppwm/logs')
    
    # Fallback to script directory if we can't write to system locations
    if not can_write_to_dir(log_dir):
        log_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'logs')
        print(f"{Fore.LIGHTYELLOW_EX}Warning: Cannot write to system log directories. Using local directory: {log_dir}{Style.RESET_ALL}")
    
    # Create logs directory if it doesn't exist
    try:
        os.makedirs(log_dir, exist_ok=True)
    except PermissionError:
        display_error("Cannot create log directory: Permission denied")
        sys.exit(1)
    except Exception as e:
        display_error(f"Failed to create log directory: {str(e)}")
        sys.exit(1)

    # Configure log file path
    log_file = os.path.join(log_dir, 'ppwm.log')

    # Configure logging format with detailed timestamps
    file_formatter = logging.Formatter(
        '%(asctime)s [%(levelname)-8s] %(name)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    console_formatter = logging.Formatter(
        '%(asctime)s - %(levelname)-8s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    # Set up rotating file handler
    try:
        file_handler = RotatingFileHandler(
            filename=log_file,
            maxBytes=MAX_LOG_SIZE,
            backupCount=BACKUP_COUNT,
            encoding='utf-8'
        )
        file_handler.setFormatter(file_formatter)
        file_handler.setLevel(logging.DEBUG)
    except PermissionError:
        display_error("Cannot create log file: Permission denied")
        sys.exit(1)
    except Exception as e:
        display_error(f"Failed to initialize logging: {str(e)}")
        sys.exit(1)

    # Set up console handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(console_formatter)
    console_handler.setLevel(logging.WARNING)

    # Configure root logger
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.DEBUG)
    root_logger.addHandler(file_handler)
    root_logger.addHandler(console_handler)

    # Set up custom error handler that uses display_error
    class ErrorHandler(logging.Handler):
        def emit(self, record):
            if record.levelno >= logging.ERROR:
                msg = self.format(record)
                display_error(msg)

    # Add error handler to root logger
    error_handler = ErrorHandler()
    error_handler.setLevel(logging.ERROR)
    root_logger.addHandler(error_handler)

    # Log initial startup information with timestamp
    startup_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    root_logger.info(f"Logging system initialized at {startup_time}")
    root_logger.debug(f"Log directory: {log_dir}")
    root_logger.debug(f"Max log size: 5 MB")
    root_logger.debug(f"Maximum log files: 5")

    return root_logger

def can_write_to_dir(directory):
    """Check if we can write to the specified directory"""
    logger.debug(f"Checking write permissions for directory: {directory}")
    try:
        result = os.access(directory, os.W_OK)
        logger.debug(f"Directory {directory} is {'writable' if result else 'not writable'}")
        return result
    except Exception as e:
        logger.error(f"Error checking directory permissions: {str(e)}")
        return False

# Initialize logging when module is imported
logger = setup_logging()

# ========== Custom Exceptions ==========
class InputValidationError(Exception):
    """Raised when input validation fails"""
    pass

class MenuExecutionError(Exception):
    """Raised when a menu action fails to execute"""
    pass

# ========== Input Handling Functions ==========
def handle_interrupt():
    """Handle Ctrl+C interrupt with clean exit"""
    print()  # Add newline after ^C
    graceful_exit("Received interrupt signal, shutting down...", 0)

def get_input(prompt, default=None, validator=None, choices=None, required=False):
    """Get user input with optional validation and choice selection"""
    logger.debug(f"Input prompt: '{prompt}', Default: {default}, Required: {required}")
    try:
        print(f"\n{Fore.LIGHTYELLOW_EX}{prompt}{Style.RESET_ALL}")
        
        # Display available choices if provided
        if choices:
            print("\nAvailable options:")
            for choice in choices:
                if isinstance(choice, tuple):
                    if len(choice) == 3:
                        # Display choice with explanation
                        number, description, explanation = choice
                        print(f"  {Style.DIM}{Fore.LIGHTWHITE_EX}•{Style.RESET_ALL} {Fore.LIGHTCYAN_EX}({number}){Style.RESET_ALL} {Fore.LIGHTWHITE_EX}{description}")
                        print(f"      {Style.DIM}{explanation}{Style.RESET_ALL}")
                    else:
                        # Display choice without explanation
                        number, description = choice
                        print(f"  {Style.DIM}{Fore.LIGHTWHITE_EX}•{Style.RESET_ALL} {Fore.LIGHTCYAN_EX}({number}){Style.RESET_ALL} {Fore.LIGHTWHITE_EX}{description}")
                else:
                    # Display simple choice
                    print(f"  {Style.DIM}{Fore.LIGHTWHITE_EX}•{Style.RESET_ALL} {Fore.LIGHTWHITE_EX}{choice}")
            print()

        # Show default value if provided
        if default is not None:
            print(f"{Fore.LIGHTWHITE_EX}(Default: {Fore.LIGHTBLUE_EX}{default}{Fore.LIGHTWHITE_EX}){Style.RESET_ALL}")
        
        # Prepare input prompt
        prompt_text = f"{Fore.LIGHTWHITE_EX}Your Entry: {Fore.LIGHTCYAN_EX}▸ {Style.RESET_ALL}"

        # Input loop
        while True:
            # Get and display user input
            user_input = input(prompt_text).strip()
            logger.debug(f"Received input: '{user_input}'")
            print(f"\033[F\033[K{prompt_text}{Style.BRIGHT}{Fore.LIGHTWHITE_EX}{user_input}{Style.RESET_ALL}")

            # Handle empty input
            if not user_input:
                if default is not None:
                    logger.debug(f"Using default value: {default}")
                    print(f"{Fore.LIGHTGREEN_EX}✓ {Fore.LIGHTBLUE_EX}Default option {Style.BRIGHT}{Fore.LIGHTWHITE_EX}{default}{Style.RESET_ALL} {Fore.LIGHTBLUE_EX}used{Style.RESET_ALL}")
                    return default
                if required:
                    logger.debug("Required field left empty")
                    display_error("This field cannot be empty")
                    continue

            # Validate against choices
            if choices and user_input not in [c[0] if isinstance(c, tuple) else c for c in choices]:
                logger.debug(f"Invalid choice entered: {user_input}")
                display_error("Invalid selection: Please choose from the available options")
                continue

            # Run custom validation
            if validator and not validator(user_input):
                logger.debug(f"Custom validation failed for input: {user_input}")
                display_error("Invalid input: Please check your entry and try again")
                continue

            logger.debug(f"Valid input received: {user_input}")
            return user_input
    except KeyboardInterrupt:
        logger.info("Input interrupted by user")
        handle_interrupt()
    except Exception as e:
        logger.error(f"Input error: {str(e)}")
        display_error(f"Input error: {str(e)}")
        raise

def confirm_action(prompt):
    """Request yes/no confirmation from user"""
    logger.debug(f"Requesting confirmation: {prompt}")
    def yes_no_validator(value):
        """Validate yes/no input variations"""
        return value.lower() in ['yes', 'no', 'y', 'n']
    
    try:
        response = get_input(
            f"{prompt} {Fore.LIGHTCYAN_EX}(yes/no){Style.RESET_ALL}", 
            validator=yes_no_validator
        )
        result = response.lower() in ['yes', 'y']
        logger.debug(f"User confirmed: {result}")
        return result
    except KeyboardInterrupt:
        logger.info("User interrupted confirmation prompt")
        print(f"\n{Fore.LIGHTYELLOW_EX}Operation cancelled by user{Style.RESET_ALL}")
        return False

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
    history = HistoryBar()
    
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

def process_menu_choice(choice, menu_actions):
    """
    Process menu selection including navigation options.
    
    Args:
        choice (str): User's menu selection
        menu_actions (dict): Dictionary of menu actions
    
    Returns:
        tuple: (bool, bool) - (should_exit, was_handled)
    """
    logger.debug(f"Processing menu choice: {choice}")
    history = HistoryBar()
    
    if choice.lower() == "x":
        logger.info("Exit requested")
        if confirm_action("Are you sure you want to exit?"):
            logger.info("User confirmed exit")
            return True, True
        logger.info("User cancelled exit")
        return False, True
        
    if choice.lower() == "b" and len(history.stack) > 1:
        logger.info("Back navigation requested")
        history.pop()
        return False, True
        
    return False, choice in menu_actions