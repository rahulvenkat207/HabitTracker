# HabitGarden

HabitGarden is a habit tracking application with gamification features that helps users build and maintain positive habits through visualization and rewards.

## Project Structure

```
.
├── frontend/              # React + Vite frontend
│   └── garden-grow/       # Main frontend application
├── backend/               # Express.js + Supabase backend
│   ├── src/               # Source code
│   ├── drizzle/           # Database migrations
│   └── package.json       # Backend dependencies
├── docs/                  # Documentation
└── scripts/               # Utility scripts for testing and development
```

## Tech Stack

### Frontend
- **Framework**: React + Vite
- **UI Library**: Shadcn UI
- **Styling**: Tailwind CSS
- **Animations**: Framer Motion
- **State Management**: Zustand

### Backend
- **Framework**: Express.js
- **Database**: Supabase (PostgreSQL)
- **ORM**: Drizzle ORM
- **Authentication**: Supabase Auth (JWT)
- **Language**: TypeScript

## Features

- Habit tracking with customizable frequency
- Streak management and visualization
- Progress heatmap (GitHub-style)
- Garden visualization that grows with your habits
- User authentication and profiles
- Responsive design for all devices

## Setup

### Frontend

1. Navigate to the frontend directory:
   ```bash
   cd frontend/garden-grow
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Start the development server:
   ```bash
   npm run dev
   ```

### Backend

1. Navigate to the backend directory:
   ```bash
   cd backend
   ```

2. Copy `.env.example` to `.env` and fill in your values:
   ```bash
   cp .env.example .env
   ```

3. Install dependencies:
   ```bash
   npm install
   ```

4. Start the development server:
   ```bash
   npm run dev
   ```

## Development Tools

### Email Confirmation Handling

For development purposes, this project includes documentation on how to configure Supabase:

1. **Supabase Configuration**: See [Supabase Development Setup](docs/supabase-development-setup.md) for instructions on configuring email confirmation settings.

2. **Supabase No Confirmation Setup**: See [Supabase No Confirmation Setup](docs/supabase-no-confirmation-setup.md) for instructions on disabling email confirmation for development.

### API Testing

This project includes scripts to test all backend API endpoints:

1. **Curl Commands**: See [API Endpoints Documentation](docs/api-endpoints.md) for a complete list of curl commands to test each endpoint.

2. **Automated Testing Scripts**:
   - [test-api.sh](scripts/test-api.sh) - Bash script for Unix/Linux/Mac
   - [test-api.bat](scripts/test-api.bat) - Batch script for Windows

To use the testing scripts:
```bash
# Unix/Linux/Mac
cd scripts
chmod +x test-api.sh
./test-api.sh YOUR_JWT_TOKEN

# Windows
cd scripts
test-api.bat YOUR_JWT_TOKEN
```

## Available Scripts

### Frontend
- `npm run dev` - Start the development server
- `npm run build` - Build for production
- `npm run preview` - Preview the production build

### Backend
- `npm run build` - Compile TypeScript to JavaScript
- `npm run start` - Start the production server
- `npm run dev` - Start the development server with hot reloading
- `npm run migrate` - Run database migrations
- `npm run studio` - Open Drizzle Studio for database management

## Environment Variables

Both frontend and backend require environment variables to be set. Check the respective `.env.example` files in each directory for details.

## Deployment

### Separate Deployment Approach

This project is designed to deploy frontend and backend services separately, which provides more flexibility and scalability.

### Backend Deployment

Navigate to the [backend directory](file:///c:/VibeCoding_Projects/HabitTracker/backend) for detailed deployment instructions. The backend can be deployed to services like:
- Render (using the provided `render.yaml`)
- Railway
- Heroku
- Any cloud provider that supports Node.js applications

### Frontend Deployment

Navigate to the [frontend directory](file:///c:/VibeCoding_Projects/HabitTracker/frontend/garden-grow) for detailed deployment instructions. The frontend can be deployed to services like:
- Render (using the provided `render.yaml`)
- Vercel
- Netlify
- GitHub Pages
- Any static hosting service

### Render Deployment

This project includes separate `render.yaml` files for easy deployment to Render:

1. **Backend Deployment**:
   - Go to the [backend directory](file:///c:/VibeCoding_Projects/HabitTracker/backend)
   - Follow the Render deployment instructions in the backend README

2. **Frontend Deployment**:
   - Go to the [frontend/garden-grow directory](file:///c:/VibeCoding_Projects/HabitTracker/frontend/garden-grow)
   - Follow the Render deployment instructions in the frontend README

### Docker Deployment

This project includes Dockerfiles for both frontend and backend services:

1. Build the backend image:
   ```bash
   cd backend
   docker build -t habitgarden-backend .
   ```

2. Build the frontend image:
   ```bash
   cd frontend/garden-grow
   docker build -t habitgarden-frontend .
   ```

3. Run the containers:
   ```bash
   docker run -p 8080:8080 -e NODE_ENV=production -e PORT=8080 habitgarden-backend
   docker run -p 3000:80 habitgarden-frontend
   ```

Note: You'll need to provide the required environment variables when running the containers.