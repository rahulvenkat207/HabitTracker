# HabitTracker Backend API Testing

This directory contains several scripts to test the HabitTracker backend API endpoints.

## Available Test Scripts

### 1. test-api.sh (Bash Script)
A shell script for Unix/Linux/MacOS systems that tests the API endpoints.

### 2. test-api.bat (Batch Script)
A Windows batch script that tests the API endpoints using curl.

### 3. test_api.py (Python Script)
A comprehensive Python script that provides detailed testing of the API endpoints.

## Prerequisites

1. The backend server must be running:
   ```bash
   cd backend
   npm run dev
   ```

2. For authenticated endpoints, you'll need a valid JWT token from Supabase.

## API Endpoints

### Public Endpoints
- `GET /health` - Health check endpoint

### Authenticated Endpoints (Require JWT token)
- `GET /habits` - Get all habits for the user
- `POST /habits` - Create a new habit
- `GET /habits/:id` - Get a specific habit
- `PUT /habits/:id` - Update a specific habit
- `DELETE /habits/:id` - Delete a specific habit

- `GET /streaks/:habitId` - Get streak information for a habit
- `POST /streaks/:habitId/check` - Check/update streak for a habit
- `GET /streaks/:habitId/history` - Get streak history for a habit
- `PUT /streaks/:habitId` - Reset streak for a habit

- `GET /progress/:habitId` - Get progress for a habit
- `POST /progress/:habitId` - Mark progress for today
- `DELETE /progress/:habitId/:date` - Unmark progress for a specific date
- `GET /progress/:habitId/range` - Get progress for a date range

## Using the Test Scripts

### Bash Script (Unix/Linux/MacOS)
```bash
cd backend
chmod +x test-api.sh
./test-api.sh
```

### Windows Batch Script
```cmd
cd backend
test-api.bat
```

### Python Script
```bash
cd backend
python test_api.py
```

## Authentication

Most endpoints require authentication with a JWT token. To test authenticated endpoints:

1. Obtain a valid JWT token from the frontend application or Supabase
2. For the bash script, set the TOKEN variable in the script
3. For the batch script, set the TOKEN variable in the script
4. For the Python script, use the `set_token()` method

## Example with Authentication (Python)

```python
tester = HabitTrackerAPITester()
token = "your-valid-jwt-token"
tester.set_token(token)
tester.run_all_tests()
```