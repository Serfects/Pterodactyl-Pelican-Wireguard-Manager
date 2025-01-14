import os, subprocess

def get_wireguard_status(configs):
    statuses = {}
    for config in configs:
        result = subprocess.run(["systemctl", "is-enabled", f"wg-quick@{config}"], capture_output=True, text=True)
        statuses[config] = "enabled" if "enabled" in result.stdout else "disabled"
    return statuses

def set_default_policies(policy, interface=None):
    os.system(f"iptables -P INPUT {policy}")
    os.system(f"iptables -P FORWARD {policy}")
    os.system(f"iptables -P OUTPUT ACCEPT")
    os.system(f"iptables -F -i {interface}" if interface else "iptables -F")
    print(f"Default policies set to {policy} for interface {interface}." if interface else f"Default policies set to {policy}. All rules flushed.")

def reset_iptables():
    mode = input("Do you want to reset:\n (1) Global settings\n (2) WireGuard interface settings?\n(Default: 1): ").strip() or "1"
    if mode == "1":
        policy = "ACCEPT" if input("Set default policies to:\n (1) Open (ACCEPT)\n (2) Restrictive (DROP)?\n(Default: 1): ").strip() or "1" == "1" else "DROP"
        set_default_policies(policy)
    elif mode == "2":
        interface = input("Enter the WireGuard interface name (e.g., wg0, wg1): ").strip()
        if not interface: return print("Invalid interface name. Returning to menu.")
        policy = "ACCEPT" if input("Set default policies to:\n (1) Open (ACCEPT)\n (2) Restrictive (DROP)?\n(Default: 1): ").strip() or "1" == "1" else "DROP"
        set_default_policies(policy, interface)
    else:
        print("Invalid option. Returning to menu.")

def toggle_forwarding(ip_version):
    key = "net.ipv4.ip_forward" if ip_version == "IPv4" else "net.ipv6.conf.all.forwarding"
    current_status = "enabled" if subprocess.check_output(["sysctl", key], text=True).split("=")[1].strip() == "1" else "disabled"
    print(f"Current {ip_version} forwarding status: {current_status}")
    enable = input(f"Enable {ip_version} forwarding?\n (yes/no)\n(Default: {'yes' if current_status == 'disabled' else 'no'}): ").strip().lower() or ("yes" if current_status == "disabled" else "no")
    status = "1" if enable == "yes" else "0"
    os.system(f"sysctl -w {key}={status}")
    if input("Make this change permanent?\n (yes/no)\n(Default: no): ").strip().lower() == "yes":
        with open("/etc/sysctl.conf", "a") as f: f.write(f"{key}={status}\n")
        os.system("sysctl -p")
    print(f"{ip_version} forwarding {'enabled' if enable == 'yes' else 'disabled'}.")

def forwarding_menu():
    while True:
        choice = input("=== Enable/Disable Forwarding ===\n1. IPv4 Forwarding\n2. IPv6 Forwarding\nx. Return to Utilities Menu\nYour choice: ").strip()
        if choice == "1": toggle_forwarding("IPv4")
        elif choice == "2": toggle_forwarding("IPv6")
        elif choice == "x": break
        else: print("Invalid choice. Try again.")

def disable_ipv6():
    def get_status(key):
        try:
            return subprocess.check_output(["sysctl", key], text=True).split("=")[1].strip()
        except subprocess.CalledProcessError:
            return "unknown"

    ipv6_status = {
        "all": "disabled" if get_status("net.ipv6.conf.all.disable_ipv6") == "1" else "enabled",
        "default": "disabled" if get_status("net.ipv6.conf.default.disable_ipv6") == "1" else "enabled",
        "forwarding": "enabled" if get_status("net.ipv6.conf.all.forwarding") == "1" else "disabled"
    }

    print("=== Current IPv6 Status ===")
    print(f"System-wide: {ipv6_status['all']}")
    print(f"Default: {ipv6_status['default']}")
    print(f"Forwarding: {ipv6_status['forwarding']}")

    disable_ipv6 = input("Disable IPv6 across the system?\n (yes/no)\n(Default: no): ").strip().lower() or "no"
    if disable_ipv6 != "yes":
        print("IPv6 disable operation canceled.")
        return

    os.system("sysctl -w net.ipv6.conf.all.disable_ipv6=1")
    os.system("sysctl -w net.ipv6.conf.default.disable_ipv6=1")
    forward_disable = input("Disable IPv6 forwarding as well?\n (yes/no)\n(Default: yes): ").strip().lower() or "yes"
    if forward_disable == "yes":
        os.system("sysctl -w net.ipv6.conf.all.forwarding=0")

    make_permanent = input("Make this change permanent?\n (yes/no)\n(Default: no): ").strip().lower() or "no"
    if make_permanent == "yes":
        with open("/etc/sysctl.conf", "a") as f:
            f.write("net.ipv6.conf.all.disable_ipv6=1\n")
            f.write("net.ipv6.conf.default.disable_ipv6=1\n")
            if forward_disable == "yes":
                f.write("net.ipv6.conf.all.forwarding=0\n")
        os.system("sysctl -p")

    print("IPv6 has been disabled. Reboot required for kernel-level changes.")
    if input("Reboot now?\n (yes/no)\n(Default: no): ").strip().lower() == "yes":
        os.system("reboot")

def validate_wireguard_configs():
    configs = [f for f in os.listdir("/etc/wireguard/") if f.endswith(".conf")]
    if not configs: return print("No WireGuard configuration files found.")
    for cfg in configs:
        result = subprocess.run(["wg", "showconf", os.path.join("/etc/wireguard/", cfg)], capture_output=True)
        print(f"Config: {cfg} - {'Valid' if result.returncode == 0 else 'Invalid'}")

def view_active_connections():
    try: print(subprocess.check_output(["wg"], text=True))
    except subprocess.CalledProcessError as e: print(f"Error retrieving active connections: {e}")

def toggle_interface_autostart():
    configs = [f[:-5] for f in os.listdir("/etc/wireguard/") if f.endswith(".conf")]
    if not configs: return print("No WireGuard configurations found. Ensure /etc/wireguard/ contains valid .conf files.")
    statuses = get_wireguard_status(configs)
    print("=== Available WireGuard Interfaces ===")
    for i, config in enumerate(configs, 1):
        print(f"{i}. {config} (Autostart: {statuses[config]})")
    choice = input("Select an interface to enable/disable autostart\n(Default: 1): ").strip() or "1"
    if not choice.isdigit() or int(choice) < 1 or int(choice) > len(configs):
        return print("Invalid selection. Returning to menu.")
    interface = configs[int(choice) - 1]
    action = input(f"Enable or Disable autostart for {interface}?\n (enable/disable)\n(Default: enable): ").strip().lower() or "enable"
    if action not in ["enable", "disable"]: return print("Invalid action. Returning to menu.")
    os.system(f"systemctl {action} wg-quick@{interface}")
    print(f"Autostart for {interface} has been {action}d.")

def view_services_and_processes_by_port():
    print("=== Services and Processes by Port ===")
    try:
        result = subprocess.check_output(["ss", "-tuln"], text=True).splitlines()
        header = f"{'Proto':<8}{'Local Address':<25}{'Foreign Address':<25}{'State':<15}{'PID/Program Name':<20}"
        print(header)
        print("=" * len(header))
        for line in result[1:]:
            print(line)
    except Exception as e:
        print(f"Error retrieving port information: {e}")

def utilities_menu():
    while True:
        choice = input("=== Utilities Menu ===\n1. Reset iptables Rules\n2. Enable/Disable Forwarding\n3. Disable IPv6\n4. Validate WireGuard Configurations\n5. View Active WireGuard Connections\n6. Toggle Interface Autostart\n7. View Services and Processes by Port\nx. Return to Main Menu\nYour choice: ").strip()
        if choice == "1": reset_iptables()
        elif choice == "2": forwarding_menu()
        elif choice == "3": disable_ipv6()
        elif choice == "4": validate_wireguard_configs()
        elif choice == "5": view_active_connections()
        elif choice == "6": toggle_interface_autostart()
        elif choice == "7": view_services_and_processes_by_port()
        elif choice == "x": break
        else: print("Invalid choice. Try again.")
