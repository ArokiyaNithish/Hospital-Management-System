@echo off
cd /d "%~dp0"
call venv\Scripts\activate
echo Running migrations...
python manage.py makemigrations
python manage.py migrate
echo.
echo Creating Superuser...
python manage.py createsuperuser
pause
