#!/bin/bash

# Update and upgrade the system
sudo apt-get update
sudo apt-get upgrade -y

# Resolve conflicts by removing libmysqlclient-dev if needed
sudo apt-get remove -y libmysqlclient-dev

# Install dependencies
sudo apt-get install -y \
    curl \
    python3.10-dev \
    gcc \
    nginx \
    python3-pip \
    pkg-config \
    libmariadb-dev \
    python3.10-venv

# Install Node.js 20 LTS (since Node.js 16.x is deprecated)
curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
sudo apt-get install -y nodejs

# Verify Node.js installation
node -v
npm -v

# Create Virtual Environment
python3.10 -m venv /home/ubuntu/openxp-backend/env

# Activate the virtual environment
source /home/ubuntu/openxp-backend/env/bin/activate

# Upgrade pip, setuptools, and wheel in the virtual environment
pip install --upgrade pip setuptools wheel

# Install the required Python packages using the binary option
pip install --prefer-binary -r /home/ubuntu/openxp-backend/w_requirements.txt

# Install uwsgi within the virtual environment
pip install uwsgi

# Creating directories for md and vassals
mkdir -p /home/ubuntu/openxp-backend/env/md/vassals

# Remove existing symlink if it exists before creating a new one
if [ -L /home/ubuntu/openxp-backend/env/md/vassals/openxp_uwsgi.ini ]; then
    rm /home/ubuntu/openxp-backend/env/md/vassals/openxp_uwsgi.ini
fi
ln -s /home/ubuntu/openxp-backend/openxp_uwsgi.ini /home/ubuntu/openxp-backend/env/md/vassals/

# Create a symlink for Nginx configuration
sudo ln -s /home/ubuntu/openxp-backend/openxp.conf /etc/nginx/sites-available/

# Create a symlink from sites-available to sites-enabled
sudo ln -s /etc/nginx/sites-available/openxp.conf /etc/nginx/sites-enabled/

# Test the nginx configuration
sudo nginx -t

# Restart the nginx service
sudo systemctl restart nginx

# Remove existing symlink if it exists before creating a new one
if [ -L /etc/systemd/system/emperor.uwsgi.service ]; then
    sudo rm /etc/systemd/system/emperor.uwsgi.service
fi
sudo ln -s /home/ubuntu/openxp-backend/emperor.uwsgi.service /etc/systemd/system/

# Reload the systemd daemon
sudo systemctl daemon-reload

# Start the uwsgi emperor service
sudo systemctl start emperor.uwsgi.service

# Optionally, enable the service to start on boot
sudo systemctl enable emperor.uwsgi.service
