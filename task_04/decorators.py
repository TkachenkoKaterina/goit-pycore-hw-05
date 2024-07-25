from colorama import Back, Style

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return f"{Back.YELLOW}Give me name and phone please.{Style.RESET_ALL}"
        except IndexError:
            return f"{Back.YELLOW}Invalid command format. Provide the required arguments.{Style.RESET_ALL}"
        except KeyError:
            return f"{Back.RED}Contact not found.{Style.RESET_ALL}"
    return inner
