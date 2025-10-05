# Deploying the Frontend to Railway

This guide explains how to deploy the HabitGarden frontend to Railway.

## Prerequisites

1. A Railway account (https://railway.app/)
2. The backend already deployed to Railway
3. Supabase project set up

## Deployment Steps

### 1. Prepare Environment Variables

Before deploying, you'll need to set the following environment variables in Railway:

- `VITE_SUPABASE_URL` - Your Supabase project URL
- `VITE_SUPABASE_ANON_KEY` - Your Supabase anonymous key
- `VITE_API_URL` - Your deployed backend URL (e.g., https://rare-integrity-production.up.railway.app)

### 2. Deploy to Railway

1. Go to https://railway.app/
2. Click "New Project"
3. Select "Deploy from GitHub" or "Deploy from CLI"
4. If using GitHub:
   - Connect your GitHub account
   - Select your repository
   - Set the root directory to `frontend/garden-grow`
5. If using CLI:
   - Install the Railway CLI: `npm install -g @railway/cli`
   - Login: `railway login`
   - Initialize: `railway init` (in the frontend/garden-grow directory)
6. Railway will automatically detect the Dockerfile and build the project

### 3. Configure the Service

After deployment, configure the following in the Railway dashboard:

1. Go to your service settings
2. In the "Environment" tab, add the required environment variables:
   - `VITE_SUPABASE_URL` = your Supabase URL
   - `VITE_SUPABASE_ANON_KEY` = your Supabase anon key
   - `VITE_API_URL` = your backend URL (e.g., https://rare-integrity-production.up.railway.app)
3. In the "Settings" tab, make sure the root directory is set to `frontend/garden-grow`

### 4. Environment Variables

The frontend requires the following environment variables:

| Variable | Description | Example |
|----------|-------------|---------|
| `VITE_SUPABASE_URL` | Supabase project URL | `https://your-project.supabase.co` |
| `VITE_SUPABASE_ANON_KEY` | Supabase anonymous key | `eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...` |
| `VITE_API_URL` | Backend API URL | `https://rare-integrity-production.up.railway.app` |

### 5. Redeployment

After making changes to the frontend code:

1. Push your changes to GitHub
2. Railway will automatically redeploy the application
3. Or manually trigger a deployment in the Railway dashboard

## Configuration Details

### Dockerfile

The frontend uses a multi-stage Docker build:
1. First stage builds the React application using Node.js
2. Second stage serves the built files using Nginx

### Nginx Configuration

The nginx.conf file is configured to:
- Serve static files from the build directory
- Handle client-side routing with `try_files $uri $uri/ /index.html`
- Enable gzip compression for better performance
- Set security headers
- Cache static assets

### Railway Configuration

The railway.toml file specifies:
- Dockerfile build process
- Nginx start command
- Restart policy
- Port configuration

## Troubleshooting

### Common Issues

1. **Blank page after deployment**
   - Check that environment variables are correctly set
   - Verify the API URL is correct
   - Check the browser console for errors

2. **API calls failing**
   - Ensure the backend is deployed and running
   - Check CORS configuration on the backend
   - Verify the API URL in environment variables

3. **Environment variables not loading**
   - Make sure variables are prefixed with `VITE_`
   - Check that the variables are set in the Railway dashboard
   - Redeploy after changing environment variables

### Checking Logs

To check deployment logs:
1. Go to your Railway project
2. Select your frontend service
3. Click on the "Deployments" tab
4. Select the latest deployment to view logs

To check runtime logs:
1. Go to your Railway project
2. Select your frontend service
3. Click on the "Logs" tab