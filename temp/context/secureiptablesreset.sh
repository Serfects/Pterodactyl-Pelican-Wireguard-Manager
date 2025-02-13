#!/bin/sh
#
# Secure iptables setup - Resets and secures iptables for IPv4 and IPv6.
#

# Paths to iptables and ip6tables
IPTABLES="/sbin/iptables"
IP6TABLES="/sbin/ip6tables"

#
# Flush existing rules and set default policies
#

echo "Flushing existing iptables rules and setting default policies..."

# Reset IPv4 iptables
$IPTABLES -F
$IPTABLES -X
$IPTABLES -t nat -F
$IPTABLES -t nat -X
$IPTABLES -t mangle -F
$IPTABLES -t mangle -X
$IPTABLES -P INPUT DROP
$IPTABLES -P FORWARD DROP
$IPTABLES -P OUTPUT ACCEPT

# Reset IPv6 ip6tables
$IP6TABLES -F
$IP6TABLES -X
$IP6TABLES -t nat -F
$IP6TABLES -t nat -X
$IP6TABLES -t mangle -F
$IP6TABLES -t mangle -X
$IP6TABLES -P INPUT DROP
$IP6TABLES -P FORWARD DROP
$IP6TABLES -P OUTPUT ACCEPT

echo "Default policies set to DROP for INPUT and FORWARD, ACCEPT for OUTPUT."

#
# Allow loopback (localhost) traffic and drop invalid packets
#

echo "Allowing loopback traffic and dropping invalid packets..."

# IPv4
$IPTABLES -A INPUT -i lo -j ACCEPT
$IPTABLES -A OUTPUT -o lo -j ACCEPT
$IPTABLES -A INPUT -m conntrack --ctstate INVALID -j DROP
$IPTABLES -A INPUT -m conntrack --ctstate RELATED,ESTABLISHED -j ACCEPT

# IPv6
$IP6TABLES -A INPUT -i lo -j ACCEPT
$IP6TABLES -A OUTPUT -o lo -j ACCEPT
$IP6TABLES -A INPUT -m conntrack --ctstate INVALID -j DROP
$IP6TABLES -A INPUT -m conntrack --ctstate RELATED,ESTABLISHED -j ACCEPT

#
# Allow essential services
#

echo "Allowing essential services (e.g., SSH, WireGuard)..."

# SSH (port 22) - adjust if using a non-standard port
$IPTABLES -A INPUT -p tcp --dport 22 -m conntrack --ctstate NEW -j ACCEPT
$IP6TABLES -A INPUT -p tcp --dport 22 -m conntrack --ctstate NEW -j ACCEPT

# WireGuard (UDP, adjust port as needed)
WG_PORT=51820
$IPTABLES -A INPUT -p udp --dport $WG_PORT -m conntrack --ctstate NEW -j ACCEPT
$IP6TABLES -A INPUT -p udp --dport $WG_PORT -m conntrack --ctstate NEW -j ACCEPT

#
# (Optional) Add other services or ports as needed
#
# Example: Allow HTTP/HTTPS traffic
# $IPTABLES -A INPUT -p tcp --dport 80 -m conntrack --ctstate NEW -j ACCEPT
# $IPTABLES -A INPUT -p tcp --dport 443 -m conntrack --ctstate NEW -j ACCEPT

#
# Log and drop all other traffic
#

echo "Logging and dropping all other traffic..."

# IPv4
$IPTABLES -A INPUT -j LOG --log-prefix "IPTables-Dropped: " --log-level 4
$IPTABLES -A INPUT -j DROP

# IPv6
$IP6TABLES -A INPUT -j LOG --log-prefix "IP6Tables-Dropped: " --log-level 4
$IP6TABLES -A INPUT -j DROP

#
# Save the rules for persistence
#

echo "Saving iptables rules for persistence..."
iptables-save > /etc/iptables/rules.v4
ip6tables-save > /etc/iptables/rules.v6
echo "iptables rules saved."

echo "Secure iptables setup complete."
