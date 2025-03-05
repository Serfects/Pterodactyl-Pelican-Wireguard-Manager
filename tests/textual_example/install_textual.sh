#!/bin/bash
# Script to properly install Textual and verify its installation

# Set text color variables
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo -e "${BLUE}=========================================================${NC}"
echo -e "${YELLOW}Textual Installation and Verification Script${NC}"
echo -e "${BLUE}=========================================================${NC}"

# Get the current directory
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$SCRIPT_DIR" || exit 1

echo -e "${YELLOW}Step 1: Checking Python installation${NC}"
if ! command -v python3 &> /dev/null; then
    echo -e "${RED}Error: Python 3 is not installed.${NC}"
    exit 1
fi

PYTHON_VERSION=$(python3 --version)
echo -e "${GREEN}Using $PYTHON_VERSION${NC}"

# Create a virtual environment if it doesn't exist
echo -e "${YELLOW}Step 2: Setting up a virtual environment${NC}"
if [ ! -d "venv" ]; then
    echo -e "Creating a new virtual environment..."
    python3 -m venv venv
    if [ $? -ne 0 ]; then
        echo -e "${RED}Error: Could not create virtual environment. Installing venv...${NC}"
        if command -v apt-get &> /dev/null; then
            sudo apt-get update
            sudo apt-get install -y python3-venv
            python3 -m venv venv
        elif command -v yum &> /dev/null; then
            sudo yum install -y python3-venv
            python3 -m venv venv
        else
            echo -e "${RED}Error: Couldn't install python3-venv. Please install it manually.${NC}"
            exit 1
        fi
    fi
else
    echo -e "${GREEN}Virtual environment already exists.${NC}"
fi

# Activate virtual environment
echo -e "${YELLOW}Step 3: Activating virtual environment${NC}"
source venv/bin/activate
if [ $? -ne 0 ]; then
    echo -e "${RED}Error: Could not activate virtual environment.${NC}"
    exit 1
fi

echo -e "${GREEN}Virtual environment activated.${NC}"
echo -e "Using Python: $(which python3)"

# Upgrade pip
echo -e "${YELLOW}Step 4: Upgrading pip${NC}"
python3 -m pip install --upgrade pip
if [ $? -ne 0 ]; then
    echo -e "${RED}Warning: Could not upgrade pip. Continuing with existing version.${NC}"
fi

# Install Textual with specific version range
echo -e "${YELLOW}Step 5: Installing Textual${NC}"
python3 -m pip install "textual>=0.20.0,<0.30.0" rich
if [ $? -ne 0 ]; then
    echo -e "${RED}Error: Failed to install Textual.${NC}"
    exit 1
fi

echo -e "${GREEN}Textual installed successfully.${NC}"

# Verify the installation
echo -e "${YELLOW}Step 6: Verifying Textual installation${NC}"

# Create a temporary Python script to check Textual
cat > check_textual.py << EOF
try:
    import textual
    print(f"Textual version: {textual.__version__}")
    print("Textual was installed successfully.")
    
    from textual.app import App
    from textual.widgets import Button, Label, Input
    print("Core Textual modules imported successfully.")
    
    # Check if ProgressBar exists and how to use it
    from textual.widgets import ProgressBar
    progress = ProgressBar()
    try:
        progress.progress = 50
        print("ProgressBar supports .progress attribute")
    except AttributeError:
        # Try the update method instead
        if hasattr(progress, "update"):
            print("ProgressBar supports .update() method")
        else:
            print("Could not determine ProgressBar update mechanism")
    
except ImportError as e:
    print(f"Error importing Textual: {e}")
    exit(1)
EOF

# Run the verification script
python3 check_textual.py
VERIFY_RESULT=$?

# Clean up
rm check_textual.py

if [ $VERIFY_RESULT -eq 0 ]; then
    echo -e "${GREEN}Textual was verified successfully.${NC}"
    
    # Create an activation script for convenience
    cat > activate_env.sh << EOF
#!/bin/bash
# Source this file to activate the virtual environment
source "$(pwd)/venv/bin/activate"
echo "Virtual environment activated! You can now run:"
echo "python3 textual_example.py"
EOF

    chmod +x activate_env.sh
    
    echo -e "${BLUE}=========================================================${NC}"
    echo -e "${GREEN}Installation Complete!${NC}"
    echo -e "${YELLOW}To run the Textual example:${NC}"
    echo -e "  1. ${BLUE}Activate the environment:${NC} source ${SCRIPT_DIR}/activate_env.sh"
    echo -e "  2. ${BLUE}Run the example:${NC} python3 textual_example.py"
    echo -e "${BLUE}=========================================================${NC}"
else
    echo -e "${RED}Textual verification failed. Please check the error messages above.${NC}"
    exit 1
fi
