#!/bin/bash
# Script to install required dependencies for the PPWM test scripts

# Set text color variables
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo -e "${BLUE}=========================================================${NC}"
echo -e "${YELLOW}PPWM Test Dependencies Installer${NC}"
echo -e "${BLUE}=========================================================${NC}"

# Directory setup
TESTS_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
PT_DIR="$TESTS_DIR/prompt_toolkit_example"
TX_DIR="$TESTS_DIR/textual_example"

# Function to check if a command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Check for Python
if ! command_exists python3; then
    echo -e "${RED}Error: Python 3 is not installed.${NC}"
    echo -e "Please install Python 3 and try again."
    exit 1
fi

echo -e "${GREEN}Python 3 found.${NC}"
python3 --version

# Check for pip
if ! command_exists pip3; then
    echo -e "${YELLOW}Warning: pip3 not found. Trying to install...${NC}"
    if command_exists apt-get; then
        sudo apt-get update
        sudo apt-get install -y python3-pip
    elif command_exists yum; then
        sudo yum install -y python3-pip
    else
        echo -e "${RED}Error: Couldn't install pip3. Please install pip manually.${NC}"
        exit 1
    fi
fi

# Check again for pip after attempted install
if ! command_exists pip3; then
    echo -e "${RED}Error: pip3 installation failed.${NC}"
    exit 1
fi

echo -e "${GREEN}pip3 found.${NC}"

# Function to install requirements from file
install_requirements() {
    local req_file="$1"
    local package_type="$2"
    
    if [ -f "$req_file" ]; then
        echo -e "${YELLOW}Installing ${package_type} dependencies...${NC}"
        pip3 install -r "$req_file"
        if [ $? -eq 0 ]; then
            echo -e "${GREEN}Successfully installed ${package_type} dependencies.${NC}"
        else
            echo -e "${RED}Failed to install some ${package_type} dependencies.${NC}"
        fi
    else
        echo -e "${RED}Error: $req_file not found.${NC}"
    fi
}

# Install prompt_toolkit dependencies
install_requirements "$PT_DIR/requirements.txt" "prompt_toolkit"

# Install textual dependencies
install_requirements "$TX_DIR/requirements.txt" "textual"

# Set execute permissions
echo -e "${YELLOW}Setting execute permissions for the test scripts...${NC}"
chmod +x "$PT_DIR/prompt_toolkit_example.py" 2>/dev/null
chmod +x "$TX_DIR/textual_example.py" 2>/dev/null

echo -e "${BLUE}=========================================================${NC}"
echo -e "${GREEN}Installation complete!${NC}"
echo -e "${YELLOW}To run the test scripts:${NC}"
echo -e "  ${BLUE}Prompt Toolkit Example:${NC} cd $PT_DIR && python3 prompt_toolkit_example.py"
echo -e "  ${BLUE}Textual Example:${NC} cd $TX_DIR && python3 textual_example.py"
echo -e "${BLUE}=========================================================${NC}"
