#!/usr/bin/env python3
"""
HR AI System - Data Setup Script
Ensures all required data files exist and creates sample data if needed
"""

import sys
from pathlib import Path

# Add project root to path
PROJECT_ROOT = Path(__file__).parent.absolute()
sys.path.append(str(PROJECT_ROOT))

def main():
    print("🚀 HR AI System - Data Setup")
    print("=" * 40)
    
    try:
        from config import validate_data_files, ensure_directories
        
        # Ensure directories exist
        ensure_directories()
        
        # Validate and create data files if needed
        validate_data_files(auto_create=True)
        
        print("\n✅ Setup completed successfully!")
        print("🎯 Your HR AI System is ready to run!")
        print("\n📋 Next steps:")
        print("   1. Activate virtual environment: venv\\Scripts\\activate")
        print("   2. Start Flask backend: python src/app.py")
        print("   3. Start dashboard: streamlit run src/dashboard.py")
        
    except Exception as e:
        print(f"\n❌ Setup failed: {e}")
        print("\n🔧 Manual setup required:")
        print("   1. Ensure Python 3.8+ is installed")
        print("   2. Install dependencies: pip install -r requirements.txt")
        print("   3. Create feedback/ directory")
        print("   4. Add required CSV files (cvs.csv, jds.csv, feedbacks.csv)")
        return 1
    
    return 0

if __name__ == "__main__":
    exit(main())