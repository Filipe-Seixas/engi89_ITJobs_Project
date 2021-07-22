#!/bin/bash

 #setting env variables for Flask, first 2 lines for now and the next 2 lines for next logins
 #actually not needed to get the whole thing working but was needed when doing "flask run"
export FLASK_APP=main.py
export FLASK_RUN_HOST=0.0.0.0
echo "export FLASK_APP=main.py" >> ~/.profile
echo "export FLASK_RUN_HOST=0.0.0.0" >> ~/.profile

 #go into venv and install flask and gunicorn
source flask_venv/bin/activate
sudo /home/vagrant/flask_venv/bin/python3 -m pip install --upgrade pip
sudo pip install flask gunicorn
deactivate

 #adding permissions
sudo chmod a+rwx /home/vagrant/flask_app
sudo chmod a+rwx /usr/local/bin/gunicorn

 #setting the systemd file
sudo cp /opt/vagrant/environment/flask_app.service /etc/systemd/system/
sudo systemctl start flask_app
sudo systemctl enable flask_app

 #set up reverse proxy
sudo rm -rf /etc/nginx/sites-available/default
sudo cp /opt/vagrant/environment/default /etc/nginx/sites-available/
sudo systemctl restart nginx
sudo ufw allow 'Nginx Full'

echo "COMPLETE - Enter the machine's IP adress into your web browser"
