# Quick Start Guide - HR AI System

## 🚀 **Get Running in 5 Minutes**

### **Prerequisites**
- Python 3.8+ installed
- Git installed
- Terminal/Command prompt

### **Step 1: Download & Setup (2 minutes)**
```bash
# Clone repository
git clone https://github.com/ISHANSHIRODE01/Ishan_HR_AI_System.git
cd Ishan_HR_AI_System

# Automated setup (Windows)
setup_venv.bat

# Automated setup (Linux/macOS)
chmod +x setup_venv.sh && ./setup_venv.sh

# Setup data files (auto-generates missing files)
python setup_data.py
```

### **Step 2: Verify Installation (1 minute)**
```bash
# Test system (should show 6/6 tests passed)
python tests/simple_test.py

# Test missing data handling (NEW)
python tests/test_missing_data_handling.py
```

### **Step 3: Start System (2 minutes)**
```bash
# Terminal 1: Start Flask Backend
python src/app.py

# Terminal 2: Start Dashboard
streamlit run src/dashboard.py
```

### **Step 4: Access System**
- **API**: http://localhost:5000
- **Dashboard**: http://localhost:8501

## ✅ **Success Indicators**
- Flask shows: "Running on http://127.0.0.1:5000"
- Dashboard opens in browser
- Tests show: "6/6 tests passed"

## 🔧 **If Something Goes Wrong**
```bash
# Most common fix: Activate virtual environment
venv\Scripts\activate     # Windows
source venv/bin/activate  # Linux/macOS

# Missing data files? (Auto-fixed now!)
python setup_data.py

# Then retry the commands
```

**✅ NEW**: Missing data files are now auto-generated!

**Need detailed help?** See [INSTALLATION_GUIDE.md](INSTALLATION_GUIDE.md)