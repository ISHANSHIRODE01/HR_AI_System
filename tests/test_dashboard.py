#!/usr/bin/env python3
"""
Dashboard Test Script for HR AI System
Tests Streamlit dashboard functionality
"""

import sys
import os
import pandas as pd
from pathlib import Path

# Add project root to path
sys.path.append(str(Path(__file__).parent.parent))
sys.path.append(str(Path(__file__).parent.parent / 'src'))

def test_dashboard_components():
    """Test dashboard components without running Streamlit"""
    print("Testing Dashboard Components...")
    print("=" * 40)
    
    try:
        # Test imports
        from agents.rl_agent import RLAgent
        print("PASS: RL Agent import successful")
        
        # Test data loading
        cvs_path = 'feedback/cvs.csv'
        jds_path = 'feedback/jds.csv'
        feedbacks_path = 'feedback/feedbacks.csv'
        
        if all(os.path.exists(p) for p in [cvs_path, jds_path, feedbacks_path]):
            print("PASS: All required CSV files exist")
        else:
            print("FAIL: Missing CSV files")
            return False
        
        # Test agent initialization
        agent = RLAgent(cvs_path, jds_path)
        feedback_df = pd.read_csv(feedbacks_path)
        print("PASS: Agent and data loading successful")
        
        # Test feedback processing
        for _, feedback in feedback_df.head(5).iterrows():
            agent.update_reward(feedback)
        
        print(f"PASS: Processed {len(agent.history)} feedback entries")
        print(f"INFO: Total reward: {agent.total_reward_over_time}")
        
        # Test data for dashboard
        if len(agent.history) > 0:
            history_df = pd.DataFrame(agent.history)
            print(f"PASS: History DataFrame created with {len(history_df)} rows")
            
            # Test metrics calculation
            total_feedbacks = len(feedback_df)
            cumulative_reward = agent.total_reward_over_time
            
            print(f"INFO: Dashboard metrics ready:")
            print(f"  - Total Feedbacks: {total_feedbacks}")
            print(f"  - Cumulative Reward: {cumulative_reward}")
            print(f"  - History Entries: {len(agent.history)}")
        else:
            print("WARN: No history entries found")
        
        # Test Q-table access
        q_table_shape = agent.q_table.shape
        print(f"PASS: Q-table accessible with shape {q_table_shape}")
        
        return True
        
    except Exception as e:
        print(f"FAIL: Dashboard test failed: {e}")
        return False

def test_streamlit_imports():
    """Test Streamlit-related imports"""
    print("\nTesting Streamlit Imports...")
    print("=" * 40)
    
    try:
        import streamlit as st
        print("PASS: Streamlit imported successfully")
        
        import plotly.express as px
        print("PASS: Plotly imported successfully")
        
        import numpy as np
        print("PASS: NumPy imported successfully")
        
        return True
        
    except ImportError as e:
        print(f"FAIL: Import error: {e}")
        return False

def main():
    """Run dashboard tests"""
    print("HR AI System - Dashboard Test Suite")
    print("=" * 50)
    
    tests = [
        ("Dashboard Components", test_dashboard_components),
        ("Streamlit Imports", test_streamlit_imports)
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
    print("DASHBOARD TEST SUMMARY")
    print("=" * 50)
    
    passed = sum(results.values())
    total = len(results)
    
    for test_name, result in results.items():
        status = "PASS" if result else "FAIL"
        print(f"{test_name}: {status}")
    
    print(f"\nOverall: {passed}/{total} tests passed")
    
    if passed == total:
        print("SUCCESS: Dashboard components are ready!")
        print("\nTo start the dashboard, run:")
        print("streamlit run dashboard.py")
    else:
        print("WARNING: Some dashboard tests failed.")
    
    return passed == total

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)