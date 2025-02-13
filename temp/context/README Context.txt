here is the readme:

# WireGuard Management Script

## Overview

The WireGuard Management Script is an advanced yet user-friendly tool tailored to simplify the deployment, configuration, and maintenance of WireGuard VPN solutions. This script is built with versatility and scalability in mind, providing powerful features for managing server and client configurations, port forwarding, firewall rules, and more. It is designed for homelab enthusiasts, developers, and small businesses that require a robust VPN infrastructure.

### Primary Objectives

1. **Seamless VPN Deployment**:

   - Enable users to set up a WireGuard VPN quickly without requiring extensive networking expertise.

2. **Enhanced Security and Privacy**:

   - Ensure external users interact only with the WireGuard VPS's public IP while the client machine remains concealed.
   - Maintain full visibility of external user details on client-hosted services.

3. **Dynamic Port Management**:

   - Automate the addition, modification, and removal of port-forwarding rules for services and games hosted by the WireGuard client.
   - Include detailed templates to organize ports into categories and subsections for easy management.

4. **Integrated Firewall Automation**:

   - Dynamically update `iptables` rules to reflect configuration changes, ensuring smooth traffic routing and security.

5. **User-Centric Design**:

   - Provide interactive menus and intuitive prompts, enabling even novice users to configure advanced networking setups.

## Key Features and Detailed Capabilities

### 1. **Configuration Management**

- **Generate New Configurations**:

  - Automatically create server and client configurations with customizable options, such as MTU, DNS settings, and listening ports.
  - Automatically assign subnet and IP addresses to avoid conflicts.

- **Interactive Modification**:

  - Modify existing configurations dynamically, including adding or editing ports and forwarding rules.

- **Backup and Restore**:

  - Save backups of configurations with timestamps and restore them easily if needed.

### 2. **Port Management**

- **Purpose**:

  - Simplify port-forwarding rules for accessing client-hosted services via the WireGuard VPS's public IP.

- **Dynamic Template Creation**:

  - Organize ports into two main categories:
    - **Games**: For gaming servers.
    - **Services**: For other hosted applications.
  - Each category can have multiple subsections representing specific services or games.

- **Advanced Rules**:

  - Automatically generate `iptables` rules to forward traffic to the WireGuard client while ensuring external users see only the WireGuard VPS's public IP.
  - Support TCP, UDP, or both protocols, with separate rules for each if required.

- **Flexible Input Options**:

  - Add individual ports, ranges, or combinations (e.g., `667, 669, 671-673, 675`).
  - Allow users to attach optional comments to each port for clarity.

### 3. **Firewall and Routing Automation**

- **Rule Management**:

  - Automatically apply or remove `iptables` rules when ports are added, modified, or deleted.

- **IPv4 and IPv6 Handling**:

  - Fully supports IPv4 for routing and NAT.
  - Includes options to disable IPv6 entirely for added security.

### 4. **Validation and Troubleshooting**

- **Configuration Validation**:

  - Validate `.conf` files to ensure they are error-free before deployment.

- **Active Connection Monitoring**:

  - View active WireGuard connections for real-time insights.

### 5. **Client Support Tools**

- **Client Configuration Generator**:

  - Automatically generate client configuration files that align with server settings.

- **Post-Setup Automation**:

  - Provide scripts to simplify configuration setup on client machines.

### 6. **Port Summary and Export**

- **Managed Port Overview**:

  - Summarize all tracked ports, categorized by use case, for easy review.

- **Export Options**:

  - Export port summaries to a file for documentation or external firewall updates.

## Use Case Example

Imagine hosting a gaming server behind a WireGuard VPN:

1. The script enables port forwarding rules on the WireGuard VPS to allow external players to access the server.
2. Traffic is tunneled securely to the client machine hosting the game.
3. Players interact with the WireGuard VPS’s public IP, ensuring the client machine’s IP remains private.
4. External players’ real IPs are visible to the gaming server for proper handling.

This process applies similarly to other services, providing flexibility and security across all use cases.

## Directory Structure

```
/etc/wireguard/
|-- <config_name>-YYYYMMDD-HHMMSS/
    |-- <config_name>_server.conf
    |-- <config_name>_client.conf
    |-- logs/
        |-- server.log
        |-- client.log
|-- backups/
    |-- <config_name>-YYYYMMDD-HHMMSS
        |-- backup_server.conf
        |-- backup_client.conf
|-- managed_ports/
    |-- port_summary.txt
```

- **Configurations**:

  - Stored in timestamped directories for easy versioning.
  - Each configuration has dedicated logs for server and client events.

- **Backups**:

  - Automatically created before significant changes or deletions, stored in a dedicated directory with clear file naming.

- **Managed Ports**:

  - All tracked ports are summarized and saved for external use or documentation.

## ## Order of Operations Tree

```plaintext
Main Menu
|
|-- Generate New Configuration
|   |-- Create Server Config
|       |-- Specify Listening Port
|       |-- Include MTU Settings
|       |-- Enable/Disable IPv4 Forwarding
|   |-- Create Client Config
|       |-- Assign Client IP
|       |-- Specify DNS Settings
|       |-- Generate Client Key Pair
|
|-- Modify Existing Configuration
|   |-- Select Configuration
|       |-- Add Port
|           |-- Specify Protocol (TCP/UDP/Both)
|           |-- Input Port or Range
|           |-- Add Optional Comments
|       |-- Edit Port
|           |-- Change Protocol
|           |-- Modify Port Number
|       |-- Delete Port
|           |-- Select Port to Remove
|
|-- Backup and Restore
|   |-- Backup Configuration
|       |-- List Available Configurations
|       |-- Create Timestamped Backup
|   |-- Restore Configuration
|       |-- List Available Backups
|       |-- Validate and Overwrite Configuration
|
|-- Port Summary
|   |-- View Managed Ports
|       |-- Display Categories (Games/Services)
|       |-- List Subsections and Ports
|   |-- Export Ports Summary
|       |-- Generate Summary File
|
|-- Utilities
    |-- Validate Configurations
    |   |-- Check Config Syntax
    |   |-- Detect Errors
    |-- Monitor Connections
    |   |-- View Active Peers
    |   |-- Display Real-Time Data Transfer
    |-- Toggle Autostart
        |-- Enable/Disable Interface Autostart
```

## Example WireGuard Configuration

### Server Configuration

```ini
[Interface]
# The IP address of the server within the VPN subnet.
Address = 10.60.1.1/24

# Private key for the server. This is used to authenticate the server within the WireGuard network.
PrivateKey = SERVER_PRIVATE_KEY

# The port WireGuard will listen on for incoming connections.
ListenPort = 51820

# Firewall rules automatically added by the script.
# These rules handle NAT and routing traffic for the VPN.
PostUp = iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE
PostUp = iptables -A FORWARD -i wg0 -j ACCEPT
PostUp = iptables -A FORWARD -o wg0 -j ACCEPT
PostDown = iptables -t nat -D POSTROUTING -o eth0 -j MASQUERADE
PostDown = iptables -D FORWARD -i wg0 -j ACCEPT
PostDown = iptables -D FORWARD -o wg0 -j ACCEPT

# Categories added by the script for port management.
[Category: Games]
Subsection: GameServer1
# Port: 27015 (UDP) - Used for GameServer1 traffic
PostUp = iptables -t nat -A PREROUTING -p udp --dport 27015 -j DNAT --to-destination 10.60.1.2:27015
PostDown = iptables -t nat -D PREROUTING -p udp --dport 27015 -j DNAT --to-destination 10.60.1.2:27015

[Category: Services]
Subsection: WebServer
# Port: 80 (TCP) - Web traffic
PostUp = iptables -t nat -A PREROUTING -p tcp --dport 80 -j DNAT --to-destination 10.60.1.2:80
PostDown = iptables -t nat -D PREROUTING -p tcp --dport 80 -j DNAT --to-destination 10.60.1.2:80

[Peer]
# Public key of the client. This key identifies the client to the server.
PublicKey = CLIENT_PUBLIC_KEY

# Allowed IPs for the client within the VPN subnet.
AllowedIPs = 10.60.1.2/32

# Persistent keepalive to maintain a connection through NAT.
PersistentKeepalive = 25
```

### Client Configuration

```ini
[Interface]
# The IP address of the client within the VPN subnet.
Address = 10.60.1.2/24

# Private key for the client. This key authenticates the client to the server.
PrivateKey = CLIENT_PRIVATE_KEY

# Optional DNS server for the client.
DNS = 1.1.1.1

# Optional firewall rules to enhance security or route traffic as required.
# These rules can be included or skipped during client configuration generation.
PostUp = iptables -A OUTPUT -o wg0 -j ACCEPT
PostDown = iptables -D OUTPUT -o wg0 -j ACCEPT

[Peer]
# Public key of the server. This key identifies the server to the client.
PublicKey = SERVER_PUBLIC_KEY

# Endpoint of the server (VPS public IP and port).
# This is where the client sends its traffic.
Endpoint = SERVER_PUBLIC_IP:51820

# Allowed IPs for routing all traffic through the VPN.
# 0.0.0.0/0 ensures all traffic is tunneled through the VPN.
AllowedIPs = 0.0.0.0/0

# Persistent keepalive to maintain a connection through NAT.
PersistentKeepalive = 25
```