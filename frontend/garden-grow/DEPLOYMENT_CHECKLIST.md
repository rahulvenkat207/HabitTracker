# Deployment Checklist

Use this checklist to ensure your HabitGarden frontend is properly configured for deployment to Railway.

## Pre-Deployment Checklist

### Environment Variables
- [ ] `VITE_SUPABASE_URL` is set to your Supabase project URL
- [ ] `VITE_SUPABASE_ANON_KEY` is set to your Supabase anonymous key
- [ ] `VITE_API_URL` is set to your backend URL (https://rare-integrity-production.up.railway.app)

### Code Configuration
- [ ] Dockerfile is correctly configured for multi-stage build
- [ ] nginx.conf is configured to listen on port 8080
- [ ] railway.toml is configured with correct settings
- [ ] API base URL is correctly set in api.ts

### Local Testing
- [ ] Application builds successfully with `npm run build`
- [ ] Application runs locally with `npm run preview`
- [ ] Environment variables load correctly
- [ ] API calls work correctly

## Deployment Steps

### 1. Push Code to Repository
- [ ] Commit all changes
- [ ] Push to GitHub

### 2. Configure Railway
- [ ] Create new project in Railway
- [ ] Connect GitHub repository
- [ ] Set root directory to `frontend/garden-grow`
- [ ] Set environment variables in Railway dashboard

### 3. Deploy
- [ ] Trigger deployment
- [ ] Monitor deployment logs
- [ ] Wait for deployment to complete

## Post-Deployment Verification

### Health Check
- [ ] Visit https://your-app-url.up.railway.app/health.html
- [ ] Verify all environment variables are present
- [ ] Verify API connectivity is working

### Functionality Testing
- [ ] Test user authentication (sign up, sign in, sign out)
- [ ] Test habit creation and management
- [ ] Test progress tracking
- [ ] Test streak tracking

### Error Monitoring
- [ ] Check Railway logs for errors
- [ ] Check browser console for errors
- [ ] Verify all API calls are successful

## Troubleshooting

### If You See a 502 Error
1. Check Railway deployment logs
2. Verify nginx is configured to listen on port 8080
3. Ensure environment variables are set correctly
4. Check that the Docker build completed successfully

### If Environment Variables Are Missing
1. Verify variables are set in Railway dashboard
2. Ensure variables are prefixed with `VITE_`
3. Redeploy after setting variables

### If API Calls Fail
1. Verify backend is deployed and running
2. Check CORS configuration on backend
3. Verify API URL is correct in environment variables

## Common Issues and Solutions

### Build Failures
- Check that all dependencies are listed in package.json
- Ensure build command works locally (`npm run build`)
- Check for TypeScript errors

### Nginx Configuration Issues
- Verify nginx.conf is correctly copied to container
- Ensure server is listening on correct port
- Check that static files are in correct directory

### Port Configuration
- Ensure PORT environment variable is set to 8080
- Verify nginx is configured to listen on port 8080
- Check that Dockerfile exposes port 8080

## Support Resources

- Railway Documentation: https://docs.railway.app/
- Railway Status: https://status.railway.app/
- Railway Discord: https://discord.gg/railway
- HabitGarden Documentation: [README.md](README.md)
- Deployment Troubleshooting: [DEPLOYMENT_TROUBLESHOOTING.md](DEPLOYMENT_TROUBLESHOOTING.md)