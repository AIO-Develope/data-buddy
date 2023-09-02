from colorama import Fore, Style

def colored_message(message, color, style=Style.NORMAL):
    return f"{style}{color}{message}{Style.RESET_ALL}"

def info(message):
    formatted_message = colored_message(message, Fore.BLUE, Style.BRIGHT)
    print(formatted_message)

def error(message):
    formatted_message = colored_message(message, Fore.RED, Style.BRIGHT)
    print(formatted_message)

def done(message):
    formatted_message = colored_message(message, Fore.GREEN, Style.BRIGHT)
    print(formatted_message)
