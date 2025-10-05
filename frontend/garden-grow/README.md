# HabitGarden Frontend

This is the frontend application for the Habit Tracker project, built with React, TypeScript, and Vite.

## Setup

1. Install dependencies:
```bash
npm install
```

2. Create a `.env` file based on `.env.example`:
```bash
cp .env.example .env
```

3. Update the `.env` file with your actual values:
- `VITE_SUPABASE_URL`: Your Supabase project URL
- `VITE_SUPABASE_ANON_KEY`: Your Supabase anonymous key
- `VITE_API_URL`: The URL of your backend API (default: http://localhost:8080)

## Development

Start the development server:
```bash
npm run dev
```

## Supabase Configuration

This frontend connects to Supabase for authentication and to the backend API for habit tracking functionality:

1. **Supabase Authentication**: Uses the Supabase JavaScript client with the anonymous key for user authentication
2. **Backend API**: Communicates with the Express backend for all habit-related operations

Note: The Supabase service role key should only be used in the backend for security reasons. The frontend only needs the anonymous key for client-side operations.

## Environment Variables

- `VITE_SUPABASE_URL`: Your Supabase project URL (e.g., https://your-project.supabase.co)
- `VITE_SUPABASE_ANON_KEY`: Your Supabase anonymous key (safe to expose in frontend)
- `VITE_API_URL`: Your backend API URL (default: http://localhost:8080)

## Project info

**URL**: https://lovable.dev/projects/ba30a417-9997-4139-aad2-ad2b994932c2

## How can I edit this code?

There are several ways of editing your application.

**Use Lovable**

Simply visit the [Lovable Project](https://lovable.dev/projects/ba30a417-9997-4139-aad2-ad2b994932c2) and start prompting.

Changes made via Lovable will be committed automatically to this repo.

**Use your preferred IDE**

If you want to work locally using your own IDE, you can clone this repo and push changes. Pushed changes will also be reflected in Lovable.

The only requirement is having Node.js & npm installed - [install with nvm](https://github.com/nvm-sh/nvm#installing-and-updating)

Follow these steps:

```sh
# Step 1: Clone the repository using the project's Git URL.
git clone <YOUR_GIT_URL>

# Step 2: Navigate to the project directory.
cd <YOUR_PROJECT_NAME>

# Step 3: Install the necessary dependencies.
npm i

# Step 4: Start the development server with auto-reloading and an instant preview.
npm run dev
```

**Edit a file directly in GitHub**

- Navigate to the desired file(s).
- Click the "Edit" button (pencil icon) at the top right of the file view.
- Make your changes and commit the changes.

**Use GitHub Codespaces**

- Navigate to the main page of your repository.
- Click on the "Code" button (green button) near the top right.
- Select the "Codespaces" tab.
- Click on "New codespace" to launch a new Codespace environment.
- Edit files directly within the Codespace and commit and push your changes once you're done.

## What technologies are used for this project?

This project is built with:

- Vite
- TypeScript
- React
- shadcn-ui
- Tailwind CSS

## How can I deploy this project?

Simply open [Lovable](https://lovable.dev/projects/ba30a417-9997-4139-aad2-ad2b994932c2) and click on Share -> Publish.

## Can I connect a custom domain to my Lovable project?

Yes, you can!

To connect a domain, navigate to Project > Settings > Domains and click Connect Domain.

Read more here: [Setting up a custom domain](https://docs.lovable.dev/features/custom-domain#custom-domain)
