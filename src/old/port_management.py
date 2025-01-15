import os

def get_input(prompt, default=None):
    return input(f"{prompt}\n(Default: {default}): ").strip() or default

def list_configs(config_dir="/etc/wireguard"):
    return [f for f in os.listdir(config_dir) if f.endswith(".conf")]

def select_config():
    configs = list_configs()
    if not configs:
        print("No WireGuard configurations found in /etc/wireguard.")
        return None
    for i, config in enumerate(configs, 1): print(f"{i}. {config}")
    choice = get_input("Select a configuration by number")
    return configs[int(choice) - 1] if choice.isdigit() and 1 <= int(choice) <= len(configs) else None

def initialize_template(config_path):
    with open(config_path, "a") as config:
        config.write("\n[Category: Games]\n[Category: Services]\n[Category: Miscellaneous]\n")
    print("Template initialized.")

def list_categories(config_path):
    with open(config_path) as config: lines = config.readlines()
    games, services, miscellaneous, current = [], [], [], None
    for line in lines:
        if "[Category: Games]" in line: current = games
        elif "[Category: Services]" in line: current = services
        elif "[Category: Miscellaneous]" in line: current = miscellaneous
        elif line.startswith("Subsection:") and current is not None:
            current.append(line.split(":", 1)[1].strip())
    return games, services, miscellaneous

def add_subsection(config_path, category):
    new_name = get_input(f"Enter name for new subsection in {category}")
    games, services, miscellaneous = list_categories(config_path)
    if new_name in (games if category == "Games" else services if category == "Services" else miscellaneous):
        print(f"Subsection '{new_name}' already exists in {category}.")
    else:
        with open(config_path, "a") as config: config.write(f"Subsection: {new_name}\n")
        print(f"Added subsection '{new_name}' to {category}.")

def display_ports(config_path, category, subsection):
    with open(config_path) as config: lines = config.readlines()
    ports, found = [], False
    for line in lines:
        if line.strip() == f"Subsection: {subsection}": found = True
        elif found and line.startswith("Port:"): ports.append(line.strip())
        elif found and not line.startswith("Port:"): break
    for i, port in enumerate(ports, 1): print(f"{i}. {port}")
    return ports

def generate_postup_postdown(config_path, port, protocol, action, forward_port=None):
    with open(config_path, "a" if action == "add" else "r+") as config:
        config.seek(0); lines = config.readlines(); config.truncate(0)
        for line in lines:
            if f"Port: {port}/{protocol}" in line and action == "delete": continue
            config.write(line)
        if action == "add":
            target_port = forward_port or port
            if protocol in ["tcp", "udp"]:
                config.write(f"PostUp = iptables -t nat -A PREROUTING -p {protocol} --dport {port} -j DNAT --to-destination <client_ip>:{target_port}\n")
                config.write(f"PostUp = iptables -A FORWARD -p {protocol} --dport {port} -j ACCEPT\n")
                config.write(f"PostDown = iptables -t nat -D PREROUTING -p {protocol} --dport {port} -j DNAT --to-destination <client_ip>:{target_port}\n")
                config.write(f"PostDown = iptables -D FORWARD -p {protocol} --dport {port} -j ACCEPT\n")
            elif protocol == "both":
                for proto in ["tcp", "udp"]:
                    config.write(f"PostUp = iptables -t nat -A PREROUTING -p {proto} --dport {port} -j DNAT --to-destination <client_ip>:{target_port}\n")
                    config.write(f"PostUp = iptables -A FORWARD -p {proto} --dport {port} -j ACCEPT\n")
                    config.write(f"PostDown = iptables -t nat -D PREROUTING -p {proto} --dport {port} -j DNAT --to-destination <client_ip>:{target_port}\n")
                    config.write(f"PostDown = iptables -D FORWARD -p {proto} --dport {port} -j ACCEPT\n")

def backup_prompt(config_path):
    if get_input("Would you like to create a backup before proceeding? (yes/no)", "yes").lower() == "yes":
        timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        backup_name = f"{os.path.basename(config_path)}-{timestamp}"
        backup_dir = os.path.join(os.path.dirname(config_path), "backups")
        os.makedirs(backup_dir, exist_ok=True)
        backup_path = os.path.join(backup_dir, backup_name)
        os.rename(config_path, backup_path)
        print(f"Backup created at {backup_path}.")

def modify_ports(config_path, category, subsection, action):
    backup_prompt(config_path)  # Backup before modifications
    ports = display_ports(config_path, category, subsection)
    if not ports and action != "add": return
    if action == "add":
        protocol = get_input("Enter protocol\n (tcp/udp/both)", "tcp").lower()
        if protocol not in ["tcp", "udp", "both"]: return
        port_input = get_input("Enter ports (e.g., 667, 669-671)")
        forward_to_different_port = get_input("Forward these ports to different ports on the client?\n (yes/no)", "no").lower()
        if forward_to_different_port == "yes" and "-" in port_input:
            print("Forwarding ranges of ports to different client ports is not supported. Please add individual ports instead.")
            return
        forward_mapping = {}
        if forward_to_different_port == "yes":
            for port in port_input.split(","):
                target_port = get_input(f"Enter the client port to forward {port.strip()} to")
                if not target_port.isdigit() or int(target_port) < 1 or int(target_port) > 65535:
                    print("Invalid port number. Returning to menu.")
                    return
                forward_mapping[port.strip()] = target_port
        for part in port_input.split(","):
            port = part.strip()
            if forward_to_different_port == "yes":
                generate_postup_postdown(config_path, port, protocol, action, forward_mapping.get(port))
            else:
                generate_postup_postdown(config_path, port, protocol, action)
        print(f"Added ports to {subsection} in {category}.")
        backup_prompt(config_path)  # Backup after adding ports
    elif action in ["edit", "delete"]:
        choice = get_input(f"Select a port to {action} by number")
        if not choice.isdigit() or int(choice) < 1 or int(choice) > len(ports): return
        selected_port = ports[int(choice) - 1]
        port, protocol = selected_port.split()[1].split("/")
        if action == "edit":
            new_protocol = get_input("Enter new protocol\n (tcp/udp/both)", protocol).lower()
            new_port = get_input("Enter new port", port)
            forward_to_different_port = get_input("Forward to a different client port?\n (yes/no)", "no").lower()
            forward_port = None
            if forward_to_different_port == "yes":
                forward_port = get_input(f"Enter the client port to forward {new_port} to")
            generate_postup_postdown(config_path, port, protocol, "delete")
            generate_postup_postdown(config_path, new_port, new_protocol, "add", forward_port)
            backup_prompt(config_path)  # Backup after modifying ports
        elif action == "delete":
            generate_postup_postdown(config_path, port, protocol, "delete")
            backup_prompt(config_path)  # Backup before deleting ports
        print(f"{action.capitalize()}d port for {subsection} in {category}.")

def delete_subsection(config_path, category, subsection):
    backup_prompt(config_path)  # Backup before deleting subsection
    with open(config_path) as config: lines = config.readlines()
    with open(config_path, "w") as config:
        skip = False
        for line in lines:
            if line.strip() == f"Subsection: {subsection}": skip = True
            elif skip and not line.startswith("Port: "): skip = False
            elif not skip: config.write(line)
    print(f"Deleted subsection {subsection} from {category}.")
