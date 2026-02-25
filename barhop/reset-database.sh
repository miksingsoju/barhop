#!/bin/bash
find . -type d -name "migrations" -exec rm -rf {} +
echo Begin reset database.
echo Recreating database... 
mysql -u afterhoursco -p -e "DROP DATABASE IF EXISTS barhop; CREATE DATABASE barhop;"
echo Database created successfully. Making migrations...
source ..\venv\scripts\activate
python3 manage.py makemigrations bars reservations reviews user_management
python3 manage.py migrate 
python3 manage.py createsuperuser 
deactivate 
echo Migrations successful.