#!/usr/bin/env python3
"""Simple requirements verification script"""

import sys
import subprocess

def check_package(package):
    try:
        __import__(package)
        print(f"[OK] {package} - OK")
        return True
    except ImportError:
        print(f"[FAIL] {package} - Missing")
        return False

def main():
    packages = ['flask', 'pandas', 'numpy', 'sklearn', 'streamlit']
    
    print("Checking core packages...")
    all_good = True
    
    for pkg in packages:
        if not check_package(pkg):
            all_good = False
    
    if all_good:
        print("\n[SUCCESS] All packages installed successfully!")
    else:
        print("\n[WARNING] Some packages missing. Run: pip install -r requirements.txt")

if __name__ == "__main__":
    main()