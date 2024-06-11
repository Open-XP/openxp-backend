# Use an official Node runtime as a parent image
FROM node:16

# Set the working directory
WORKDIR /Frontend

# Copy package.json and package-lock.json
COPY package*.json ./

# Install dependencies
RUN npm install

# Bundle app source
COPY . .

# Expose port 3000
EXPOSE 3000

# Define the command to run your app
CMD ["npm", "start"]
