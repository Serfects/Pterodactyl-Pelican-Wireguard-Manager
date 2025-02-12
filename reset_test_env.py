import os
import subprocess
from pathlib import Path

def reset_environment():
    print("[WARNING] This will delete and recreate the test environment")
    answer = input("Are you sure you want to continue? (yes/no): ")

    if answer.lower() == "yes":
        print("[INFO] Deactivating current environment if active...")
        os.system("deactivate 2>/dev/null")
        
        test_env = Path("test_environment")
        if test_env.exists():
            print("[INFO] Removing existing test environment...")
            os.system(f"rm -rf {test_env}")
        
        print("[INFO] Running setup script to create fresh environment...")
        print("----------------------------------------")
        setup_result = subprocess.run(["python", "setup_test_env.py"], capture_output=False)
        print("----------------------------------------")
        
        if setup_result.returncode == 0:
            print("[SUCCESS] Test environment reset complete")
            print("[INFO] Use 'source test_environment/activate_env.sh' to activate the new environment")
        else:
            print(f"[ERROR] Setup script failed with status: {setup_result.returncode}")
            print("[INFO] Check the output above for errors")
    else:
        print("[INFO] Reset cancelled")
        input("[INFO] Press Enter to exit...")

if __name__ == "__main__":
    reset_environment()
