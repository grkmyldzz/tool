from colorama import Fore, Style
import os

def print_success(message):
    print(Fore.GREEN + "[ + ] " + message)
    print(Style.RESET_ALL)

def print_error(message):
    print(Fore.RED + "[ - ] " + message)
    print(Style.RESET_ALL)

def print_status(message):
    print(Fore.YELLOW + "[ * ] " + message)
    print(Style.RESET_ALL)

def ask_question(message):
    return input(Fore.BLUE + "[ ? ] " + message + ": " + Style.RESET_ALL)

def parse_proxy_file(file_path):
    if not os.path.exists(file_path):
        print_error("Proxy file not found!")
        return []
        
    with open(file_path, 'r') as file:
        proxies = file.read().strip().split('\n')
        return [proxy.strip() for proxy in proxies if proxy.strip()] 