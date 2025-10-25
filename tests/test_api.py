#!/usr/bin/env python3
"""
API Test Script for HR AI System
Tests Flask endpoints with real HTTP requests
"""

import requests
import json
import time
import sys

def test_api_endpoints():
    """Test Flask API endpoints"""
    base_url = "http://localhost:5000"
    
    print("Testing HR AI System API Endpoints")
    print("=" * 50)
    
    # Test 1: Health Check
    print("1. Testing Health Check Endpoint...")
    try:
        response = requests.get(f"{base_url}/", timeout=5)
        if response.status_code == 200:
            print(f"   PASS: Health check successful")
            print(f"   Response: {response.text}")
        else:
            print(f"   FAIL: Health check failed ({response.status_code})")
            return False
    except requests.exceptions.RequestException as e:
        print(f"   FAIL: Cannot connect to server - {e}")
        print("   Make sure Flask app is running: python app.py")
        return False
    
    # Test 2: Feedback Submission
    print("\n2. Testing Feedback Submission...")
    test_feedback = {
        "candidate_id": 1,
        "jd_id": 1,
        "feedback_score": 4,
        "comment": "Excellent technical skills and good communication"
    }
    
    try:
        response = requests.post(
            f"{base_url}/update_feedback",
            json=test_feedback,
            headers={"Content-Type": "application/json"},
            timeout=10
        )
        
        if response.status_code == 200:
            print("   PASS: Feedback submission successful")
            result = response.json()
            print(f"   Status: {result.get('status')}")
            print(f"   Policy Change: {result.get('rl_policy_change')}")
            print(f"   Summary: {result.get('feedback_summary')}")
        else:
            print(f"   FAIL: Feedback submission failed ({response.status_code})")
            print(f"   Response: {response.text}")
            return False
    except requests.exceptions.RequestException as e:
        print(f"   FAIL: Request failed - {e}")
        return False
    
    # Test 3: Multiple Feedback Submissions
    print("\n3. Testing Multiple Feedback Submissions...")
    test_cases = [
        {"candidate_id": 2, "jd_id": 2, "feedback_score": 5, "comment": "Perfect match for ML Engineer role"},
        {"candidate_id": 3, "jd_id": 1, "feedback_score": 2, "comment": "Lacks required data science experience"},
        {"candidate_id": 4, "jd_id": 3, "feedback_score": 3, "comment": "Good frontend skills but needs backend experience"}
    ]
    
    for i, test_case in enumerate(test_cases, 1):
        try:
            response = requests.post(
                f"{base_url}/update_feedback",
                json=test_case,
                headers={"Content-Type": "application/json"},
                timeout=10
            )
            
            if response.status_code == 200:
                result = response.json()
                print(f"   Test {i} PASS: Candidate {test_case['candidate_id']} -> {result.get('rl_policy_change', 'No policy')}")
            else:
                print(f"   Test {i} FAIL: Status {response.status_code}")
                return False
                
        except requests.exceptions.RequestException as e:
            print(f"   Test {i} FAIL: {e}")
            return False
    
    # Test 4: Error Handling
    print("\n4. Testing Error Handling...")
    invalid_data = {"candidate_id": 1}  # Missing required fields
    
    try:
        response = requests.post(
            f"{base_url}/update_feedback",
            json=invalid_data,
            headers={"Content-Type": "application/json"},
            timeout=5
        )
        
        if response.status_code == 400:
            print("   PASS: Error handling works correctly")
            result = response.json()
            print(f"   Error message: {result.get('message')}")
        else:
            print(f"   FAIL: Expected 400 error, got {response.status_code}")
            return False
    except requests.exceptions.RequestException as e:
        print(f"   FAIL: Request failed - {e}")
        return False
    
    print("\n" + "=" * 50)
    print("API TEST SUMMARY: ALL TESTS PASSED!")
    print("Your HR AI System API is working correctly.")
    return True

def main():
    """Main test function"""
    print("HR AI System - API Test Suite")
    print("Make sure the Flask app is running before starting tests")
    print("Start Flask app with: python app.py")
    print("\nPress Enter to continue with tests or Ctrl+C to exit...")
    
    try:
        input()
    except KeyboardInterrupt:
        print("\nTests cancelled by user.")
        sys.exit(0)
    
    success = test_api_endpoints()
    
    if success:
        print("\n🎉 All API tests passed! Your system is ready for production.")
    else:
        print("\n⚠️ Some tests failed. Check the Flask app and try again.")
    
    return success

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)