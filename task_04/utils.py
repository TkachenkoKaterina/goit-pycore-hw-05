import re

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args

def is_valid_name(name):
    pattern = r"^[A-Za-z\s]+$"
    return re.match(pattern, name)

def is_valid_phone(phone):
    pattern = r"^\+\d{1,3}\d{4,14}$"
    return re.match(pattern, phone)
