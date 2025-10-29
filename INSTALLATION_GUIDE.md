# Complete Installation Guide - HR AI System (Simplified)

## Overview
This guide provides detailed installation instructions for the simplified HR AI System with no external dependencies.

## System Requirements

### Software Requirements
- **Python 3.8+** (Required)
- **Git** (Optional, for cloning)
- **Command Line/Terminal** access

### Hardware Requirements
- **RAM**: 512MB minimum, 1GB recommended
- **Storage**: 100MB free space
- **CPU**: Any modern processor

## Installation Steps

### Step 1: Verify Prerequisites
```bash
# Check Python version
python --version
# Should show 3.8 or higher

# Check pip
pip --version

# Check Git (optional)
git --version
```

### Step 2: Download Project
**Option A: Git Clone (Recommended)**
```bash
git clone https://github.com/ISHANSHIRODE01/Ishan_HR_AI_System.git
cd Ishan_HR_AI_System
```

**Option B: Download ZIP**
1. Visit: https://github.com/ISHANSHIRODE01/Ishan_HR_AI_System
2. Click "Code" → "Download ZIP"
3. Extract and navigate to folder

### Step 3: Create Virtual Environment
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate

# Linux/macOS:
source venv/bin/activate

# Verify activation (should show (venv) in prompt)
```

### Step 4: Install Dependencies
```bash
# Upgrade pip
pip install --upgrade pip

# Install all dependencies
pip install -r requirements.txt

# Verify installation
pip list
```

### Step 5: Verify Data Files
```bash
# Check required files exist
ls feedback/
# Should show: cvs.csv, jds.csv, feedbacks.csv
```

### Step 6: Run Tests
```bash
python tests/simple_test.py
# Expected output: "6/6 tests passed"
```

### Step 7: Start System
```bash
# Method 1: Manual (Recommended)
# Terminal 1:
python src/app.py

# Terminal 2 (new terminal, activate venv first):
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/macOS
streamlit run src/dashboard.py

# Method 2: Windows Batch (if available)
scripts\start_system.bat
```

### Step 8: Verify Access
- **Flask API**: http://localhost:5000
- **Dashboard**: http://localhost:8501
- **Health Check**: http://localhost:5000/health

## Configuration (Optional)

### Environment Variables
Create `.env` file (optional):
```env
FLASK_ENV=development
FLASK_DEBUG=True
FLASK_PORT=5000
STREAMLIT_PORT=8501
```

### Data Customization
You can modify the CSV files in `feedback/`:
- `cvs.csv`: Add your candidate profiles
- `jds.csv`: Add your job descriptions
- `feedbacks.csv`: Historical feedback data

## Troubleshooting

### Common Issues

#### 1. "python: command not found"
**Solution**: Install Python from python.org or try `python3`

#### 2. "ModuleNotFoundError"
**Solution**: Activate virtual environment
```bash
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/macOS
```

#### 3. "Permission denied"
**Solution**: Run as administrator or use `sudo` (Linux/macOS)

#### 4. "Port already in use"
**Solution**: 
- Kill existing processes
- Streamlit will auto-switch to port 8503
- Change port in code if needed

#### 5. "CSV file not found"
**Solution**: Ensure you're in the project root directory

### Verification Checklist
- [ ] Python 3.8+ installed
- [ ] Virtual environment created and activated
- [ ] Dependencies installed successfully
- [ ] All tests passing (6/6)
- [ ] Flask API accessible at localhost:5000
- [ ] Dashboard accessible at localhost:8501
- [ ] No import or encoding errors

## What's New in Simplified Version

### Removed Features
- External AI API integration (Gemini)
- Unicode characters causing encoding issues
- Complex API key management
- External network dependencies

### Improved Features
- Faster startup time
- Better cross-platform compatibility
- Simpler configuration
- More reliable operation

### Maintained Features
- Full reinforcement learning functionality
- Interactive Streamlit dashboard
- Complete Flask API
- All visualizations and metrics
- Comprehensive testing suite

## Performance Expectations
- **Startup Time**: 5-10 seconds
- **Response Time**: 50-100ms per request
- **Memory Usage**: 20-50MB
- **CPU Usage**: Low (< 5% on modern systems)

## Next Steps
1. **Test the API**: Submit feedback via POST requests
2. **Explore Dashboard**: View learning progress and metrics
3. **Customize Data**: Add your own candidates and job descriptions
4. **Deploy**: Consider Docker or cloud deployment for production

## Support
- **Documentation**: README.md and this guide
- **Testing**: Run `python tests/simple_test.py`
- **Issues**: GitHub Issues page
- **Community**: GitHub Discussions

**Installation complete! Your HR AI System is ready for use.**