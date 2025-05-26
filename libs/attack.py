#!/usr/bin/env python3
# coding=utf-8

import requests
from random import choice
from .utils import print_success, print_error
import json
import random
import time

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15",
]

REPORT_REASONS = {
    "1": "spam",
    "2": "self_injury",
    "3": "hate_speech",
    "4": "harassment",
    "5": "violence",
    "6": "scam",
    "7": "false_information",
    "8": "intellectual_property",
    "9": "eating_disorders"
}

def get_random_user_agent():
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.59"
    ]
    return random.choice(user_agents)

def get_headers():
    return {
        'User-Agent': choice(USER_AGENTS),
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Content-Type': 'application/json',
        'X-IG-App-ID': '936619743392459',
        'Origin': 'https://www.instagram.com',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Referer': 'https://www.instagram.com/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
    }

def get_user_id(username, proxy=None):
    try:
        url = f"https://www.instagram.com/api/v1/users/web_profile_info/?username={username}"
        proxies = {'http': proxy, 'https': proxy} if proxy else None
        
        response = requests.get(url, headers=get_headers(), proxies=proxies, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            return data['data']['user']['id']
        return None
            
    except Exception as e:
        print_error(f"Error getting user ID: {str(e)}")
        return None

def report_profile_attack(username, proxy=None):
    headers = {
        "User-Agent": get_random_user_agent(),
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "en-US,en;q=0.5",
        "Content-Type": "application/json",
        "Origin": "https://www.instagram.com",
        "DNT": "1",
        "Connection": "keep-alive",
        "Referer": f"https://www.instagram.com/{username}/"
    }
    
    proxies = {"http": proxy, "https": proxy} if proxy else None
    
    try:
        # Simulate report request (this is a mock implementation)
        reason = random.choice(list(REPORT_REASONS.values()))
        print_success(f"Reported profile {username} for {reason}")
        time.sleep(random.uniform(1, 3))  # Random delay between requests
        return True
    except Exception as e:
        print_error(f"Failed to report profile {username}: {str(e)}")
        return False

def report_post_attack(post_url, proxy=None):
    headers = {
        "User-Agent": get_random_user_agent(),
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "en-US,en;q=0.5",
        "Content-Type": "application/json",
        "Origin": "https://www.instagram.com",
        "DNT": "1",
        "Connection": "keep-alive",
        "Referer": post_url
    }
    
    proxies = {"http": proxy, "https": proxy} if proxy else None
    
    try:
        # Simulate report request (this is a mock implementation)
        reason = random.choice(list(REPORT_REASONS.values()))
        print_success(f"Reported post {post_url} for {reason}")
        time.sleep(random.uniform(1, 3))  # Random delay between requests
        return True
    except Exception as e:
        print_error(f"Failed to report post {post_url}: {str(e)}")
        return False 