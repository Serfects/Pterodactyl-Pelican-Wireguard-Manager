from utils import get_input, confirm_action, show_progress

def test_utils_features():
    print("\n=== Testing Utils Module Features ===")
    
    name = get_input("Enter your name", required=True)
    
    port = get_input("Enter port number", default="51820")
    
    color = get_input("Select a color", choices=["red", "blue", "green"])
    
    role = get_input("Select your role", choices=[
        ("1", "Administrator - Full access"),
        ("2", "User - Limited access"),
        ("3", "Guest - View only")
    ])
    
    server_type = get_input("Select server configuration", choices=[
        ("1", "Basic Server", "Recommended for testing and development"),
        ("2", "Standard Server", "Good for most use cases"),
        ("3", "Advanced", "Custom configuration required"),
        ("4", "Exit")
    ])
    
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
    
    if confirm_action("Would you like to see the progress indicator?"):
        show_progress("Short task", 1)
        show_progress("Medium task", 2)
        show_progress("Long task", 3)
    
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
