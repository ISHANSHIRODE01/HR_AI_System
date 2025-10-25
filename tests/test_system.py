#!/usr/bin/env python3
"""
Comprehensive Test Suite for HR AI System
Tests all components: RL Agent, Flask App, Dashboard, Data Files
"""

import os
import sys
import pandas as pd
import numpy as np
import requests
import subprocess
import time
from pathlib import Path

# Add project root to path
sys.path.append(str(Path(__file__).parent))

class Colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    END = '\033[0m'

def print_status(message, status="INFO"):
    colors = {"PASS": Colors.GREEN, "FAIL": Colors.RED, "WARN": Colors.YELLOW, "INFO": Colors.BLUE}
    print(f"{colors.get(status, Colors.BLUE)}[{status}]{Colors.END} {message}")

def test_data_files():
    """Test if all required data files exist and have correct structure"""
    print_status("Testing Data Files...", "INFO")
    
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
                    print_status(f"{file_path}: Missing columns {missing_cols}", "FAIL")
                    all_passed = False
                else:
                    print_status(f"{file_path}: ✓ Structure valid ({len(df)} rows)", "PASS")
            except Exception as e:
                print_status(f"{file_path}: Error reading - {e}", "FAIL")
                all_passed = False
        else:
            print_status(f"{file_path}: File not found", "FAIL")
            all_passed = False
    
    return all_passed

def test_rl_agent():
    """Test RL Agent functionality"""
    print_status("Testing RL Agent...", "INFO")
    
    try:
        from agents.rl_agent import RLAgent
        
        # Initialize agent
        agent = RLAgent('feedback/cvs.csv', 'feedback/jds.csv')
        print_status("RL Agent initialization: ✓", "PASS")
        
        # Test state generation
        state = agent.get_state(1, 1, "Good candidate")
        print_status(f"State generation: ✓ {state}", "PASS")
        
        # Test action selection
        action = agent.choose_action(state)
        print_status(f"Action selection: ✓ Action {action}", "PASS")
        
        # Test feedback processing
        feedback = pd.Series({
            'candidate_id': 1,
            'jd_id': 1,
            'feedback_score': 4,
            'comment': 'Great candidate'
        })
        agent.update_reward(feedback)
        print_status(f"Feedback processing: ✓ History length: {len(agent.history)}", "PASS")
        
        return True
        
    except Exception as e:
        print_status(f"RL Agent test failed: {e}", "FAIL")
        return False

def test_flask_app():
    """Test Flask application"""
    print_status("Testing Flask App...", "INFO")
    
    try:
        # Import and check app
        from app import app, AGENT
        
        if AGENT is None:
            print_status("Flask App: Agent not initialized", "FAIL")
            return False
        
        print_status("Flask App: ✓ Imports successful", "PASS")
        
        # Test app configuration
        with app.test_client() as client:
            # Test home route
            response = client.get('/')
            if response.status_code == 200:
                print_status("Home route: ✓ Accessible", "PASS")
            else:
                print_status(f"Home route: Failed ({response.status_code})", "FAIL")
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
                print_status("Feedback endpoint: ✓ Working", "PASS")
                result = response.get_json()
                print_status(f"Response: {result.get('status', 'No status')}", "INFO")
            else:
                print_status(f"Feedback endpoint: Failed ({response.status_code})", "FAIL")
                return False
        
        return True
        
    except Exception as e:
        print_status(f"Flask App test failed: {e}", "FAIL")
        return False

def test_dashboard_imports():
    """Test dashboard imports and basic functionality"""
    print_status("Testing Dashboard Imports...", "INFO")
    
    try:
        # Test if dashboard can be imported
        import dashboard
        print_status("Dashboard imports: ✓ Successful", "PASS")
        
        # Check if required functions exist
        if hasattr(dashboard, 'load_agent_and_feedback'):
            print_status("Dashboard functions: ✓ Found", "PASS")
        else:
            print_status("Dashboard functions: Missing load_agent_and_feedback", "WARN")
        
        return True
        
    except Exception as e:
        print_status(f"Dashboard test failed: {e}", "FAIL")
        return False

def test_dependencies():
    """Test if all required dependencies are installed"""
    print_status("Testing Dependencies...", "INFO")
    
    required_packages = [
        'pandas', 'numpy', 'sklearn', 'flask', 'streamlit', 
        'plotly', 'textblob', 'nltk'
    ]
    
    missing_packages = []
    for package in required_packages:
        try:
            __import__(package)
            print_status(f"{package}: ✓ Installed", "PASS")
        except ImportError:
            print_status(f"{package}: Missing", "FAIL")
            missing_packages.append(package)
    
    if missing_packages:
        print_status(f"Install missing packages: pip install {' '.join(missing_packages)}", "WARN")
        return False
    
    return True

def test_project_structure():
    """Test project structure"""
    print_status("Testing Project Structure...", "INFO")
    
    required_dirs = ['agents', 'feedback', 'models']
    required_files = ['app.py', 'dashboard.py', 'main.py', 'requirements.txt']
    
    all_good = True
    
    for directory in required_dirs:
        if os.path.exists(directory):
            print_status(f"Directory {directory}/: ✓ Exists", "PASS")
        else:
            print_status(f"Directory {directory}/: Missing", "FAIL")
            all_good = False
    
    for file in required_files:
        if os.path.exists(file):
            print_status(f"File {file}: ✓ Exists", "PASS")
        else:
            print_status(f"File {file}: Missing", "FAIL")
            all_good = False
    
    return all_good

def run_integration_test():
    """Run end-to-end integration test"""
    print_status("Running Integration Test...", "INFO")
    
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
        
        print_status(f"Processed 5 feedbacks: {initial_reward} → {final_reward}", "PASS")
        print_status(f"History entries: {len(agent.history)}", "INFO")
        
        # Test decision making
        state = agent.get_state(1, 1, "Excellent candidate")
        action = agent.choose_action(state)
        actions = ['accept', 'reject', 'reconsider']
        print_status(f"Decision for candidate 1, job 1: {actions[action]}", "INFO")
        
        return True
        
    except Exception as e:
        print_status(f"Integration test failed: {e}", "FAIL")
        return False

def main():
    """Run all tests"""
    print_status("=" * 60, "INFO")
    print_status("HR AI SYSTEM - COMPREHENSIVE TEST SUITE", "INFO")
    print_status("=" * 60, "INFO")
    
    tests = [
        ("Project Structure", test_project_structure),
        ("Dependencies", test_dependencies),
        ("Data Files", test_data_files),
        ("RL Agent", test_rl_agent),
        ("Flask App", test_flask_app),
        ("Dashboard", test_dashboard_imports),
        ("Integration", run_integration_test)
    ]
    
    results = {}
    
    for test_name, test_func in tests:
        print_status(f"\n--- {test_name} Test ---", "INFO")
        try:
            results[test_name] = test_func()
        except Exception as e:
            print_status(f"{test_name} test crashed: {e}", "FAIL")
            results[test_name] = False
    
    # Summary
    print_status("\n" + "=" * 60, "INFO")
    print_status("TEST SUMMARY", "INFO")
    print_status("=" * 60, "INFO")
    
    passed = sum(results.values())
    total = len(results)
    
    for test_name, result in results.items():
        status = "PASS" if result else "FAIL"
        print_status(f"{test_name}: {status}", status)
    
    print_status(f"\nOverall: {passed}/{total} tests passed", 
                "PASS" if passed == total else "WARN")
    
    if passed == total:
        print_status("🎉 All tests passed! Your HR AI System is ready to use.", "PASS")
    else:
        print_status("⚠️  Some tests failed. Check the issues above.", "WARN")
    
    return passed == total

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)