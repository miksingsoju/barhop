#!/usr/bin/env bash
set -e
echo "Begin installation."
source venv/bin/activate
echo "Python environment setup successful. Making migrations..."
pip install -r barhop/requirements.txt
sudo mysql -u root -e "DROP DATABASE IF EXISTS BARHOP; CREATE DATABASE barhop; DROP USER IF EXISTS 'afterhoursco'@'%'; CREATE USER 'afterhoursco'@'%' IDENTIFIED BY 'password'; GRANT ALL PRIVILEGES ON barhop.* TO 'afterhoursco'@'%';";
echo "MySQL Database setup successful. Installing packages..."
python3 -m venv venv 
cd barhop
python3 manage.py makemigrations
python3 manage.py migrate
echo "Migrations successful. Creating Superuser..."
python3 manage.py createsuperuser
deactivate
echo "Installation successful."