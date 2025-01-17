#!/bin/bash

INSTALL_DIR="/opt/wireguard-script"
SYMLINK="/usr/local/bin/wireguard-manager"
WIREGUARD_ETC="/etc/wireguard"

DEFAULT_DEPENDENCIES="curl iptables iproute2 ss git"
NON_DEFAULT_DEPENDENCIES="wireguard-tools python3 python3-pip"
ALL_DEPENDENCIES="$DEFAULT_DEPENDENCIES $NON_DEFAULT_DEPENDENCIES"

function get_yes_no_input() {
    local prompt="$1"
    while true; do
        read -rp "$prompt (yes/no): " response
        case "$response" in
            yes|no) echo "$response"; return ;;
            *) echo "Invalid input. Please type 'yes' or 'no'." ;;
        esac
    done
}

function return_to_menu() {
    echo "Returning to the main menu."
    sleep 2
    main_menu
}

function install_script() {
    echo "Checking for required dependencies..."
    for dep in $ALL_DEPENDENCIES; do
        if ! dpkg -l | grep -qw "$dep"; then
            MISSING_DEPS="$MISSING_DEPS $dep"
        fi
    done

    if [ -n "$MISSING_DEPS" ]; then
        echo "The following packages are required for installation:$MISSING_DEPS"
        response=$(get_yes_no_input "Would you like to install them?")
        if [ "$response" == "no" ]; then
            echo "Installation canceled. Please run the installation process again to proceed."
            return_to_menu
        fi

        echo "Installing required dependencies..."
        apt-get update
        apt-get install -y $MISSING_DEPS
        echo "Required dependencies installed."
    fi

    echo "Cloning the script repository..."
    mkdir -p "$INSTALL_DIR"
    # Replace URL with the actual GitHub repo URL
    git clone https://github.com/your-repo/wireguard-script.git "$INSTALL_DIR"

    echo "Creating a symlink for easier execution..."
    ln -sf "$INSTALL_DIR/wireguard_script_base.py" "$SYMLINK"

    echo "Copying script to $WIREGUARD_ETC for reference..."
    cp "$INSTALL_DIR/wireguard_script_base.py" "$WIREGUARD_ETC/wireguard-manager"

    echo "Installation complete."
    echo "You can now run the script by typing 'wireguard-manager'."
    echo "A copy of the script has been placed in $WIREGUARD_ETC for reference."
    echo "Press Enter to return to the main menu."
    read
    return_to_menu
}

function uninstall_script() {
    echo "The following files will be removed during uninstallation:"
    echo "$INSTALL_DIR"
    echo "$SYMLINK"
    echo "$WIREGUARD_ETC/wireguard-manager"
    response=$(get_yes_no_input "Are you sure you want to uninstall the script and delete these files permanently?")
    if [ "$response" == "no" ]; then
        return_to_menu
    fi

    echo "Removing script files..."
    rm -rf "$INSTALL_DIR"
    rm -f "$SYMLINK"
    rm -f "$WIREGUARD_ETC/wireguard-manager"
    echo "Script files removed."

    echo "Non-default dependencies installed by the script: $NON_DEFAULT_DEPENDENCIES"
    response=$(get_yes_no_input "Would you like to remove these non-default dependencies?")
    if [ "$response" == "yes" ]; then
        echo "Removing non-default dependencies..."
        apt-get remove --purge -y $NON_DEFAULT_DEPENDENCIES
        echo "Non-default dependencies removed."
    else
        echo "The following non-default dependencies remain installed and must be removed manually if desired:"
        echo "$NON_DEFAULT_DEPENDENCIES"
    fi

    echo "The following default dependencies remain installed and must be removed manually if desired:"
    echo "$DEFAULT_DEPENDENCIES"
    echo "To remove them manually, run: sudo apt-get remove --purge -y $DEFAULT_DEPENDENCIES $NON_DEFAULT_DEPENDENCIES"
    echo "Uninstallation complete. Press Enter to return to the main menu."
    read
    return_to_menu
}

function main_menu() {
    while true; do
        echo "WireGuard Script Installation/Uninstallation Menu"
        echo "1. Install the WireGuard script"
        echo "2. Uninstall the WireGuard script"
        echo "x. Exit"
        read -rp "Your choice: " choice
        case "$choice" in
            1) install_script ;;
            2) uninstall_script ;;
            x) echo "Exiting. Goodbye!"; exit 0 ;;
            *) echo "Invalid choice. Please select 1, 2, or x." ;;
        esac
    done
}

if [ "$EUID" -ne 0 ]; then
    echo "Please run this script as root (use sudo)."
    exit 1
fi

main_menu
