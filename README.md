# Installation
A click-to-install solution has been provided for convenience **(Windows only)**. Assuming you have MySQL installed correctly (open a terminal and run `mysql -V` to verify), the installation process can be simplified to the following steps:

### 1. Clone the repository
```bash
git clone https://github.com/miksingsoju/barhop.git
```

### **2. Setup Environment Variables**
Create a `.env` file (it should be beside `manage.py` in the barhop folder) with the following details.
```bash
# Django secret key
SECRET_KEY='your_secret_key_here'

# Django admin
DJANGO_SUPERUSER_USERNAME = 'afterhoursco'
DJANGO_SUPERUSER_EMAIL = 'admin@afterhoursco.com'
DJANGO_SUPERUSER_PASSWORD = 'password'

# Database connection
DB_NAME = 'barhop'
DB_USER = 'afterhoursco'
DB_PASSWORD = 'password'
DB_HOST = 'localhost'
DB_PORT = '3306'

# Debug mode (True for development, False for production)
DEBUG='True'
```

### 3. Run Install.bat
- Inside the repository folder, there should be a file `install.bat`. Simply double-click to automatically install the project.
- A terminal will pop up to prompt you for your MySQL root password.
    - Note: the terminal will exit if you enter the wrong password. If this happens, you can double-click `install.bat` again to retry.
    - Installation should begin after entering the correct password.
- If the terminal exits at any point in time, something has likely gone wrong. Contact me (Adara) for troubleshooting or proceed with Manual Installation instead.

## Manual Installation

### 1. Clone the repository
```bash
git clone https://github.com/miksingsoju/barhop.git
cd barhop
```

### **2. Make a Python Virtual Environment**
Note: for Unix-based systems, use `python3` instead for all python commands.
```bash
python -m venv venv
venv\scripts\activate
```

### **3. Install requirements.txt**
```bash
pip install -r requirements.txt
```

### **4. Setup Environment Variables**
Create a `.env` file (it should be beside `manage.py` in the barhop folder) with the following details.
```bash
# Django secret key
SECRET_KEY='your_secret_key_here'

# Django admin
DJANGO_SUPERUSER_USERNAME = 'afterhoursco'
DJANGO_SUPERUSER_EMAIL = 'admin@afterhoursco.com'
DJANGO_SUPERUSER_PASSWORD = 'password'

# Database connection
DB_NAME = 'barhop'
DB_USER = 'afterhoursco'
DB_PASSWORD = 'password'
DB_HOST = 'localhost'
DB_PORT = '3306'

# Debug mode (True for development, False for production)
DEBUG='True'
```

### 5. Setup MySQL Database
For this section, we assume you have MySQL installed, running and that you know the credentials for your root user. In a **separate terminal**, execute the following:
```bash
mysql -u root -p -e "CREATE USER 'afterhoursco'@'%' IDENTIFIED BY 'password';
CREATE DATABASE barhop; GRANT ALL PRIVILEGES ON barhop.* TO 'afterhoursco'@'%';"
```
MySQL should prompt you for your root password. Should there be no errors, you may `exit` this terminal.

### 6. Make Migrations and Create Superuser
On the original terminal (with venv running), execute the following. If the `.env` file was created properly, the following command should also automatically create a Django superuser with no input.
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser --no-input
```
<br/>

# Running the Server
Assuming the virtual environment has already been activated, the server can be started with the following:
```bash
python manage.py runserver
```
Otherwise, a simple click-to-run solution has been been provided in the form of a batch file **(Windows only)**. Simply double-click `run.bat` to start the server.<br/><br/>


# Resetting the Database
Another additional batch file to reset the database and migrations has been provided for convenience **(Windows only)**. Simply click `reset-database.bat` to rebuild an empty database from scratch. Note that when entering the password, use the one for the **afterhoursco** user.<br/><br/>


# Troubleshooting
TBA
