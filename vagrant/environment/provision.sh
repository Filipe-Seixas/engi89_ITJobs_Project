#!/bin/bash

 #updating python3 and installing required packages
sudo apt-get update -y
sudo apt-get install software-properties-common -y
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt-get update -y
sudo apt-get install build-essential libpq-dev libssl-dev openssl libffi-dev zlib1g-dev -y
sudo apt-get install python3-pip python3-dev python3.7-venv python3.7-gdbm -y
sudo apt-get install python3.7 -y
sudo apt-get install dos2unix -y
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.7 1
sudo update-alternatives --config python3
python3 -m pip install --upgrade pip
python3 -m pip install requests
python3 -m pip install bs4
sudo apt-get upgrade -y
sudo apt-get install nginx -y
sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv D68FA50FEA312927
sudo apt-get install python-software-properties -y

 #copying app into a easier to manage location to avoid errors
mkdir /home/vagrant/flask_app/
sudo cp -r /opt/vagrant/flask_app/* /home/vagrant/flask_app/

 #moving over the bash script to finish the setup along with creating the virtual environment
sudo cp /opt/vagrant/environment/finish_setup.sh /home/vagrant/
cd /home/vagrant/
sudo chmod +x finish_setup.sh
sudo dos2unix finish_setup.sh
python3 -m venv flask_venv

 #run this right after logging in
#sudo ./finish_setup.sh

 #for testing
	#cd /home/vagrant/flask_app
	#gunicorn --bind 0.0.0.0:8000 --workers 5 main:flask_app
	#http://192.168.10.120:8000
