#!/bin/sh
#
#Regular iptables reset
#
# Configurations
IPTABLES="/sbin/iptables"
IP6TABLES="/sbin/ip6tables"

#
# Reset IPv4 iptables
#

echo "Resetting IPv4 iptables to default..."

# Reset the default policies in the filter table
$IPTABLES -P INPUT ACCEPT
$IPTABLES -P FORWARD ACCEPT
$IPTABLES -P OUTPUT ACCEPT

# Reset the default policies in the nat table
$IPTABLES -t nat -P PREROUTING ACCEPT
$IPTABLES -t nat -P POSTROUTING ACCEPT
$IPTABLES -t nat -P OUTPUT ACCEPT

# Reset the default policies in the mangle table
$IPTABLES -t mangle -P PREROUTING ACCEPT
$IPTABLES -t mangle -P POSTROUTING ACCEPT
$IPTABLES -t mangle -P INPUT ACCEPT
$IPTABLES -t mangle -P OUTPUT ACCEPT
$IPTABLES -t mangle -P FORWARD ACCEPT

# Flush all the rules in the filter, nat, and mangle tables
$IPTABLES -F
$IPTABLES -t nat -F
$IPTABLES -t mangle -F

# Erase all chains that are not default in filter, nat, and mangle tables
$IPTABLES -X
$IPTABLES -t nat -X
$IPTABLES -t mangle -X

echo "IPv4 iptables reset complete."

#
# Reset IPv6 ip6tables
#

echo "Resetting IPv6 ip6tables to default..."

# Reset the default policies in the filter table
$IP6TABLES -P INPUT ACCEPT
$IP6TABLES -P FORWARD ACCEPT
$IP6TABLES -P OUTPUT ACCEPT

# Reset the default policies in the nat table (if supported, some systems don't use NAT with IPv6)
$IP6TABLES -t nat -P PREROUTING ACCEPT
$IP6TABLES -t nat -P POSTROUTING ACCEPT
$IP6TABLES -t nat -P OUTPUT ACCEPT

# Reset the default policies in the mangle table
$IP6TABLES -t mangle -P PREROUTING ACCEPT
$IP6TABLES -t mangle -P POSTROUTING ACCEPT
$IP6TABLES -t mangle -P INPUT ACCEPT
$IP6TABLES -t mangle -P OUTPUT ACCEPT
$IP6TABLES -t mangle -P FORWARD ACCEPT

# Flush all the rules in the filter, nat, and mangle tables
$IP6TABLES -F
$IP6TABLES -t nat -F
$IP6TABLES -t mangle -F

# Erase all chains that are not default in filter, nat, and mangle tables
$IP6TABLES -X
$IP6TABLES -t nat -X
$IP6TABLES -t mangle -X

echo "IPv6 ip6tables reset complete."

#
# Save the cleared rules for persistence
#

echo "Saving current iptables rules for persistence..."
iptables-save > /etc/iptables/rules.v4
ip6tables-save > /etc/iptables/rules.v6
echo "iptables and ip6tables rules saved."

#
# Finish
#

echo "iptables and ip6tables have been reset to default values and saved for persistence."
