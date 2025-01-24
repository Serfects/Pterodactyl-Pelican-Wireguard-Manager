import os, subprocess
from datetime import datetime

def get_input(prompt, default=None):
    return input(f"{prompt}\n(Default: {default}): ").strip() or default

def generate_keys():
    priv = subprocess.check_output(['wg', 'genkey']).decode().strip()
    return priv, subprocess.check_output(['wg', 'pubkey'], input=priv.encode()).decode().strip()

def get_network_info():
    try:
        iface = [line.split()[4] for line in subprocess.check_output(['ip', 'route']).decode().splitlines() if 'default' in line][0]
    except:
        iface = None
    try:
        public_ip = subprocess.check_output(['curl', '-s', 'https://api.ipify.org']).decode().strip()
    except:
        public_ip = None
    return iface, public_ip

def generate_config():
    cfg_name = get_input("Enter config name", "wg0")
    include_mtu = get_input("Include MTU?\n (yes/no)", "no").lower() == "yes"
    mtu = get_input("Enter MTU", "1420") if include_mtu else None
    include_dns = get_input("Include DNS?\n (yes/no)", "yes").lower() == "yes"
    dns_ip = get_input("Enter DNS IP", "1.1.1.1") if include_dns else None
    port = get_input("Enter listening port", "51820")
    iface, pub_ip = get_network_info()

    iface = get_input(f"Enter interface\n({'Autodetected: ' + iface if iface else 'Unable to detect, enter manually'})", iface or "")
    pub_ip = get_input(f"Enter public IP\n({'Autodetected: ' + pub_ip if pub_ip else 'Unable to detect, enter manually'})", pub_ip or "")
    keepalive = get_input("Persistent keepalive", "25")

    if get_input("Generate keys?\n (yes/no)", "yes").lower() == "yes":
        srv_priv, srv_pub = generate_keys()
        cli_priv, cli_pub = generate_keys()
    else:
        srv_priv = get_input("Enter server private key")
        srv_pub = get_input("Enter server public key")
        cli_priv = get_input("Enter client private key")
        cli_pub = get_input("Enter client public key")

    subnet = int(get_input("Enter subnet to use\n (10.60.x.1, where x cannot be 0)", "2"))
    client_ip = get_input(f"Enter client IP\n (10.60.{subnet}.x, where x cannot be 0 or 1)", f"10.60.{subnet}.2")
    wg_ip = f"10.60.{subnet}.1/24"
    subnet_cidr = f"10.60.{subnet}.0/24"

    include_allow_deny_server = get_input("Add automatic allow/deny rules for the server?\n (yes/no)", "yes").lower() == "yes"
    include_allow_deny_client = get_input("Add automatic allow/deny rules for the client?\n (yes/no)", "yes").lower() == "yes"

    server_allow_deny = (f"PostUp = iptables -P INPUT ACCEPT\n"
                         f"PostUp = iptables -P FORWARD ACCEPT\n"
                         f"PostDown = iptables -P INPUT DROP\n"
                         f"PostDown = iptables -P FORWARD DROP\n") if include_allow_deny_server else ""

    client_allow_deny = (f"PostUp = iptables -P INPUT ACCEPT\n"
                         f"PostUp = iptables -P FORWARD ACCEPT\n"
                         f"PostDown = iptables -P INPUT DROP\n"
                         f"PostDown = iptables -P FORWARD DROP\n") if include_allow_deny_client else ""

    postup = (f"PostUp = iptables -t nat -A POSTROUTING -s {subnet_cidr} -o {iface} -j SNAT --to-source {pub_ip}\n"
              f"PostUp = iptables -A FORWARD -i {iface} -o {cfg_name} -j ACCEPT\n"
              f"PostUp = iptables -A FORWARD -i {cfg_name} -j ACCEPT\n"
              f"{server_allow_deny}"
              f"PostDown = iptables -t nat -D POSTROUTING -s {subnet_cidr} -o {iface} -j SNAT --to-source {pub_ip}\n"
              f"PostDown = iptables -D FORWARD -i {iface} -o {cfg_name} -j ACCEPT\n"
              f"PostDown = iptables -D FORWARD -i {cfg_name} -j ACCEPT\n")

postup = (f"PostUp = iptables -t nat -A POSTROUTING -s {subnet_cidr} -o {iface} -j SNAT --to-source {pub_ip}\n"
          f"PostUp = iptables -I FORWARD 1 -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT\n"
          f"PostUp = iptables -A FORWARD -i {iface} -o {cfg_name} -j ACCEPT\n"
          f"PostUp = iptables -A FORWARD -i {cfg_name} -j ACCEPT\n"
          f"{server_allow_deny}"
          f"PostDown = iptables -t nat -D POSTROUTING -s {subnet_cidr} -o {iface} -j SNAT --to-source {pub_ip}\n"
          f"PostDown = iptables -D FORWARD 1 -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT\n"
          f"PostDown = iptables -D FORWARD -i {iface} -o {cfg_name} -j ACCEPT\n"
          f"PostDown = iptables -D FORWARD -i {cfg_name} -j ACCEPT\n")

    out_dir = f"/etc/wireguard/{cfg_name}-{datetime.now().strftime('%Y%m%d-%H%M%S')}"
    os.makedirs(out_dir, exist_ok=True)

    srv_cfg = f"""[Interface]
Address = {wg_ip}
{f'MTU = {mtu}\n' if include_mtu else ''}ListenPort = {port}
PrivateKey = {srv_priv}
{postup}

# Categories and Subsections
[Category: Games]
[Category: Services]
[Category: Miscellaneous]

[Peer]
PublicKey = {cli_pub}
AllowedIPs = {client_ip.split('/')[0]}/32
PersistentKeepalive = {keepalive}
"""

    cli_cfg = f"""[Interface]
Address = {client_ip}/24
PrivateKey = {cli_priv}
{f'DNS = {dns_ip}\n' if include_dns else ''}
{f'MTU = {mtu}\n' if include_mtu else ''}
{client_allow_deny}[Peer]
PublicKey = {srv_pub}
Endpoint = {pub_ip}:{port}
AllowedIPs = 0.0.0.0/0
PersistentKeepalive = {keepalive}
"""

    for path, content in [(f"{out_dir}/{cfg_name}_server.conf", srv_cfg), (f"{out_dir}/{cfg_name}_client.conf", cli_cfg)]:
        with open(path, "w") as f: f.write(content)

    print(f"Config saved to {out_dir}.")
    choice = get_input("Press 'r' to return to main menu\n or 'p' to enter Port Management.")
    if choice == 'p':
        from port_management import manage_ports
        manage_ports()
