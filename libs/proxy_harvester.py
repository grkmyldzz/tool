#!/usr/bin/env python3
# coding=utf-8

import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
from .utils import print_status, print_error, print_success
import time
import os

def verify_proxy(proxy):
    try:
        response = requests.get('https://www.tiktok.com', 
                              proxies={'http': proxy, 'https': proxy},
                              timeout=10)
        return proxy if response.status_code == 200 else None
    except:
        return None

def find_proxies():
    print_status("Gathering proxies from multiple sources...")
    proxies = set()
    
    # List of HTTPS proxy sources
    sources = [
        "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all",
        "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=10000&country=all",
        "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks5&timeout=10000&country=all"
    ]
    
    session = requests.Session()
    session.verify = False  # Disable SSL verification
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    for source in sources:
        try:
            print_status(f"Fetching proxies...")
            response = session.get(source, headers=headers, timeout=30)
            if response.status_code == 200:
                proxy_list = response.text.strip().split('\n')
                valid_proxies = [proxy.strip() for proxy in proxy_list if ':' in proxy and proxy.strip()]
                proxies.update(valid_proxies)
                print_success(f"Found {len(valid_proxies)} proxies")
            time.sleep(2)  # Add delay between requests
        except Exception as e:
            continue
    
    # If no proxies found, use default list
    if not proxies:
        print_status("Using default proxy list...")
        default_proxies = [
            "20.111.54.16:80",
            "20.205.61.143:80",
            "52.24.80.166:80",
            "104.148.36.10:80",
            "185.162.230.55:80",
            "159.203.61.169:8080",
            "167.172.158.85:81",
            "35.236.207.242:80",
            "146.190.123.209:80",
            "138.197.148.215:80",
            "142.93.61.46:80",
            "157.245.27.9:3128",
            "165.227.71.60:80",
            "157.230.48.102:80",
            "68.183.185.62:80"
        ]
        proxies.update(default_proxies)
    
    return list(proxies)

def verify_proxies(proxies):
    print_status(f"Found {len(proxies)} proxies, verifying them now...")
    
    verified_proxies = []
    with ThreadPoolExecutor(max_workers=50) as executor:
        results = executor.map(verify_proxy, proxies)
        verified_proxies = [proxy for proxy in results if proxy]
    
    return verified_proxies 