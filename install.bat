@echo off
echo Begin installation. &&^
mysql -u root -p -e "DROP DATABASE IF EXISTS BARHOP; CREATE DATABASE barhop; DROP USER IF EXISTS 'afterhoursco'@'%%'; CREATE USER 'afterhoursco'@'%%' IDENTIFIED BY 'password'; GRANT ALL PRIVILEGES ON barhop.* TO 'afterhoursco'@'%';" ||^
pause && exit &^
echo MySQL Database setup successful. Installing packages... &&^
python -m venv venv && cd barhop &&^
..\venv\scripts\activate && pip install -r requirements.txt &&^
echo Python environment setup successful. Making migrations... &&^
python manage.py makemigrations && python manage.py migrate &&^
echo Migrations successful. Creating Superuser... &&^
python manage.py createsuperuser --no-input && deactivate &&^
echo Installation successful. && pause