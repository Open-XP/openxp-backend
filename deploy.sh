#!/bin/bash

# Start the SSH agent and add the SSH key
echo "Starting SSH agent"
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/school

# Switch to the main branch
echo "Switching to branch main"
git checkout main

# Build the frontend app
echo "Building App"
cd openxp-frontend
npm run build

cd ..

# Deploy the frontend using rsync, excluding node_modules and environment variable files
echo "Deploying frontend"
rsync -avz --exclude 'node_modules' --exclude '*.env' --exclude 'build' --exclude 'venv' -e "ssh -i ~/.ssh/school -o StrictHostKeyChecking=no" ./ ubuntu@13.49.145.101:~/openxp-backend

echo "App deployed"
