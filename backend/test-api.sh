#!/bin/bash

# Backend API Test Script
# This script tests the HabitTracker backend API endpoints

# Configuration
BASE_URL="http://localhost:8080"
TOKEN=""  # Will be set after authentication

echo "=== HabitTracker Backend API Test Script ==="
echo "Base URL: $BASE_URL"
echo

# Function to make API calls
make_request() {
    local method=$1
    local endpoint=$2
    local data=$3
    local auth_required=$4
    
    local url="$BASE_URL$endpoint"
    local headers=""
    
    # Add authorization header if required
    if [[ "$auth_required" == "true" && -n "$TOKEN" ]]; then
        headers="-H 'Authorization: Bearer $TOKEN'"
    fi
    
    # Add content-type header for POST/PUT requests with data
    if [[ -n "$data" ]]; then
        headers="$headers -H 'Content-Type: application/json'"
    fi
    
    echo "Making $method request to $endpoint"
    
    if [[ -n "$data" ]]; then
        curl -s -X "$method" "$url" $headers -d "$data" | jq .
    else
        curl -s -X "$method" "$url" $headers | jq .
    fi
    
    echo
}

# 1. Health Check
echo "1. Testing Health Check Endpoint"
make_request "GET" "/health" "" "false"

# 2. JWT Debug (if you have a token)
echo "2. JWT Debug Endpoint (skipping - requires valid token)"
echo "To test JWT: curl -X POST $BASE_URL/debug-jwt -H 'Authorization: Bearer YOUR_TOKEN'"
echo

# 3. Habit Endpoints (will fail without auth)
echo "3. Testing Habit Endpoints (will fail without auth)"
make_request "GET" "/habits" "" "true"

# 4. Streak Endpoints (will fail without auth)
echo "4. Testing Streak Endpoints (will fail without auth)"
make_request "GET" "/streaks/1" "" "true"

# 5. Progress Endpoints (will fail without auth)
echo "5. Testing Progress Endpoints (will fail without auth)"
make_request "GET" "/progress/1" "" "true"

echo "=== Test Script Complete ==="
echo
echo "Note: Most endpoints require authentication with a valid JWT token."
echo "To properly test authenticated endpoints:"
echo "1. Start the backend server: npm run dev (in backend directory)"
echo "2. Obtain a valid JWT token from the frontend or Supabase"
echo "3. Set the TOKEN variable in this script"
echo "4. Uncomment the authenticated tests below"
echo

# Template for authenticated requests (uncomment and modify when you have a token)
# TOKEN="your-jwt-token-here"
# make_request "POST" "/habits" '{"name":"Test Habit","description":"A test habit","frequency":"daily"}' "true"
# make_request "GET" "/habits" "" "true"
# make_request "POST" "/progress/1" "" "true"
# make_request "GET" "/streaks/1" "" "true"