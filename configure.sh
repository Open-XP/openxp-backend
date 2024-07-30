#!/bin/bash

# Update and upgrade the system
sudo apt-get update
sudo apt-get upgrade --y

# Install Node.js
curl -fsSL https://deb.nodesource.com/setup_16.x | sudo -E bash -
sudo apt install -y nodejs


# Install Python 3.8 and pip
sudo apt-get install python3.8-dev

# Install gcc and uwsgi
sudo apt-get install gcc -y

# Install nginx
sudo apt-get install nginx -y

# Install pip and uwsgi
sudo apt install python3-pip -y
pip install uwsgi

sudo apt-get install pkg-config -y
sudo apt-get install libmariadb-dev -y
sudo apt-get install libmysqlclient-dev -y



# Create Virtual Enivronment
sudo apt-get install python3-venv -y
python3 -m venv /home/ubuntu/openxp-backend/env

# Activate the virtual environment
source /home/ubuntu/openxp-backend/env/bin/activate

# Install the required Python packages
pip install -r /home/ubuntu/openxp-backend/u_requirements.txt

# Creating a directory for md directory and vassals subdirectory
mkdir -p /home/ubuntu/openxp-backend/env/md/vassals

# Creating a symlink to the vassals directory
ln -s /home/ubuntu/openxp-backend/openxp_uwsgi.ini /home/ubuntu/openxp-backend/env/md/vassals/

# Creating a symlink to the nginx directory
sudo ln -s /home/ubuntu/openxp-backend/openxp.conf /etc/nginx/sites-enabled/
sudo ln -s /home/ubuntu/openxp-backend/openxp.conf /etc/nginx/sites-available/

# Test the nginx configuration
sudo nginx -t

# Restart the nginx service
sudo systemctl restart nginx

# Creating a symlink to the uwsgi emperor service
sudo ln -s /home/ubuntu/openxp-backend/emperor.uwsgi.service /etc/systemd/system/

# Reload the systemd daemon
sudo systemctl daemon-reload

# Start the uwsgi emperor service
sudo systemctl start emperor.uwsgi.service