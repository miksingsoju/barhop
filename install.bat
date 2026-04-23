@echo off
echo Begin installation. Please login to your MySQL root account. &&^
mysql -u root -p -e "DROP DATABASE IF EXISTS BARHOP; CREATE DATABASE barhop; DROP USER IF EXISTS 'afterhoursco'@'%%'; CREATE USER 'afterhoursco'@'%%' IDENTIFIED BY 'password'; GRANT ALL PRIVILEGES ON barhop.* TO 'afterhoursco'@'%';" ||^
pause && exit &^
echo MySQL Database setup successful. Installing packages... &&^
python -m venv venv && cd barhop &&^
..\venv\scripts\activate && pip install -r requirements.txt &&^
echo Python environment setup successful. Making migrations... &&^
python manage.py makemigrations user_management bars reservations reviews && python manage.py migrate &&^
echo Migrations successful. Creating Superuser... &&^
python manage.py createsuperuser --no-input && deactivate &&^
echo Migrations successful. Begin populating data. &&^
echo Please login to the MySQL AfterHoursCo account. &&^
mysql -u afterhoursco -p barhop < barhop_data.sql ||^
pause && exit &^
echo Installation successful. && pause