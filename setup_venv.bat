@echo off
echo ========================================
echo HR AI System - Virtual Environment Setup
echo ========================================

echo Checking Python installation...
python --version
if %errorlevel% neq 0 (
    echo ERROR: Python not found. Please install Python 3.8+
    pause
    exit /b 1
)

echo.
echo Creating virtual environment...
python -m venv venv
if %errorlevel% neq 0 (
    echo ERROR: Failed to create virtual environment
    pause
    exit /b 1
)

echo.
echo Activating virtual environment...
call venv\Scripts\activate.bat

echo.
echo Installing dependencies...
pip install --upgrade pip
pip install -r requirements.txt

echo.
echo ========================================
echo Virtual Environment Setup Complete!
echo ========================================
echo.
echo To activate the environment in future sessions:
echo   venv\Scripts\activate
echo.
echo To deactivate:
echo   deactivate
echo.
echo Now you can run the system:
echo   python src/app.py
echo   streamlit run src/dashboard.py
echo.
pause