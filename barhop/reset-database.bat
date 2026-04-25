@echo off
(FOR /d /r . %%d IN (migrations) DO @IF EXIST "%%d" rd /s /q "%%d") &&^
echo Begin reset database. && echo Recreating database... &&^
mysql -u afterhoursco -p -e "DROP DATABASE IF EXISTS barhop; CREATE DATABASE barhop;" ||^
pause && exit &^
echo Database created successfully. Making migrations... &&^
..\venv\scripts\activate &&^
python manage.py makemigrations user_management bars reservations reviews &&^
python manage.py migrate && python manage.py createsuperuser --no-input && deactivate &&^
echo Migrations successful. Begin populating data. &&^
echo Please login to the MySQL AfterHoursCo account. &&^
mysql -u afterhoursco -p barhop < barhop_data.sql ||^
pause && exit &^
echo Database setup complete. && pause