@echo off
REM HabitTracker Backend API Test Script for Windows
REM This script tests the HabitTracker backend API endpoints using curl

set BASE_URL=http://localhost:8080
set TOKEN=

echo ==================================================
echo HabitTracker Backend API Test Script (Windows)
echo ==================================================
echo Base URL: %BASE_URL%
echo.

REM Function to make GET requests
:GET_REQUEST
set ENDPOINT=%1
set AUTH_REQUIRED=%2
echo Testing GET %ENDPOINT%

if "%AUTH_REQUIRED%"=="true" (
    if defined TOKEN (
        curl -s -X GET "%BASE_URL%%ENDPOINT%" -H "Authorization: Bearer %TOKEN%" -H "Content-Type: application/json" | jq .
    ) else (
        curl -s -X GET "%BASE_URL%%ENDPOINT%" -H "Content-Type: application/json" | jq .
    )
) else (
    curl -s -X GET "%BASE_URL%%ENDPOINT%" -H "Content-Type: application/json" | jq .
)
echo.
goto :eof

REM Function to make POST requests
:POST_REQUEST
set ENDPOINT=%1
set DATA=%2
set AUTH_REQUIRED=%3
echo Testing POST %ENDPOINT%

if "%AUTH_REQUIRED%"=="true" (
    if defined TOKEN (
        curl -s -X POST "%BASE_URL%%ENDPOINT%" -H "Authorization: Bearer %TOKEN%" -H "Content-Type: application/json" -d "%DATA%" | jq .
    ) else (
        curl -s -X POST "%BASE_URL%%ENDPOINT%" -H "Content-Type: application/json" -d "%DATA%" | jq .
    )
) else (
    curl -s -X POST "%BASE_URL%%ENDPOINT%" -H "Content-Type: application/json" -d "%DATA%" | jq .
)
echo.
goto :eof

REM 1. Health Check
echo 1. Testing Health Check Endpoint
call :GET_REQUEST "/health" "false"

REM 2. JWT Debug Endpoint (skipped - requires valid token)
echo 2. JWT Debug Endpoint (skipped - requires valid token)
echo To test JWT: curl -X POST %BASE_URL%/debug-jwt -H "Authorization: Bearer YOUR_TOKEN"
echo.

REM 3. Habit Endpoints (will fail without auth)
echo 3. Testing Habit Endpoints (will fail without auth)
call :GET_REQUEST "/habits" "true"

REM 4. Streak Endpoints (will fail without auth)
echo 4. Testing Streak Endpoints (will fail without auth)
call :GET_REQUEST "/streaks/1" "true"

REM 5. Progress Endpoints (will fail without auth)
echo 5. Testing Progress Endpoints (will fail without auth)
call :GET_REQUEST "/progress/1" "true"

echo ==================================================
echo Test Script Complete
echo ==================================================
echo.
echo Note: Most endpoints require authentication with a valid JWT token.
echo To properly test authenticated endpoints:
echo 1. Start the backend server: npm run dev (in backend directory)
echo 2. Obtain a valid JWT token from the frontend or Supabase
echo 3. Set the TOKEN variable in this script
echo 4. Uncomment the authenticated tests below
echo.

REM Template for authenticated requests (uncomment and modify when you have a token)
REM set TOKEN=your-jwt-token-here
REM call :POST_REQUEST "/habits" "{\"name\":\"Test Habit\",\"description\":\"A test habit\",\"frequency\":\"daily\"}" "true"
REM call :GET_REQUEST "/habits" "true"