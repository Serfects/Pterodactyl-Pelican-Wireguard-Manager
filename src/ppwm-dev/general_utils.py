from colorama import Fore, Style
import time
import sys

class InputValidationError(Exception):
    pass

class MenuExecutionError(Exception):
    pass

def get_input(prompt, default=None, validator=None, choices=None, required=False):
    print(f"\n{Fore.YELLOW}{prompt}{Style.RESET_ALL}")
    
    if choices:
        print("\nAvailable options:")
        for choice in choices:
            if isinstance(choice, tuple):
                if len(choice) == 3:
                    number, description, explanation = choice
                    print(f"  {Style.DIM}{Fore.WHITE}•{Style.RESET_ALL} {Fore.LIGHTCYAN_EX}({number}){Style.RESET_ALL} {Fore.WHITE}{description}")
                    print(f"      {Style.DIM}{explanation}{Style.RESET_ALL}")
                else:
                    number, description = choice
                    print(f"  {Style.DIM}{Fore.WHITE}•{Style.RESET_ALL} {Fore.LIGHTCYAN_EX}({number}){Style.RESET_ALL} {Fore.WHITE}{description}")
            else:
                print(f"  {Style.DIM}{Fore.WHITE}•{Style.RESET_ALL} {Fore.WHITE}{choice}")
        print()

    if default is not None:
        print(f"{Fore.WHITE}(Default: {Fore.LIGHTBLUE_EX}{default}{Fore.WHITE}){Style.RESET_ALL}")
        prompt_text = f"{Fore.WHITE}Your Entry: {Fore.LIGHTCYAN_EX}▸ {Style.RESET_ALL}"
    else:
        prompt_text = f"{Fore.WHITE}Your Entry: {Fore.LIGHTCYAN_EX}▸ {Style.RESET_ALL}"

    while True:
        user_input = input(prompt_text).strip()
        print(f"\033[F\033[K{prompt_text}{Style.BRIGHT}{Fore.WHITE}{user_input}{Style.RESET_ALL}")

        if not user_input:
            if default is not None:
                print(f"{Fore.LIGHTGREEN_EX}✓ {Fore.LIGHTBLUE_EX}Default option {Style.BRIGHT}{Fore.WHITE}{default}{Style.RESET_ALL} {Fore.LIGHTBLUE_EX}used{Style.RESET_ALL}")
                return default
            if required:
                print(f"{Fore.YELLOW}⚠ {Fore.LIGHTRED_EX}This field is required.{Style.RESET_ALL}")
                continue

        if choices and user_input not in [c[0] if isinstance(c, tuple) else c for c in choices]:
            print(f"{Fore.YELLOW}⚠ {Fore.LIGHTRED_EX}Invalid choice. Please select one of the options above.{Style.RESET_ALL}")
            continue

        if validator and not validator(user_input):
            print(f"{Fore.YELLOW}⚠ {Fore.LIGHTRED_EX}Invalid input. Please try again.{Style.RESET_ALL}")
            continue

        return user_input

def confirm_action(prompt):
    def yes_no_validator(value):
        return value.lower() in ['yes', 'no', 'y', 'n']
    
    try:
        response = get_input(f"{prompt} {Fore.LIGHTCYAN_EX}(yes/no){Style.RESET_ALL}", 
                           validator=yes_no_validator)
        return response.lower() in ['yes', 'y']
    except KeyboardInterrupt:
        print(f"\n{Fore.YELLOW}Operation cancelled by user{Style.RESET_ALL}")
        return False

def show_progress(message, duration):
    if duration < 0:
        raise ValueError("Duration must be non-negative")

    try:
        print(f"\n{Fore.LIGHTMAGENTA_EX}{message}...{Style.RESET_ALL}")
        # Always show 12 dots with 0.1s delay each
        for _ in range(12):
            sys.stdout.write(f"{Fore.LIGHTCYAN_EX}·{Style.RESET_ALL}")
            sys.stdout.flush()
            time.sleep(0.1)
        print(f"\n{Fore.LIGHTGREEN_EX}✓ {Fore.GREEN}Complete!{Style.RESET_ALL}")
    except KeyboardInterrupt:
        print(f"\n{Fore.YELLOW}Progress interrupted{Style.RESET_ALL}")
        raise