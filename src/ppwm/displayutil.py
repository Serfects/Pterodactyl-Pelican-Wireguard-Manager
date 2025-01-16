"""Display utilities for consistent terminal output."""

SCREEN_WIDTH = 80
BORDER_CHAR = "="
PADDING = 2

def center_text(text: str) -> str:
    """Center text within screen width."""
    return text.center(SCREEN_WIDTH)

def create_border() -> str:
    """Create border line of defined width."""
    return BORDER_CHAR * SCREEN_WIDTH

def format_option(key: str, text: str) -> str:
    """Format menu option with consistent padding."""
    return " " * PADDING + f"{key}. {text}"