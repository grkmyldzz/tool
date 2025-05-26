import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
from .utils import print_status, print_error

def verify_proxy(proxy):
    try:
        response = requests.get('https://www.tiktok.com', 
                              proxies={'http': proxy, 'https': proxy},
                              timeout=10)
        return proxy if response.status_code == 200 else None
    except:
        return None

def find_proxies():
    proxy_sources = [
        'https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt',
        'https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/http.txt',
        'https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt'
    ]
    
    proxies = set()
    
    for source in proxy_sources:
        try:
            response = requests.get(source, timeout=10)
            if response.status_code == 200:
                new_proxies = response.text.strip().split('\n')
                proxies.update(new_proxies)
        except:
            print_error(f"Failed to fetch proxies from {source}")
            continue
    
    print_status(f"Found {len(proxies)} proxies, verifying them now...")
    
    verified_proxies = []
    with ThreadPoolExecutor(max_workers=50) as executor:
        results = executor.map(verify_proxy, proxies)
        verified_proxies = [proxy for proxy in results if proxy]
    
    return verified_proxies 