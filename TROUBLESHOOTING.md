# Troubleshooting Guide - HR AI System

## \ud83d\udd34 **Common Issues & Solutions**

### **Issue 1: "can't open file 'app.py'"**
```
python app.py
# Error: can't open file 'E:\Ishan_HR_AI_System\app.py': No such file or directory
```

**\u2705 Solution:**
```bash
# Use correct path:
python src/app.py
```

### **Issue 2: Dashboard on Different Port**
```
# Expected: http://localhost:8501
# Actual: http://localhost:8503
```

**\u2705 This is Normal:**
- Streamlit auto-switches ports if 8501 is busy
- Use whatever port is shown in terminal

### **Issue 3: Gemini API Warnings**
```
Gemini Client Error: Missing key inputs argument!
Exception ignored in: <function Client.__del__>
```

**\u2705 This is Expected:**
- System works perfectly without Gemini API
- These warnings don't affect functionality
- To remove: Set `GOOGLE_AI_API_KEY` environment variable

### **Issue 4: Plotly Deprecation Warnings**
```
The keyword arguments have been deprecated and will be removed in a future release.
```

**\u2705 This is Normal:**
- Dashboard still works perfectly
- Warnings are from Streamlit/Plotly version compatibility
- Functionality is not affected

## \ud83d\udfe2 **System Status Check**

### **Flask Backend Working If You See:**
```
RL Agent initialized successfully.
* Running on http://127.0.0.1:5000
* Debug mode: on
```

### **Dashboard Working If You See:**
```
You can now view your Streamlit app in your browser.
Local URL: http://localhost:8501 (or 8503)
```

## \ud83d\udd27 **Quick Fixes**

### **Reset Everything:**
```bash
# Stop all processes (Ctrl+C)
# Restart Flask
python src/app.py

# Restart Dashboard (new terminal)
streamlit run src/dashboard.py
```

### **Test System:**
```bash
# Run tests
python tests/simple_test.py

# Should show: 6/6 tests passed
```

### **Verify Files:**
```bash
# Check structure
dir src
# Should show: app.py, dashboard.py, main.py
```

## \u2705 **System is Working If:**
- Flask shows "Running on http://127.0.0.1:5000"
- Dashboard opens in browser
- API responds to curl requests
- Tests pass (6/6)

**All warnings mentioned above are NORMAL and expected!**