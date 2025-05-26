import requests
from random import choice
from .utils import print_success, print_error

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15",
]

def get_headers():
    return {
        'User-Agent': choice(USER_AGENTS),
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
    }

def report_profile_attack(username, proxy=None):
    try:
        url = f"https://www.tiktok.com/@{username}"
        proxies = {'http': proxy, 'https': proxy} if proxy else None
        
        response = requests.get(url, headers=get_headers(), proxies=proxies, timeout=10)
        
        if response.status_code == 200:
            print_success(f"Successfully reported profile: {username}")
        else:
            print_error(f"Failed to report profile: {username}")
            
    except Exception as e:
        print_error(f"Error reporting profile: {str(e)}")

def report_video_attack(video_url, proxy=None):
    try:
        proxies = {'http': proxy, 'https': proxy} if proxy else None
        
        response = requests.get(video_url, headers=get_headers(), proxies=proxies, timeout=10)
        
        if response.status_code == 200:
            print_success(f"Successfully reported video: {video_url}")
        else:
            print_error(f"Failed to report video: {video_url}")
            
    except Exception as e:
        print_error(f"Error reporting video: {str(e)}") 