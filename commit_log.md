===============================================================================================================
## Date/Time: YYYY-MM-DD
## Commit Name: cleanup and workspace reorganization

### Changes Made
1. Commit Log
    - Reverted commit_log.md to the previous style where the newest commit is at the top
    - Cleaned up other commits to make styling and spacing uniform
    - Added older commits that were missing from the log

2. Memory File
    - Added memory.md file to place general information about the project so Copilot has more information to work with

3. copilot_instructions.md
    - Large change for the instructions
    - Heavily optimized copilot_instructions.md for better understanding and faster reasoning for Copilot
    - Added new instructions based on the suggestions that Copilot gave originally that I should add to the instructions to make it function better and or more efficiently
    - Added an old version of the longer instructions to the old directory
===============================================================================================================
## Date/Time: Tue Feb 25 11:52:32 2025 +0000
## Commit Name: module reorg code structure improvements

### Changes Made
1. Complete Code Reorganization
    - Created a clean module hierarchy with base_utils, navigation, display_utils, and input_utils
    - Eliminated circular dependencies between modules
    - Restructured imports to follow a logical hierarchy
    
2. Class and Function Renaming
    - Renamed HistoryBar class to MenuNavigationTracker for clarity
    - Renamed display_error to show_error for consistency
    - Renamed format_error to format_error_message for clarity
    - Updated all references throughout codebase
    
3. Documentation Improvements
    - Added comprehensive module-level docstrings
    - Added detailed function and class docstrings
    - Added section headers with clear comments
    - Updated all documentation to match new function and class names
    
4. Code Quality Improvements
    - Fixed logger initialization across modules
    - Improved error handling with custom exception classes
    - Added more precise logging statements
    - Removed redundant code
    
5. Created New Module Architecture
    - Created base_utils.py as the foundation module with core utilities
    - Created navigation.py for all navigation-related functionality
    - Restructured existing modules to use the new architecture
    - Fixed circular dependencies between modules
    
6. Enhanced Error Handling
    - Created a consistent error hierarchy with AppError as the base class
    - Added specific error types for different modules (DisplayError, NavigationError, etc.)
    - Improved error messages and logging for better debugging
    
7. Improved Documentation
    - Added comprehensive module-level docstrings explaining dependencies
    - Enhanced function-level docstrings with detailed explanations
    - Added consistent code section headers for better readability
    
8. Streamlined Code Organization
    - Removed duplicated code and centralized common functionality
    - Grouped related functions together in appropriate modules
    - Made imported functions and constants more explicit
    
9. Import Structure Cleanup
    - Reorganized imports to clearly show module dependencies
    - Removed unnecessary imports
    - Added import comments to clarify purpose of imported components
    
10. Module Renaming for Better Self-Documentation
    - Renamed `disp_utils.py` to `display_utils.py` for clearer purpose indication
    - Renamed `general_utils.py` to `input_utils.py` to better reflect its primary responsibility
    
11. Class and Constant Naming Improvements
    - Renamed `HistoryBar` to `MenuNavigationTracker` to better describe its purpose
    - Renamed `HISTORYBAR_BORDER_CHAR` to `NAV_BORDER_CHAR` for consistency
    
12. Function Renaming for Better Clarity
    - Renamed `display_error()` to `show_error()` for consistency with other display functions
    - Renamed `format_error()` to `format_error_message()` to distinguish from show_error
    - Renamed `get_input()` to `prompt_user()` for clearer action description
    - Renamed `confirm_action()` to `prompt_confirmation()` for naming consistency
    
13. Cross-Module References Updated
    - Updated all import statements to reference the renamed modules and classes
    - Updated all function calls to use the new function names
    - Ensured consistent module load messages
    
14. Complete Code Reorganization
    - Created a clean module hierarchy with base_utils, navigation, display_utils, and input_utils
    - Eliminated circular dependencies between modules
    - Restructured imports to follow a logical hierarchy
    
15. Class and Function Renaming
    - Renamed HistoryBar class to MenuNavigationTracker for clarity
    - Renamed display_error to show_error for consistency
    - Renamed format_error to format_error_message for clarity
    - Updated all references throughout codebase
    
16. Documentation Improvements
    - Added comprehensive module-level docstrings
    - Added detailed function and class docstrings
    - Added section headers with clear comments
    - Updated all documentation to match new function and class names
    
17. Code Quality Improvements
    - Fixed logger initialization across modules
    - Improved error handling with custom exception classes
    - Added more precise logging statements
    - Removed redundant code
    
18. Test Script Modernization
    - Updated functest.py to work with the new module structure
    - Ensured all tests reference the new class/function names
    - Added comprehensive testing for all core utilities
    
19. New Tests Added
    - Added tests for MenuNavigationTracker functionality
    - Added tests for display utilities (error formatting, borders, etc.)
    - Added tests for input validation and handling
    
20. Improved Test Structure
    - Reorganized test menu to match the flow of the actual application
    - Added clear section navigation with back/exit functionality
    - Implemented proper error handling throughout test script

===============================================================================================================
## Date/Time: Tue Feb 25 09:06:38 2025 +0000
## Commit Name: General additions commit b4 using claude 3.7

### Changes Made
1. Logging Feature
   - Added logging functionality to script to create log files for errors and debugging
   - Added rotating file feature to log files to prevent them from getting too large
   - Added much more logging to nearly all functions of the script in each module
   - Ensured that errors that are displayed to the user follow the correct error message formatting and are also logged to the log file
   - Added more error messages for errors that could come up to all the modules

2. copilot_instructions.md
   - Updated copilot_instructions.md to include new instructions for specifiying to use resuable code and use standards already set in the other modules

3. Root Check
   - Added a root check to the script to make sure the script is ran as root and automatically closes after showing the user a message if it is not

4. Test Script
   - Updated the test script to add testing in for error handling, the root check feature, and testing the logging features
   - Added logging to the test script
   - Updated imports
   - Added new test functions and compatibility for the new b for back and x for exit navigation features
   The major changes include:

   Added new test functions:

   - test_logging_system(): Tests the logging configuration and functionality
   - test_root_check(): Tests the root privilege checking
   - test_error_handling(): Tests various error scenarios
   - Updated imports to include new utilities:

   - Added imports for logging-related functions
   - Added import for root check functionality
   - Added proper logging throughout the test script

   - Updated the main menu to include the new test options

   - Improved error handling and display formatting

5. B for back X for exit
   - Added the functionality for the reusable B to go back and X to exit to all the menus in the script
   - Addded a border above this dialog to make it stand out more
   - Made the text very dark and the above border slightly lighter

===============================================================================================================
## Date/Time: Mon Feb 24 09:49:12 2025 +0000
## Commit Name: Appearance changes finalization

### Changes Made
1. 
   - added copilot instructions file

===============================================================================================================
## Date/Time: Tue Feb 18 09:05:06 2025 +0000
## Commit Name: Appearance changes finalization

### Changes Made
1. disp_utils.py
   - Reorganized again to make sure things are under the right sections
   - Removed all unused code from previous history bar implementation
   - Updated color of show_progress success message to be bright green

2. History Bar
   - Completely rewrote the history bar to only show one single menu name at a time and simplified the logic and overall functionality of this feature
   - Made the history bar text bold and bright white to make it stand out more

3. functest.py
   - Updated the test script to properly reflect the changes made to the history bar
   - Added a new ASCII art test showing different levels of boldness

4. ASCII Art
   - Updated the ASCII art to correct some boldness issues and make it look better

5. general_utils.py
   - Updated all colors of get_input to be brighter but not bold, just generally makes things look better

===============================================================================================================
## Date/Time: Fri Feb 14 02:20:55 2025 +0000
## Commit Name: Saving progress, test script working

### Changes Made
1. History Bar
   - Add push/pop methods to the HistoryBar class for managing navigation history. This is supposed to fix a fatal error.
   - Added a error handling feature to properly handle names of menus that are over the 70 character limit
   - Fixed double arrows for truncated ellipsis

2. Test Script
   - Created Test Script
   - Added colorama import to test script since that was causing a fatal error
   - Added menu bar test to check all features of menu bar
   - Changed input method to the one we use in the actual script insted of the python one so the ctrl+c handling works properly

3. general_utils.py
   - Added a signal handler to general_utils.py for ctrl+c to exit the program gracefully

Still need to add logging
fix history bar arrows and long message


===============================================================================================================
## Date/Time: Thu Feb 13 23:31:51 2025 +0000
## Commit Name: Formatting changes, reorginizational changes

### Changes Made
1. History Bar
   - Renamed breadcrumb bar to historybar and updated imports and references throughout the code
   - Changed history bar character constant name to HISTORY_BAR_CHAR
   - Added colors to history bar, current menu is cyan, previous menu and elepsis are dim white, arrows are light blue
   - Made sure a maximum of 70 characters are displayed in the history bar
   - Added truncation and proper centering logic and calculations to history bar
   - Added ANSI escape code handling for proper length calculation
   - Changed border character to a single line
   - Improved history bar truncation logic to handle very long names
   - 

2. disp_utils.py
   - Reorganized the code to make it more readable and added inline comments to break up different sections, and added docstrings to explain features
   - Moved ASCII art to the bottom of the file
   - Added explanative comments for sections and detailed docstrings explaining functions of the code
   - Reorganized the code to make it more readable and added inline comments to break up different sections
   - Added graceful exit and screen clearing functions to disp_utils.py and removed them from main_menu.py

3. main_menu.py
   - Updated imports to support the new history bar and the changed name from BreadcrumbManager to HistoryBar
   - Updated the history bar to use the new history bar from disp_utils.py
   - Added explanative comments for sections and detailed docstrings explaining functions of the code
   - Reorganized the code to make it more readable and added inline comments to break up different sections
   - Removed the graceful exit and screen clearing functions and relocated them to disp_utils.py for better organization
   - Updated the imports to support the moved functions
   - Removed unused imports (Fore, Stylem create_border)
   - Updated error handling to use correct calls to functions and color coding located in the disp_utils.py module

===============================================================================================================
## Date/Time: Thu Feb 13 03:00:39 2025 +0000
## Commit Name: Further changes to ASCII art and disp_utils.py

### Changes Made
1. disp_utils.py module
    - Added show_progress function to disp_utils.py
    - Added ASCII art to disp_utils.py
    - Removed ASCII art from main_menu.py
    - Removed show_progress from general_utils.py
    - Updated imports in all three modules to support the moved functions
    - Changed max character limit to 70 characters
    - Made sure that all references of the show_progress function were removed from all the modules
    - Removed show_progress import from all modules
    - Removed format_option and PADDING = 2 functionality since it wasnt being used anywhere
    - Changed border of breadcrumb bar
    - Removed top border of breadcrumb bar and put it directly under the ASCII art
    - Still need to change breadcrumb bar name in code to history bar, add colors that match the new art colors, change the arrow symbol make sure it is centered, make sure that it truncates properly as well as changed the border name in the code
    - Still want to move the escape codes to be part of the ASCII art code block
    
2. ASCII Art
    - Added new color to ASCII art, but it is untested
    - Created example_output.txt to show what the new ASCII art looks like
    
3. Main Menu
    - Blank line for spacing functionality added to breadcrumb bar

===============================================================================================================
## Date/Time: Wed Feb 12 00:50:58 2025 +0000
## Commit Name: Reset-Added env scipts/temp and modified ASCII art

### Changes Made
1. Reset-Added env scipts/temp and modified ASCII art
    - Modified ASCII art to what it should be
    - Added commit_log.md to keep track of commits and log my changes form old commit
    - Added reset_test_env.py to reset the test environment from old commit
    - Added setup_test_env.py to setup the test environment from old commit
    - Added start_test_env.py to start the test environment from old commit
    - Added temp folder and temp files for things that I wanted to bring over from the abandoned commit
    - Modified .gitignore to remove commit_log.md from being ignored

===============================================================================================================
## Date/Time: Wed Feb 5 02:47:07 2025 +0000
## Commit Name: General cleanup for later additions

### Changes Made
1. General cleanup for later additions
    - Created a copy of ppwm-dev named ppwm-dev-old to sill retain the original information before anything is changed drastically
    - Deleted unnecessary files from ppwm-dev directory
    - Readded back the test scripts since they work for now
    - Removed all typehints, docscript, and inline comments/hastag comments from all files within ppwm-dev and from the test scripts
    - Removed all currently unused import and from's at the top of the modules
    - Removed the features from the main menu that previous supported the non-existent imports
    - Replaced those removed features with placeholders
    - Moved the test scripts to /old/ with a .bak appension
    - Removed an unused Back import from utils.py
    - Renamed main.py -> main_menu.py
    - Renamed utils.py -> general_utils.py
    - Renamed displayutil.py -> disp_utils.py
    - Updated imports in main_menu.py to match new names
    - Made the show_progress functionality faster with more dots
    - Removed the show_progress functionality from everything in the script for right now, which was only the main menu

===============================================================================================================
## Date/Time: Fri Jan 24 09:55:10 2025 +0000
## Commit Name: somehow still working on iptables rules

### Changes Made
1. iptables Rules
    - Continued work on iptables rules

===============================================================================================================
## Date/Time: Wed Jan 22 03:08:09 2025 +0000
## Commit Name: changes to wireguard config generation

### Changes Made
1. Wireguard Config Generation
    - Added chat.txt to document Copilot changes made to config_generation.py
    - Added more context files to the context directory
    - Added High_Level_Explanation and example_wg_config for further context
    - Removed example_wg_config from the src/old directory

===============================================================================================================
## Date/Time: Tue Jan 21 02:26:30 2025 +0000
## Commit Name: Merge branch 'refactor' of https://github.com/Serfects/Pterodactyl-Pelican-Wireguard-Manager into refactor

### Changes Made
1. Merge Refactor Branch
    - Merged changes from the refactor branch

===============================================================================================================
## Date/Time: Fri Jan 17 00:15:11 2025 +0000
## Commit Name: main modules heavily edited and modified

### Changes Made
1. Main Modules
    - Heavily edited and modified main modules

===============================================================================================================
## Date/Time: Thu Jan 16 05:40:13 2025 +0000
## Commit Name: renamed main directory to ppwm-dev

### Changes Made
1. Directory Renaming
    - Renamed main directory to ppwm-dev

===============================================================================================================
## Date/Time: Thu Jan 16 05:35:00 2025 +0000
## Commit Name: Remove ignored files from repository

### Changes Made
1. Repository Cleanup
    - Removed ignored files from the repository

===============================================================================================================
## Date/Time: Thu Jan 16 05:32:51 2025 +0000
## Commit Name: Add .gitignore file for Python project

### Changes Made
1. .gitignore
    - Added .gitignore file for Python project

===============================================================================================================
## Date/Time: Thu Jan 16 03:05:46 2025 +0000
## Commit Name: added ASCII art to main menu

### Changes Made
1. ASCII Art
    - Added ASCII art to main menu

===============================================================================================================
## Date/Time: Wed Jan 15 02:54:30 2025 +0000
## Commit Name: beginning stages of refactoring the project

### Changes Made
1. Project Refactoring
    - Moved files to create directories for the old script and separate it from the new script
    - Created main.py as the new entry point

===============================================================================================================
## Date/Time: YYYY-MM-DD
## Commit Name: [commit name goes here]

### Changes Made
1. Example 1
   - Details

2. Example 2
   - Details
