/**
 * Simple deployment test script
 * This script can be used to verify that the frontend is properly configured
 */

// Test environment variables
console.log('Testing environment variables...');

const requiredEnvVars = [
  'VITE_SUPABASE_URL',
  'VITE_SUPABASE_ANON_KEY',
  'VITE_API_URL'
];

const missingEnvVars = requiredEnvVars.filter(envVar => !import.meta.env[envVar]);

if (missingEnvVars.length > 0) {
  console.error('Missing environment variables:', missingEnvVars);
  console.error('Please set these variables in your Railway dashboard');
} else {
  console.log('All required environment variables are present');
  console.log('VITE_SUPABASE_URL:', import.meta.env.VITE_SUPABASE_URL);
  console.log('VITE_API_URL:', import.meta.env.VITE_API_URL);
}

// Test API connectivity
async function testApiConnectivity() {
  try {
    console.log('Testing API connectivity...');
    const apiUrl = import.meta.env.VITE_API_URL || 'http://localhost:8080';
    console.log('API URL:', apiUrl);
    
    // Test health endpoint (if it exists)
    const healthResponse = await fetch(`${apiUrl}/health`);
    if (healthResponse.ok) {
      const healthData = await healthResponse.json();
      console.log('API Health Check:', healthData);
    } else {
      console.log('API Health Check: Not available or requires authentication');
    }
  } catch (error) {
    console.error('API Connectivity Test Failed:', error.message);
  }
}

// Run tests
testApiConnectivity();