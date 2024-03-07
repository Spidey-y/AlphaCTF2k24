# Use a light Node.js base image
FROM node:alpine

# Set the working directory in the container
WORKDIR /app

# Copy package.json and package-lock.json (if available) to the container
COPY package*.json ./

# Install http-server globally
RUN npm install -g http-server

# Copy index.html and any other assets
COPY challenge/ .

# create a new user
RUN adduser -D appuser
# change to the new user
USER appuser
# Expose the port on which your app runs
EXPOSE 8001

# Command to run your app
CMD ["http-server", "-p", "8001"]
