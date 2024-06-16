# Use an official Node runtime as a parent image
FROM node:16

# Set the working directory
WORKDIR /Frontend

# Copy package.json and package-lock.json
COPY package*.json ./

# Install dependencies, including 'serve' for serving the application
RUN npm install && npm install -g serve

# Bundle app source
COPY . .

# Build your application
RUN npm run build --production

# Expose the port that serve will run on
EXPOSE 3000

# Serve the build directory with serve

CMD ["serve", "-s", "build"]