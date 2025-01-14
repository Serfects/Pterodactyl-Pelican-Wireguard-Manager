import os
from datetime import datetime

def get_input(prompt, default=None):
    return input(f"{prompt}\n(Default: {default}): ").strip() or default

def list_configs(directory):
    return [f for f in os.listdir(directory) if f.endswith(".conf")]

def backup_config():
    config_dir = "/etc/wireguard"
    backup_dir = os.path.join(config_dir, "backups")
    os.makedirs(backup_dir, exist_ok=True)

    configs = list_configs(config_dir)
    if not configs:
        print("No configurations found to back up.")
        return

    print("=== Available Configurations to Backup ===")
    for i, config in enumerate(configs, 1):
        print(f"{i}. {config}")

    choice = get_input("Select a configuration to backup")
    if not choice.isdigit() or int(choice) < 1 or int(choice) > len(configs):
        print("Invalid selection.")
        return

    selected_config = configs[int(choice) - 1]
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    backup_name = f"{selected_config}-{timestamp}"
    backup_path = os.path.join(backup_dir, backup_name)

    os.rename(os.path.join(config_dir, selected_config), backup_path)
    print(f"Backup completed: {backup_path}")

def restore_config():
    backup_dir = "/etc/wireguard/backups"
    if not os.path.exists(backup_dir):
        print("No backups found.")
        return

    backups = list_configs(backup_dir)
    if not backups:
        print("No backups found to restore.")
        return

    print("=== Available Backups to Restore ===")
    for i, backup in enumerate(backups, 1):
        print(f"{i}. {backup}")

    choice = get_input("Select a backup to restore")
    if not choice.isdigit() or int(choice) < 1 or int(choice) > len(backups):
        print("Invalid selection.")
        return

    selected_backup = backups[int(choice) - 1]
    config_dir = "/etc/wireguard"
    restore_path = os.path.join(config_dir, selected_backup.split('-')[0] + ".conf")

    if os.path.exists(restore_path):
        overwrite = get_input(f"{restore_path} exists. Overwrite? (yes/no)", "no").lower()
        if overwrite != "yes":
            print("Restore canceled.")
            return

    os.rename(os.path.join(backup_dir, selected_backup), restore_path)
    print(f"Restore completed: {restore_path}")

def backup_restore_menu():
    while True:
        print("=== Backup and Restore Menu ===\n1. Backup Configurations\n2. Restore Configurations\nx. Return to Main Menu")
        choice = get_input("Your choice")
        if choice == "1":
            backup_config()
        elif choice == "2":
            restore_config()
        elif choice == "x":
            break
        else:
            print("Invalid choice. Try again.")
