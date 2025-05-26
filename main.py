#!/usr/bin/env python3
# coding=utf-8

from libs.check_modules import check_modules
from sys import exit
from os import _exit

check_modules()

from os import path
from libs.logo import print_logo
from libs.utils import print_success, print_error, ask_question, print_status, parse_proxy_file
from libs.proxy_harvester import find_proxies
from libs.attack import report_profile_attack, report_post_attack, REPORT_REASONS
from multiprocessing import Process
from colorama import Fore, Style

def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

def profile_attack_process(username, proxy_list):
    if len(proxy_list) == 0:
        for _ in range(10):
            report_profile_attack(username, None)
        return

    for proxy in proxy_list:
        report_profile_attack(username, proxy)

def post_attack_process(post_url, proxy_list):
    if len(proxy_list) == 0:
        for _ in range(10):
            report_post_attack(post_url, None)
        return

    for proxy in proxy_list:
        report_post_attack(post_url, proxy)

def post_attack(proxies):
    post_url = ask_question("Enter the link of the Instagram post you want to report")
    print(Style.RESET_ALL)
    
    processes = []
    if len(proxies) == 0:
        for k in range(5):
            p = Process(target=post_attack_process, args=(post_url, []))
            processes.append(p)
            p.start()
            print_status(f"{k + 1}. Transaction Opened!")
    else:
        chunk = list(chunks(proxies, 10))
        print("")
        print_status("Post complaint attack is starting!\n")

        for i, proxy_list in enumerate(chunk, 1):
            p = Process(target=post_attack_process, args=(post_url, proxy_list))
            processes.append(p)
            p.start()
            print_status(f"{i}. Transaction Opened!")

    for p in processes:
        p.join()

def profile_attack(proxies):
    username = ask_question("Enter the Instagram username of the person you want to report")
    print(Style.RESET_ALL)
    
    processes = []
    if len(proxies) == 0:
        for k in range(5):
            p = Process(target=profile_attack_process, args=(username, []))
            processes.append(p)
            p.start()
            print_status(f"{k + 1}. Transaction Opened!")
    else:
        chunk = list(chunks(proxies, 10))
        print("")
        print_status("Profile complaint attack is starting!\n")

        for i, proxy_list in enumerate(chunk, 1):
            p = Process(target=profile_attack_process, args=(username, proxy_list))
            processes.append(p)
            p.start()
            print_status(f"{i}. Transaction Opened!")

    for p in processes:
        p.join()

def print_report_reasons():
    print("\nAvailable report reasons:")
    for key, value in REPORT_REASONS.items():
        print(f"{key} - {value.replace('_', ' ').title()}")
    print("")

def main():
    print_success("Modules loaded!\n")

    ret = ask_question("Would you like to use a proxy? [Y/N]")

    proxies = []

    if ret.upper() == "Y":
        ret = ask_question("Would you like to collect your proxies from the internet? [Y/N]")

        if ret.upper() == "Y":
            print_status("Gathering proxy from the Internet! This may take a while.\n")
            proxies = find_proxies()
        elif ret.upper() == "N":
            print_status("Please have a maximum of 50 proxies in a file!")
            file_path = ask_question("Enter the path to your proxy list")
            proxies = parse_proxy_file(file_path)
        else:
            print_error("Answer not understood, exiting!")
            exit(1)

        print_success(f"{len(proxies)} Number of proxies found!\n")
    elif ret.upper() == "N":
        pass
    else:
        print_error("Answer not understood, exiting!")
        exit(1)

    print("")
    print_status("1 - Report an Instagram profile")
    print_status("2 - Report an Instagram post")
    report_choice = ask_question("Please select the complaint method")
    print("")

    if not report_choice.isdigit():
        print_error("The answer is not understood.")
        exit(1)
    
    choice = int(report_choice)
    if choice not in [1, 2]:
        print_error("The answer is not understood.")
        exit(1)

    print_report_reasons()

    if choice == 1:
        profile_attack(proxies)
    else:
        post_attack(proxies)

if __name__ == "__main__":
    print_logo()
    try:
        main()
        print(Style.RESET_ALL)
    except KeyboardInterrupt:
        print("\n\n" + Fore.RED + "[ * ] The program is closing!")
        print(Style.RESET_ALL)
        _exit(0) 