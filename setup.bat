@echo off
echo ========================================
echo ELocate Setup Script
echo ========================================
echo.

echo Installing dependencies...
pip install -r requirements.txt
echo.

echo Running migrations...
python manage.py makemigrations
python manage.py migrate
echo.

echo ========================================
echo Setup Complete!
echo ========================================
echo.
echo Next steps:
echo 1. Create admin user: python manage.py createsuperuser
echo 2. Run server: python manage.py runserver
echo 3. Visit: http://127.0.0.1:8000/
echo.
pause
