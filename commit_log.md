===============================================================================================================
## Date/Time: YYYY-MM-DD
## Commit Name: [commit name goes here]

### Changes Made
1. Logging Feature
   - Added logging functionality to script to create log files for errors and debugging
   - Added rotating file feature to log files to prevent them from getting too large
   - Added much more logging to nearly all functions of the script in each module
   - Ensured that errors that are displayed to the user follow the correct error message formatting and are also logged to the log file
   - Added more error messages for errors that could come up to all the modules

2. copilot_instructions.md
   - Updated copilot_instructions.md to include new instructions for specifiying to use resuable code and use standards already set in the other modules
   - 

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
1. 
   - Modified ASCII art to what it should be
   - Added commit_log.md to keep track of commits and log my changes form old commit
   - Added reset_test_env.py to reset the test environment from old commit
   - Added setup_test_env.py to setup the test environment from old commit
   - Added start_test_env.py to start the test environment from old commit
   - Added temp folder and temp files for things that I wanted to bring over from the abandoned commit
   - Modified .gitignore to remove commit_log.md from being ignored

===============================================================================================================
## Date/Time: YYYY-MM-DD
## Commit Name: (REVERTED TO ABOVE) ASCII art change, test env, new test script

### Changes Made
1. 
- Moved show_progress functionality to disp_utils.py
- Added show_progress to main_menu.py for now but not actually using it anywhere
- Made show_progress more dynamic with a variable duration but not using it anywhere
- Made show_progress use 20 dots over the span of 1.5 seconds by default but could be modified using the duration parameter
- Moved ASCII art to disp_utils.py
- Removed ASCII art from main_menu.py
- Created a header function in disp_utils.py to print the ASCII art at the top of basically every screen so it acts like a GUI but this needs more work because I dont know if it is working for every new prompt right now
- Main menu modified to use this new header function
- Updated imports to support the new ASCII art header function
- Created a new testscript.py that works similar to the other two test scripts but is more dynamic and can be used for testing the new environment
- Created a new test environment setup with a virtual environment and a fake root filesystem for testing scripts in the future
- Created auto setup scripts for the test environment
- Created a new directory for test scripts
- Created helper scripts for the test environment

===============================================================================================================
## Date/Time: YYYY-MM-DD
## Commit Name: [commit name goes here]

### Changes Made
1. Example 1
   - Details

2. Example 2
   - Details
