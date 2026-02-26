
@echo off
(FOR /d /r . %%d IN (migrations) DO @IF EXIST "%%d" rd /s /q "%%d") &&^
echo Begin reset database. && echo Recreating database... &&^
mysql -u afterhoursco -p -e "DROP DATABASE IF EXISTS barhop; CREATE DATABASE barhop;" ||^
pause && exit &^
echo Database created successfully. Making migrations... &&^
..\venv\scripts\activate &&^
python manage.py makemigrations bars reservations reviews user_management &&^
python manage.py migrate && python manage.py createsuperuser --no-input && deactivate &&^
echo Migrations successful. && pause