#!/usr/bin/env python3
"""
Demonstration of prompt_toolkit features for PPWM.

This example showcases interactive features of prompt_toolkit that could be
used in the PPWM application, focusing on multiple selection interfaces,
styled prompts, and interactive forms.

Run with: python3 prompt_toolkit_example.py
"""
import sys
import os
from datetime import datetime

# Check if prompt_toolkit is installed
try:
    from prompt_toolkit import Application, HTML
    from prompt_toolkit.shortcuts import (
        checkboxlist_dialog, input_dialog, message_dialog, 
        yes_no_dialog, radiolist_dialog, button_dialog,
        clear
    )
    from prompt_toolkit.formatted_text import HTML
    from prompt_toolkit.styles import Style
    from prompt_toolkit.layout.containers import HSplit, VSplit, Window
    from prompt_toolkit.layout.layout import Layout
    from prompt_toolkit.layout.controls import FormattedTextControl
    from prompt_toolkit.key_binding import KeyBindings
    from prompt_toolkit.widgets import Box, Frame, ProgressBar
    from prompt_toolkit.completion import WordCompleter
    from prompt_toolkit.shortcuts import prompt
    from prompt_toolkit.styles import Style
except ImportError:
    print("""
    Error: prompt_toolkit is not installed. 
    Please install it with:
    
    pip install prompt-toolkit
    """)
    sys.exit(1)

# Define style
style = Style.from_dict({
    'dialog': 'bg:#222222',
    'dialog frame.label': 'bg:#000000 #3498db bold',
    'dialog.body': 'bg:#333333 #ffffff',
    'dialog shadow': 'bg:#111111',
    'button': 'bg:#3498db #ffffff',
    'button.focused': 'bg:#2980b9 #ffffff',
    'checkbox': '#3498db',
    'checkbox-list': 'bg:#333333 #ffffff',
    'checkbox-selected': 'bg:#2980b9 #ffffff',
    'dialog.body text-area': 'bg:#222222 #ffffff',
    'dialog.body text-area.cursor-position': 'bg:#ffffff #000000',
})

# ASCII art for PPWM
ASCII_ART = """
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::        ____       ____  ______        ____  __       ____        ::
::        \\ \\ \\     |  _ \\|  _ \\ \\      / /  \\/  |     / / /        ::
::         \\ \\ \\    | |_) | |_) \\ \\ /\\ / /| |\\/| |    / / /         ::
::         / / /    |  __/|  __/ \\ V  V / | |  | |    \\ \\ \\         ::
::        /_/_/     |_|   |_|     \\_/\_/  |_|  |_|     \\_\\_\\        ::
::                                                                  ::
::               Pterodactyl-Pelican-Wireguard-Manager              ::
::                           By: Serfects                           ::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
"""

# Sample data - Fixed to have only 2 elements per tuple
VPS_SERVICES = [
    ("web", "HTTP/HTTPS Web Server"),
    ("dns", "DNS Server"),
    ("ssh", "SSH Server"),
    ("email", "Email Server"),
    ("monitoring", "Monitoring Tools"),
    ("database", "Database Server"), 
    ("docker", "Docker Platform"),
    ("proxy", "Reverse Proxy"),
    ("ftp", "FTP Server"),
    ("vpn", "VPN Service"),
    ("firewall", "Firewall Management"),
    ("backup", "Backup Service"),
    ("analytics", "Analytics Platform"),
    ("cache", "Caching Service"),
    ("loadbalancer", "Load Balancer"),
    ("cdn", "Content Delivery Network"),
    ("messaging", "Messaging Queue"),
    ("storage", "Object Storage"),
]

# Default values for pre-selection
DEFAULT_SERVICES = ["web", "ssh", "monitoring", "docker"]

PORT_PROTOCOLS = [
    ("tcp", "TCP"),
    ("udp", "UDP"),
    ("both", "Both TCP & UDP"),
]

# Multi-page selection data
SERVER_ROLES = [
    ("web", "Web Server"),
    ("db", "Database Server"),
    ("game", "Game Server"),
    ("mail", "Mail Server"),
    ("media", "Media Server"),
    ("vpn", "VPN Server"),
    ("proxy", "Reverse Proxy"),
    ("dns", "DNS Server"),
    ("ldap", "LDAP Server"),
    ("analytics", "Analytics Server"),
    ("monitoring", "Monitoring Server"),
    ("backup", "Backup Server"),
]

SECURITY_OPTIONS = [
    ("firewall", "Firewall"),
    ("fail2ban", "Fail2Ban"),
    ("selinux", "SELinux"),
    ("ssh_hardening", "SSH Hardening"),
    ("ufw", "UFW"),
    ("encryption", "Disk Encryption"),
]

MONITORING_OPTIONS = [
    ("prometheus", "Prometheus"),
    ("grafana", "Grafana"),
    ("netdata", "Netdata"),
    ("nagios", "Nagios"),
    ("zabbix", "Zabbix"),
]

# Additional sample data
PORTS = [
    {"id": 1, "port": 80, "protocol": "TCP", "service": "Web Server", "forwarded_to": "10.0.0.2"},
    {"id": 2, "port": 443, "protocol": "TCP", "service": "Web Server (SSL)", "forwarded_to": "10.0.0.2"},
    {"id": 3, "port": 25565, "protocol": "TCP/UDP", "service": "Minecraft", "forwarded_to": "10.0.0.4"},
    {"id": 4, "port": 22, "protocol": "TCP", "service": "SSH", "forwarded_to": "10.0.0.3"},
    {"id": 5, "port": 53, "protocol": "UDP", "service": "DNS", "forwarded_to": "10.0.0.5"},
]

WG_COMMANDS = [
    "status", "show", "add-peer", "remove-peer", "list-peers", 
    "add-port", "remove-port", "list-ports", "help", "quit"
]

def main():
    """Main function to run the demo."""
    # Clear the screen
    clear()
    
    # Display welcome screen
    message_dialog(
        title="prompt_toolkit Demo for PPWM",
        text=ASCII_ART + "\n\nThis demo showcases features of prompt_toolkit that could enhance PPWM.",
        style=style
    ).run()
    
    # Show main menu
    while True:
        # Fixed the buttons format - removed the third parameter (True) from the first button
        result = button_dialog(
            title="PPWM Feature Demos",
            text="Select a feature to explore:",
            buttons=[
                ("MultiSelect", "1"),  # Fixed: removed the True parameter
                ("Multi-Page Config", "2"),
                ("Form Input", "3"),
                ("Progress", "4"),
                ("Styling", "5"),
                ("Command Shell", "6"),  # New option
                ("Port Manager", "7"),   # New option
                ("Exit", "x"),
            ],
            style=style
        ).run()
        
        if result == "1":
            show_multiselect_demo()
        elif result == "2":
            show_multipage_config()
        elif result == "3":
            show_form_demo()
        elif result == "4":
            show_progress_demo()
        elif result == "5":
            show_styling_demo()
        elif result == "6":
            show_command_shell()  # New function
        elif result == "7":
            show_port_manager()   # New function
        else:
            # Exit
            message_dialog(
                title="Thank You",
                text="Thank you for exploring prompt_toolkit features for PPWM!",
                style=style
            ).run()
            return

def show_multiselect_demo():
    """Demo of multiple selection features with enhanced scrolling."""
    # Multiple selection with checkboxlist - remove key_bindings parameter
    result = checkboxlist_dialog(
        title="Select Services to Enable",
        text="Choose services to install on your VPS:\n\n"
             "Use Space to toggle selection\n"
             "Enter to confirm, Esc to cancel",
        values=VPS_SERVICES,
        default_values=DEFAULT_SERVICES,
        style=style
    ).run()
    
    if result:
        # Show selected services
        selected_services = [desc for key, desc in VPS_SERVICES if key in result]
        message_dialog(
            title="Selected Services",
            text="You selected the following services:\n\n" + "\n".join(f"• {service}" for service in selected_services),
            style=style
        ).run()
    
    # Radio button selection for protocols
    protocol = radiolist_dialog(
        title="Select Protocol",
        text="Choose the protocol for port forwarding:",
        values=PORT_PROTOCOLS,
        style=style
    ).run()
    
    if protocol:
        message_dialog(
            title="Protocol Selected",
            text=f"Selected protocol: {dict(PORT_PROTOCOLS)[protocol]}",
            style=style
        ).run()

def show_multipage_config():
    """Demo of multi-page configuration with back/forward navigation and persistent selections."""
    # Start with empty selections
    all_selections = {
        "roles": [],
        "security": [],
        "monitoring": []
    }
    
    # Step 1: Introduction
    message_dialog(
        title="Multi-Page Configuration",
        text="This demo will guide you through a multi-step configuration process.\n"
             "Each step allows you to select multiple options.\n\n"
             "You can navigate back and forth between pages while keeping your selections.",
        style=style
    ).run()
    
    # Page navigation loop
    current_page = 0
    total_pages = 3
    
    while 0 <= current_page < total_pages:
        if current_page == 0:
            # Page 1: Server Roles
            page_title = "Step 1 of 3: Server Roles"
            help_text = "Select server roles to configure"
            
            # Show the roles selection dialog
            roles_result = checkboxlist_dialog(
                title=page_title,
                text=help_text,
                values=SERVER_ROLES,
                default_values=all_selections["roles"],
                style=style
            ).run()
            
            if roles_result is None:  # User cancelled
                break
                
            all_selections["roles"] = roles_result
            
            # Navigation and selection options at bottom
            action = button_dialog(
                title="Options",
                text=f"Current page: {page_title}",
                buttons=[
                    ("Select All", "all"),
                    ("Select None", "none"),
                    ("Next →", "next"),
                    ("Cancel", "cancel")
                ],
                style=style
            ).run()
            
            if action == "all":
                all_selections["roles"] = [key for key, _ in SERVER_ROLES]
                continue
            elif action == "none":
                all_selections["roles"] = []
                continue
            elif action == "next":
                current_page += 1
                continue
            elif action == "cancel":
                break
            
        elif current_page == 1:
            # Page 2: Security Options
            page_title = "Step 2 of 3: Security Options" 
            help_text = "Select security options to configure"
            
            # Show the security options dialog
            security_result = checkboxlist_dialog(
                title=page_title,
                text=help_text,
                values=SECURITY_OPTIONS,
                default_values=all_selections["security"],
                style=style
            ).run()
            
            if security_result is None:  # User cancelled
                break
                
            all_selections["security"] = security_result
            
            # Navigation and selection options at bottom
            action = button_dialog(
                title="Options",
                text=f"Current page: {page_title}",
                buttons=[
                    ("Select All", "all"),
                    ("Select None", "none"),
                    ("← Back", "back"),
                    ("Next →", "next"),
                    ("Cancel", "cancel")
                ],
                style=style
            ).run()
            
            if action == "all":
                all_selections["security"] = [key for key, _ in SECURITY_OPTIONS]
                continue
            elif action == "none":
                all_selections["security"] = []
                continue
            elif action == "back":
                current_page -= 1
                continue
            elif action == "next":
                current_page += 1
                continue
            elif action == "cancel":
                break
            
        elif current_page == 2:
            # Page 3: Monitoring Options
            page_title = "Step 3 of 3: Monitoring Options"
            help_text = "Select monitoring tools to install"
            
            # Show the monitoring options dialog
            monitoring_result = checkboxlist_dialog(
                title=page_title,
                text=help_text,
                values=MONITORING_OPTIONS,
                default_values=all_selections["monitoring"],
                style=style
            ).run()
            
            if monitoring_result is None:  # User cancelled
                break
                
            all_selections["monitoring"] = monitoring_result
            
            # Navigation and selection options at bottom
            action = button_dialog(
                title="Options",
                text=f"Current page: {page_title}",
                buttons=[
                    ("Select All", "all"),
                    ("Select None", "none"),
                    ("← Back", "back"),
                    ("Finish", "finish"),
                    ("Cancel", "cancel")
                ],
                style=style
            ).run()
            
            if action == "all":
                all_selections["monitoring"] = [key for key, _ in MONITORING_OPTIONS]
                continue
            elif action == "none":
                all_selections["monitoring"] = []
                continue
            elif action == "back":
                current_page -= 1
                continue
            elif action == "finish":
                current_page += 1  # Move to summary
                break  # Exit the configuration loop to show summary later
            elif action == "cancel":
                break
    
    # Check if the user completed all steps
    if current_page >= total_pages:
        # User completed all steps, display the summary
        
        # Get selected items for summary display
        selected_roles = [desc for key, desc in SERVER_ROLES if key in all_selections["roles"]]
        selected_security = [desc for key, desc in SECURITY_OPTIONS if key in all_selections["security"]]
        selected_monitoring = [desc for key, desc in MONITORING_OPTIONS if key in all_selections["monitoring"]]
        
        # Build the summary text
        summary_text = HTML(
            "<b>Configuration Summary</b>\n\n"
            "<ansiblue><u>Server Roles:</u></ansiblue>\n" +
            "\n".join(f"• {role}" for role in selected_roles) +
            "\n\n<ansiblue><u>Security Options:</u></ansiblue>\n" +
            "\n".join(f"• {option}" for option in selected_security) +
            "\n\n<ansiblue><u>Monitoring Tools:</u></ansiblue>\n" +
            "\n".join(f"• {tool}" for tool in selected_monitoring)
        )
        
        # Show the summary
        message_dialog(
            title="Configuration Summary",
            text=summary_text,
            style=style
        ).run()
        
        # Confirm configuration
        if yes_no_dialog(
            title="Confirm Configuration",
            text="Do you want to apply this configuration?",
            style=style
        ).run():
            # Show success message with progress
            show_progress_demo(quick=True)
            message_dialog(
                title="Configuration Applied",
                text=HTML("<ansigreen>Configuration has been successfully applied!</ansigreen>"),
                style=style
            ).run()

def show_form_demo():
    """Demo of form input capabilities."""
    # Get VPS hostname
    hostname = input_dialog(
        title="VPS Configuration",
        text="Enter your VPS hostname:",
        default="vps.example.com",
        style=style
    ).run()
    
    if not hostname:
        return
    
    # Get IP address with validation
    ip_address = None
    while not ip_address:
        ip = input_dialog(
            title="VPS Configuration",
            text="Enter your VPS IP address:",
            default="198.51.100.1",
            style=style
        ).run()
        
        if not ip:
            return
            
        # Simple validation (very basic)
        parts = ip.split(".")
        if len(parts) == 4 and all(p.isdigit() and 0 <= int(p) <= 255 for p in parts):
            ip_address = ip
        else:
            message_dialog(
                title="Invalid IP",
                text="Please enter a valid IPv4 address (e.g., 198.51.100.1)",
                style=style
            ).run()
    
    # Show confirmation of settings
    message_dialog(
        title="Configuration Confirmed",
        text=f"VPS Configuration:\n\nHostname: {hostname}\nIP Address: {ip_address}",
        style=style
    ).run()

def show_progress_demo(quick=False):
    """Demo progress bars and loading indicators."""
    import time
    from prompt_toolkit.shortcuts import ProgressBar
    
    # Ask if user wants to start operation
    if not quick and not yes_no_dialog(
        title="Start Operation",
        text="This will demonstrate progress tracking. Continue?",
        style=style
    ).run():
        return
    
    # Setup progress tracking titles
    title1 = HTML("<b>Updating system packages...</b>")
    title2 = HTML("<b>Configuring WireGuard components...</b>")
    title3 = HTML("<b>Setting up forwarding rules...</b>")
    
    # Run progress bars
    with ProgressBar(title=title1, style=style) as pb1:
        for i in pb1(range(100)):
            time.sleep(0.02)
    
    with ProgressBar(title=title2, style=style) as pb2:
        for i in pb2(range(100)):
            time.sleep(0.01)
    
    with ProgressBar(title=title3, style=style) as pb3:
        values = [0, 20, 30, 40, 50, 60, 70, 80, 90, 95, 96, 97, 98, 99, 100]
        for i in pb3(values):
            time.sleep(0.1)
    
    # Show completion
    message_dialog(
        title="Operation Complete",
        text="All operations completed successfully!",
        style=style
    ).run()

def show_styling_demo():
    """Demo of styled text and themed UI components."""
    message_dialog(
        title="Styled UI Elements",
        text=HTML(
            "prompt_toolkit supports rich text <b>formatting</b> with:\n\n"
            "<ansired>Error messages in red</ansired>\n"
            "<ansigreen>Success messages in green</ansigreen>\n"
            "<ansiyellow>Warnings in yellow</ansiyellow>\n"
            "<ansiblue>Information in blue</ansiblue>\n\n"
            "You can also use <u>underlines</u> and <i>italics</i> for emphasis."
        ),
        style=style
    ).run()
    
    # Show a custom dialog with formatted content
    message_dialog(
        title="PPWM Status Overview",
        text=HTML(
            "<b>WireGuard Status:</b> <ansigreen>Active</ansigreen>\n"
            "<b>Active Clients:</b> <ansiblue>3 of 5</ansiblue>\n"
            "<b>Last Connection:</b> <ansiblue>2023-12-15 13:45</ansiblue>\n"
            "\n<b>System Information:</b>\n"
            "  <b>CPU:</b> <ansiyellow>15%</ansiyellow>\n"
            "  <b>Memory:</b> <ansiyellow>32%</ansiyellow>\n"
            "  <b>Disk:</b> <ansigreen>24%</ansigreen>\n"
            "\n<b>Recent Events:</b>\n"
            "  <ansigray>13:42:01</ansigray> <ansigreen>Client 2 connected</ansigreen>\n"
            "  <ansigray>13:30:15</ansigray> <ansired>Failed login attempt</ansired>\n"
            "  <ansigray>13:15:22</ansigray> <ansiblue>Config file updated</ansiblue>"
        ),
        style=style
    ).run()

def show_command_shell():
    """Interactive command shell with auto-completion."""
    # Clear screen
    clear()
    
    # Display welcome message
    print(HTML(
        "<ansiyellow>::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::</ansiyellow>\n"
        "<ansiblue>PPWM Command Shell Demo</ansiblue>\n"
        "<ansiyellow>::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::</ansiyellow>\n\n"
        "Type commands to manage WireGuard. Use <ansigreen>help</ansigreen> to see available commands.\n"
        "Press <ansigreen>Ctrl+D</ansigreen> or type <ansigreen>quit</ansigreen> to exit.\n"
    ).format())
    
    # Create command completer
    command_completer = WordCompleter(WG_COMMANDS)
    
    # Command loop
    history = []
    while True:
        try:
            command = prompt(
                HTML("<ansiblue>wg></ansiblue> "),
                completer=command_completer,
                style=style
            )
            
            # Add to history
            if command and command not in history:
                history.append(command)
            
            # Process command
            if command == "quit":
                break
                
            elif command == "help":
                print(HTML(
                    "<b>Available commands:</b>\n\n"
                    "<ansigreen>status</ansigreen>      - Show WireGuard status\n"
                    "<ansigreen>show</ansigreen>        - Show WireGuard configuration\n"
                    "<ansigreen>add-peer</ansigreen>    - Add a new peer\n"
                    "<ansigreen>remove-peer</ansigreen> - Remove an existing peer\n"
                    "<ansigreen>list-peers</ansigreen>  - List all peers\n"
                    "<ansigreen>add-port</ansigreen>    - Add a port forwarding rule\n"
                    "<ansigreen>remove-port</ansigreen> - Remove a port forwarding rule\n"
                    "<ansigreen>list-ports</ansigreen>  - List all port forwarding rules\n"
                    "<ansigreen>help</ansigreen>        - Show this help\n"
                    "<ansigreen>quit</ansigreen>        - Exit the shell\n"
                ).format())
                
            elif command == "status":
                print(HTML(
                    "<ansigreen>● WireGuard is running</ansigreen>\n"
                    "<b>Interface:</b> wg0\n"
                    "<b>Public IP:</b> 203.0.113.10\n"
                    "<b>Active Peers:</b> 3/4\n"
                ).format())
                
            elif command == "list-peers":
                print(HTML(
                    "<b>Connected Peers:</b>\n\n"
                    "<ansigreen>●</ansigreen> <b>laptop</b> (10.0.0.2) - Last handshake: 2 minutes ago\n"
                    "<ansigreen>●</ansigreen> <b>phone</b> (10.0.0.3) - Last handshake: 5 minutes ago\n"
                    "<ansired>○</ansired> <b>server</b> (10.0.0.4) - Last handshake: 3 hours ago\n"
                    "<ansigreen>●</ansigreen> <b>tablet</b> (10.0.0.5) - Last handshake: 15 minutes ago\n"
                ).format())
                
            elif command == "list-ports":
                print(HTML("<b>Port Forwarding Rules:</b>\n").format())
                for port in PORTS:
                    print(HTML(
                        f"<b>ID {port['id']}:</b> Port {port['port']} ({port['protocol']}) - "
                        f"{port['service']} → {port['forwarded_to']}"
                    ).format())
                    
            elif command:
                print(HTML(f"<ansiyellow>Simulating command:</ansiyellow> {command}\n").format())
                
        except KeyboardInterrupt:
            continue
        except EOFError:
            break
            
    print("\nExiting command shell")

def show_port_manager():
    """Interactive port forwarding rule manager."""
    # Display title and intro
    message_dialog(
        title="Port Forwarding Manager",
        text="This demo shows how to manage port forwarding rules using prompt_toolkit.",
        style=style
    ).run()
    
    while True:
        # Show table of ports
        port_table = "\n".join([
            f"{port['id']}: {port['port']} ({port['protocol']}) - {port['service']} → {port['forwarded_to']}"
            for port in PORTS
        ])
        
        action = button_dialog(
            title="Port Forwarding Rules",
            text=HTML(
                "<b>Current Port Forwarding Rules:</b>\n\n" + port_table + 
                "\n\nSelect an action to perform:"
            ),
            buttons=[
                ("Add Rule", "add"),
                ("Edit Rule", "edit"),
                ("Delete Rule", "delete"),
                ("Back", "back"),
            ],
            style=style
        ).run()
        
        if action == "back":
            break
            
        elif action == "add":
            # Input port number
            port_number = input_dialog(
                title="Add Port Forwarding Rule",
                text="Enter the external port number:",
                style=style
            ).run()
            
            if not port_number:
                continue
                
            # Select protocol
            protocol = radiolist_dialog(
                title="Add Port Forwarding Rule",
                text="Select the protocol:",
                values=[
                    ("tcp", "TCP"),
                    ("udp", "UDP"),
                    ("both", "TCP and UDP"),
                ],
                style=style
            ).run()
            
            if not protocol:
                continue
                
            # Input service name
            service = input_dialog(
                title="Add Port Forwarding Rule",
                text="Enter a description for this service:",
                style=style
            ).run()
            
            if not service:
                continue
                
            # Select destination from peers
            destination = radiolist_dialog(
                title="Add Port Forwarding Rule",
                text="Forward to which internal host?",
                values=[
                    ("10.0.0.2", "laptop (10.0.0.2)"),
                    ("10.0.0.3", "phone (10.0.0.3)"),
                    ("10.0.0.4", "server (10.0.0.4)"),
                    ("10.0.0.5", "tablet (10.0.0.5)"),
                ],
                style=style
            ).run()
            
            if not destination:
                continue
                
            # Show confirmation with all details
            protocol_name = {"tcp": "TCP", "udp": "UDP", "both": "TCP/UDP"}[protocol]
            if yes_no_dialog(
                title="Confirm Port Forwarding",
                text=f"Add the following port forwarding rule?\n\n"
                     f"Port: {port_number}\n"
                     f"Protocol: {protocol_name}\n"
                     f"Service: {service}\n"
                     f"Destination: {destination}",
                style=style
            ).run():
                # Add new rule (in a real app, this would modify iptables/nftables)
                new_id = max(p["id"] for p in PORTS) + 1
                PORTS.append({
                    "id": new_id,
                    "port": int(port_number),
                    "protocol": protocol_name,
                    "service": service,
                    "forwarded_to": destination
                })
                message_dialog(
                    title="Success",
                    text=HTML(f"<ansigreen>Port forwarding rule added successfully!</ansigreen>"),
                    style=style
                ).run()
        
        elif action == "delete":
            # Select rule to delete
            options = [(str(p["id"]), f"Port {p['port']} ({p['protocol']}) - {p['service']}") for p in PORTS]
            rule_id = radiolist_dialog(
                title="Delete Port Forwarding Rule",
                text="Select the rule to delete:",
                values=options,
                style=style
            ).run()
            
            if not rule_id:
                continue
                
            # Find the rule
            rule = next((p for p in PORTS if str(p["id"]) == rule_id), None)
            
            # Confirm deletion
            if yes_no_dialog(
                title="Confirm Deletion",
                text=f"Are you sure you want to delete this rule?\n\n"
                     f"Port {rule['port']} ({rule['protocol']}) - {rule['service']} → {rule['forwarded_to']}",
                style=style
            ).run():
                # Remove the rule
                PORTS[:] = [p for p in PORTS if str(p["id"]) != rule_id]
                message_dialog(
                    title="Success",
                    text=HTML(f"<ansigreen>Port forwarding rule deleted successfully!</ansigreen>"),
                    style=style
                ).run()

if __name__ == "__main__":
    main()
