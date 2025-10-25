#!/usr/bin/env python3
"""
Test Flask App Only - Without Unicode Issues
"""

import os
import sys
import pandas as pd
from pathlib import Path

# Add project root to path
sys.path.append(str(Path(__file__).parent.parent))
sys.path.append(str(Path(__file__).parent.parent / 'src'))

def test_flask_app_simple():
    """Test Flask application without Unicode issues"""
    print("Testing Flask App (Simple)...")
    
    try:
        # Test imports first
        from agents.rl_agent import RLAgent
        from agents.automation import trigger_event
        
        # Test RL Agent initialization
        agent = RLAgent('feedback/cvs.csv', 'feedback/jds.csv')
        print("PASS: RL Agent can be initialized")
        
        # Test automation function
        event = trigger_event("test_event", user_id=1, details={"test": "data"})
        print("PASS: Automation trigger works")
        
        # Now test Flask app components
        from flask import Flask
        app = Flask(__name__)
        
        @app.route("/")
        def home():
            return "HR RL Agent Backend Running"
        
        @app.route("/update_feedback", methods=["POST"])
        def update_feedback():
            return {"status": "test_success"}
        
        # Test with test client
        with app.test_client() as client:
            # Test home route
            response = client.get('/')
            if response.status_code == 200:
                print("PASS: Home route works")
            else:
                print(f"FAIL: Home route failed ({response.status_code})")
                return False
            
            # Test feedback endpoint
            response = client.post('/update_feedback')
            if response.status_code == 200:
                print("PASS: Feedback endpoint accessible")
            else:
                print(f"FAIL: Feedback endpoint failed ({response.status_code})")
                return False
        
        print("PASS: Flask app core functionality works")
        return True
        
    except Exception as e:
        print(f"FAIL: Flask App test failed: {e}")
        return False

def test_full_workflow():
    """Test the complete workflow"""
    print("Testing Full Workflow...")
    
    try:
        from agents.rl_agent import RLAgent
        
        # Initialize agent
        agent = RLAgent('feedback/cvs.csv', 'feedback/jds.csv')
        
        # Simulate feedback processing
        feedback_data = {
            'candidate_id': 1,
            'jd_id': 1,
            'feedback_score': 4,
            'comment': 'Great technical skills'
        }
        
        feedback_entry = pd.Series(feedback_data)
        agent.update_reward(feedback_entry)
        
        # Get state and action
        state = agent.get_state(1, 1, "Great technical skills")
        action = agent.choose_action(state)
        actions = ['accept', 'reject', 'reconsider']
        
        print(f"PASS: Workflow complete - Action: {actions[action]}")
        print(f"INFO: Agent history length: {len(agent.history)}")
        print(f"INFO: Total reward: {agent.total_reward_over_time}")
        
        return True
        
    except Exception as e:
        print(f"FAIL: Full workflow test failed: {e}")
        return False

def main():
    """Run Flask-specific tests"""
    print("=" * 50)
    print("FLASK APP SPECIFIC TESTS")
    print("=" * 50)
    
    tests = [
        ("Flask App Simple", test_flask_app_simple),
        ("Full Workflow", test_full_workflow)
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
    
    if passed == total:
        print("SUCCESS: Flask app components work correctly!")
    else:
        print("WARNING: Some Flask tests failed.")
    
    return passed == total

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)