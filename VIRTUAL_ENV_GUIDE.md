# Virtual Environment Guide - HR AI System

## 🎯 **Why Virtual Environment is Required**

Virtual environments isolate Python dependencies to prevent conflicts between projects. This ensures:
- ✅ **Clean Dependencies**: Only required packages installed
- ✅ **Version Control**: Exact package versions as specified
- ✅ **No Conflicts**: Isolated from system Python packages
- ✅ **Reproducible**: Same environment across different machines

## 🚀 **Quick Setup**

### **Option 1: Automated Setup (Recommended)**

**Windows:**
```bash
setup_venv.bat
```

**Linux/macOS:**
```bash
chmod +x setup_venv.sh
./setup_venv.sh
```

### **Option 2: Manual Setup**

**Step 1: Create Virtual Environment**
```bash
python -m venv venv
```

**Step 2: Activate Virtual Environment**
```bash
# Windows
venv\Scripts\activate

# Linux/macOS
source venv/bin/activate
```

**Step 3: Install Dependencies**
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

## ✅ **Verify Setup**

**Check if virtual environment is active:**
```bash
# Should show path to venv
which python    # Linux/macOS
where python    # Windows

# Should show (venv) in prompt
# Example: (venv) PS E:\Ishan_HR_AI_System>
```

**Test installation:**
```bash
python -c "import flask, streamlit, pandas; print('All dependencies installed!')"
```

## 🔄 **Daily Usage**

### **Activate Environment (Every Session)**
```bash
# Windows
venv\Scripts\activate

# Linux/macOS
source venv/bin/activate
```

### **Run the System**
```bash
# Start Flask backend
python src/app.py

# Start dashboard (new terminal, activate venv first)
streamlit run src/dashboard.py
```

### **Deactivate When Done**
```bash
deactivate
```

## 🔧 **Troubleshooting**

### **Issue: "ModuleNotFoundError"**
```bash
# Solution: Activate virtual environment
venv\Scripts\activate     # Windows
source venv/bin/activate  # Linux/macOS

# Verify activation
python -c "import sys; print(sys.prefix)"
# Should show path containing 'venv'
```

### **Issue: "Command not found: python"**
```bash
# Try python3 instead
python3 -m venv venv
python3 src/app.py
```

### **Issue: Virtual environment not activating**
```bash
# Windows: Try different activation script
venv\Scripts\activate.bat
# or
venv\Scripts\Activate.ps1

# Linux/macOS: Check shell
bash
source venv/bin/activate
```

### **Issue: Permission denied (Linux/macOS)**
```bash
chmod +x setup_venv.sh
chmod +x venv/bin/activate
```

## 📋 **Environment Management**

### **Update Dependencies**
```bash
# Activate environment first
source venv/bin/activate  # or venv\Scripts\activate

# Update packages
pip install --upgrade -r requirements.txt
```

### **Add New Dependencies**
```bash
# Install new package
pip install package_name

# Update requirements file
pip freeze > requirements.txt
```

### **Clean Installation**
```bash
# Remove old environment
rm -rf venv          # Linux/macOS
rmdir /s venv        # Windows

# Create fresh environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate
pip install -r requirements.txt
```

## ✅ **Success Indicators**

**Virtual environment is working if:**
- ✅ Prompt shows `(venv)` prefix
- ✅ `which python` shows venv path
- ✅ `python src/app.py` runs without import errors
- ✅ `streamlit run src/dashboard.py` works
- ✅ Tests pass: `python tests/simple_test.py`

**Your HR AI System is ready when all indicators are green!**