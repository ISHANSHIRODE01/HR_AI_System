#!/usr/bin/env python3
"""
Test configuration and environment setup
"""

import os
import sys
from pathlib import Path

# Add project root to path
sys.path.append(str(Path(__file__).parent.parent))

def test_config_validation():
    """Test configuration file validation"""
    print("Testing Configuration Validation...")
    
    try:
        from config import validate_data_files, CVS_PATH, JDS_PATH, FEEDBACKS_PATH
        
        # Test file existence
        validate_data_files()
        print("PASS: All required data files exist")
        
        # Test path types
        assert CVS_PATH.exists(), "CVS file missing"
        assert JDS_PATH.exists(), "JDS file missing" 
        assert FEEDBACKS_PATH.exists(), "Feedbacks file missing"
        print("PASS: Path validation successful")
        
        return True
        
    except Exception as e:
        print(f"FAIL: Configuration test failed: {e}")
        return False

def test_environment_variables():
    """Test environment variable handling"""
    print("Testing Environment Variables...")
    
    try:
        from config import GOOGLE_AI_API_KEY
        
        if GOOGLE_AI_API_KEY:
            print("PASS: Google AI API key found")
        else:
            print("INFO: Google AI API key not set (optional)")
        
        return True
        
    except Exception as e:
        print(f"FAIL: Environment test failed: {e}")
        return False

def main():
    """Run configuration tests"""
    print("=" * 50)
    print("CONFIGURATION TESTS")
    print("=" * 50)
    
    tests = [
        ("Config Validation", test_config_validation),
        ("Environment Variables", test_environment_variables)
    ]
    
    results = {}
    
    for test_name, test_func in tests:
        print(f"\n--- {test_name} Test ---")
        try:
            results[test_name] = test_func()
        except Exception as e:
            print(f"FAIL: {test_name} test crashed: {e}")
            results[test_name] = False
    
    # Summary
    print("\n" + "=" * 50)
    print("TEST SUMMARY")
    print("=" * 50)
    
    passed = sum(results.values())
    total = len(results)
    
    for test_name, result in results.items():
        status = "PASS" if result else "FAIL"
        print(f"{test_name}: {status}")
    
    print(f"\nOverall: {passed}/{total} tests passed")
    
    return passed == total

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)