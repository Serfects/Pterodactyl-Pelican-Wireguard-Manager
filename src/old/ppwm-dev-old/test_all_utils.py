from utils import get_input, confirm_action, show_progress

def test_utils_features():
    print("\n=== Testing Utils Module Features ===")
    
    # 1. Basic required input
    print("\nTesting required input:")
    name = get_input("Enter your name", required=True)
    
    # 2. Input with default value
    print("\nTesting default value (press Enter to use default):")
    port = get_input("Enter port number", default="51820")
    
    # 3. Simple choices
    print("\nTesting simple choices:")
    color = get_input("Select a color", choices=["red", "blue", "green"])
    
    # 4. Numbered choices with descriptions
    print("\nTesting numbered choices with descriptions:")
    role = get_input("Select your role", choices=[
        ("1", "Administrator - Full access"),
        ("2", "User - Limited access"),
        ("3", "Guest - View only")
    ])
    
    # Test choices with explanations
    print("\nTesting choices with explanations:")
    server_type = get_input("Select server configuration", choices=[
        ("1", "Basic Server", "Recommended for testing and development"),
        ("2", "Standard Server", "Good for most use cases"),
        ("3", "Advanced", "Custom configuration required"),
        ("4", "Exit")  # No explanation needed for this option
    ])
    
    # 5. Input with validation
    print("\nTesting input validation (must be 1-100):")
    def number_validator(value):
        try:
            num = int(value)
            return 1 <= num <= 100
        except ValueError:
            return False
            
    score = get_input(
        "Enter a number between 1-100",
        validator=number_validator
    )
    
    # 6. Yes/No confirmation
    print("\nTesting yes/no confirmation (try: yes, y, no, n):")
    if confirm_action("Would you like to see the progress indicator?"):
        # 7. Progress indicator
        print("\nTesting progress indicators:")
        show_progress("Short task", 1)
        show_progress("Medium task", 2)
        show_progress("Long task", 3)
    
    # Show all collected inputs
    if confirm_action("Would you like to see all your inputs?"):
        print("\n=== Input Summary ===")
        print(f"Name: {name}")
        print(f"Port: {port}")
        print(f"Color: {color}")
        print(f"Role: {role}")
        print(f"Server Type: {server_type}")
        print(f"Score: {score}")

if __name__ == "__main__":
    test_utils_features()
