# Quick Start Guide - HR AI System (Simplified)

**Get your HR AI System running in 5 minutes!**

## Prerequisites
- Python 3.8+ installed
- Command line access

## Step 1: Download
```bash
git clone https://github.com/ISHANSHIRODE01/Ishan_HR_AI_System.git
cd Ishan_HR_AI_System
```

## Step 2: Setup Environment
```bash
# Create virtual environment
python -m venv venv

# Activate it
# Windows:
venv\Scripts\activate
# Linux/macOS:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

## Step 3: Verify Installation
```bash
python tests/simple_test.py
# Expected: "6/6 tests passed"
```

## Step 4: Start System
```bash
# Terminal 1 - Flask Backend
python src/app.py

# Terminal 2 - Dashboard (new terminal, activate venv first)
streamlit run src/dashboard.py
```

## Step 5: Access
- **API**: http://localhost:5000
- **Dashboard**: http://localhost:8501

## Test API
```bash
curl -X POST http://localhost:5000/update_feedback \
  -H "Content-Type: application/json" \
  -d '{"candidate_id": 1, "jd_id": 1, "feedback_score": 4, "comment": "Great candidate"}'
```

## Troubleshooting
- **Import errors**: Ensure virtual environment is activated
- **Port busy**: Streamlit will auto-switch to 8503
- **Missing files**: All required CSV files are included

## What's Different (Simplified Version)
- ✅ No external API keys required
- ✅ No Unicode encoding issues
- ✅ Faster startup and response times
- ✅ Self-contained system

**That's it! Your HR AI System is ready to use.**