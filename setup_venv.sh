#!/bin/bash
echo "========================================"
echo "HR AI System - Virtual Environment Setup"
echo "========================================"

echo "Checking Python installation..."
python3 --version
if [ $? -ne 0 ]; then
    echo "ERROR: Python3 not found. Please install Python 3.8+"
    exit 1
fi

echo ""
echo "Creating virtual environment..."
python3 -m venv venv
if [ $? -ne 0 ]; then
    echo "ERROR: Failed to create virtual environment"
    exit 1
fi

echo ""
echo "Activating virtual environment..."
source venv/bin/activate

echo ""
echo "Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

echo ""
echo "========================================"
echo "Virtual Environment Setup Complete!"
echo "========================================"
echo ""
echo "To activate the environment in future sessions:"
echo "  source venv/bin/activate"
echo ""
echo "To deactivate:"
echo "  deactivate"
echo ""
echo "Now you can run the system:"
echo "  python src/app.py"
echo "  streamlit run src/dashboard.py"
echo ""