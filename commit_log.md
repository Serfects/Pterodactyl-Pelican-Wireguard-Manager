===============================================================================================================
## Date/Time: Wed Feb 12 00:50:58 2025 +0000
## Commit Name: Reset-Added env scipts/temp and modified ASCII art

### Changes Made
1. 
   - Modified ASCII art to what it should be
   - Modified .gitignore to remove commit_log.md from being ignored

===============================================================================================================
## Date/Time: Thu Feb 13 03:00:39 2025 +0000
## Commit Name: Further changes to ASCII art and disp_utils.py

### Changes Made
1. disp_utils.py module
   - Added show_progress function to disp_utils.py
   - Still want to move the escape codes to be part of the ASCII art code block

2. ASCII Art
   - Added new color to ASCII art, but it is untested
   - Created example_output.txt to show what the new ASCII art looks like

3. Main Menu
   - Blank line for spacing functionality added to breadcrumb bar

===============================================================================================================
## Date/Time: Thu Feb 13 23:31:51 2025 +0000
## Commit Name: Formatting changes, reorginizational changes

### Changes Made
1. History Bar
   - Renamed breadcrumb bar to historybar and updated imports and references throughout the code
   - 

2. disp_utils.py
   - Reorganized the code to make it more readable and added inline comments to break up different sections, and added docstrings to explain features
   - Added graceful exit and screen clearing functions to disp_utils.py and removed them from main_menu.py

3. main_menu.py
   - Updated imports to support the new history bar and the changed name from BreadcrumbManager to HistoryBar
   - Updated error handling to use correct calls to functions and color coding located in the disp_utils.py module

===============================================================================================================
## Date/Time: Fri Feb 14 02:20:55 2025 +0000
## Commit Name: Saving progress, test script working

### Changes Made
1. History Bar
   - Add push/pop methods to the HistoryBar class for managing navigation history. This is supposed to fix a fatal error.
   - Fixed double arrows for truncated ellipsis

2. Test Script
   - Created Test Script
   - Changed input method to the one we use in the actual script insted of the python one so the ctrl+c handling works properly

3. general_utils.py
   - Added a signal handler to general_utils.py for ctrl+c to exit the program gracefully

Still need to add logging
fix history bar arrows and long message


===============================================================================================================
## Date/Time: Tue Feb 18 09:05:06 2025 +0000
## Commit Name: Appearance changes finalization

### Changes Made
1. disp_utils.py
   - Reorganized again to make sure things are under the right sections
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
## Date/Time: Tue Feb 25 09:06:38 2025 +0000
## Commit Name: General additions commit b4 using claude 3.7

### Changes Made
1. Logging Feature
   - Added logging functionality to script to create log files for errors and debugging
   - Added more error messages for errors that could come up to all the modules

2. copilot_instructions.md
   - Updated copilot_instructions.md to include new instructions for specifiying to use resuable code and use standards already set in the other modules

3. Root Check
   - Added a root check to the script to make sure the script is ran as root and automatically closes after showing the user a message if it is not

4. Test Script
   - Updated the test script to add testing in for error handling, the root check feature, and testing the logging features
   - Improved error handling and display formatting

5. B for back X for exit
   - Added the functionality for the reusable B to go back and X to exit to all the menus in the script
   - Made the text very dark and the above border slightly lighter

===============================================================================================================
## Date/Time: YYYY-MM-DD
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
## Date/Time: YYYY-MM-DD
## Commit Name: [commit name goes here]

### Changes Made
1. [Major Change Category]
   - [Specific change details]
   - [Additional details if needed]

2. [Another Major Change Category]
   - [Specific change details]
   - [Additional details if needed]
