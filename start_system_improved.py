#!/usr/bin/env python3
"""
Improved HR AI System Startup Script
Handles common issues and provides better error reporting
"""

import os
import sys
import subprocess
import time
from pathlib import Path

# Fix Windows Unicode issues
if sys.platform == "win32":
    import codecs
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)
    sys.stderr = codecs.getwriter('utf-8')(sys.stderr.buffer)

def check_python_version():
    """Check if Python version is compatible"""
    if sys.version_info < (3, 8):
        print("[ERROR] Python 3.8+ required. Current version:", sys.version)
        return False
    print(f"[OK] Python {sys.version_info.major}.{sys.version_info.minor} detected")
    return True

def check_dependencies():
    """Check if required packages are installed"""
    required_packages = ['flask', 'pandas', 'streamlit', 'requests']
    missing = []
    
    for package in required_packages:
        try:
            __import__(package)
            print(f"[OK] {package} installed")
        except ImportError:
            missing.append(package)
            print(f"[MISSING] {package}")
    
    if missing:
        print(f"\n[INSTALL] Installing missing packages: {', '.join(missing)}")
        subprocess.run([sys.executable, "-m", "pip", "install"] + missing)
        return True
    return True

def check_data_files():
    """Check if required data files exist"""
    data_dir = Path("feedback")
    required_files = ["cvs.csv", "jds.csv", "feedbacks.csv"]
    
    if not data_dir.exists():
        print("[ERROR] feedback/ directory not found")
        return False
    
    missing_files = []
    for file in required_files:
        file_path = data_dir / file
        if file_path.exists():
            print(f"[OK] {file} found")
        else:
            missing_files.append(file)
            print(f"[MISSING] {file}")
    
    if missing_files:
        print(f"\n[WARNING] Missing data files: {', '.join(missing_files)}")
        print("The system will still run but may have limited functionality")
    
    return len(missing_files) == 0

def check_api_key():
    """Check API key configuration"""
    env_file = Path(".env")
    api_key = os.getenv("GOOGLE_AI_API_KEY")
    
    if env_file.exists():
        print("[OK] .env file found")
        if api_key:
            print(f"[OK] Google AI API key configured (length: {len(api_key)})")
            return True
        else:
            print("[WARNING] .env file exists but no GOOGLE_AI_API_KEY found")
    else:
        print("[WARNING] .env file not found")
    
    if not api_key:
        print("[INFO] Gemini AI features will be disabled")
        print("   To enable: Set GOOGLE_AI_API_KEY in .env file")
    
    return api_key is not None

def start_flask():
    """Start Flask backend"""
    print("\n[STARTING] Flask Backend...")
    try:
        # Start Flask in background
        process = subprocess.Popen(
            [sys.executable, "src/app.py"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        
        # Wait a moment for startup
        time.sleep(3)
        
        # Check if process is still running
        if process.poll() is None:
            print("[OK] Flask backend started successfully")
            print("   API available at: http://localhost:5000")
            print("   Health check: http://localhost:5000/health")
            return process
        else:
            stdout, stderr = process.communicate()
            print("[ERROR] Flask failed to start")
            print("STDOUT:", stdout.decode())
            print("STDERR:", stderr.decode())
            return None
            
    except Exception as e:
        print(f"[ERROR] Error starting Flask: {e}")
        return None

def start_dashboard():
    """Start Streamlit dashboard"""
    print("\n[STARTING] Streamlit Dashboard...")
    try:
        # Start Streamlit
        subprocess.run([
            sys.executable, "-m", "streamlit", "run", "src/dashboard.py",
            "--server.port", "8501"
        ])
    except KeyboardInterrupt:
        print("\n[INFO] Dashboard stopped by user")
    except Exception as e:
        print(f"[ERROR] Error starting dashboard: {e}")

def main():
    """Main startup routine"""
    print("=" * 50)
    print("HR AI System - Improved Startup")
    print("=" * 50)
    
    # System checks
    if not check_python_version():
        return False
    
    check_dependencies()
    check_data_files()
    check_api_key()
    
    print("\n" + "=" * 50)
    print("System Status Summary")
    print("=" * 50)
    
    # Start Flask backend
    flask_process = start_flask()
    if not flask_process:
        print("[ERROR] Cannot start system - Flask backend failed")
        return False
    
    try:
        # Start dashboard (this will block)
        start_dashboard()
    finally:
        # Cleanup
        if flask_process and flask_process.poll() is None:
            print("\n[STOP] Stopping Flask backend...")
            flask_process.terminate()
            flask_process.wait()
    
    print("[INFO] HR AI System stopped")
    return True

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n[INFO] Startup cancelled by user")
    except Exception as e:
        print(f"[ERROR] Unexpected error: {e}")
        sys.exit(1)