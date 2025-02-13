## Date/Time: YYYY-MM-DD
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








# Commit Log Template

## Date/Time: YYYY-MM-DD
## Commit Name: [commit name goes here]

### Changes Made
1. Example 1
   - Details

2. Example 2
   - Details