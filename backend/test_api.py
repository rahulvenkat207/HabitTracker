#!/usr/bin/env python3
"""
HabitTracker Backend API Test Script

This script provides a comprehensive test suite for the HabitTracker backend API.
It tests all available endpoints and handles authentication where needed.
"""

import requests
import json
import os
from typing import Optional

class HabitTrackerAPITester:
    def __init__(self, base_url: str = "http://localhost:8080"):
        self.base_url = base_url
        self.session = requests.Session()
        self.token: Optional[str] = None
        
    def set_token(self, token: str):
        """Set the JWT token for authenticated requests"""
        self.token = token
        self.session.headers.update({'Authorization': f'Bearer {token}'})
        
    def make_request(self, method: str, endpoint: str, data: Optional[dict] = None):
        """Make an HTTP request to the API"""
        url = f"{self.base_url}{endpoint}"
        headers = {'Content-Type': 'application/json'} if data else {}
        
        try:
            if method.upper() == "GET":
                response = self.session.get(url, headers=headers)
            elif method.upper() == "POST":
                response = self.session.post(url, json=data, headers=headers)
            elif method.upper() == "PUT":
                response = self.session.put(url, json=data, headers=headers)
            elif method.upper() == "DELETE":
                response = self.session.delete(url, headers=headers)
            else:
                raise ValueError(f"Unsupported HTTP method: {method}")
                
            return response
        except requests.exceptions.RequestException as e:
            print(f"Error making request to {url}: {e}")
            return None
            
    def test_health_check(self):
        """Test the health check endpoint"""
        print("Testing Health Check Endpoint...")
        response = self.make_request("GET", "/health")
        if response:
            print(f"Status Code: {response.status_code}")
            print(f"Response: {response.json()}")
        print()
        
    def test_jwt_debug(self, token: str):
        """Test the JWT debug endpoint"""
        print("Testing JWT Debug Endpoint...")
        # This endpoint requires a token in the Authorization header
        headers = {'Authorization': f'Bearer {token}'}
        try:
            response = requests.post(f"{self.base_url}/debug-jwt", headers=headers)
            print(f"Status Code: {response.status_code}")
            print(f"Response: {response.json()}")
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
        print()
        
    def test_habit_endpoints(self):
        """Test habit-related endpoints"""
        print("Testing Habit Endpoints...")
        
        # Get habits (requires auth)
        print("1. Getting all habits...")
        response = self.make_request("GET", "/habits")
        if response:
            print(f"Status Code: {response.status_code}")
            if response.status_code == 200:
                print(f"Response: {response.json()}")
            else:
                print(f"Error: {response.text}")
        
        # Try to create a habit (requires auth)
        print("\n2. Creating a new habit...")
        habit_data = {
            "name": "Test Habit",
            "description": "A test habit for API testing",
            "frequency": "daily"
        }
        response = self.make_request("POST", "/habits", habit_data)
        if response:
            print(f"Status Code: {response.status_code}")
            if response.status_code == 201:
                print(f"Created Habit: {response.json()}")
            else:
                print(f"Error: {response.text}")
        print()
        
    def test_streak_endpoints(self):
        """Test streak-related endpoints"""
        print("Testing Streak Endpoints...")
        
        # Get streak for habit ID 1 (requires auth)
        print("1. Getting streak for habit ID 1...")
        response = self.make_request("GET", "/streaks/1")
        if response:
            print(f"Status Code: {response.status_code}")
            if response.status_code == 200:
                print(f"Response: {response.json()}")
            else:
                print(f"Error: {response.text}")
        print()
        
    def test_progress_endpoints(self):
        """Test progress-related endpoints"""
        print("Testing Progress Endpoints...")
        
        # Get progress for habit ID 1 (requires auth)
        print("1. Getting progress for habit ID 1...")
        response = self.make_request("GET", "/progress/1")
        if response:
            print(f"Status Code: {response.status_code}")
            if response.status_code == 200:
                print(f"Response: {response.json()}")
            else:
                print(f"Error: {response.text}")
        print()
        
    def run_all_tests(self):
        """Run all API tests"""
        print("=" * 50)
        print("HabitTracker Backend API Test Suite")
        print("=" * 50)
        print(f"Base URL: {self.base_url}")
        print()
        
        # Test health check (no auth required)
        self.test_health_check()
        
        # Test habit endpoints (will fail without auth)
        self.test_habit_endpoints()
        
        # Test streak endpoints (will fail without auth)
        self.test_streak_endpoints()
        
        # Test progress endpoints (will fail without auth)
        self.test_progress_endpoints()
        
        print("=" * 50)
        print("Test Suite Complete")
        print("=" * 50)
        print()
        print("Note: Most endpoints require authentication.")
        print("To run authenticated tests:")
        print("1. Set a valid JWT token using set_token()")
        print("2. Re-run the tests")

def main():
    # Initialize the API tester
    tester = HabitTrackerAPITester()
    
    # Run all tests
    tester.run_all_tests()
    
    # Example of how to test with authentication:
    # token = "your-jwt-token-here"
    # tester.set_token(token)
    # tester.run_all_tests()

if __name__ == "__main__":
    main()