# Complete Installation Guide - HR AI System

## 🎯 **Overview**

This guide will walk you through installing the HR AI System from scratch. Follow each step carefully for a successful setup.

**Estimated Time**: 10-15 minutes  
**Difficulty**: Beginner-friendly

---

## 📋 **Pre-Installation Checklist**

### **System Requirements**
- **Operating System**: Windows 10+, macOS 10.14+, or Linux (Ubuntu 18.04+)
- **RAM**: Minimum 4GB, Recommended 8GB+
- **Storage**: 2GB free space
- **Internet**: Required for downloading dependencies

### **Required Software**
- [ ] **Python 3.8+** - [Download from python.org](https://python.org/downloads/)
- [ ] **Git** - [Download from git-scm.com](https://git-scm.com/downloads)
- [ ] **Text Editor/IDE** (Optional) - VS Code, PyCharm, etc.

---

## 🔧 **Step-by-Step Installation**

### **Step 1: Verify Prerequisites**

Open your terminal/command prompt and run:

```bash
# Check Python version (must be 3.8 or higher)
python --version
# If above fails, try:
python3 --version

# Check Git installation
git --version

# Check pip (Python package manager)
pip --version
```

**Expected Output:**
```
Python 3.8.10 (or higher)
git version 2.x.x
pip 21.x.x (or higher)
```

**❌ If any command fails:**
- **Python**: Download and install from [python.org](https://python.org/downloads/)
- **Git**: Download and install from [git-scm.com](https://git-scm.com/downloads)
- **pip**: Usually comes with Python, try `python -m pip --version`

### **Step 2: Download the Project**

**Method A: Git Clone (Recommended)**
```bash
# Clone the repository
git clone https://github.com/ISHANSHIRODE01/Ishan_HR_AI_System.git

# Navigate to project directory
cd Ishan_HR_AI_System

# Verify download
ls
# Should show: src/, agents/, feedback/, tests/, etc.
```

**Method B: Download ZIP**
1. Visit: https://github.com/ISHANSHIRODE01/Ishan_HR_AI_System
2. Click green "Code" button → "Download ZIP"
3. Extract ZIP file to desired location
4. Open terminal in extracted folder

### **Step 3: Set Up Virtual Environment**

**🎯 Why Virtual Environment?**
- Keeps project dependencies isolated
- Prevents conflicts with other Python projects
- Ensures consistent environment across machines

**Automated Setup (Easiest):**
```bash
# Windows
setup_venv.bat

# Linux/macOS
chmod +x setup_venv.sh
./setup_venv.sh
```

**Manual Setup:**
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\\Scripts\\activate

# Linux/macOS:
source venv/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install dependencies
pip install -r requirements.txt
```

**✅ Verify Virtual Environment:**
```bash
# Your prompt should show (venv) at the beginning
# Example: (venv) C:\\Ishan_HR_AI_System>

# Check Python location
where python    # Windows
which python    # Linux/macOS
# Should point to venv directory
```

### **Step 4: Install Dependencies**

```bash
# Make sure virtual environment is activated (you should see (venv) in prompt)

# Install all required packages
pip install -r requirements.txt

# Verify installation
pip list
# Should show Flask, streamlit, pandas, etc.
```

**Expected Packages:**
- Flask==3.0.3
- streamlit==1.37.0
- pandas==2.2.2
- numpy==1.26.4
- scikit-learn==1.5.2
- And more...

### **Step 5: Verify Installation**

**Run System Tests:**
```bash
# Test system components
python tests/simple_test.py

# Expected output:
# ============================================================
# HR AI SYSTEM - SIMPLE TEST SUITE
# ============================================================
# ...
# Overall: 6/6 tests passed
# SUCCESS: All tests passed! Your HR AI System is ready to use.
```

**Test Configuration:**
```bash
python tests/test_config.py

# Expected output:
# Overall: 2/2 tests passed
```

### **Step 6: Start the System**

**🚨 IMPORTANT: Always activate virtual environment first!**

**Check Virtual Environment:**
```bash
# Should show (venv) in your prompt
# If not, activate it:
venv\\Scripts\\activate     # Windows
source venv/bin/activate    # Linux/macOS
```

**Start Flask Backend:**
```bash
python src/app.py
```

**Expected Output:**
```
RL Agent initialized successfully.
No Google AI API key found. Gemini features disabled.
 * Running on http://127.0.0.1:5000
 * Debug mode: on
```

**Start Dashboard (New Terminal):**
```bash
# Open new terminal/command prompt
cd Ishan_HR_AI_System

# Activate virtual environment
venv\\Scripts\\activate     # Windows
source venv/bin/activate    # Linux/macOS

# Start dashboard
streamlit run src/dashboard.py
```

**Expected Output:**
```
You can now view your Streamlit app in your browser.

Local URL: http://localhost:8501
Network URL: http://192.168.x.x:8501
```

### **Step 7: Verify System is Working**

**Test Web Interfaces:**
1. **Flask API**: Open http://localhost:5000 in browser
   - Should show: "HR RL Agent Backend Running"

2. **Dashboard**: Should open automatically at http://localhost:8501
   - Should show HR RL Agent Transparency Dashboard

**Test API Functionality:**
```bash
# Health check
curl http://localhost:5000/

# Submit test feedback
curl -X POST http://localhost:5000/update_feedback \
  -H "Content-Type: application/json" \
  -d '{
    "candidate_id": 1,
    "jd_id": 1,
    "feedback_score": 4,
    "comment": "Test feedback"
  }'
```

---

## 🔧 **Troubleshooting**

### **Common Issues & Solutions**

#### **Issue: "ModuleNotFoundError"**
```
ModuleNotFoundError: No module named 'flask'
```
**Solution:**
```bash
# Activate virtual environment
venv\\Scripts\\activate     # Windows
source venv/bin/activate    # Linux/macOS

# Reinstall dependencies
pip install -r requirements.txt
```

#### **Issue: "python: command not found"**
**Solution:**
```bash
# Try python3 instead
python3 --version
python3 -m venv venv

# Or add Python to PATH (Windows)
# Or reinstall Python from python.org
```

#### **Issue: "can't open file 'app.py'"**
**Solution:**
```bash
# Use correct path
python src/app.py  # NOT python app.py

# Verify you're in project root
ls src/
# Should show: app.py, dashboard.py, main.py
```

#### **Issue: Virtual Environment Not Activating**
**Windows:**
```bash
# Try different activation methods
venv\\Scripts\\activate.bat
# or
venv\\Scripts\\Activate.ps1
```

**Linux/macOS:**
```bash
# Check shell and try
bash
source venv/bin/activate
```

#### **Issue: Permission Denied (Linux/macOS)**
```bash
chmod +x setup_venv.sh
chmod +x venv/bin/activate
```

#### **Issue: Port Already in Use**
- Streamlit will automatically use port 8503 if 8501 is busy
- Or stop other applications using the ports

---

## ✅ **Installation Success Checklist**

**Prerequisites:**
- [ ] Python 3.8+ installed and working
- [ ] Git installed (if cloning)
- [ ] Terminal/Command prompt access

**Project Setup:**
- [ ] Project downloaded/cloned successfully
- [ ] Can navigate to project directory
- [ ] All project files present (src/, agents/, feedback/, etc.)

**Virtual Environment:**
- [ ] Virtual environment created: `python -m venv venv`
- [ ] Virtual environment activated: Shows `(venv)` in prompt
- [ ] Python points to venv: `which python` shows venv path

**Dependencies:**
- [ ] Dependencies installed: `pip install -r requirements.txt`
- [ ] No installation errors
- [ ] Required packages present: `pip list` shows Flask, streamlit, etc.

**System Tests:**
- [ ] Configuration tests pass: `python tests/test_config.py`
- [ ] System tests pass: `python tests/simple_test.py` (6/6)
- [ ] No import errors

**System Running:**
- [ ] Flask backend starts: `python src/app.py`
- [ ] Flask accessible: http://localhost:5000 responds
- [ ] Dashboard starts: `streamlit run src/dashboard.py`
- [ ] Dashboard accessible: http://localhost:8501 opens
- [ ] API responds to test requests
- [ ] No critical errors in terminals

**🎉 If all items are checked, your HR AI System is successfully installed and ready to use!**

---

## 📞 **Getting Help**

If you encounter issues not covered in this guide:

1. **Check Logs**: Look at terminal output for specific error messages
2. **Run Tests**: `python tests/simple_test.py` for diagnostics
3. **Verify Environment**: Ensure virtual environment is activated
4. **Check Documentation**: 
   - [TROUBLESHOOTING.md](TROUBLESHOOTING.md)
   - [VIRTUAL_ENV_GUIDE.md](VIRTUAL_ENV_GUIDE.md)
   - [README.md](README.md)
5. **GitHub Issues**: Report bugs at repository issues page

**Remember**: Most issues are related to virtual environment not being activated or dependencies not installed correctly.