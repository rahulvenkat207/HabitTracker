# Deployment Troubleshooting Guide

This guide helps you troubleshoot common issues when deploying the HabitGarden frontend to Railway.

## Common 502 Errors and Solutions

### 1. Port Configuration Issues

**Problem**: The application is not listening on the correct port.

**Solution**: 
- Ensure nginx is configured to listen on port 8080
- Set the PORT environment variable to 8080 in Railway
- Check that the Dockerfile exposes port 8080

### 2. Build Failures

**Problem**: The application fails to build during deployment.

**Solution**:
- Check the build logs in Railway for specific error messages
- Ensure all dependencies are correctly listed in package.json
- Verify that the build command (`npm run build`) works locally

### 3. Environment Variables Not Set

**Problem**: Required environment variables are missing.

**Solution**:
- In the Railway dashboard, go to your service > Settings > Environment
- Add the following variables:
  - `VITE_SUPABASE_URL` = your Supabase project URL
  - `VITE_SUPABASE_ANON_KEY` = your Supabase anonymous key
  - `VITE_API_URL` = your backend URL (e.g., https://rare-integrity-production.up.railway.app)

### 4. Health Check Endpoint

**Problem**: Railway cannot verify that the application is running.

**Solution**:
- Visit https://your-app-url.up.railway.app/health.html to verify the deployment
- This page will show you the status of environment variables and API connectivity

## Railway-Specific Troubleshooting

### Checking Deployment Logs

1. Go to your Railway project
2. Select your frontend service
3. Click on the "Deployments" tab
4. Select the latest deployment to view logs

### Checking Runtime Logs

1. Go to your Railway project
2. Select your frontend service
3. Click on the "Logs" tab

### Redeploying

1. Make changes to your code
2. Push to GitHub
3. Railway will automatically redeploy
4. Or manually trigger a deployment in the Railway dashboard

## Dockerfile Issues

### Multi-stage Build Problems

If you're having issues with the multi-stage Docker build:

1. Ensure you have enough memory allocated to Docker
2. Check that the build stage completes successfully
3. Verify that files are correctly copied between stages

### Nginx Configuration

If nginx is not serving files correctly:

1. Check that the built files are in the correct directory (`/usr/share/nginx/html`)
2. Verify the nginx configuration file is correctly copied
3. Ensure the server is listening on the correct port

## Environment Variable Issues

### Variables Not Loading

1. Make sure all environment variables are prefixed with `VITE_`
2. Check that variables are set in the Railway dashboard
3. Redeploy after changing environment variables

### API URL Issues

1. Verify that the backend URL is correct
2. Check that the backend is deployed and running
3. Ensure CORS is properly configured on the backend

## Network and Connectivity Issues

### CORS Errors

If you see CORS errors in the browser console:

1. Check that the backend has proper CORS configuration
2. Ensure the frontend URL is allowed in the backend CORS settings
3. Verify that the API URL in environment variables is correct

### API Connectivity

If the frontend cannot connect to the backend:

1. Verify the backend URL is correct
2. Check that the backend is running
3. Ensure there are no network restrictions between services

## Testing Locally

Before deploying, test locally:

1. Set environment variables in a `.env` file
2. Run `npm run build` to test the build process
3. Run `npm run preview` to test the production build

## Health Check

Visit the health check page at `/health.html` to verify:

1. Environment variables are correctly set
2. API connectivity is working
3. The application is properly deployed

## Contact Support

If you continue to have issues:

1. Check the Railway status page for service outages
2. Review the Railway documentation
3. Contact Railway support if needed