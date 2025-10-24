@echo off
echo ========================================
echo HR AI System - Startup Script
echo ========================================

echo Checking Python installation...
python --version
if %errorlevel% neq 0 (
    echo ERROR: Python not found. Please install Python 3.8+
    pause
    exit /b 1
)

echo.
echo Installing/Updating dependencies...
pip install -r requirements.txt

echo.
echo Running system tests...
python tests\simple_test.py
if %errorlevel% neq 0 (
    echo WARNING: Some tests failed. Check the output above.
    echo Press any key to continue anyway or Ctrl+C to exit...
    pause
)

echo.
echo ========================================
echo Starting HR AI System Components
echo ========================================

echo.
echo Starting Flask Backend on port 5000...
echo You can access the API at: http://localhost:5000
echo API Documentation: http://localhost:5000 (basic endpoint)
echo.
echo To start the Streamlit Dashboard, open a new terminal and run:
echo streamlit run src\dashboard.py
echo.
echo Press Ctrl+C to stop the Flask server
echo.

python src\app.py