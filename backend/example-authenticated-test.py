#!/usr/bin/env python3
"""
Example of how to test the HabitTracker backend API with authentication
"""

import requests
import json

# Configuration
BASE_URL = "http://localhost:8080"
# Replace this with a real JWT token from your Supabase authentication
JWT_TOKEN = "YOUR_REAL_JWT_TOKEN_HERE"

def test_with_auth():
    """Example of testing with authentication"""
    headers = {
        "Authorization": f"Bearer {JWT_TOKEN}",
        "Content-Type": "application/json"
    }
    
    print("Testing HabitTracker API with Authentication")
    print("=" * 50)
    
    # 1. Test getting habits
    print("1. Getting all habits...")
    try:
        response = requests.get(f"{BASE_URL}/habits", headers=headers)
        print(f"Status Code: {response.status_code}")
        if response.status_code == 200:
            habits = response.json()
            print(f"Found {len(habits)} habits")
            for habit in habits:
                print(f"  - {habit['name']}")
        else:
            print(f"Error: {response.text}")
    except Exception as e:
        print(f"Error: {e}")
    
    print()
    
    # 2. Test creating a habit
    print("2. Creating a new habit...")
    habit_data = {
        "name": "Test Habit from Python",
        "description": "This habit was created via Python API test",
        "frequency": "daily"
    }
    
    try:
        response = requests.post(f"{BASE_URL}/habits", headers=headers, json=habit_data)
        print(f"Status Code: {response.status_code}")
        if response.status_code == 201:
            new_habit = response.json()
            print(f"Created habit: {new_habit['name']} with ID: {new_habit['id']}")
        else:
            print(f"Error: {response.text}")
    except Exception as e:
        print(f"Error: {e}")
    
    print()
    
    # 3. Test JWT validation
    print("3. Testing JWT validation...")
    jwt_headers = {
        "Authorization": f"Bearer {JWT_TOKEN}"
    }
    
    try:
        response = requests.post(f"{BASE_URL}/test-jwt", headers=jwt_headers)
        print(f"Status Code: {response.status_code}")
        if response.status_code == 200:
            result = response.json()
            print(f"JWT Valid: {result['success']}")
            print(f"User ID: {result['user']['id']}")
        else:
            print(f"Error: {response.text}")
    except Exception as e:
        print(f"Error: {e}")

def test_without_auth():
    """Example of testing without authentication (public endpoints)"""
    print("Testing HabitTracker API without Authentication")
    print("=" * 50)
    
    # 1. Test health check
    print("1. Testing health check...")
    try:
        response = requests.get(f"{BASE_URL}/health")
        print(f"Status Code: {response.status_code}")
        if response.status_code == 200:
            health = response.json()
            print(f"Health Status: {health['status']}")
            print(f"Timestamp: {health['timestamp']}")
        else:
            print(f"Error: {response.text}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    print("HabitTracker Backend API Test Examples")
    print("=====================================")
    print()
    
    # Test public endpoints
    test_without_auth()
    print()
    
    # Test authenticated endpoints
    if JWT_TOKEN != "YOUR_REAL_JWT_TOKEN_HERE":
        test_with_auth()
    else:
        print("Skipping authenticated tests - no valid JWT token provided")
        print("To run authenticated tests:")
        print("1. Replace JWT_TOKEN with a valid token from Supabase")
        print("2. Re-run this script")