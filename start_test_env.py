import os
from pathlib import Path

print("[INFO] Starting test environment...")
activate_script = Path("test_environment/activate_env.sh")

if activate_script.exists():
    print("[SUCCESS] Test environment found")
    print("[INFO] To activate, run:")
    print("  source test_environment/activate_env.sh")
    print(f"[INFO] Virtual environment: {os.getenv('VIRTUAL_ENV', 'Not activated')}")
else:
    print("[ERROR] Test environment not found. Run setup_test_env.py first")
