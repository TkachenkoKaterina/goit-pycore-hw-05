from colorama import init, Fore, Style, Back
from decorators import input_error
from commands import add_contact, change_contact, show_phone, show_all
from utils import parse_input

init(autoreset=True)

def main():
    contacts = {}
    print(f"{Fore.GREEN}Welcome to the assistant bot!{Style.RESET_ALL}")
    while True:
        user_input = input(f"{Fore.CYAN}Enter a command: {Style.RESET_ALL}")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print(f"{Fore.MAGENTA}Good bye!{Style.RESET_ALL}")
            break
        elif command == "hello":
            print(f"{Fore.GREEN}How can I help you?{Style.RESET_ALL}")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print(f"{Fore.RED}Invalid command.{Style.RESET_ALL} Choose from: {Back.LIGHTMAGENTA_EX}hello, add, change, phone, all, close, exit{Style.RESET_ALL}")

if __name__ == "__main__":
    main()
