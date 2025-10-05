# HabitGarden Backend

Backend for HabitGarden - A habit tracking application with gamification

## Technologies Used

- Node.js with Express
- TypeScript
- PostgreSQL with Drizzle ORM
- Supabase for Authentication
- Zod for validation

## Setup

1. Clone the repository
2. Navigate to the backend directory: `cd backend`
3. Install dependencies: `npm install`
4. Copy `.env.example` to `.env` and fill in the values
5. Run database migrations: `npm run migrate`
6. Start the development server: `npm run dev`

## Scripts

- `npm run build` - Compile TypeScript to JavaScript
- `npm start` - Start the production server
- `npm run dev` - Start the development server with auto-reload
- `npm run migrate` - Run database migrations
- `npm run studio` - Open Drizzle Studio for database management
- `npm run seed` - Seed the database with sample data
- `npm run apply-rls` - Apply Row Level Security policies

## Environment Variables

Create a `.env` file in the backend directory with the following variables:

```
NODE_ENV=development
PORT=8080
SUPABASE_URL=your_supabase_project_url
SUPABASE_SERVICE_ROLE_KEY=your_supabase_service_role_key
SUPABASE_ANON_KEY=your_supabase_anon_key
DATABASE_URL=your_postgresql_database_url
```

## Deployment

### Render Deployment (Backend Only)

1. Fork this repository to your GitHub account
2. Create a new Web Service on Render
3. Connect your forked repository
4. Set the root directory to `backend`
5. Render will automatically detect the service from `render.yaml`
6. Add the required environment variables:
   - `NODE_ENV`: production
   - `PORT`: 8080
   - `SUPABASE_URL`: your Supabase project URL
   - `SUPABASE_SERVICE_ROLE_KEY`: your Supabase service role key
   - `SUPABASE_ANON_KEY`: your Supabase anonymous key
   - `DATABASE_URL`: your PostgreSQL database URL
7. Click "Create Web Service"

The application will automatically deploy and restart on every push to the main branch.

### Manual Render Configuration

If you prefer to configure manually instead of using the `render.yaml` file:

1. Fork this repository to your GitHub account
2. Create a new Web Service on Render
3. Connect your forked repository
4. Set the root directory to `backend`
5. Set the build command to: `npm install && npm run build`
6. Set the start command to: `npm start`
7. Add the required environment variables:
   - `NODE_ENV`: production
   - `PORT`: 8080
   - `SUPABASE_URL`: your Supabase project URL
   - `SUPABASE_SERVICE_ROLE_KEY`: your Supabase service role key
   - `SUPABASE_ANON_KEY`: your Supabase anonymous key
   - `DATABASE_URL`: your PostgreSQL database URL
8. Click "Create Web Service"

### Railway Deployment

1. Fork this repository to your GitHub account
2. Create a new project on Railway
3. Connect your forked repository
4. Set the root directory to `backend`
5. Railway will automatically detect the Node.js project
6. Add the required environment variables in the Railway dashboard
7. The application will automatically deploy on every push to the main branch

## API Endpoints

- `POST /auth/signup` - Register a new user
- `POST /auth/signin` - Sign in an existing user
- `GET /habits` - Get all habits for the authenticated user
- `POST /habits` - Create a new habit
- `PUT /habits/:id` - Update an existing habit
- `DELETE /habits/:id` - Delete a habit
- `GET /progress/:habitId` - Get progress data for a habit
- `POST /progress/:habitId` - Mark progress for a habit on a specific date
- `DELETE /progress/:habitId/:date` - Unmark progress for a habit on a specific date
- `GET /streaks/:habitId` - Get streak data for a habit
- `POST /streaks/:habitId/check` - Check and update streak for a habit
- `PUT /streaks/:habitId` - Reset streak for a habit
- `POST /debug-jwt` - Debug JWT token validation
- `POST /test-jwt` - Test JWT validation with middleware
- `GET /health` - Health check endpoint

## Database Schema

The application uses PostgreSQL with the following tables:
- `users` - User information
- `habits` - Habit definitions
- `progress` - Habit progress tracking
- `streaks` - Habit streak tracking

Row Level Security (RLS) is enabled on all tables to ensure data isolation between users.