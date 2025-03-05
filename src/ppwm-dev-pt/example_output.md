# MULTI-SELECTION INTERFACE EXAMPLES

============================================================
# Example 1: Interactive Checkbox Interface (Current Implementation)
============================================================
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::        ____       ____  ______        ____  __       ____        ::
::        \ \ \     |  _ \|  _ \ \      / /  \/  |     / / /        ::
::         \ \ \    | |_) | |_) \ \ /\ / /| |\/| |    / / /         ::
::         / / /    |  __/|  __/ \ V  V / | |  | |    \ \ \         ::
::        /_/_/     |_|   |_|     \_/\_/  |_|  |_|     \_\_\        ::
::                                                                  ::
::               Pterodactyl-Pelican-Wireguard-Manager              ::
::                           By: Serfects                           ::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
                         VPS Setup Wizard                               
──────────────────────────────────────────────────────────────────────

Select services to enable on the VPS

Use arrow keys or numbers to navigate, space to select, and enter to confirm.
Press 'a' to select all, 'n' to deselect all, 'i' to invert selection

▸ [x] HTTP/HTTPS Web Server
     Basic web server for hosting panel interfaces
  
  [ ] DNS Server
     For domain name resolution and management
  
  [x] SSH Server
     Remote access with enhanced security
  
  [ ] Email Server
     For sending notifications and alerts
  
  [x] Monitoring Tools
     System performance and health tracking

Press Enter when finished selecting options


============================================================
# Example 2: Text-Based Selection (Simple Alternative)
============================================================
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::        ____       ____  ______        ____  __       ____        ::
::        \ \ \     |  _ \|  _ \ \      / /  \/  |     / / /        ::
::         \ \ \    | |_) | |_) \ \ /\ / /| |\/| |    / / /         ::
::         / / /    |  __/|  __/ \ V  V / | |  | |    \ \ \         ::
::        /_/_/     |_|   |_|     \_/\_/  |_|  |_|     \_\_\        ::
::                                                                  ::
::               Pterodactyl-Pelican-Wireguard-Manager              ::
::                           By: Serfects                           ::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
                         VPS Setup Wizard                               
──────────────────────────────────────────────────────────────────────

Select services to enable on the VPS

Available options:
1. HTTP/HTTPS Web Server
   Basic web server for hosting panel interfaces
2. DNS Server
   For domain name resolution and management
3. SSH Server
   Remote access with enhanced security
4. Email Server
   For sending notifications and alerts
5. Monitoring Tools
   System performance and health tracking

Enter numbers for selected options (comma separated, e.g. 1,3,5): 1,3,5

Services selected: HTTP/HTTPS Web Server, SSH Server, Monitoring Tools

Press Enter to continue...


============================================================
# Example 3: Progressive Selection Interface
============================================================
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::        ____       ____  ______        ____  __       ____        ::
::        \ \ \     |  _ \|  _ \ \      / /  \/  |     / / /        ::
::         \ \ \    | |_) | |_) \ \ /\ / /| |\/| |    / / /         ::
::         / / /    |  __/|  __/ \ V  V / | |  | |    \ \ \         ::
::        /_/_/     |_|   |_|     \_/\_/  |_|  |_|     \_\_\        ::
::                                                                  ::
::               Pterodactyl-Pelican-Wireguard-Manager              ::
::                           By: Serfects                           ::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
                         VPS Setup Wizard                               
──────────────────────────────────────────────────────────────────────

Select services to enable on the VPS

Current selections:
1. [x] HTTP/HTTPS Web Server
2. [ ] DNS Server
3. [x] SSH Server
4. [ ] Email Server
5. [x] Monitoring Tools

Commands: [number] toggle, a (all), n (none), i (invert), d (done)

Command: 2

Current selections:
1. [x] HTTP/HTTPS Web Server
2. [x] DNS Server
3. [x] SSH Server
4. [ ] Email Server
5. [x] Monitoring Tools

Commands: [number] toggle, a (all), n (none), i (invert), d (done)

Command: d

Services selected: HTTP/HTTPS Web Server, DNS Server, SSH Server, Monitoring Tools

Press Enter to continue...


============================================================
# Example 4: Library-Based Dialog (prompt_toolkit)
============================================================
┌─ Select services to enable on the VPS ───────────────────────────┐
│                                                                  │
│ ❯ ☑ HTTP/HTTPS Web Server                                        │
│   ☐ DNS Server                                                   │
│   ☑ SSH Server                                                   │
│   ☐ Email Server                                                 │
│   ☑ Monitoring Tools                                             │
│                                                                  │
│                                                                  │
│                          < OK > < Cancel >                       │
└──────────────────────────────────────────────────────────────────┘

Console info: Use arrow keys to move, <space> to select, <enter> to accept


============================================================
# Example 5: Textual TUI Framework
============================================================
┏━━ PPWM Setup Wizard ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                                                                  ┃
┃                  Select services to enable on the VPS            ┃
┃                                                                  ┃
┃  [x] HTTP/HTTPS Web Server                                       ┃
┃      Basic web server for hosting panel interfaces               ┃
┃                                                                  ┃
┃  [ ] DNS Server                                                  ┃
┃      For domain name resolution and management                   ┃
┃                                                                  ┃
┃  [x] SSH Server                                                  ┃
┃      Remote access with enhanced security                        ┃
┃                                                                  ┃
┃  [ ] Email Server                                                ┃
┃      For sending notifications and alerts                        ┃
┃                                                                  ┃
┃  [x] Monitoring Tools                                            ┃
┃      System performance and health tracking                      ┃
┃                                                                  ┃
┃                                                                  ┃
┃                                                                  ┃
┃             [  Select All  ]  [  Confirm  ]  [  Cancel  ]        ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛

# Benefits of Textual TUI framework:
- Rich UI components with responsive layouts
- Event-driven architecture similar to web frameworks
- Handles keyboard, mouse, and terminal resize events
- Cross-platform support for most terminal emulators
- Theming and styling capabilities
- Built-in widgets like SelectionList specifically for multiple selection
- Can scale to full application UI with minimal code

# Considerations:
- More dependencies (installs textual and its requirements)
- Higher learning curve compared to simple CLI interfaces
- May not work well in all terminal environments (especially basic SSH clients)
- Requires more substantial code changes to integrate with existing app
- Not compatible with older terminals lacking modern features

# PPWM DEVELOPMENT STANDARDS - PROMPT_TOOLKIT VERSION

## UI Framework & Requirements

- **Primary UI Framework:** 
  - Use prompt_toolkit (v3.0.38+) for all user interface components
  - Python 3.11+ is the target runtime environment
  - No colorama dependency (use prompt_toolkit's styling instead)
  - Use pygments for syntax highlighting in configuration editors

- **Directory Structure:**
  - Place all code in `/workspaces/Pterodactyl-Pelican-Wireguard-Manager/src/ppwm-dev-pt/`
  - Keep dependency.md in the same directory as the source code
  - Organize module dependencies with utility modules at the lowest level

## Interface Design Principles

- **Keyboard-First Navigation:**
  - All UI elements must be fully accessible and operable via keyboard
  - Define logical tab order for all interactive elements
  - Use keyboard shortcuts for common actions (provide on-screen hints)
  - Mouse support should be implemented but always remain optional

- **Terminal Compatibility:**
  - Design for modern terminal emulators with 256 color or true color support
  - Implement graceful fallbacks for color depth and formatting
  - Handle terminal resizing appropriately
  - Minimum recommended terminal size is 80x24 characters

- **Styling & Consistency:**
  - Use PPWM_STYLE dictionary in pt_components.py for all UI styling
  - Follow the established color scheme:
    - Primary blue (#3498db) for highlights, buttons, and focus
    - Success green (#2ecc71) for completion and positive feedback
    - Error red (#e74c3c) for errors and destructive actions
    - Warning yellow (#f39c12) for warnings and cautions
  - Use consistent symbols for status indicators (✓, ⚠, etc.)
  - Use HTML formatting (`<tag>text</tag>`) for all styled text

## Implementation Guidelines

- **Module Structure:**
  - Import pt_components.py as the base for all UI functionality
  - Use functions like show_message(), prompt_input(), show_progress_bar()
  - Avoid direct terminal manipulation (clear screen, cursor movement)

- **Dialog Components:**
  - All dialogs should use prompt_toolkit dialog components
  - Dialog title should clearly indicate the dialog's purpose
  - Include keyboard shortcut reminders in dialog text or bottom toolbar
  - Ensure proper dialog focus management

- **Form Input:**
  - Implement validation feedback with clear error messages
  - Provide sensible defaults when appropriate
  - Use auto-completion where it enhances usability
  - Support cancellation (Escape) and confirmation (Enter) 

- **Progress Indicators:**
  - Use deterministic progress bars when the total work is known
  - Use indeterminate progress indicators for unknown duration operations
  - Show operation status messages during longer processes

- **Menu Systems:**
  - Implement keyboard shortcuts for navigation
  - Ensure consistent menu structure and navigation
  - Support both number keys and arrow keys for selection

## Accessibility Considerations

- **Screen Reader Compatibility:**
  - Use descriptive labels for all interactive elements
  - Ensure all error messages and important feedback can be reviewed

- **Terminal Environment:**
  - Check terminal capabilities at startup (color support, size)
  - Warn users if terminal dimensions are below recommended size
  - Adapt to different terminal environments when possible

- **Feedback & Status:**
  - Provide clear success/error messaging after operations
  - Use bottom toolbar for contextual help and status updates
  - Support clipboard operations where appropriate




# SUPPLEMENTARY PROMPT_TOOLKIT INSTRUCTIONS

These instructions specifically apply to the prompt_toolkit version of PPWM and should be considered as extensions to the main instructions rather than replacements.

## Version-Specific Framework Guidelines

- **Transition from Standard to PT Version:**
  - The prompt_toolkit version (ppwm-dev-pt) is a parallel development path
  - When adapting code from ppwm-dev to ppwm-dev-pt, integrate with prompt_toolkit components
  - Replace direct terminal operations with prompt_toolkit equivalents

- **Component Usage Hierarchy:**
  - First try to use existing pt_components.py functions
  - For new UI elements, use prompt_toolkit shortcuts (e.g., dialog functions)
  - Only create custom widgets when necessary for specialized functionality

- **HTML Formatting Over ANSI:**
  - Replace Colorama's Fore/Style with HTML-style formatting tags
  - Convert: `Fore.RED + "text" + Style.RESET_ALL` → `"<ansired>text</ansired>"`
  - Use HTML() constructor for complex or dynamic formatting

- **Managing Terminal State:**
  - Use prompt_toolkit's ApplicationState for persistent UI state
  - Avoid direct modification of terminal settings (cursor position, etc.)
  - Use Layout objects for complex UI arrangements instead of print statements

## Interface Development Best Practices

- **Key Bindings Integration:**
  - Use KeyBindings objects for keyboard shortcuts
  - Register common keys consistently (Esc for back/cancel, etc.)
  - Document keyboard shortcuts in UI and help screens

- **Display Flow Control:**
  - Use nested dialogs instead of clearing screen and redrawing
  - Maintain state between UI interactions through proper object design
  - Consider using Application objects for complex multi-page workflows

- **Validation Patterns:**
  - Use prompt_toolkit's Validator classes for input validation
  - Show validation errors inline rather than as separate errors
  - Validate incrementally when possible (as user types)










Serfects: is it possible to give prompt_toolkit optional mouse support? I dont want you to do anything, I just want to know if it supports that feature

GitHub Copilot: Yes, Logan, prompt_toolkit does support optional mouse support. You can enable it by setting the `mouse_support=True` parameter when creating applications or dialogs.

When enabled, prompt_toolkit allows users to:
- Click on UI elements like buttons and checkboxes
- Position the cursor by clicking
- Select text with mouse dragging
- Scroll through content
- Navigate through menus

The mouse support works in most modern terminal emulators that support mouse reporting protocols. You can enable it selectively for specific features or make it a global setting. It's completely optional and can be toggled on or off based on user preferences or terminal capabilities.

For example, when creating a prompt, you would use:
```python
prompt_toolkit.prompt('Enter something: ', mouse_support=True)
```

Or for an application:
```python
Application(mouse_support=True, ...)
```

Serfects: For the newest version of prompt_toolkit that you have available to you, what text colors does prompt_toolkit support? Does it also support text size?

GitHub Copilot: Logan, based on the latest versions of prompt_toolkit:

### Text Colors in prompt_toolkit

prompt_toolkit supports a wide range of text colors through both HTML-like formatting and ANSI color codes:

1. **Basic ANSI colors**:
   - `<ansired>`, `<ansigreen>`, `<ansiyellow>`, `<ansiblue>`
   - `<ansimagenta>`, `<ansicyan>`, `<ansiwhite>`, `<ansiblack>`
   - `<ansigray>`

2. **Bright ANSI colors**:
   - `<ansibright-red>`, `<ansibright-green>`, `<ansibright-yellow>`, etc.

3. **Background colors**:
   - `<bg:colorname>` or `<style bg="colorname">`

4. **RGB colors**:
   - `<#ff0000>` (hex color codes)
   - `<rgb: r,g,b>` format 

5. **Custom named colors** (defined in your Style object)

### Text Size

prompt_toolkit does **not** support text size changes. Since it runs in a terminal, it's limited to the terminal's font size settings. The terminal typically uses a single font size for all content.

Instead of size variations, you can use:
- `<b>` for bold
- `<i>` for italics 
- `<u>` for underline
- Color variations for emphasis

These styling options create visual hierarchy without changing the actual text size.

Serfects: Got it, so in your opinion, it would be much easier to convert the current script to using prompt_toolkit rather than converting it to textual. And prompt_toolkit has a lot of the same features of textual, just kind of more dumbed down and overall simpler.

GitHub Copilot: Yes Logan, you've captured it perfectly. Converting the current script to use prompt_toolkit would be significantly easier than migrating to Textual for several reasons:

### Why prompt_toolkit is the Easier Path

1. **Evolution vs. Revolution**: prompt_toolkit would be an evolution of your current CLI approach, while Textual would require a full redesign as a TUI application.

2. **Code Reuse**: Your existing menu structure, input handling, and navigation system can largely be maintained with prompt_toolkit, just enhanced with better dialogs and styling.

3. **Learning Curve**: prompt_toolkit has a gentler learning curve and follows patterns closer to your current implementation.

4. **Dependencies**: Lighter weight with fewer dependencies than Textual.

### Features prompt_toolkit Shares with Textual

- Multiple selection interfaces (checkbox lists, radio buttons)
- Rich text formatting and colors
- Dialog boxes and formatted prompts
- Progress indicators
- Mouse support (which you asked about earlier)
- Command history and tab completion

prompt_toolkit is essentially a middle ground - more powerful than raw terminal input/output but less complex than a full TUI framework like Textual. It would give you most of the UI enhancements you'd want without requiring a complete rewrite of your application architecture.

Serfects: Do you think prompt_toolkit could have a text editor similar to what you had in the example textual script?

GitHub Copilot: Yes Logan, prompt_toolkit absolutely supports text editors similar to what was shown in the Textual example. The prompt_toolkit library includes robust text editing components that can be configured for various use cases:

### Text Editor Capabilities in prompt_toolkit

1. **Multi-line Editing**:
   - `TextArea` widget provides a full-featured multi-line editor
   - Supports scrolling, cursor positioning, and text selection

2. **Syntax Highlighting**:
   - Uses Pygments library for language-specific syntax highlighting
   - Supports the same languages as Textual (including INI, Python, etc.)

3. **Key Bindings**:
   - Custom keyboard shortcuts (like Ctrl+S for save)
   - Emacs and Vi key binding modes built in
   - Customizable keymaps for application-specific needs

4. **Editor Features**:
   - Line numbers
   - Search and replace
   - Copy/paste functionality
   - Undo/redo support
   - Auto-indentation

Here's an abbreviated example of how you could create a configuration editor with prompt_toolkit:

```python
from prompt_toolkit import Application
from prompt_toolkit.layout.containers import HSplit, Window
from prompt_toolkit.layout.layout import Layout
from prompt_toolkit.widgets import TextArea, Frame, Button
from prompt_toolkit.lexers import PygmentsLexer
from pygments.lexers.configs import IniLexer

# Create text area with syntax highlighting
editor = TextArea(
    lexer=PygmentsLexer(IniLexer),
    text=initial_config_text,
    line_numbers=True,
)

# Add key bindings for save
kb = KeyBindings()
@kb.add('c-s')
def _(event):
    # Save file logic here
    print("Saving file...")

# Create layout with editor and buttons
layout = Layout(
    HSplit([
        Frame(title="WireGuard Configuration Editor", body=editor),
        Window(height=1),  # Spacer
        Window(content=FormattedTextControl("Ctrl-S: Save | Esc: Back"))
    ])
)

# Create and run application
app = Application(
    layout=layout,
    key_bindings=kb,
    full_screen=True,
)
app.run()
```

This gives you a very capable text editor that's similar to what was shown in the Textual example, but with prompt_toolkit's architecture.

Serfects: Got it, okay. Thank you for the information. Here is what we are going to do. I have made a new directory called ppwm-dev-pt located at /workspaces/Pterodactyl-Pelican-Wireguard-Manager/src/ppwm-dev-pt . All of the files from the main script that we have been working on have been copied to this directory. I want to use this new directory and the copied files to attempt to begin to convert the current script over to using prompt_toolkit for the UI. I want to take this is steps, going module by module as to not hit the response limit. I want to keep as much of the current color scheme as we can, but the rest is up to you to modify however you feel would look best for the new converted UI.

GitHub Copilot: # Converting PPWM to Use prompt_toolkit UI

Logan, I understand you want to convert the existing PPWM application to use prompt_toolkit incrementally while keeping the current color scheme. I'll approach this systematically, module by module, starting with the most essential components.

## Section 1: Initial Setup and Basic Dependencies

First, let's create a new module to handle prompt_toolkit-specific UI components and update the dependencies.

### [pt_components.py](vscode-remote://codespaces/workspaces/Pterodactyl-Pelican-Wireguard-Manager/src/ppwm-dev-pt/pt_components.py)

This new module will serve as the bridge between our application and prompt_toolkit's UI capabilities:

```python
"""
prompt_toolkit UI components for PPWM application.

This module provides specialized UI components built with prompt_toolkit
that replace the traditional terminal-based UI. It includes enhanced input
prompts, dialogs, menus, and formatted text display capabilities.

Module Dependencies:
- base_utils.py: For logging and constants
- No circular dependencies with other modules
"""
import logging
import os
from prompt_toolkit import prompt, HTML
from prompt_toolkit.styles import Style
from prompt_toolkit.formatted_text import HTML, FormattedText
from prompt_toolkit.shortcuts import (
    clear, input_dialog, message_dialog, yes_no_dialog,
    button_dialog, checkboxlist_dialog, radiolist_dialog
)
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.validation import Validator, ValidationError
from base_utils import AppError, SCREEN_WIDTH

# Initialize logger for this module
logger = logging.getLogger(__name__)

# ========== Custom Exceptions ==========
class UIComponentError(AppError):
    """Exception raised for prompt_toolkit UI component errors"""
    pass

# ========== Global Styles ==========
# Using a similar color scheme to the original application
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
    'text-area.cursor': 'bg:#ffffff #000000',
    
    # Selection components
    'checkbox': '#3498db',
    'checkbox-list': 'bg:#171717 #ffffff',
    'checkbox-selected': 'bg:#2980b9 #ffffff',
    
    # Radio buttons
    'radio': '#3498db',
    'radio-checked': '#3498db',
    'radio-selected': 'bg:#2980b9 #ffffff',
    
    # Messages
    'success-text': '#2ecc71',
    'error-text': '#e74c3c',
    'warning-text': '#f39c12',
    'info-text': '#3498db',
})

# ========== Helper Functions ==========
def convert_ansi_to_html(ansi_text):
    """
    Convert ANSI color codes to HTML format for prompt_toolkit.
    
    Args:
        ansi_text (str): Text with ANSI escape sequences
        
    Returns:
        str: HTML formatted text for prompt_toolkit
    """
    # This is a simplified conversion - a more complete version would handle more ANSI codes
    html_text = ansi_text
    
    # Basic ANSI to HTML conversions
    conversions = [
        # Bright/Light colors
        ('\033[1;31m', '<ansired>'),     # Light Red
        ('\033[1;32m', '<ansigreen>'),   # Light Green
        ('\033[1;33m', '<ansiyellow>'),  # Light Yellow
        ('\033[1;34m', '<ansiblue>'),    # Light Blue
        ('\033[1;35m', '<ansimagenta>'), # Light Magenta
        ('\033[1;36m', '<ansicyan>'),    # Light Cyan
        ('\033[1;37m', '<ansiwhite>'),   # Light White
        
        # Regular colors
        ('\033[0;31m', '<ansired>'),     # Red
        ('\033[0;32m', '<ansigreen>'),   # Green
        ('\033[0;33m', '<ansiyellow>'),  # Yellow
        ('\033[0;34m', '<ansiblue>'),    # Blue
        ('\033[0;35m', '<ansimagenta>'), # Magenta
        ('\033[0;36m', '<ansicyan>'),    # Cyan
        
        # Text formatting
        ('\033[1m', '<b>'),              # Bold
        ('\033[3m', '<i>'),              # Italic
        ('\033[4m', '<u>'),              # Underline
        
        # Reset
        ('\033[0m', '</>')               # Reset
    ]
    
    # Apply conversions
    for ansi, html in conversions:
        html_text = html_text.replace(ansi, html)
    
    # Handle any remaining ANSI escape sequences
    import re
    html_text = re.sub(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])', '', html_text)
    
    return html_text

def clear_screen():
    """
    Clear the terminal screen using prompt_toolkit's clear function.
    """
    clear()
    logger.debug("Screen cleared using prompt_toolkit")

# ========== Basic UI Components ==========
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
    
    # Convert potential ANSI codes to HTML
    if '<ansi' not in text and '\033[' in text:
        text = convert_ansi_to_html(text)
    
    # Display the message
    message_dialog(
        title=title,
        text=HTML(text),
        style=used_style
    ).run()

def show_error_dialog(message, title="Error"):
    """
    Display an error message dialog.
    
    Args:
        message (str): Error message to display
        title (str, optional): Dialog title. Defaults to "Error".
    """
    logger.error(message)
    styled_message = f"<ansired>⚠ {message}</ansired>"
    show_message(title, styled_message)

def show_success_dialog(message, title="Success"):
    """
    Display a success message dialog.
    
    Args:
        message (str): Success message to display
        title (str, optional): Dialog title. Defaults to "Success".
    """
    logger.info(message)
    styled_message = f"<ansigreen>✓ {message}</ansigreen>"
    show_message(title, styled_message)

def show_warning_dialog(message, title="Warning"):
    """
    Display a warning message dialog.
    
    Args:
        message (str): Warning message to display
        title (str, optional): Dialog title. Defaults to "Warning".
    """
    logger.warning(message)
    styled_message = f"<ansiyellow>⚠ {message}</ansiyellow>"
    show_message(title, styled_message)

# ========== Enhanced Input Functions ==========
def prompt_input(prompt_text, default="", validator=None, completer=None, style=None):
    """
    Get user input with enhanced features from prompt_toolkit.
    
    Args:
        prompt_text (str): The prompt text to display
        default (str, optional): Default value. Defaults to empty string.
        validator (callable, optional): Validation function. Defaults to None.
        completer (Completer, optional): Auto-completion. Defaults to None.
        style (Style, optional): Custom style. Defaults to PPWM_STYLE.
    
    Returns:
        str: The user's input text
    
    Raises:
        KeyboardInterrupt: If user cancels input with Ctrl+C
    """
    logger.debug(f"Prompting user for input: {prompt_text}")
    used_style = style if style else PPWM_STYLE
    
    # Convert potential ANSI codes to HTML for the prompt text
    if '<ansi' not in prompt_text and '\033[' in prompt_text:
        prompt_text = convert_ansi_to_html(prompt_text)
    
    # Create a validator if provided with a validation function
    class InputValidator(Validator):
        def validate(self, document):
            if validator and not validator(document.text):
                raise ValidationError(message="Invalid input")
    
    # Get input from user
    try:
        result = prompt(
            HTML(prompt_text),
            default=default,
            validator=InputValidator() if validator else None,
            completer=completer,
            style=used_style
        )
        logger.debug(f"User input received: {result}")
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
    
    # Convert potential ANSI codes to HTML
    if '<ansi' not in prompt_text and '\033[' in prompt_text:
        prompt_text = convert_ansi_to_html(prompt_text)
    
    # Display confirmation dialog
    result = yes_no_dialog(
        title=title,
        text=HTML(prompt_text),
        yes_text=yes_text,
        no_text=no_text,
        style=used_style
    ).run()
    
    logger.debug(f"Confirmation result: {result}")
    return result

# Initialize the module
logger.debug("pt_components module loaded")
```

### [dependency.md](vscode-remote://codespaces/workspaces/Pterodactyl-Pelican-Wireguard-Manager/dependency.md)

Let's update (or create) the dependency file to include prompt_toolkit:

```markdown


Made changes.

# PPWM Project Dependencies

This file documents the external dependencies required for the project.

## Core Dependencies

- **colorama** (>=0.4.4)
  - Used for terminal text coloring and formatting
  - Required for both the original CLI version and prompt_toolkit version

- **prompt_toolkit** (>=3.0.0)
  - Used for enhanced terminal UI components
  - Features: styled dialogs, interactive menus, text highlighting
  - Required only for the prompt_toolkit version (ppwm-dev-pt)

- **pygments** (>=2.7.0)
  - Used for syntax highlighting in configuration file editing
  - Required only when using the configuration editor feature

## Installation

These dependencies can be installed via pip:

```bash
pip install colorama prompt-toolkit pygments
```

## Version Notes

The prompt_toolkit version (3.0+) includes many UI improvements but may have compatibility 
issues with very old terminals. The standard version using just colorama should work on 
virtually all terminal emulators.
```

------
That completes Section 1. Would you like me to proceed with Section 2: Enhancing Input Functions by updating the input_utils.py module to use prompt_toolkit, or would you prefer to review these changes first?
------

Made changes.

Serfects: I want to build this script using the newest stable versions of everything that we are going to use, including python, as long as all of the versions of all of the things that we are going to include are compatable with each other, which they should be. I am not worried about very very old terminals. Odds are if the user is using this script in the first place, they are on a newer more modern terminal anyway. Please update the dependencies to use the newest stable versions of everything that we are using in this script that you have available to you, including pythong. And then we can work on updating the code of each module to reflect the newest stable versions of everything, including python. If the newer versions of prompt_toolkit handles colors and styling of text on its own, I would like to use the features built into prompt_toolkit for coloring and style, so we can drop colorama unless it is necessary for something else. Like i said, i am not worried about the super old terminals. We are building this to be modern, while having compatability across many modern systems.

GitHub Copilot: # Updating PPWM for Modern Terminal Environments

Logan, I'll update the project to use the newest stable versions of all dependencies and focus on modern terminals. Let's start with updating the dependencies and then we'll work on modernizing the code.

## Section 1: Updating Dependencies and Core Components

### [dependency.md](vscode-remote://codespaces/workspaces/Pterodactyl-Pelican-Wireguard-Manager/dependency.md)

```markdown
# PPWM Project Dependencies

This file documents the external dependencies required for the project.

## Core Dependencies

- **Python** (>=3.11)
  - The application is built on Python 3.11+
  - Takes advantage of modern Python features for better performance and reliability

- **prompt_toolkit** (>=3.0.38)
  - Used for modern terminal UI components
  - Features: styled dialogs, interactive menus, text highlighting, mouse support
  - Provides consistent styling across different terminal emulators
  - Handles all terminal color and formatting needs

- **pygments** (>=2.15.1)
  - Used for syntax highlighting in configuration file editing
  - Required when using the configuration editor feature

## Optional Dependencies

- **pyperclip** (>=1.8.2)
  - Used for clipboard operations (copy/paste)
  - Enhances user experience with text manipulation

## Installation

These dependencies can be installed via pip:

```bash
pip install "prompt-toolkit>=3.0.38" "pygments>=2.15.1" "pyperclip>=1.8.2"
```

## Notes

The application is designed for modern terminals and does not require colorama, as prompt_toolkit handles terminal styling across platforms. This provides a more consistent and feature-rich user interface.

For best results, use a terminal that supports:
- 256 colors or true color
- Unicode characters
- Mouse events (optional, enhances usability)
```

### [pt_components.py](vscode-remote://codespaces/workspaces/Pterodactyl-Pelican-Wireguard-Manager/src/ppwm-dev-pt/pt_components.py)

I'll now update the component module to use prompt_toolkit's native styling:

```python


Made changes.

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
```

### [base_utils.py](vscode-remote://codespaces/workspaces/Pterodactyl-Pelican-Wireguard-Manager/src/ppwm-dev-pt/base_utils.py)

Now, let's update the base_utils.py to work without colorama and use more modern Python capabilities:

```python


Made changes.

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
```

------
That completes Section 1. Would you like me to proceed with Section 2: Updating Input Utilities to use prompt_toolkit, or would you prefer to review these changes first?
------

Made changes.

Serfects: I am going to move the dependency.md file into the same ppwm-dev-pt directory as the rest of the files, and I just wanted to let you know that so you are aware of the change. I think it will keep things more organized for now, unless that is going to be a problem. Also, I want to add that I want all of the UI components of prompt_toolkit that we are updating in the codebase of this project to be primarily compatible and optimized with just keyboard inputs, with mouse support being entirely optional for all aspects of the UI that will be displayed to the user.

Seperately, with the changes that we are making to the main script and all of the new specifications that we have now have set moving forward, I think it would be helpful for you to generate a new block of system instructions/copilot-instuctions that I can add to your current instructions file to make following the new standards and normals that we have set within this conversation, easier to follow across multiple sessions and for any edits/additions/modifications that will be done in the future of this project. Please add the new block of instructions to the bottom of the example_output.md file with the new instructions that you feel are best to properly convey to Copilot the new and or changed standards and specifications that we have been going over. I will then add it to the overall copilot-instructions.md file.

GitHub Copilot: I understand both requests, Logan. Moving the dependency.md file into the ppwm-dev-pt directory makes sense for better organization. There won't be any problems with that approach.

Regarding the keyboard-first UI with optional mouse support, I'll make sure all future components follow this principle, ensuring every feature is fully accessible via keyboard navigation while offering mouse support as a convenience.

I'll add the new instruction block to the example_output.md file as requested.

```markdown
# MULTI-SELECTION INTERFACE EXAMPLES

============================================================
# Example 1: Interactive Checkbox Interface (Current Implementation)
============================================================
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::        ____       ____  ______        ____  __       ____        ::
::        \ \ \     |  _ \|  _ \ \      / /  \/  |     / / /        ::
::         \ \ \    | |_) | |_) \ \ /\ / /| |\/| |    / / /         ::
::         / / /    |  __/|  __/ \ V  V / | |  | |    \ \ \         ::
::        /_/_/     |_|   |_|     \_/\_/  |_|  |_|     \_\_\        ::
::                                                                  ::
::               Pterodactyl-Pelican-Wireguard-Manager              ::
::                           By: Serfects                           ::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
                         VPS Setup Wizard                               
──────────────────────────────────────────────────────────────────────

Select services to enable on the VPS

Use arrow keys or numbers to navigate, space to select, and enter to confirm.
Press 'a' to select all, 'n' to deselect all, 'i' to invert selection

▸ [x] HTTP/HTTPS Web Server
     Basic web server for hosting panel interfaces
  
  [ ] DNS Server
     For domain name resolution and management
  
  [x] SSH Server
     Remote access with enhanced security
  
  [ ] Email Server
     For sending notifications and alerts
  
  [x] Monitoring Tools
     System performance and health tracking

Press Enter when finished selecting options

// ...existing code...

# PPWM DEVELOPMENT STANDARDS - PROMPT_TOOLKIT VERSION

## UI Framework & Requirements

- **Primary UI Framework:** 
  - Use prompt_toolkit (v3.0.38+) for all user interface components
  - Python 3.11+ is the target runtime environment
  - No colorama dependency (use prompt_toolkit's styling instead)
  - Use pygments for syntax highlighting in configuration editors

- **Directory Structure:**
  - Place all code in `/workspaces/Pterodactyl-Pelican-Wireguard-Manager/src/ppwm-dev-pt/`
  - Keep dependency.md in the same directory as the source code
  - Organize module dependencies with utility modules at the lowest level

## Interface Design Principles

- **Keyboard-First Navigation:**
  - All UI elements must be fully accessible and operable via keyboard
  - Define logical tab order for all interactive elements
  - Use keyboard shortcuts for common actions (provide on-screen hints)
  - Mouse support should be implemented but always remain optional

- **Terminal Compatibility:**
  - Design for modern terminal emulators with 256 color or true color support
  - Implement graceful fallbacks for color depth and formatting
  - Handle terminal resizing appropriately
  - Minimum recommended terminal size is 80x24 characters

- **Styling & Consistency:**
  - Use PPWM_STYLE dictionary in pt_components.py for all UI styling
  - Follow the established color scheme:
    - Primary blue (#3498db) for highlights, buttons, and focus
    - Success green (#2ecc71) for completion and positive feedback
    - Error red (#e74c3c) for errors and destructive actions
    - Warning yellow (#f39c12) for warnings and cautions
  - Use consistent symbols for status indicators (✓, ⚠, etc.)
  - Use HTML formatting (`<tag>text</tag>`) for all styled text

## Implementation Guidelines

- **Module Structure:**
  - Import pt_components.py as the base for all UI functionality
  - Use functions like show_message(), prompt_input(), show_progress_bar()
  - Avoid direct terminal manipulation (clear screen, cursor movement)

- **Dialog Components:**
  - All dialogs should use prompt_toolkit dialog components
  - Dialog title should clearly indicate the dialog's purpose
  - Include keyboard shortcut reminders in dialog text or bottom toolbar
  - Ensure proper dialog focus management

- **Form Input:**
  - Implement validation feedback with clear error messages
  - Provide sensible defaults when appropriate
  - Use auto-completion where it enhances usability
  - Support cancellation (Escape) and confirmation (Enter) 

- **Progress Indicators:**
  - Use deterministic progress bars when the total work is known
  - Use indeterminate progress indicators for unknown duration operations
  - Show operation status messages during longer processes

- **Menu Systems:**
  - Implement keyboard shortcuts for navigation
  - Ensure consistent menu structure and navigation
  - Support both number keys and arrow keys for selection

## Accessibility Considerations

- **Screen Reader Compatibility:**
  - Use descriptive labels for all interactive elements
  - Ensure all error messages and important feedback can be reviewed

- **Terminal Environment:**
  - Check terminal capabilities at startup (color support, size)
  - Warn users if terminal dimensions are below recommended size
  - Adapt to different terminal environments when possible

- **Feedback & Status:**
  - Provide clear success/error messaging after operations
  - Use bottom toolbar for contextual help and status updates
  - Support clipboard operations where appropriate
```


Made changes.

Similar code found with 3 license types

Serfects: I am now including the copilot-insturctions.md file as a reference. Do not edit the copilot-instructions.md file. I want you to look at the copilot-instructions.md file, and compare it to the instructions block that you just wrote at the bottom of the example_output.md file. I want you to verify that the new instructions that you wrote arent duplicating any already existing instructions that are currently in the copilot-instructions.md file. If part of the new instructions you just wrote are duplicating previously existing instructions, I want you to rewrite the new instruction in a way that doesnt restate any of the previously existing instructions, unless it is absolutely necessary to make sure the new instruction is understood correctly by copilot. My main goal is to not have any redundent or counter/opposite instructions that will degrade copilots ability to follow the instructions. Please add the new version of the block of new instructions that follow these directions below the other new instructions that you just created in the example_output.md file.

GitHub Copilot: Looking at the copilot-instructions.md file and comparing it to the new instructions I wrote, I see several areas where my additions duplicate or potentially conflict with existing guidelines. Let me create a revised version that complements rather than duplicates the existing instructions:

```markdown
# MULTI-SELECTION INTERFACE EXAMPLES

// ...existing code...

# PPWM DEVELOPMENT STANDARDS - PROMPT_TOOLKIT VERSION

## UI Framework & Requirements

- **Primary UI Framework:** 
  - Use prompt_toolkit (v3.0.38+) for all user interface components
  - Python 3.11+ is the target runtime environment
  - No colorama dependency (use prompt_toolkit's styling instead)
  - Use pygments for syntax highlighting in configuration editors

- **Directory Structure:**
  - Place all code in `/workspaces/Pterodactyl-Pelican-Wireguard-Manager/src/ppwm-dev-pt/`
  - Keep dependency.md in the same directory as the source code
  - Organize module dependencies with utility modules at the lowest level

## Interface Design Principles

- **Keyboard-First Navigation:**
  - All UI elements must be fully accessible and operable via keyboard
  - Define logical tab order for all interactive elements
  - Use keyboard shortcuts for common actions (provide on-screen hints)
  - Mouse support should be implemented but always remain optional

- **Terminal Compatibility:**
  - Design for modern terminal emulators with 256 color or true color support
  - Implement graceful fallbacks for color depth and formatting
  - Handle terminal resizing appropriately
  - Minimum recommended terminal size is 80x24 characters

- **Styling & Consistency:**
  - Use PPWM_STYLE dictionary in pt_components.py for all UI styling
  - Follow the established color scheme:
    - Primary blue (#3498db) for highlights, buttons, and focus
    - Success green (#2ecc71) for completion and positive feedback
    - Error red (#e74c3c) for errors and destructive actions
    - Warning yellow (#f39c12) for warnings and cautions
  - Use consistent symbols for status indicators (✓, ⚠, etc.)
  - Use HTML formatting (`<tag>text</tag>`) for all styled text

## Implementation Guidelines

- **Module Structure:**
  - Import pt_components.py as the base for all UI functionality
  - Use functions like show_message(), prompt_input(), show_progress_bar()
  - Avoid direct terminal manipulation (clear screen, cursor movement)

- **Dialog Components:**
  - All dialogs should use prompt_toolkit dialog components
  - Dialog title should clearly indicate the dialog's purpose
  - Include keyboard shortcut reminders in dialog text or bottom toolbar
  - Ensure proper dialog focus management

- **Form Input:**
  - Implement validation feedback with clear error messages
  - Provide sensible defaults when appropriate
  - Use auto-completion where it enhances usability
  - Support cancellation (Escape) and confirmation (Enter) 

- **Progress Indicators:**
  - Use deterministic progress bars when the total work is known
  - Use indeterminate progress indicators for unknown duration operations
  - Show operation status messages during longer processes

- **Menu Systems:**
  - Implement keyboard shortcuts for navigation
  - Ensure consistent menu structure and navigation
  - Support both number keys and arrow keys for selection

## Accessibility Considerations

- **Screen Reader Compatibility:**
  - Use descriptive labels for all interactive elements
  - Ensure all error messages and important feedback can be reviewed

- **Terminal Environment:**
  - Check terminal capabilities at startup (color support, size)
  - Warn users if terminal dimensions are below recommended size
  - Adapt to different terminal environments when possible

- **Feedback & Status:**
  - Provide clear success/error messaging after operations
  - Use bottom toolbar for contextual help and status updates
  - Support clipboard operations where appropriate

# SUPPLEMENTARY PROMPT_TOOLKIT INSTRUCTIONS

These instructions specifically apply to the prompt_toolkit version of PPWM and should be considered as extensions to the main instructions rather than replacements.

## Version-Specific Framework Guidelines

- **Transition from Standard to PT Version:**
  - The prompt_toolkit version (ppwm-dev-pt) is a parallel development path
  - When adapting code from ppwm-dev to ppwm-dev-pt, integrate with prompt_toolkit components
  - Replace direct terminal operations with prompt_toolkit equivalents

- **Component Usage Hierarchy:**
  - First try to use existing pt_components.py functions
  - For new UI elements, use prompt_toolkit shortcuts (e.g., dialog functions)
  - Only create custom widgets when necessary for specialized functionality

- **HTML Formatting Over ANSI:**
  - Replace Colorama's Fore/Style with HTML-style formatting tags
  - Convert: `Fore.RED + "text" + Style.RESET_ALL` → `"<ansired>text</ansired>"`
  - Use HTML() constructor for complex or dynamic formatting

- **Managing Terminal State:**
  - Use prompt_toolkit's ApplicationState for persistent UI state
  - Avoid direct modification of terminal settings (cursor position, etc.)
  - Use Layout objects for complex UI arrangements instead of print statements

## Interface Development Best Practices

- **Key Bindings Integration:**
  - Use KeyBindings objects for keyboard shortcuts
  - Register common keys consistently (Esc for back/cancel, etc.)
  - Document keyboard shortcuts in UI and help screens

- **Display Flow Control:**
  - Use nested dialogs instead of clearing screen and redrawing
  - Maintain state between UI interactions through proper object design
  - Consider using Application objects for complex multi-page workflows

- **Validation Patterns:**
  - Use prompt_toolkit's Validator classes for input validation
  - Show validation errors inline rather than as separate errors
  - Validate incrementally when possible (as user types)
```


Made changes.

Serfects: I have made the necessary changes to the copilot-instructions.md file and you should now have more clear direction with how to proceed with the changes in this project. I would like to restart the updating of the project that we started with the "I want to build this script using the newest stable versions of everything that we are going to use, including python, as long as all of the versions of all of the things that we are going to include are compatable with each other, which they should be. I am not worried about very very old terminals. Odds are if the user is using this script in the first place, they are on a newer more modern terminal anyway. Please update the dependencies to use the newest stable versions of everything that we are using in this script that you have available to you, including pythong. And then we can work on updating the code of each module to reflect the newest stable versions of everything, including python. If the newer versions of prompt_toolkit handles colors and styling of text on its own, I would like to use the features built into prompt_toolkit for coloring and style, so we can drop colorama unless it is necessary for something else. Like i said, i am not worried about the super old terminals. We are building this to be modern, while having compatability across many modern systems." prompt. Lets go back, make a revised plan, and start updating this project. We can restart with the dependency.md, base_utils.py, and pt_components.py changes to verify that all changes were properly made, and move on from there.

GitHub Copilot: # Revised Plan for Modernizing PPWM with prompt_toolkit

Logan, I'll help you modernize the PPWM project using prompt_toolkit and the latest Python features. Let's take a systematic approach to convert the application while maintaining its core functionality.

## Section 1: Foundation Update (Dependencies and Core Utilities)

Let's start by updating the foundation files to establish our modern approach:

### [dependency.md](vscode-remote://codespaces/workspaces/Pterodactyl-Pelican-Wireguard-Manager/src/ppwm-dev-pt/dependency.md)

```markdown
# PPWM Project Dependencies

This file documents the external dependencies required for the project.

## Core Dependencies

- **Python** (>=3.11)
  - The application targets Python 3.11+ for improved performance and modern language features
  - Leverages structural pattern matching, improved error messages, and better typing

- **prompt_toolkit** (>=3.0.39)
  - Modern terminal user interface framework
  - Features: styled dialogs, interactive menus, text highlighting, keyboard/mouse navigation
  - Handles all terminal color and formatting needs across platforms
  - Documentation: https://python-prompt-toolkit.readthedocs.io/

- **pygments** (>=2.16.1)
  - Syntax highlighting library for displaying code and configuration snippets
  - Used by prompt_toolkit for syntax highlighting in text editors
  - Documentation: https://pygments.org/

## Optional Dependencies

- **pyperclip** (>=1.8.2)
  - Cross-platform clipboard access for copying/pasting text
  - Enhances usability when dealing with configuration snippets or commands
  - Documentation: https://github.com/asweigart/pyperclip

## Development Dependencies

- **pytest** (>=7.4.0)
  - Testing framework for validating application functionality
  - Used only during development or when running tests
  - Documentation: https://docs.pytest.org/

## Installation

These dependencies can be installed via pip:

```bash
# Core dependencies (required)
pip install "prompt-toolkit>=3.0.39" "pygments>=2.16.1"

# Optional enhancements
pip install "pyperclip>=1.8.2"

# Development only
pip install "pytest>=7.4.0"
```

## Platform Notes

- This application targets modern terminals with 256-color or true-color support
- Mouse support is available but not required (keyboard navigation works for all features)
- Minimum recommended terminal size: 80x24 characters
```

### [base_utils.py](vscode-remote://codespaces/workspaces/Pterodactyl-Pelican-Wireguard-Manager/src/ppwm-dev-pt/base_utils.py)

```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python


Made changes.

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
import signal
from logging.handlers import RotatingFileHandler
from datetime import datetime
from pathlib import Path
from functools import wraps
from contextlib import contextmanager

# ========== General Constants ==========
SCREEN_WIDTH = 80  # Modern terminal width standard
APP_NAME = "PPWM"
APP_VERSION = "2.0.0"
APP_DESCRIPTION = "Pterodactyl-Pelican-Wireguard-Manager"

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

# ========== Signal Handlers ==========
def setup_signal_handlers():
    """
    Set up handlers for system signals to ensure graceful application behavior.
    """
    def handle_interrupt(signum, frame):
        """Handle keyboard interrupts (SIGINT) gracefully."""
        print("\nOperation cancelled by user. Exiting...")
        sys.exit(0)
    
    def handle_terminate(signum, frame):
        """Handle termination signals (SIGTERM) gracefully."""
        print("\nReceived termination signal. Shutting down...")
        sys.exit(0)
    
    # Register signal handlers
    signal.signal(signal.SIGINT, handle_interrupt)
    signal.signal(signal.SIGTERM, handle_terminate)

# ========== System Check Functions ==========
def check_root():
    """
    Check if the script is running with root privileges.
    
    Exits with status code 1 if not running as root on Unix-like systems.
    Does nothing on Windows.
    
    Returns:
        bool: True if running as root or on Windows
    """
    # Skip check on Windows - concept of root doesn't apply
    if platform.system() == 'Windows':
        return True
        
    if os.geteuid() != 0:
        basic_error_display("This application requires root privileges")
        input("\nPress Enter to exit...")
        sys.exit(1)
    return True

def check_python_version(min_version=(3, 11)):
    """
    Check if the current Python version meets minimum requirements.
    
    Args:
        min_version (tuple): Minimum required version as (major, minor)
        
    Returns:
        bool: True if version requirement is met, False otherwise
    """
    current = sys.version_info[:2]
    return current >= min_version

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
    Get detailed information about the system.
    
    Returns:
        dict: System information
    """
    return {
        'platform': platform.system(),
        'platform_version': platform.version(),
        'platform_release': platform.release(),
        'python_version': platform.python_version(),
        'python_implementation': platform.python_implementation(),
        'machine': platform.machine(),
        'processor': platform.processor(),
        'hostname': platform.node(),
        'username': os.environ.get('USER') or os.environ.get('USERNAME') or 'unknown',
        'terminal': os.environ.get('TERM', 'unknown'),
        'terminal_size': os.get_terminal_size() if hasattr(os, 'get_terminal_size') else None,
    }

# ========== Performance & Resource Management ==========
@contextmanager
def timing_context(operation_name):
    """
    Context manager for timing operations.
    
    Args:
        operation_name (str): Name of the operation being timed
        
    Yields:
        None
    """
    start_time = datetime.now()
    yield
    end_time = datetime.now()
    duration = (end_time - start_time).total_seconds()
    logger.debug(f"Operation '{operation_name}' completed in {duration:.2f} seconds")

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
    root_logger.debug(f"Platform: {system_info['platform']} {system_info['platform_release']}")
    
    # Check Python version requirement
    if not check_python_version():
        root_logger.warning(f"Running on Python {platform.python_version()}, but 3.11+ is recommended")
        
    return root_logger

# ========== Custom Exceptions ==========
class AppError(Exception):
    """Base exception class for application-specific errors"""
    pass

# Setup signal handlers
setup_signal_handlers()

# Initialize logger when the module is imported
logger = logging.getLogger(__name__)
logger = setup_logging()
logger.debug("base_utils module loaded")
```

### [pt_components.py](vscode-remote://codespaces/workspaces/Pterodactyl-Pelican-Wireguard-Manager/src/ppwm-dev-pt/pt_components.py)

```python


Made changes.

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
from prompt_toolkit.formatted_text import HTML, FormattedText, ANSI
from prompt_toolkit.shortcuts import (
    clear, input_dialog, message_dialog, yes_no_dialog,
    button_dialog, checkboxlist_dialog, radiolist_dialog, ProgressBar
)
from prompt_toolkit.filters import Condition
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.mouse import MouseEventType
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.validation import Validator, ValidationError
from prompt_toolkit.output import ColorDepth
from prompt_toolkit.layout.dimension import D
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

# Standard colors for consistent usage across the application
PPWM_COLORS = {
    'primary': '#3498db',       # Main app color (blue)
    'success': '#2ecc71',       # Success/completion (green)
    'error': '#e74c3c',         # Errors/problems (red)
    'warning': '#f39c12',       # Warnings/cautions (yellow)
    'info': '#3498db',          # Information/help (blue)
    'muted': '#7f8c8d',         # Less important text (gray)
    'highlight': '#9b59b6',     # Highlighted elements (purple)
    'active': '#2ecc71',        # Active elements (green)
    'inactive': '#95a5a6',      # Inactive elements (light gray)
    'background': '#171717',    # Main background color
    'foreground': '#ffffff',    # Main text color
}

# Standard symbols for consistent usage
PPWM_SYMBOLS = {
    'check': '✓',               # Success/completion
    'warning': '⚠',             # Warning
    'error': '✗',               # Error
    'info': 'ℹ',                # Information
    'bullet': '•',              # List item
    'right_arrow': '→',         # Next/forward
    'left_arrow': '←',          # Previous/back
    'ellipsis': '…',            # Truncation
    'spinner': '⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏', # Progress animation
}

# ========== UI Settings ==========
# Settings for the UI components
UI_SETTINGS = {
    'mouse_support': True,         # Enable mouse support by default
    'color_depth': 'DEPTH_24_BIT', # Use true color if supported
    'min_terminal_width': 80,      # Minimum terminal width for proper display
    'min_terminal_height': 24,     # Minimum terminal height for proper display
    'wrap_lines': True,            # Wrap long lines in dialogs
    'enable_shortcuts': True,      # Enable keyboard shortcuts
    'dialog_width': 75,            # Standard dialog width
}

# ========== Key Bindings ==========
# Common key bindings that can be used across the application
def get_standard_kb():
    """
    Get standard key bindings for navigation and actions.
    
    Returns:
        KeyBindings: Key bindings object
    """
    kb = KeyBindings()
    
    @kb.add('escape')
    def _(event):
        """Bind escape key to cancel/exit."""
        event.app.exit(False)
    
    @kb.add('c-c')
    def _(event):
        """Handle Ctrl+C gracefully."""
        event.app.exit(False)
    
    return kb

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

# ========== HTML Formatting Helper Functions ==========
def format_html(text, tag=None, color=None, style=None):
    """
    Format text with HTML-style tags for prompt_toolkit.
    
    Args:
        text (str): Text to format
        tag (str, optional): HTML tag (b, i, u, etc.)
        color (str, optional): Color name or hex code
        style (str, optional): Additional style attributes
    
    Returns:
        str: Formatted HTML string
    """
    if not text:
        return ""
        
    formatted = text
    
    # Apply color if provided
    if color:
        if color.startswith('#'):
            formatted = f'<ansifg color="{color}">{formatted}</ansifg>'
        else:
            formatted = f'<ansi{color}>{formatted}</ansi{color}>'
    
    # Apply tag if provided
    if tag:
        formatted = f'<{tag}>{formatted}</{tag}>'
        
    # Apply style if provided
    if style:
        formatted = f'<style {style}>{formatted}</style>'
        
    return formatted

def success_text(text):
    """Format text as success message."""
    return format_html(text, color="green", tag="b")

def error_text(text):
    """Format text as error message."""
    return f"<ansired>{PPWM_SYMBOLS['error']} {text}</ansired>"

def warning_text(text):
    """Format text as warning message."""
    return f"<ansiyellow>{PPWM_SYMBOLS['warning']} {text}</ansiyellow>"

def info_text(text):
    """Format text as info message."""
    return f"<ansiblue>{PPWM_SYMBOLS['info']} {text}</ansiblue>"

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
    if not isinstance(text, HTML) and not text.startswith("<"):
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
    styled_message = error_text(message)
    show_message(title, styled_message)

def show_success_dialog(message, title="Success"):
    """
    Display a success message dialog.
    
    Args:
        message (str): Success message to display
        title (str, optional): Dialog title. Defaults to "Success".
    """
    logger.info(message)
    styled_message = f"<ansigreen>{PPWM_SYMBOLS['check']} {message}</ansigreen>"
    show_message(title, styled_message)

def show_warning_dialog(message, title="Warning"):
    """
    Display a warning message dialog.
    
    Args:
        message (str): Warning message to display
        title (str, optional): Dialog title. Defaults to "Warning".
    """
    logger.warning(message)
    styled_message = warning_text(message)
    show_message(title, styled_message)

def show_info_dialog(message, title="Information"):
    """
    Display an information message dialog.
    
    Args:
        message (str): Information message to display
        title (str, optional): Dialog title. Defaults to "Information".
    """
    logger.info(message)
    styled_message = info_text(message)
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
            yield task
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
    spinner_chars = PPWM_SYMBOLS['spinner']
    print_formatted_text(HTML(f"<ansicyan>{message}...</ansicyan>"))
    
    try:
        for i in range(int(duration * 10)):
            char = spinner_chars[i % len(spinner_chars)]
            print_formatted_text(
                HTML(f"\r<ansicyan>{message}...</ansicyan> <ansiblue>{char}</ansiblue>"), 
                end="", 
                flush=True
            )
            time.sleep(0.1)
        print_formatted_text(HTML(f"\r<ansigreen>{PPWM_SYMBOLS['check']}</ansigreen> <ansigreen>Complete!</ansigreen>  "))
    except KeyboardInterrupt:
        print_formatted_text(HTML(f"\r<ansiyellow>{PPWM_SYMBOLS['error']}</ansiyellow> <ansiyellow>Cancelled!</ansiyellow>  "))
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

def prompt_multi_select(title, text,

Made changes.






I have made the necessary changes to the copilot-instructions.md file and you should now have more clear direction with how to proceed with the changes in this project. I would like to restart the updating of the project that we started with the "I want to build this script using the newest stable versions of everything that we are going to use, including python, as long as all of the versions of all of the things that we are going to include are compatable with each other, which they should be. I am not worried about very very old terminals. Odds are if the user is using this script in the first place, they are on a newer more modern terminal anyway. Please update the dependencies to use the newest stable versions of everything that we are using in this script that you have available to you, including pythong. And then we can work on updating the code of each module to reflect the newest stable versions of everything, including python. If the newer versions of prompt_toolkit handles colors and styling of text on its own, I would like to use the features built into prompt_toolkit for coloring and style, so we can drop colorama unless it is necessary for something else. Like i said, i am not worried about the super old terminals. We are building this to be modern, while having compatability across many modern systems." prompt. Lets go back, make a revised plan, and start updating this project. We can restart with the dependency.md, base_utils.py, and pt_components.py changes to verify that all changes were properly made, and move on from there. Please start with the dependencys, i will confirm, then we will move into to base_utils.py, i will confirm, then we can move on to pt_components.py, i will confirm, and we can go on from there with what you feel is best to work on next.