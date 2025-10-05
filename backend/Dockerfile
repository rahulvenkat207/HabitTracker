# Use Node.js 18 alpine as base image
FROM node:18-alpine

# Set working directory
WORKDIR /app

# Copy package files
COPY package*.json ./

# Install all dependencies including devDependencies for building
RUN npm install

# Copy source code
COPY . .

# Build the application
RUN npm run build

# Remove devDependencies to reduce image size
RUN npm prune --production

# Expose port (Railway will use this or override with PORT env var)
EXPOSE 8080

# Create non-root user
RUN addgroup -g 1001 -S nodejs
RUN adduser -S appuser -u 1001

# Change ownership of files to non-root user
RUN chown -R appuser:nodejs /app
USER appuser

# Start the application
CMD ["npm", "start"]