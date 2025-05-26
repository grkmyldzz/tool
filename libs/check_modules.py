#!/usr/bin/env python3
# coding=utf-8

import sys
import pkg_resources
import subprocess
import urllib3
import warnings
import requests

# Disable SSL warnings and verification
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
warnings.filterwarnings('ignore', message='Unverified HTTPS request')
requests.packages.urllib3.disable_warnings()

def check_modules():
    required_modules = [
        'requests',
        'colorama',
        'bs4',
        'selenium',
        'urllib3'
    ]
    
    installed_packages = [pkg.key for pkg in pkg_resources.working_set]
    
    for module in required_modules:
        if module not in installed_packages:
            print(f"Installing {module}...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", module])
            
    return True 