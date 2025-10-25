@echo off
echo ========================================
echo HR AI System - Missing Data Files Test
echo ========================================
echo.

REM Check if virtual environment is activated
python -c "import sys; print('Virtual env active:' if hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix) else 'Virtual env NOT active')"
echo.

echo Running missing data files handling test...
python tests\test_missing_data_handling.py

echo.
echo Running main test suite...
python tests\simple_test.py

echo.
echo Testing setup script...
python setup_data.py

echo.
echo ========================================
echo Test completed. Check output above.
echo ========================================
pause