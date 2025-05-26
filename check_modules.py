import sys
import pkg_resources
import subprocess

def check_modules():
    required_modules = [
        'requests',
        'colorama',
        'bs4',
        'selenium'
    ]
    
    installed_packages = [pkg.key for pkg in pkg_resources.working_set]
    
    for module in required_modules:
        if module not in installed_packages:
            print(f"Installing {module}...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", module])
            
    return True 