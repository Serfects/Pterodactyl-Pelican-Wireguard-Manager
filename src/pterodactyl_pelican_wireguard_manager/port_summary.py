import os
from datetime import datetime

def list_configs(config_dir="/etc/wireguard"):
    return [f for f in os.listdir(config_dir) if f.endswith(".conf")]

def summarize_ports():
    config_dir = "/etc/wireguard/"
    configs = list_configs(config_dir)

    if not configs:
        print("No WireGuard configurations found.")
        return

    print("=== Managed Ports Summary ===")
    summary = []

    for config_file in configs:
        with open(os.path.join(config_dir, config_file), "r") as f:
            config_data = f.readlines()

        interface_name = config_file[:-5]  # Strip .conf
        summary.append(f"Interface: {interface_name}\n")
        current_category = None

        for line in config_data:
            line = line.strip()
            if line.startswith("[Category:"):
                current_category = line.split(":")[1].strip(" ]")
                summary.append(f"{current_category}:\n")
            elif line.startswith("Subsection:"):
                subsection_name = line.split(":")[1].strip()
                summary.append(f"  - {subsection_name}:\n")
            elif line.startswith("# Port:"):
                port_info = line.split(":", 1)[1].strip()
                summary.append(f"    {port_info}\n")
            elif line.startswith("# Forward:"):
                forward_info = line.split(":", 1)[1].strip()
                summary.append(f"      -> {forward_info}\n")

    for entry in summary:
        print(entry)

    export = input("Export summary to file? (yes/no)\n(Default: no): ").strip().lower() or "no"
    if export == "yes":
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        export_path = f"/etc/wireguard/managed_ports_summary_{timestamp}.txt"
        with open(export_path, "w") as summary_file:
            summary_file.write("\n".join(summary))
        print(f"Summary exported to {export_path}.")

def port_summary_menu():
    while True:
        choice = input("=== Port Summary Menu ===\n1. View Managed Ports Summary\n2. Export Managed Ports Summary\nx. Return to Main Menu\nYour choice: ").strip()
        if choice == "1":
            summarize_ports()
        elif choice == "2":
            summarize_ports()
        elif choice == "x":
            break
        else:
            print("Invalid choice. Try again.")
