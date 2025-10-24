#!/usr/bin/env python3
"""
Simple Test Suite for HR AI System
Tests core functionality without Unicode characters
"""

import os
import sys
import pandas as pd
import numpy as np
from pathlib import Path

# Add project root to path
sys.path.append(str(Path(__file__).parent.parent))
sys.path.append(str(Path(__file__).parent.parent / 'src'))

def test_data_files():
    """Test if all required data files exist and have correct structure"""
    print("Testing Data Files...")
    
    required_files = {
        'feedback/cvs.csv': ['candidate_id', 'name', 'skills'],
        'feedback/jds.csv': ['jd_id', 'title', 'description'],
        'feedback/feedbacks.csv': ['candidate_id', 'jd_id', 'feedback_score', 'comment']
    }
    
    all_passed = True
    for file_path, required_cols in required_files.items():
        if os.path.exists(file_path):
            try:
                df = pd.read_csv(file_path)
                missing_cols = [col for col in required_cols if col not in df.columns]
                if missing_cols:
                    print(f"FAIL: {file_path} - Missing columns {missing_cols}")
                    all_passed = False
                else:
                    print(f"PASS: {file_path} - Structure valid ({len(df)} rows)")
            except Exception as e:
                print(f"FAIL: {file_path} - Error reading: {e}")
                all_passed = False
        else:
            print(f"FAIL: {file_path} - File not found")
            all_passed = False
    
    return all_passed

def test_rl_agent():
    """Test RL Agent functionality"""
    print("Testing RL Agent...")
    
    try:
        from agents.rl_agent import RLAgent
        
        # Initialize agent
        agent = RLAgent('feedback/cvs.csv', 'feedback/jds.csv')
        print("PASS: RL Agent initialization successful")
        
        # Test state generation
        state = agent.get_state(1, 1, "Good candidate")
        print(f"PASS: State generation - {state}")
        
        # Test action selection
        action = agent.choose_action(state)
        print(f"PASS: Action selection - Action {action}")
        
        # Test feedback processing
        feedback = pd.Series({
            'candidate_id': 1,
            'jd_id': 1,
            'feedback_score': 4,
            'comment': 'Great candidate'
        })
        agent.update_reward(feedback)
        print(f"PASS: Feedback processing - History length: {len(agent.history)}")
        
        return True
        
    except Exception as e:
        print(f"FAIL: RL Agent test failed: {e}")
        return False

def test_flask_app():
    """Test Flask application"""
    print("Testing Flask App...")
    
    try:
        # Import and check app
        from app import app, AGENT
        
        if AGENT is None:
            print("FAIL: Flask App - Agent not initialized")
            return False
        
        print("PASS: Flask App imports successful")
        
        # Test app configuration
        with app.test_client() as client:
            # Test home route
            response = client.get('/')
            if response.status_code == 200:
                print("PASS: Home route accessible")
            else:
                print(f"FAIL: Home route failed ({response.status_code})")
                return False
            
            # Test feedback endpoint
            test_data = {
                "candidate_id": 1,
                "jd_id": 1,
                "feedback_score": 4,
                "comment": "Test feedback"
            }
            
            response = client.post('/update_feedback', 
                                 json=test_data,
                                 content_type='application/json')
            
            if response.status_code == 200:
                print("PASS: Feedback endpoint working")
                result = response.get_json()
                print(f"INFO: Response status: {result.get('status', 'No status')}")
            else:
                print(f"FAIL: Feedback endpoint failed ({response.status_code})")
                return False
        
        return True
        
    except Exception as e:
        print(f"FAIL: Flask App test failed: {e}")
        return False

def test_dependencies():
    """Test if all required dependencies are installed"""
    print("Testing Dependencies...")
    
    required_packages = [
        'pandas', 'numpy', 'sklearn', 'flask', 'streamlit', 
        'plotly', 'textblob', 'nltk'
    ]
    
    missing_packages = []
    for package in required_packages:
        try:
            __import__(package)
            print(f"PASS: {package} installed")
        except ImportError:
            print(f"FAIL: {package} missing")
            missing_packages.append(package)
    
    if missing_packages:
        print(f"WARN: Install missing packages: pip install {' '.join(missing_packages)}")
        return False
    
    return True

def test_project_structure():
    """Test project structure"""
    print("Testing Project Structure...")
    
    required_dirs = ['agents', 'feedback', 'models']
    required_files = ['src/app.py', 'src/dashboard.py', 'src/main.py', 'requirements.txt']
    
    all_good = True
    
    for directory in required_dirs:
        if os.path.exists(directory):
            print(f"PASS: Directory {directory}/ exists")
        else:
            print(f"FAIL: Directory {directory}/ missing")
            all_good = False
    
    for file in required_files:
        if os.path.exists(file):
            print(f"PASS: File {file} exists")
        else:
            print(f"FAIL: File {file} missing")
            all_good = False
    
    return all_good

def run_integration_test():
    """Run end-to-end integration test"""
    print("Running Integration Test...")
    
    try:
        # Test complete workflow
        from agents.rl_agent import RLAgent
        
        agent = RLAgent('feedback/cvs.csv', 'feedback/jds.csv')
        
        # Process multiple feedbacks
        feedbacks_df = pd.read_csv('feedback/feedbacks.csv')
        initial_reward = agent.total_reward_over_time
        
        # Process first 5 feedbacks
        for _, feedback in feedbacks_df.head(5).iterrows():
            agent.update_reward(feedback)
        
        final_reward = agent.total_reward_over_time
        
        print(f"PASS: Processed 5 feedbacks: {initial_reward} -> {final_reward}")
        print(f"INFO: History entries: {len(agent.history)}")
        
        # Test decision making
        state = agent.get_state(1, 1, "Excellent candidate")
        action = agent.choose_action(state)
        actions = ['accept', 'reject', 'reconsider']
        print(f"INFO: Decision for candidate 1, job 1: {actions[action]}")
        
        return True
        
    except Exception as e:
        print(f"FAIL: Integration test failed: {e}")
        return False

def main():
    """Run all tests"""
    print("=" * 60)
    print("HR AI SYSTEM - SIMPLE TEST SUITE")
    print("=" * 60)
    
    tests = [
        ("Project Structure", test_project_structure),
        ("Dependencies", test_dependencies),
        ("Data Files", test_data_files),
        ("RL Agent", test_rl_agent),
        ("Flask App", test_flask_app),
        ("Integration", run_integration_test)
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
    print("\n" + "=" * 60)
    print("TEST SUMMARY")
    print("=" * 60)
    
    passed = sum(results.values())
    total = len(results)
    
    for test_name, result in results.items():
        status = "PASS" if result else "FAIL"
        print(f"{test_name}: {status}")
    
    print(f"\nOverall: {passed}/{total} tests passed")
    
    if passed == total:
        print("SUCCESS: All tests passed! Your HR AI System is ready to use.")
    else:
        print("WARNING: Some tests failed. Check the issues above.")
    
    return passed == total

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)