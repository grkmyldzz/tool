#!/usr/bin/env python3
# coding=utf-8

from colorama import Fore, Style
from os import path

def print_success(message):
    print(Fore.GREEN + "[ + ] " + message + Style.RESET_ALL)

def print_error(message):
    print(Fore.RED + "[ ! ] " + message + Style.RESET_ALL)

def print_status(message):
    print(Fore.YELLOW + "[ * ] " + message + Style.RESET_ALL)

def ask_question(message):
    return input(Fore.BLUE + "[ ? ] " + message + ": " + Style.RESET_ALL)

def parse_proxy_file(proxy_file):
    if not path.exists(proxy_file):
        print_error("Proxy file not found!")
        return []
        
    with open(proxy_file, 'r') as file:
        return [line.strip() for line in file if line.strip()] 