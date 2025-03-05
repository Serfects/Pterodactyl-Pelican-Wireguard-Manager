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

