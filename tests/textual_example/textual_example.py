#!/usr/bin/env python3
"""
Enhanced Textual demo for PPWM showcasing advanced TUI capabilities.

This example demonstrates the power of Textual for creating rich terminal
interfaces with tables, charts, forms, responsive layouts, and more.
"""
import sys
import random
import json
import os
import asyncio  # Required for dashboard updates
from datetime import datetime, timedelta
from pathlib import Path

try:
    # Fix 2: Ensure we're importing the correct classes for our Textual version
    # You may need to adjust based on your specific Textual version
    from textual import on, work, events
    from textual.app import App, ComposeResult
    from textual.binding import Binding
    from textual.containers import Container, Vertical, Horizontal, Grid, ScrollableContainer
    from textual.css.query import NoMatches
    from textual.screen import Screen, ModalScreen
    from textual.widgets import (
        Header, Footer, Static, Button, Label, Checkbox, Input, TextArea,
        LoadingIndicator, ProgressBar, RadioSet, RadioButton, Markdown, Rule,
        DataTable, Tree, OptionList, ContentSwitcher, TabbedContent, Tab, 
        Switch, DirectoryTree, Select
    )
    from textual.widgets.tree import TreeNode
    from textual import log
except ImportError:
    print("""
    Error: Textual is not installed.
    Please install it with:
    
    pip install textual
    """)
    sys.exit(1)

# ASCII art - formatted for Textual (CSS styling will be applied)
ASCII_ART = r"""
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
"""

# Sample data for multi-page selection demo
SERVER_ROLES = [
    {"id": "web", "name": "Web Server", "description": "For hosting websites and web applications"},
    {"id": "db", "name": "Database Server", "description": "For hosting MySQL, PostgreSQL, etc."},
    {"id": "game", "name": "Game Server", "description": "For hosting game servers like Minecraft"},
    {"id": "mail", "name": "Mail Server", "description": "For email services"},
    {"id": "media", "name": "Media Server", "description": "For streaming media content"},
    {"id": "vpn", "name": "VPN Server", "description": "For secure remote access"},
]

SECURITY_OPTIONS = [
    {"id": "firewall", "name": "Firewall", "description": "Basic firewall protection"},
    {"id": "fail2ban", "name": "Fail2Ban", "description": "Protection against brute force attacks"},
    {"id": "selinux", "name": "SELinux", "description": "Enhanced access control"},
    {"id": "ssh_hardening", "name": "SSH Hardening", "description": "Secure SSH configuration"},
    {"id": "ufw", "name": "UFW", "description": "Uncomplicated Firewall"},
    {"id": "encryption", "name": "Disk Encryption", "description": "Encrypt sensitive data"},
]

MONITORING_OPTIONS = [
    {"id": "prometheus", "name": "Prometheus", "description": "Metrics collection and alerting"},
    {"id": "grafana", "name": "Grafana", "description": "Data visualization and monitoring"},
    {"id": "netdata", "name": "Netdata", "description": "Real-time performance monitoring"},
    {"id": "nagios", "name": "Nagios", "description": "IT infrastructure monitoring"},
    {"id": "zabbix", "name": "Zabbix", "description": "Enterprise-level monitoring solution"},
]

# Sample data for dashboard
SAMPLE_PEERS = [
    {"name": "laptop", "ip": "10.0.0.2", "status": "Connected", "handshake": "2 min ago", "transfer": "↓ 1.2 GB ↑ 250 MB"},
    {"name": "phone", "ip": "10.0.0.3", "status": "Connected", "handshake": "5 min ago", "transfer": "↓ 350 MB ↑ 45 MB"},
    {"name": "server", "ip": "10.0.0.4", "status": "Disconnected", "handshake": "3 hours ago", "transfer": "↓ 4.5 GB ↑ 1.2 GB"},
    {"name": "tablet", "ip": "10.0.0.5", "status": "Connected", "handshake": "15 min ago", "transfer": "↓ 250 MB ↑ 30 MB"},
]

# Sample logs for log viewer
SYSTEM_LOGS = [
    {"timestamp": "2023-12-15 14:21:33", "level": "INFO", "message": "WireGuard service started"},
    {"timestamp": "2023-12-15 14:21:45", "level": "INFO", "message": "Client 'laptop' connected (10.0.0.2)"},
    {"timestamp": "2023-12-15 14:25:12", "level": "INFO", "message": "Client 'phone' connected (10.0.0.3)"},
    {"timestamp": "2023-12-15 14:30:07", "level": "WARNING", "message": "Failed authentication attempt from 192.168.1.155"},
    {"timestamp": "2023-12-15 14:35:22", "level": "INFO", "message": "Client 'tablet' connected (10.0.0.5)"},
    {"timestamp": "2023-12-15 14:40:18", "level": "ERROR", "message": "Failed to update port forwarding rule: Permission denied"},
    {"timestamp": "2023-12-15 14:42:30", "level": "INFO", "message": "Port forwarding rule added for 10.0.0.2:25565"},
    {"timestamp": "2023-12-15 14:45:11", "level": "DEBUG", "message": "Routine maintenance check started"},
    {"timestamp": "2023-12-15 14:46:05", "level": "DEBUG", "message": "Routine maintenance check completed"},
]

# Sample configuration for config editor
SAMPLE_CONFIG = """[Interface]
Address = 10.0.0.1/24
ListenPort = 51820
PrivateKey = <private key>

# This is a client configuration section
[Peer]
# Laptop device
PublicKey = <laptop public key>
AllowedIPs = 10.0.0.2/32
PersistentKeepalive = 25

[Peer]
# Phone device
PublicKey = <phone public key>
AllowedIPs = 10.0.0.3/32
PersistentKeepalive = 25

[Peer]
# Server
PublicKey = <server public key>
AllowedIPs = 10.0.0.4/32
PersistentKeepalive = 25

[Peer]
# Tablet device
PublicKey = <tablet public key>
AllowedIPs = 10.0.0.5/32
PersistentKeepalive = 25"""

# ========== Custom Widgets ==========
class BetterCheckbox(Horizontal):
    """An enhanced checkbox with description and better styling."""
    
    def __init__(self, id, label, description="", value=False):
        super().__init__()
        self.checkbox_id = id
        self.label = label
        self.description = description
        self.initial_value = value
    
    def compose(self) -> ComposeResult:
        yield Checkbox(value=self.initial_value, id=f"checkbox-{self.checkbox_id}")
        yield Vertical(
            Label(self.label, classes="checkbox-label"),
            Label(self.description, classes="checkbox-description") if self.description else Static(""),
            classes="checkbox-content"
        )
    
    @property
    def value(self):
        """Get the current value of the checkbox."""
        return self.query_one(f"#checkbox-{self.checkbox_id}", Checkbox).value
    
    @value.setter
    def value(self, new_value):
        """Set the value of the checkbox."""
        self.query_one(f"#checkbox-{self.checkbox_id}", Checkbox).value = new_value

# ========== Configuration Screens ==========
KEY_BINDINGS_INFO = """
Keyboard Navigation:
- Tab/Shift+Tab: Navigate between elements
- ↑/↓/←/→: Navigate within lists and grids
- Space/Enter: Select/activate focused item
- Esc: Go back/cancel
- Q: Quit application
- F1: Show this help screen
- 1-7: Quick access to menu options
- A: Select all in selection screens
- N: Select none in selection screens
- S: Save in editor
- F: Filter in log viewer
- R: Refresh dashboard
"""

class HelpScreen(Screen):
    """Screen showing keyboard navigation help."""
    
    BINDINGS = [
        Binding("escape", "app.pop_screen", "Close Help")
    ]
    
    def compose(self) -> ComposeResult:
        yield Static(KEY_BINDINGS_INFO, id="help-text")
    
    def on_key(self, event):
        """Handle any key press to close help screen."""
        self.app.pop_screen()

class SelectionPage(Screen):
    """Base screen for selection pages with common functionality."""
    
    BINDINGS = [
        Binding("a", "select_all", "Select All"),
        Binding("n", "select_none", "Select None"),
        Binding("escape", "go_back", "Back"),
        Binding("enter", "next_page", "Next"),
        Binding("f1", "show_help", "Help"),
    ]
    
    def __init__(self, title, items, prev_selections=None):
        super().__init__()
        self.title = title
        self.items = items
        self.prev_selections = prev_selections or []
        self.selected = []
    
    def compose(self) -> ComposeResult:
        yield Header(show_clock=True)
        yield Container(
            Static(self.title, classes="page-title"),
            Static("Select the options you want to enable:", classes="page-description"),
            ScrollableContainer(
                *[BetterCheckbox(
                    id=item["id"],
                    label=item["name"],
                    description=item["description"],
                    value=item["id"] in self.prev_selections
                ) for item in self.items],
                id="options-container"
            ),
            Horizontal(
                Button("Select All", variant="primary", id="select-all"),
                Button("Select None", variant="primary", id="select-none"),
                classes="button-row"
            ),
            Horizontal(
                Button("Previous", variant="default", id="previous"),
                Button("Next", variant="success", id="next"),
                classes="button-row"
            ),
            id="page-content"
        )
        yield Footer()
    
    def on_mount(self):
        """Initialize the screen when mounted."""
        # If we have previous selections, restore them
        if self.prev_selections:
            for item in self.items:
                if item["id"] in self.prev_selections:
                    self.query_one(f"#checkbox-{item['id']}", Checkbox).value = True
    
    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Handle button press events."""
        button_id = event.button.id
        
        if button_id == "select-all":
            for item in self.items:
                self.query_one(f"#checkbox-{item['id']}", Checkbox).value = True
                
        elif button_id == "select-none":
            for item in self.items:
                self.query_one(f"#checkbox-{item['id']}", Checkbox).value = False
                
        elif button_id == "previous":
            self.save_selections()
            self.app.pop_screen()
            
        elif button_id == "next":
            self.save_selections()
            if self.__class__.__name__ == "ServerRolesScreen":
                self.app.push_screen(SecurityOptionsScreen(self.selected))
            elif self.__class__.__name__ == "SecurityOptionsScreen":
                self.app.push_screen(MonitoringOptionsScreen(self.selected))
            elif self.__class__.__name__ == "MonitoringOptionsScreen":
                self.app.push_screen(SummaryScreen(self.selected))
    
    def save_selections(self):
        """Save the current selections."""
        self.selected = []
        for item in self.items:
            checkbox = self.query_one(f"#checkbox-{item['id']}", Checkbox)
            if checkbox.value:
                self.selected.append(item["id"])

    def action_select_all(self) -> None:
        """Select all checkboxes."""
        for item in self.items:
            self.query_one(f"#checkbox-{item['id']}", Checkbox).value = True
    
    def action_select_none(self) -> None:
        """Clear all checkbox selections."""
        for item in self.items:
            self.query_one(f"#checkbox-{item['id']}", Checkbox).value = False
    
    def action_go_back(self) -> None:
        """Go back to previous screen."""
        self.save_selections()
        self.app.pop_screen()
    
    def action_next_page(self) -> None:
        """Go to the next page."""
        self.save_selections()
        if self.__class__.__name__ == "ServerRolesScreen":
            self.app.push_screen(SecurityOptionsScreen(self.selected))
        elif self.__class__.__name__ == "SecurityOptionsScreen":
            self.app.push_screen(MonitoringOptionsScreen(self.selected))
        elif self.__class__.__name__ == "MonitoringOptionsScreen":
            self.app.push_screen(SummaryScreen(self.selected))
    
    def action_show_help(self) -> None:
        """Show the keyboard help screen."""
        self.app.push_screen(HelpScreen())

class ServerRolesScreen(SelectionPage):
    """First page: Select server roles."""
    
    def __init__(self, prev_selections=None):
        super().__init__(
            title="Step 1: Server Roles",
            items=SERVER_ROLES,
            prev_selections=prev_selections
        )

class SecurityOptionsScreen(SelectionPage):
    """Second page: Select security options."""
    
    def __init__(self, prev_selections=None):
        super().__init__(
            title="Step 2: Security Options",
            items=SECURITY_OPTIONS,
            prev_selections=prev_selections
        )

class MonitoringOptionsScreen(SelectionPage):
    """Third page: Select monitoring options."""
    
    def __init__(self, prev_selections=None):
        super().__init__(
            title="Step 3: Monitoring Options",
            items=MONITORING_OPTIONS,
            prev_selections=prev_selections
        )

class SummaryScreen(Screen):
    """Final screen showing a summary of all selections."""
    
    BINDINGS = [
        Binding("escape", "app.pop_screen", "Back"),
        Binding("enter", "confirm", "Confirm"),
        Binding("f1", "show_help", "Help")
    ]
    
    def __init__(self, selections=None):
        super().__init__()
        # Fix: Use a private attribute to store selections without Textual tracking it
        self._user_selections = [] if selections is None else selections
    
    def compose(self) -> ComposeResult:
        yield Header(show_clock=True)
        yield Container(
            Static("Configuration Summary", classes="page-title"),
            Static("Review your selections before confirming:", classes="page-description"),
            ScrollableContainer(
                id="summary-container"
            ),
            Horizontal(
                Button("Back", variant="default", id="back"),
                Button("Confirm", variant="success", id="confirm"),
                classes="button-row"
            ),
            id="page-content"
        )
        yield Footer()
    
    def on_mount(self):
        """Initialize the screen when mounted and populate summary."""
        summary_container = self.query_one("#summary-container")
        
        # Use the private attribute instead of selections dictionary
        selected_items = self._user_selections
        
        # Create sections for each category
        roles = [item for item in SERVER_ROLES if item["id"] in selected_items]
        security = [item for item in SECURITY_OPTIONS if item["id"] in selected_items]
        monitoring = [item for item in MONITORING_OPTIONS if item["id"] in selected_items]
        
        # Server roles summary
        summary_container.mount(Label("Server Roles:", classes="summary-category"))
        if roles:
            for role in roles:
                summary_container.mount(
                    Label(f"• {role['name']}", classes="summary-item")
                )
        else:
            summary_container.mount(
                Label("  No server roles selected", classes="summary-empty")
            )
        summary_container.mount(Rule())
        
        # Security options summary
        summary_container.mount(Label("Security Options:", classes="summary-category"))
        if security:
            for option in security:
                summary_container.mount(
                    Label(f"• {option['name']}", classes="summary-item")
                )
        else:
            summary_container.mount(
                Label("  No security options selected", classes="summary-empty")
            )
        summary_container.mount(Rule())
        
        # Monitoring options summary
        summary_container.mount(Label("Monitoring Options:", classes="summary-category"))
        if monitoring:
            for option in monitoring:
                summary_container.mount(
                    Label(f"• {option['name']}", classes="summary-item")
                )
        else:
            summary_container.mount(
                Label("  No monitoring options selected", classes="summary-empty")
            )
    
    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Handle button press events."""
        button_id = event.button.id
        
        if button_id == "back":
            self.app.pop_screen()
        
        elif button_id == "confirm":
            self.app.push_screen(SuccessScreen())

    def action_confirm(self) -> None:
        """Confirm the configuration and proceed."""
        self.app.push_screen(SuccessScreen())
    
    def action_show_help(self) -> None:
        """Show the keyboard help screen."""
        self.app.push_screen(HelpScreen())

class SuccessScreen(Screen):
    """Screen shown after confirming selections."""
    
    def compose(self) -> ComposeResult:
        yield Header(show_clock=True)
        yield Container(
            Static("🎉 Configuration Complete", classes="success-title"),
            Static("Your server will be configured with the selected options.", classes="success-message"),
            LoadingIndicator(classes="loading", id="loading"),
            Button("Return to Main Menu", variant="primary", id="done"),
            id="success-container"
        )
        yield Footer()
    
    def on_mount(self) -> None:
        """Initialize the screen and set a timer to hide loading indicator."""
        # Fix: Use the proper call_later argument order
        self.call_later(self.hide_loading, 3)
    
    def hide_loading(self, timer=None) -> None:
        """Hide the loading indicator.
        
        Args:
            timer: The timer object passed by Textual (can be ignored)
        """
        try:
            loading = self.query_one("#loading")
            loading.remove()
            self.query_one("#success-container").mount(
                Static("Configuration applied successfully!", classes="success-message")
            )
        except Exception:
            # Handle any errors quietly
            pass
    
    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Handle button press events."""
        if event.button.id == "done":
            self.app.pop_screen()
            self.app.pop_screen()
            self.app.pop_screen()
            self.app.pop_screen()

# ========== Feature Demo Screens ==========
class WelcomeScreen(Screen):
    """Welcome screen for the demo app."""
    
    def compose(self) -> ComposeResult:
        yield Header(show_clock=True)
        yield Static(ASCII_ART, id="ascii-art")
        yield Static("Textual Demo for PPWM", id="app-title")
        yield Static("Showcasing rich terminal user interfaces with Textual", id="app-subtitle")
        yield Container(
            Button("Multi-Page Selection Demo", id="selection-demo", variant="success"),
            Button("Dashboard Demo", id="dashboard-demo", variant="primary"),
            Button("Log Viewer", id="log-viewer", variant="primary"),
            Button("Configuration Editor", id="config-editor", variant="primary"),
            Button("Exit", id="exit", variant="error"),
            id="main-buttons"
        )
        yield Footer()
    
    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Handle button press events."""
        button_id = event.button.id
        
        if button_id == "selection-demo":
            self.app.push_screen(ServerRolesScreen())
        elif button_id == "dashboard-demo":
            self.app.push_screen(DashboardScreen())
        elif button_id == "log-viewer":
            self.app.push_screen(LogViewerScreen())
        elif button_id == "config-editor":
            self.app.push_screen(ConfigEditorScreen())
        elif button_id == "exit":
            self.app.exit()

class DashboardScreen(Screen):
    """System dashboard with status overview and graphs."""
    
    def compose(self) -> ComposeResult:
        yield Header(show_clock=True)
        yield Container(
            Static("System Dashboard", classes="page-title"),
            
            # Status overview
            Grid(
                Label("WireGuard Status:", classes="dashboard-label"),
                Static("● Active", classes="status-active"),
                
                Label("Connected Peers:", classes="dashboard-label"),
                Static("3 / 4", classes="status-info"),
                
                Label("System Load:", classes="dashboard-label"),
                Static("0.45, 0.32, 0.28", classes="status-info"),
                
                Label("Memory Usage:", classes="dashboard-label"),
                # Fix: Create ProgressBar without value parameter
                ProgressBar(id="memory-bar", show_percentage=True),
                
                Label("CPU Usage:", classes="dashboard-label"),
                # Fix: Create ProgressBar without value parameter
                ProgressBar(id="cpu-bar", show_percentage=True),
                
                id="status-grid"
            ),
            
            # Clients table
            Static("Connected Clients", classes="section-title"),
            DataTable(id="peers-table"),
            
            # Actions
            Horizontal(
                Button("Refresh", variant="primary", id="refresh"),
                Button("Back", variant="default", id="back"),
                classes="button-row"
            ),
            
            id="dashboard-container"
        )
        yield Footer()
    
    def on_mount(self) -> None:
        """Setup the dashboard when mounted."""
        # Setup the peers table
        table = self.query_one("#peers-table", DataTable)
        table.add_columns("Name", "IP Address", "Status", "Last Handshake", "Data Transfer")
        
        # Add peer data
        for peer in SAMPLE_PEERS:
            table.add_row(
                peer["name"],
                peer["ip"],
                peer["status"],
                peer["handshake"],
                peer["transfer"]
            )
        
        # Set initial values for progress bars
        try:
            memory_bar = self.query_one("#memory-bar", ProgressBar)
            cpu_bar = self.query_one("#cpu-bar", ProgressBar)
            memory_bar.progress = 35
            cpu_bar.progress = 12
        except Exception as e:
            print(f"Error setting progress bar values: {e}")
        
        # Start auto-refresh
        self.update_dashboard()
    
    @work
    async def update_dashboard(self) -> None:
        """Periodically update the dashboard with new values."""
        try:
            while True:
                await asyncio.sleep(2)  # Update every 2 seconds
                
                # Update CPU and memory bars with random values
                cpu_value = random.randint(5, 50)
                memory_value = random.randint(20, 80)
                
                # Use .progress attribute 
                try:
                    self.query_one("#cpu-bar", ProgressBar).progress = cpu_value
                    self.query_one("#memory-bar", ProgressBar).progress = memory_value
                except Exception as e:
                    print(f"Error updating progress bars: {e}")
                    break
        except asyncio.CancelledError:
            # Worker was cancelled, exit gracefully
            pass
    
    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Handle button press events."""
        if event.button.id == "back":
            self.app.pop_screen()
        elif event.button.id == "refresh":
            self.notify("Dashboard refreshed")
            
            # Fix: Update progress bars using .progress attribute
            import random
            cpu_value = random.randint(5, 50)
            memory_value = random.randint(20, 80)
            
            self.query_one("#cpu-bar", ProgressBar).progress = cpu_value
            self.query_one("#memory-bar", ProgressBar).progress = memory_value

# Fix 3: Proper event handling for LogViewerScreen
class LogViewerScreen(Screen):
    """Log viewer with filtering capabilities."""
    
    def compose(self) -> ComposeResult:
        yield Header(show_clock=True)
        yield Container(
            Static("System Logs", classes="page-title"),
            
            # Log filtering
            Horizontal(
                Label("Filter:", classes="filter-label"),
                Input(placeholder="Search logs...", id="filter-input"),
                
                Label("Level:", classes="filter-label"),
                Select(
                    [(value, value) for value in ["All", "INFO", "WARNING", "ERROR", "DEBUG"]], 
                    id="level-filter",
                    value="All"
                ),
                classes="filter-bar"
            ),
            
            # Logs table
            DataTable(zebra_stripes=True, id="logs-table"),
            
            # Actions
            Horizontal(
                Button("Back", variant="default", id="back"),
                Button("Export Logs", variant="primary", id="export"),
                classes="button-row"
            ),
            
            id="logs-container"
        )
        yield Footer()
    
    def on_mount(self) -> None:
        """Set up the log viewer when mounted."""
        # Setup the logs table
        table = self.query_one("#logs-table", DataTable)
        table.add_columns("Timestamp", "Level", "Message")
        
        # Add log data
        for log in SYSTEM_LOGS:
            table.add_row(
                log["timestamp"],
                log["level"],
                log["message"]
            )
        
        # Load initial data
        self.filter_logs()
    
    # Fix: Use Textual's event handler naming convention
    def on_input_changed(self, event) -> None:
        """Handle input field changes."""
        self.filter_logs()
    
    def on_select_changed(self, event) -> None:
        """Handle select field changes."""
        self.filter_logs()
    
    def filter_logs(self) -> None:
        """Filter logs based on search text and level."""
        try:
            search_text = self.query_one("#filter-input", Input).value.lower()
            level_filter = self.query_one("#level-filter", Select).value
            
            # Clear and rebuild table
            table = self.query_one("#logs-table", DataTable)
            table.clear()
            
            for log in SYSTEM_LOGS:
                level = log["level"]
                message = log["message"] 
                timestamp = log["timestamp"]
                
                # Apply filters
                if (level_filter == "All" or level == level_filter) and \
                   (search_text == "" or search_text in message.lower() or search_text in timestamp.lower()):
                    table.add_row(timestamp, level, message)
        except Exception as e:
            print(f"Error filtering logs: {e}")

class ConfigEditorScreen(Screen):
    """Configuration editor with syntax highlighting."""
    
    BINDINGS = [
        Binding("ctrl+s", "save", "Save")
    ]
    
    def compose(self) -> ComposeResult:
        yield Header(show_clock=True)
        yield Container(
            Static("WireGuard Configuration Editor", classes="page-title"),
            TextArea(id="config-editor", language="ini"),
            Horizontal(
                Button("Back", variant="default", id="back"),
                Button("Save", variant="primary", id="save"),
                classes="button-row"
            ),
            id="editor-container"
        )
        yield Footer()
    
    def on_mount(self) -> None:
        """Initialize the editor with sample configuration."""
        self.query_one("#config-editor", TextArea).text = SAMPLE_CONFIG
    
    def action_save(self) -> None:
        """Save the configuration."""
        self.notify("Configuration saved successfully!")
    
    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Handle button press events."""
        if event.button.id == "back":
            self.app.pop_screen()
        elif event.button.id == "save":
            self.action_save()

# ========== Main Application ==========
# Fix 6: Ensure the main app properly initializes dark mode
class PPWMTextualApp(App):
    """Main Textual application for PPWM."""
    
    TITLE = "PPWM Textual Interface Demo"
    CSS_PATH = "textual.css"
    
    BINDINGS = [
        Binding("q", "quit", "Quit"),
        Binding("d", "toggle_dark", "Toggle Dark Mode"),
        Binding("f1", "show_help", "Help"),
        Binding("1", "menu_1", "Selection Demo"),
        Binding("2", "menu_2", "Dashboard"),
        Binding("3", "menu_3", "Logs"),
        Binding("4", "menu_4", "Config Editor"),
    ]
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Initialize the dark mode flag
        self._dark_mode = False
    
    def on_mount(self) -> None:
        """Called when app is mounted."""
        self.push_screen(WelcomeScreen())
    
    def action_toggle_dark(self) -> None:
        """Toggle dark mode."""
        # Use Textual's built-in dark mode toggling
        self._dark_mode = not self._dark_mode
        
        # Setting .dark property might not exist in all Textual versions
        # Try both approaches
        try:
            self.dark = self._dark_mode
        except AttributeError:
            if self._dark_mode:
                self.add_class("-dark-mode")
            else:
                self.remove_class("-dark-mode")
                
        self.notify(f"Dark mode: {self._dark_mode}")

    def action_show_help(self) -> None:
        """Show the keyboard help screen."""
        self.push_screen(HelpScreen())
    
    def action_menu_1(self) -> None:
        """Open multi-page selection demo."""
        if isinstance(self.screen, WelcomeScreen):
            self.push_screen(ServerRolesScreen())
    
    def action_menu_2(self) -> None:
        """Open dashboard demo."""
        if isinstance(self.screen, WelcomeScreen):
            self.push_screen(DashboardScreen())
    
    def action_menu_3(self) -> None:
        """Open log viewer."""
        if isinstance(self.screen, WelcomeScreen):
            self.push_screen(LogViewerScreen())
    
    def action_menu_4(self) -> None:
        """Open config editor."""
        if isinstance(self.screen, WelcomeScreen):
            self.push_screen(ConfigEditorScreen())

# Fix 7: Add useful debug output at runtime to help diagnose issues
if __name__ == "__main__":
    # Print Textual version for debugging
    try:
        from textual import __version__ as textual_version
        print(f"Running with Textual version: {textual_version}")
    except ImportError:
        print("Couldn't determine Textual version")
    
    try:
        app = PPWMTextualApp()
        app.run()
    except Exception as e:
        print(f"Error running application: {e}")
        import traceback
        traceback.print_exc()
