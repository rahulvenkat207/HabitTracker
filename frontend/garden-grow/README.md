# HabitGarden Frontend

Frontend for HabitGarden - A habit tracking application with gamification

## Technologies Used

- React with TypeScript
- Vite
- TailwindCSS
- Shadcn/ui components
- Supabase for Authentication
- React Router for navigation
- Zustand for state management

## Setup

1. Clone the repository
2. Navigate to the frontend directory: `cd frontend/garden-grow`
3. Install dependencies: `npm install`
4. Copy `.env.example` to `.env` and fill in the values
5. Start the development server: `npm run dev`

## Scripts

- `npm run dev` - Start the development server
- `npm run build` - Build the production version
- `npm run build:dev` - Build the development version
- `npm run lint` - Run ESLint
- `npm run preview` - Preview the production build locally

## Environment Variables

Create a `.env` file in the frontend directory with the following variables:

```
VITE_SUPABASE_URL=your_supabase_project_url
VITE_SUPABASE_ANON_KEY=your_supabase_anon_key
VITE_API_URL=http://localhost:8080
```

## Deployment

### Render Deployment (Frontend Only)

1. Fork this repository to your GitHub account
2. Create a new Static Site on Render
3. Connect your forked repository
4. Set the root directory to `frontend/garden-grow`
5. Render will automatically detect the service from `render.yaml`
6. Add the required environment variables:
   - `VITE_SUPABASE_URL`: your Supabase project URL
   - `VITE_SUPABASE_ANON_KEY`: your Supabase anonymous key
   - `VITE_API_URL`: your backend API URL (e.g., https://your-backend-service.onrender.com)
7. Click "Create Static Site"

The application will automatically deploy and restart on every push to the main branch.

### Manual Render Configuration

If you prefer to configure manually instead of using the `render.yaml` file:

1. Fork this repository to your GitHub account
2. Create a new Static Site on Render
3. Connect your forked repository
4. Set the root directory to `frontend/garden-grow`
5. Set the build command to: `npm install && npm run build`
6. Set the publish directory to: `dist`
7. Add the required environment variables:
   - `VITE_SUPABASE_URL`: your Supabase project URL
   - `VITE_SUPABASE_ANON_KEY`: your Supabase anonymous key
   - `VITE_API_URL`: your backend API URL (e.g., https://your-backend-service.onrender.com)
8. Click "Create Static Site"

### Vercel Deployment

1. Fork this repository to your GitHub account
2. Create a new project on Vercel
3. Connect your forked repository
4. Set the root directory to `frontend/garden-grow`
5. Vercel will automatically detect the Vite project
6. Add the required environment variables in the Vercel dashboard
7. The application will automatically deploy on every push to the main branch

## Project Structure

- `src/components` - React components
- `src/pages` - Page components
- `src/hooks` - Custom React hooks
- `src/lib` - Utility functions and API services
- `src/state` - Application state management
- `src/App.tsx` - Main application component
- `src/main.tsx` - Application entry point

## Features

- User authentication (sign up, sign in, sign out)
- Habit creation and management
- Progress tracking with calendar heatmap
- Streak tracking and visualization
- Responsive design for mobile and desktop
- Dark mode support