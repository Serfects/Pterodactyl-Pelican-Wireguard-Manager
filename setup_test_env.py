import os
import subprocess
import sys
from pathlib import Path

def create_test_env():
    # Print Python version info
    print(f"[INFO] Using Python {sys.version.split()[0]} to create virtual environment")
    
    # Define project root and ensure its a Path object
    project_root = Path("/workspaces/Pterodactyl-Pelican-Wireguard-Manager").resolve()
    
    # Define critical directories
    directories = {
        'test_env': project_root / "test_environment",    # Test environment directory
        'tests': project_root / "tests",                  # Tests directory at project root
        'venv': project_root / "test_environment/venv",   # Virtual environment
        'fake_root': project_root / "test_environment/fake_root",  # Simulated filesystem
    }
    
    # Create all required directories
    for dir_path in directories.values():
        dir_path.mkdir(parents=True, exist_ok=True)
    
    # Create tests/__init__.py if it doesn't exist
    (directories['tests'] / "__init__.py").touch(exist_ok=True)
    
    # Create virtual directories to simulate Linux filesystem
    system_dirs = [
        "etc/wireguard",
        "var/log",
        "usr/local/bin",
        "etc/systemd/system",
        "root/.config"
    ]
    
    for dir_path in system_dirs:
        (directories['fake_root'] / dir_path).mkdir(parents=True, exist_ok=True)
    
    # Create virtual environment
    if not (directories['venv'] / "bin").exists():
        subprocess.run([sys.executable, "-m", "venv", str(directories['venv'])])
    
    # Install requirements
    pip = str(directories['venv'] / "bin" / "pip") if os.name != "nt" else str(directories['venv'] / "Scripts" / "pip")
    
    requirements = [
        "pytest",
        "pytest-mock",
        "pytest-cov",
        "python-dotenv",
        "colorama"
    ]
    
    subprocess.run([pip, "install", "-U", "pip"])
    subprocess.run([pip, "install"] + requirements)
    
    # Create activation script with environment setup
    # Note: PYTHONPATH includes both src/ppwm-dev and project root for test discovery
    activate_script = f"""#!/bin/bash
source {directories['venv']}/bin/activate
export FAKE_ROOT="{directories['fake_root'].absolute()}"
export TESTING=true
export PYTHONPATH=$PYTHONPATH:{project_root / 'src/ppwm-dev'}:{project_root}
"""
    
    activate_path = directories['test_env'] / "activate_env.sh"
    with open(activate_path, "w") as f:
        f.write(activate_script)
    
    # Make activation script executable
    os.chmod(activate_path, 0o755)
    
    print("\nTest environment created successfully!")
    print("\nDirectory structure:")
    print(f"{project_root.name}/")
    print(f"├── tests/                   # Test scripts directory")
    print(f"└── test_environment/        # Test environment")
    print(f"    ├── venv/                # Virtual environment")
    print(f"    ├── fake_root/           # Simulated filesystem")
    print(f"    └── activate_env.sh      # Environment activation script")
    print("\nTo activate:")
    print(f"  source test_environment/activate_env.sh")

if __name__ == "__main__":
    create_test_env()
