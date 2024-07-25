from colorama import Back, Style
from decorators import input_error
from utils import is_valid_name, is_valid_phone

@input_error
def add_contact(args, contacts):
    if len(args) != 2:
        raise ValueError("Invalid command format")
    
    name, phone = args

    if not is_valid_name(name):
        return f"{Back.RED}Invalid name format. Name should only contain letters and spaces.{Style.RESET_ALL}"
    
    if not is_valid_phone(phone):
        return f"{Back.RED}Invalid phone format. Phone should start with '+' and contain a valid country code: for example +380972347955.{Style.RESET_ALL}"

    contacts[name] = phone
    return f"{Back.GREEN}Contact '{name}' added with phone number '{phone}'.{Style.RESET_ALL}"

@input_error
def change_contact(args, contacts):
    if len(args) != 2:
        raise ValueError("Invalid command format")
    
    name, phone = args

    if not is_valid_name(name):
        return f"{Back.RED}Invalid name format. Name should only contain letters and spaces.{Style.RESET_ALL}"
    
    if not is_valid_phone(phone):
        return f"{Back.RED}Invalid phone format. Phone should start with '+' and contain a valid country code followed by 4 to 14 digits.{Style.RESET_ALL}"

    if name in contacts:
        contacts[name] = phone
        return f"{Back.GREEN}Contact '{name}' changed to new phone number '{phone}'.{Style.RESET_ALL}"
    else:
        raise KeyError("Contact not found")

@input_error
def show_phone(args, contacts):
    if len(args) != 1:
        raise ValueError("Invalid command format")
    
    name = args[0]
    if name in contacts:
        return f"{Back.GREEN}Номер телефону {name}: {contacts[name]}{Style.RESET_ALL}"
    else:
        raise KeyError("Contact not found")

@input_error
def show_all(contacts):
    if len(contacts) == 0:
        return f"{Back.RED}Книга контактів порожня.{Style.RESET_ALL}"
    else:
        contact_list = "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])
        return f"{Back.GREEN}Всі контакти:\n{contact_list}{Style.RESET_ALL}"
