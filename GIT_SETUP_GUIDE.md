# 🚀 HR AI System - Git Setup Guide

**Complete step-by-step guide for running the HR AI System from Git**

## ✅ Issues Fixed in Latest Version

### 1. **Gemini Client Initialization** ✅ FIXED
- **Problem**: Intermittent "Gemini client not initialized" errors
- **Solution**: Added comprehensive error handling and fallback mechanisms
- **Status**: System now works with or without Gemini API key

### 2. **Windows Unicode Errors** ✅ FIXED  
- **Problem**: Unicode encoding errors on Windows systems
- **Solution**: Replaced all Unicode characters with ASCII equivalents
- **Status**: Full Windows compatibility achieved

### 3. **API Error Handling** ✅ FIXED
- **Problem**: Generic error messages for API failures
- **Solution**: Added detailed error reporting and troubleshooting guidance
- **Status**: Clear error messages with actionable solutions

---

## 📋 Prerequisites

**Required Software:**
- **Python 3.8+** ([Download](https://python.org/downloads/))
- **Git** ([Download](https://git-scm.com/downloads))
- **Command Line/Terminal** access

**Verify Installation:**
```bash
python --version    # Should show 3.8+
git --version       # Should show Git version
pip --version       # Should show pip version
```

---

## 🔧 Step-by-Step Setup

### Step 1: Clone the Repository
```bash
# Clone the latest version with all fixes
git clone https://github.com/ISHANSHIRODE01/Ishan_HR_AI_System.git

# Navigate to project directory
cd Ishan_HR_AI_System
```

### Step 2: Set Up Virtual Environment
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

### Step 3: Install Dependencies
```bash
# Upgrade pip first
pip install --upgrade pip

# Install all required packages
pip install -r requirements.txt

# Verify installation
pip list | grep flask
pip list | grep streamlit
```

### Step 4: Configure API Key (Optional)
```bash
# Copy environment template
cp .env.example .env

# Edit .env file with your API key
# Windows: notepad .env
# Linux/macOS: nano .env
```

**Add to .env file:**
```env
GOOGLE_AI_API_KEY=your_actual_api_key_here
```

**Note**: System works without API key (Gemini features disabled)

### Step 5: Verify System Health
```bash
# Run comprehensive tests
python tests/simple_test.py

# Expected output: "6/6 tests passed"
```

### Step 6: Start the System

**Option A: Use Improved Startup Script**
```bash
python start_system_improved.py
```

**Option B: Manual Startup**
```bash
# Terminal 1: Start Flask Backend
python src/app.py

# Terminal 2: Start Dashboard (new terminal, activate venv first)
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/macOS
streamlit run src/dashboard.py
```

---

## 🌐 Access Points

Once running, access these URLs:

- **Flask API**: http://localhost:5000
- **System Health**: http://localhost:5000/health
- **Dashboard**: http://localhost:8501
- **API Status**: http://localhost:5000/ (JSON response)

---

## 🔍 Troubleshooting

### Issue: "ModuleNotFoundError"
**Solution:**
```bash
# Ensure virtual environment is activated
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/macOS

# Reinstall dependencies
pip install -r requirements.txt
```

### Issue: "Port already in use"
**Solution:**
- Streamlit will auto-switch to port 8503
- Or kill existing processes and restart

### Issue: Gemini API warnings
**Solution:**
- This is normal - system works without API key
- To enable: Set `GOOGLE_AI_API_KEY` in .env file

### Issue: Data files missing
**Solution:**
```bash
# Check if files exist
ls feedback/
# Should show: cvs.csv, jds.csv, feedbacks.csv

# If missing, the system will still run with limited functionality
```

---

## 🧪 Testing the System

### 1. Health Check
```bash
curl http://localhost:5000/health
```

### 2. Submit Test Feedback
```bash
curl -X POST http://localhost:5000/update_feedback \
  -H "Content-Type: application/json" \
  -d '{
    "candidate_id": 1,
    "jd_id": 1,
    "feedback_score": 4,
    "comment": "Excellent technical skills"
  }'
```

### 3. Python Test
```python
import requests

response = requests.post('http://localhost:5000/update_feedback', 
    json={
        "candidate_id": 1,
        "jd_id": 1,
        "feedback_score": 4,
        "comment": "Great candidate"
    })

print(response.json())
```

---

## ✅ Success Checklist

- [ ] **Repository cloned** successfully
- [ ] **Virtual environment** created and activated
- [ ] **Dependencies installed** without errors
- [ ] **Tests passing**: `python tests/simple_test.py`
- [ ] **Flask running**: http://localhost:5000 accessible
- [ ] **Dashboard running**: http://localhost:8501 opens
- [ ] **Health check**: http://localhost:5000/health returns JSON
- [ ] **No Unicode errors** in terminal output

---

## 🚀 Quick Start Commands

**Complete setup in 5 commands:**
```bash
git clone https://github.com/ISHANSHIRODE01/Ishan_HR_AI_System.git
cd Ishan_HR_AI_System
python -m venv venv
venv\Scripts\activate  # Windows: or source venv/bin/activate for Linux/macOS
pip install -r requirements.txt
python start_system_improved.py
```

---

## 📊 System Status Indicators

### Healthy System:
- `[OK] Gemini Client initialized` or `[INFO] No Google AI API key found`
- `RL Agent initialized successfully`
- Flask shows: `Running on http://127.0.0.1:5000`
- Dashboard opens automatically in browser
- Health check returns `"overall": "healthy"`

### Expected Warnings (Normal):
- `[INFO] No Google AI API key found` - System works without it
- `[INFO] Google GenAI library not available` - Install with pip if needed

---

## 🔧 Advanced Configuration

### Custom Ports:
```bash
# Flask on different port
python src/app.py --port 5001

# Streamlit on different port  
streamlit run src/dashboard.py --server.port 8502
```

### Environment Variables:
```env
GOOGLE_AI_API_KEY=your_key_here
FLASK_ENV=development
FLASK_DEBUG=True
STREAMLIT_PORT=8501
```

---

## 📞 Support

**If you encounter issues:**

1. **Check this guide** - Most issues are covered here
2. **Run health check**: `curl http://localhost:5000/health`
3. **Check system logs** in terminal output
4. **Verify virtual environment** is activated
5. **Create GitHub issue** with error details

**System Requirements:**
- Python 3.8+
- 2GB RAM minimum
- 1GB disk space
- Internet connection (for Gemini API, optional)

---

**🎉 You're all set! The HR AI System should now be running smoothly.**