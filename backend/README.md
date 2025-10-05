# HabitGarden Backend

This is the backend API for HabitGarden, a habit tracking application with gamification features.

## Tech Stack

- **Framework**: Express.js
- **Database**: Supabase (PostgreSQL) with Drizzle ORM
- **Authentication**: Supabase Auth (JWT)
- **Language**: TypeScript

## Project Structure

```
src/
├── app.ts                 # Application entry point
├── config/                # Configuration files
│   ├── env.ts             # Environment variables validation
│   ├── supabase.ts        # Supabase client configuration
├── db/                    # Database related files
│   ├── drizzle.config.ts  # Drizzle ORM configuration
│   ├── schema/            # Database schema definitions
│   ├── index.ts           # Database connection
├── modules/               # Feature modules
│   ├── auth/              # Authentication module
│   ├── habits/            # Habits module
│   ├── streaks/           # Streaks module
│   ├── progress/          # Progress module
├── middleware/            # Custom middleware
│   ├── auth.middleware.ts # JWT authentication middleware
│   ├── errorHandler.ts    # Global error handling
├── utils/                 # Utility functions
│   ├── logger.ts          # Logging utility
│   ├── response.ts        # Standardized response format
```

## Setup

1. Copy `.env.example` to `.env` and fill in your values:
   ```bash
   cp .env.example .env
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Run the development server:
   ```bash
   npm run dev
   ```

## Supabase Setup

To run this backend, you'll need to set up a Supabase project:

1. Go to [Supabase](https://supabase.com/) and create a new project
2. Once your project is created, navigate to the Project Settings
3. In the API section, you'll find:
   - `SUPABASE_URL`: Your project URL
   - `SUPABASE_ANON_KEY`: The public anon key
   - `SUPABASE_SERVICE_ROLE_KEY`: The service role key (keep this secret!)
4. For the `DATABASE_URL`, you can find it in the Database section under Connection String

Update your `.env` file with these values:
```env
NODE_ENV=development
PORT=8080
SUPABASE_URL=your_actual_supabase_project_url
SUPABASE_SERVICE_ROLE_KEY=your_actual_service_role_key
SUPABASE_ANON_KEY=your_actual_anon_key
DATABASE_URL=your_actual_postgres_connection_string
```

## Security

### Row Level Security (RLS)

This application implements Row Level Security (RLS) on all database tables to ensure that users can only access their own data. The following policies are enforced:

- **Users table**: Users can only view, insert, and update their own user data
- **Habits table**: Users can only view, insert, update, and delete their own habits
- **Progress table**: Users can only view, insert, update, and delete their own progress records
- **Streaks table**: Users can only view, insert, update, and delete their own streak records

All policies use the `auth.uid()` function to verify that the authenticated user ID matches the user ID associated with the data.

## Available Scripts

- `npm run build` - Compile TypeScript to JavaScript
- `npm run start` - Start the production server
- `npm run dev` - Start the development server with hot reloading
- `npm run migrate` - Run database migrations
- `npm run studio` - Open Drizzle Studio for database management

## API Endpoints

### Habits
- `POST /habits` - Create a new habit
- `GET /habits` - Get all user habits
- `GET /habits/:id` - Get a specific habit
- `PUT /habits/:id` - Update a habit
- `DELETE /habits/:id` - Delete a habit

### Streaks
- `POST /streaks/:habitId/check` - Mark habit as done today
- `GET /streaks/:habitId` - Get streak data
- `PUT /streaks/:habitId` - Reset streak

### Progress
- `GET /progress/:habitId` - Get habit progress heatmap
- `POST /progress/:habitId` - Mark specific date as complete
- `DELETE /progress/:habitId/:date` - Unmark specific date

## Environment Variables

- `NODE_ENV` - Environment (development/production)
- `PORT` - Server port
- `SUPABASE_URL` - Supabase project URL
- `SUPABASE_SERVICE_ROLE_KEY` - Supabase service role key (server-side operations)
- `SUPABASE_ANON_KEY` - Supabase anonymous key (client-side operations)
- `DATABASE_URL` - PostgreSQL connection string