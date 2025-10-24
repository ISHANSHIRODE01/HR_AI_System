# Quick Start Guide - HR AI System

## \ud83d\ude80 **Start the System (2 Steps)**

### **Step 1: Start Flask Backend**
```bash
python src/app.py
```
**Expected Output:**
```
RL Agent initialized successfully.
Gemini Client Error: Missing key inputs argument! [NORMAL - IGNORE THIS]
* Running on http://127.0.0.1:5000
```

### **Step 2: Start Dashboard (New Terminal)**
```bash
streamlit run src/dashboard.py
```
**Expected Output:**
```
Local URL: http://localhost:8501
# OR if port busy:
Local URL: http://localhost:8503
```

## \u2705 **System Ready!**
- **API**: http://localhost:5000
- **Dashboard**: http://localhost:8501 or 8503

## \u274c **Common Mistakes**

### **Wrong Commands (Will Fail):**
```bash
python app.py                    # \u274c File not found
python dashboard.py              # \u274c File not found
```

### **Correct Commands:**
```bash
python src/app.py                # \u2705 Works
streamlit run src/dashboard.py   # \u2705 Works
```

## \ud83d\udcdd **Test the System**

### **API Test:**
```bash
curl http://localhost:5000/
```

### **Submit Feedback:**
```bash
curl -X POST http://localhost:5000/update_feedback \
  -H "Content-Type: application/json" \
  -d '{"candidate_id":1,"jd_id":1,"feedback_score":4,"comment":"Great candidate"}'
```

## \u26a0\ufe0f **Expected Warnings (Normal)**
- **Gemini Client Error** - System works without API key
- **Port 8503** - Streamlit auto-switches if 8501 busy
- **Plotly warnings** - Dashboard still works perfectly

**Your system is working correctly!**