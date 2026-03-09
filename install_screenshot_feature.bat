@echo off
echo ========================================
echo Installing Screenshot Upload Feature
echo ========================================
echo.

echo Step 1: Installing Python packages...
pip install Pillow pytesseract
echo.

echo Step 2: Checking Tesseract installation...
where tesseract >nul 2>&1
if %ERRORLEVEL% EQU 0 (
    echo [OK] Tesseract is already installed!
) else (
    echo [WARNING] Tesseract OCR not found!
    echo.
    echo Please install Tesseract manually:
    echo 1. Download from: https://github.com/UB-Mannheim/tesseract/wiki
    echo 2. Run installer
    echo 3. Add to PATH or configure in settings.py
    echo.
)

echo.
echo ========================================
echo Installation Complete!
echo ========================================
echo.
echo Next steps:
echo 1. If Tesseract not installed, download and install it
echo 2. Run: python manage.py runserver
echo 3. Visit: http://127.0.0.1:8000/calculator/
echo 4. Click "Upload Screenshot" tab
echo.
pause
