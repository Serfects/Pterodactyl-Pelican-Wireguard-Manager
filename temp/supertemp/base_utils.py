"""
Core utilities and configuration for the PPWM application.

This module serves as the foundation for the application and should be imported first
by all other modules. It provides logging setup, error handling basics, and system
checks that don't depend on other application modules.

Module Dependencies:
- No internal dependencies (doesn't import from other project modules)
- Only uses standard library modules
"""
import os
import sys
import logging
import platform
from logging.handlers import RotatingFileHandler
from datetime import datetime
from pathlib import Path

# ========== General Constants ==========
SCREEN_WIDTH = 80  # Increased from 70 for modern terminals
APP_NAME = "PPWM"
APP_VERSION = "2.0.0"

# ========== Early Error Display ==========
def basic_error_display(message):
    """
    Display an error message with basic formatting.
    
    This function is used only for early errors before the full styled display
    functionality is available.
    
    Args:
        message (str): The error message to display
    """
    print(f"\n⚠ ERROR: {message}", file=sys.stderr)

# ========== System Check Functions ==========
def check_root():
    """
    Check if the script is running with root privileges.
    
    Exits with status code 1 if not running as root.
    """
    # Skip check on Windows - concept of root doesn't apply
    if platform.system() == 'Windows':
        return True
        
    if os.geteuid() != 0:
        basic_error_display("This application requires root privileges")
        input("\nPress Enter to exit...")
        sys.exit(1)
    return True

def can_write_to_dir(directory):
    """
    Check if the application can write to the specified directory.
    
    Args:
        directory (str): Directory path to check
        
    Returns:
        bool: True if the directory is writable, False otherwise
    """
    try:
        dir_path = Path(directory)
        # Create directory if it doesn't exist
        if not dir_path.exists():
            dir_path.mkdir(parents=True, exist_ok=True)
        
        # Test write access by attempting to create a temp file
        test_file = dir_path / ".write_test"
        test_file.touch()
        test_file.unlink()
        return True
    except (PermissionError, OSError):
        return False

# ========== System Information ==========
def get_system_info():
    """
    Get information about the system.
    
    Returns:
        dict: System information
    """
    return {
        'platform': platform.system(),
        'platform_version': platform.version(),
        'python_version': platform.python_version(),
        'machine': platform.machine(),
        'processor': platform.processor(),
        'hostname': platform.node(),
        'username': os.environ.get('USER') or os.environ.get('USERNAME') or 'unknown',
    }

# ========== Logging Setup ==========
def setup_logging():
    """
    Configure and initialize the logging system.
    
    Sets up file and console handlers with appropriate formatting and log levels.
    Configures log rotation to prevent log files from growing too large.
    
    Returns:
        logging.Logger: Configured root logger
    """
    # Constants for log rotation
    MAX_LOG_SIZE = 5 * 1024 * 1024  # 5 MB in bytes
    BACKUP_COUNT = 4  # Keep 4 backups (total of 5 files including current)

    # Determine appropriate log directory based on environment and platform
    system = platform.system()
    
    if system == 'Windows':
        # Windows logging path
        log_dir = os.path.join(os.environ.get('APPDATA', ''), 'ppwm', 'logs')
    elif system == 'Darwin':  # macOS
        # macOS logging path
        log_dir = os.path.expanduser('~/Library/Logs/ppwm')
    else:  # Linux/Unix
        if os.geteuid() == 0:  # Running as root
            log_dir = '/var/log/ppwm'
        else:  # Running as normal user
            log_dir = os.path.expanduser('~/.local/share/ppwm/logs')
    
    # Fallback to script directory if we can't write to system locations
    if not can_write_to_dir(log_dir):
        script_dir = Path(__file__).resolve().parent
        log_dir = script_dir.parent / 'logs'
        print(f"Warning: Cannot write to system log directories. Using local directory: {log_dir}")
    
    # Create logs directory if it doesn't exist
    try:
        Path(log_dir).mkdir(parents=True, exist_ok=True)
    except Exception as e:
        basic_error_display(f"Failed to create log directory: {str(e)}")
        sys.exit(1)

    # Configure log file path
    log_file = Path(log_dir) / 'ppwm.log'

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
            filename=str(log_file),
            maxBytes=MAX_LOG_SIZE,
            backupCount=BACKUP_COUNT,
            encoding='utf-8'
        )
        file_handler.setFormatter(file_formatter)
        file_handler.setLevel(logging.DEBUG)
    except Exception as e:
        basic_error_display(f"Failed to initialize logging: {str(e)}")
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

    # Log initial startup information with timestamp
    system_info = get_system_info()
    startup_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    root_logger.info(f"{APP_NAME} v{APP_VERSION} - Logging system initialized at {startup_time}")
    root_logger.debug(f"Log directory: {log_dir}")
    root_logger.debug(f"Python version: {system_info['python_version']}")
    root_logger.debug(f"Platform: {system_info['platform']} {system_info['platform_version']}")
    
    return root_logger

# ========== Custom Exceptions ==========
class AppError(Exception):
    """Base exception class for application-specific errors"""
    pass

# Initialize logger when the module is imported
logger = logging.getLogger(__name__)
logger = setup_logging()
logger.debug("base_utils module loaded")
