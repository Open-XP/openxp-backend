source env/bin/activate

python manage.py collectstatic --noinput

echo "Reloading the app service with new changes"

echo "Restarting the app service"
sudo systemctl restart emperor.uwsgi.service

echo "Restarting the nginx service"
sudo systemctl restart nginx.service

echo "App reloaded"