#!/usr/bin/env python3
"""
Test Missing Data Files Handling
Tests the system's ability to handle missing data files gracefully
"""

import sys
import os
import tempfile
import shutil
from pathlib import Path

# Add project root to path
PROJECT_ROOT = Path(__file__).parent.parent.absolute()
sys.path.append(str(PROJECT_ROOT))

def test_missing_data_files():
    """Test system behavior when data files are missing"""
    print("🧪 Testing Missing Data Files Handling")
    print("=" * 50)
    
    # Create temporary directory for testing
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_path = Path(temp_dir)
        feedback_dir = temp_path / "feedback"
        
        print(f"📁 Test directory: {temp_path}")
        
        # Test 1: Missing directory
        print("\n1️⃣ Test: Missing feedback directory")
        try:
            from agents.data_generator import ensure_data_files_exist
            created_files = ensure_data_files_exist(feedback_dir)
            print(f"✅ Auto-created files: {created_files}")
            assert len(created_files) == 3, "Should create 3 files"
            print("✅ PASS: Missing directory handled correctly")
        except Exception as e:
            print(f"❌ FAIL: {e}")
            return False
        
        # Test 2: Verify created files are valid
        print("\n2️⃣ Test: Verify created files are valid CSV")
        try:
            import pandas as pd
            
            cvs_df = pd.read_csv(feedback_dir / "cvs.csv")
            jds_df = pd.read_csv(feedback_dir / "jds.csv")
            feedbacks_df = pd.read_csv(feedback_dir / "feedbacks.csv")
            
            assert len(cvs_df) > 0, "CVs should have data"
            assert len(jds_df) > 0, "JDs should have data"
            assert len(feedbacks_df) > 0, "Feedbacks should have data"
            
            # Check required columns
            assert 'candidate_id' in cvs_df.columns, "CVs missing candidate_id"
            assert 'skills' in cvs_df.columns, "CVs missing skills"
            assert 'jd_id' in jds_df.columns, "JDs missing jd_id"
            assert 'description' in jds_df.columns, "JDs missing description"
            assert 'feedback_score' in feedbacks_df.columns, "Feedbacks missing score"
            
            print("✅ PASS: Created files are valid CSV with required columns")
        except Exception as e:
            print(f"❌ FAIL: {e}")
            return False
        
        # Test 3: RL Agent can load generated data
        print("\n3️⃣ Test: RL Agent can load generated data")
        try:
            from agents.rl_agent import RLAgent
            
            agent = RLAgent(str(feedback_dir / "cvs.csv"), str(feedback_dir / "jds.csv"))
            assert len(agent.cvs) > 0, "Agent should load CVs"
            assert len(agent.jds) > 0, "Agent should load JDs"
            print("✅ PASS: RL Agent successfully loaded generated data")
        except Exception as e:
            print(f"❌ FAIL: {e}")
            return False
        
        # Test 4: Partial missing files
        print("\n4️⃣ Test: Partial missing files (only CVs missing)")
        try:
            # Remove only CVs file
            os.remove(feedback_dir / "cvs.csv")
            
            created_files = ensure_data_files_exist(feedback_dir)
            assert "cvs.csv" in created_files, "Should recreate only missing CVs"
            assert len(created_files) == 1, "Should only create 1 missing file"
            print("✅ PASS: Partial missing files handled correctly")
        except Exception as e:
            print(f"❌ FAIL: {e}")
            return False
    
    return True

def test_config_validation():
    """Test configuration validation with auto-creation"""
    print("\n🧪 Testing Configuration Validation")
    print("=" * 50)
    
    try:
        # Test with existing files (should pass)
        from config import validate_data_files
        result = validate_data_files(auto_create=False)
        print("✅ PASS: Validation with existing files")
        
        # Test auto-creation disabled with missing files
        with tempfile.TemporaryDirectory() as temp_dir:
            # Temporarily modify paths for testing
            import config
            original_data_dir = config.DATA_DIR
            config.DATA_DIR = Path(temp_dir) / "feedback"
            config.CVS_PATH = config.DATA_DIR / "cvs.csv"
            config.JDS_PATH = config.DATA_DIR / "jds.csv"
            config.FEEDBACKS_PATH = config.DATA_DIR / "feedbacks.csv"
            
            try:
                validate_data_files(auto_create=False)
                print("❌ FAIL: Should have raised FileNotFoundError")
                return False
            except FileNotFoundError:
                print("✅ PASS: Correctly raised FileNotFoundError when auto_create=False")
            finally:
                # Restore original paths
                config.DATA_DIR = original_data_dir
                config.CVS_PATH = original_data_dir / "cvs.csv"
                config.JDS_PATH = original_data_dir / "jds.csv"
                config.FEEDBACKS_PATH = original_data_dir / "feedbacks.csv"
        
        return True
    except Exception as e:
        print(f"❌ FAIL: {e}")
        return False

def main():
    """Run all tests"""
    print("🚀 HR AI System - Missing Data Files Handling Tests")
    print("=" * 60)
    
    tests_passed = 0
    total_tests = 2
    
    # Test 1: Missing data files handling
    if test_missing_data_files():
        tests_passed += 1
    
    # Test 2: Configuration validation
    if test_config_validation():
        tests_passed += 1
    
    # Results
    print("\n" + "=" * 60)
    print(f"📊 Test Results: {tests_passed}/{total_tests} tests passed")
    
    if tests_passed == total_tests:
        print("🎉 All tests passed! Missing data files handling works correctly.")
        return 0
    else:
        print("❌ Some tests failed. Check the implementation.")
        return 1

if __name__ == "__main__":
    exit(main())