#!/bin/bash

# Secure iptables reset script

IPTABLES="/sbin/iptables"
IP6TABLES="/sbin/ip6tables"

echo "Resetting all iptables rules and applying secure defaults..."

# Flush all rules for IPv4
$IPTABLES -F
$IPTABLES -t nat -F
$IPTABLES -t mangle -F
$IPTABLES -X

# Flush all rules for IPv6
$IP6TABLES -F
$IP6TABLES -t nat -F
$IP6TABLES -t mangle -F
$IP6TABLES -X

# Set default policies to DROP for IPv4
$IPTABLES -P INPUT DROP
$IPTABLES -P FORWARD DROP
$IPTABLES -P OUTPUT ACCEPT

# Set default policies to DROP for IPv6
$IP6TABLES -P INPUT DROP
$IP6TABLES -P FORWARD DROP
$IP6TABLES -P OUTPUT ACCEPT

# Allow loopback traffic (IPv4 and IPv6)
$IPTABLES -A INPUT -i lo -j ACCEPT
$IPTABLES -A OUTPUT -o lo -j ACCEPT

$IP6TABLES -A INPUT -i lo -j ACCEPT
$IP6TABLES -A OUTPUT -o lo -j ACCEPT

# Allow established and related inbound traffic (IPv4 and IPv6)
$IPTABLES -A INPUT -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT
$IP6TABLES -A INPUT -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT

# Allow SSH inbound traffic (adjust port if necessary)
$IPTABLES -A INPUT -p tcp --dport 22 -j ACCEPT
$IP6TABLES -A INPUT -p tcp --dport 22 -j ACCEPT

# Allow WireGuard traffic on port 51820 (adjust port if necessary)
$IPTABLES -A INPUT -p udp --dport 51820 -j ACCEPT
$IP6TABLES -A INPUT -p udp --dport 51820 -j ACCEPT

# Allow DNS requests (outbound for IPv4 and IPv6)
$IPTABLES -A OUTPUT -p udp --dport 53 -j ACCEPT
$IPTABLES -A OUTPUT -p tcp --dport 53 -j ACCEPT

$IP6TABLES -A OUTPUT -p udp --dport 53 -j ACCEPT
$IP6TABLES -A OUTPUT -p tcp --dport 53 -j ACCEPT

# Allow HTTP and HTTPS traffic (outbound for IPv4 and IPv6)
$IPTABLES -A OUTPUT -p tcp --dport 80 -j ACCEPT
$IPTABLES -A OUTPUT -p tcp --dport 443 -j ACCEPT

$IP6TABLES -A OUTPUT -p tcp --dport 80 -j ACCEPT
$IP6TABLES -A OUTPUT -p tcp --dport 443 -j ACCEPT

# Allow NTP traffic for time synchronization (outbound for IPv4 and IPv6)
$IPTABLES -A OUTPUT -p udp --dport 123 -j ACCEPT
$IP6TABLES -A OUTPUT -p udp --dport 123 -j ACCEPT

# Save the rules (iptables-persistent required)
if [ -x /sbin/iptables-save ] && [ -x /sbin/ip6tables-save ]; then
    echo "Saving iptables rules..."
    /sbin/iptables-save > /etc/iptables/rules.v4
    /sbin/ip6tables-save > /etc/iptables/rules.v6
    echo "Rules saved successfully!"
else
    echo "iptables-persistent not installed. Rules will not persist on reboot."
fi

echo "Secure iptables rules have been applied successfully."
