Final Recommendations for Your Config
PostUp Rules
bash
Copy
Edit
# Allow established and related traffic for performance
PostUp = /usr/sbin/iptables -I FORWARD 1 -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT

# Allow new connections forwarded from eth0 to wg0
PostUp = /usr/sbin/iptables -A FORWARD -i eth0 -o wg0 -m conntrack --ctstate NEW -j ACCEPT

# Allow all forwarded traffic from wg0 back to eth0
PostUp = /usr/sbin/iptables -A FORWARD -i wg0 -o eth0 -j ACCEPT

# NAT traffic from eth0 to the client machine
PostUp = /usr/sbin/iptables -t nat -A PREROUTING -i eth0 -p tcp --dport 80 -j DNAT --to-destination 10.60.1.10
PostUp = /usr/sbin/iptables -t nat -A PREROUTING -i eth0 -p tcp --dport 443 -j DNAT --to-destination 10.60.1.10
PostDown Rules
bash
Copy
Edit
# Remove established and related rule
PostDown = /usr/sbin/iptables -D FORWARD -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT

# Remove new connection forwarding rule
PostDown = /usr/sbin/iptables -D FORWARD -i eth0 -o wg0 -m conntrack --ctstate NEW -j ACCEPT

# Remove wg0 to eth0 forwarding rule
PostDown = /usr/sbin/iptables -D FORWARD -i wg0 -o eth0 -j ACCEPT

# Remove NAT rules
PostDown = /usr/sbin/iptables -t nat -D PREROUTING -i eth0 -p tcp --dport 80 -j DNAT --to-destination 10.60.1.10
PostDown = /usr/sbin/iptables -t nat -D PREROUTING -i eth0 -p tcp --dport 443 -j DNAT --to-desti