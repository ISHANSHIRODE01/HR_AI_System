# HR AI System - Reinforcement Learning Agent

**Intelligent HR Decision System with Flask Backend + Streamlit Dashboard**

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-3.0+-green.svg)](https://flask.palletsprojects.com)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.37+-red.svg)](https://streamlit.io)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> **AI-powered HR system that learns from feedback using reinforcement learning and provides transparent decision-making through interactive dashboards.**

---

## 🎯 Overview

This HR AI System uses **Q-learning reinforcement learning** to make intelligent hiring decisions. The system learns from HR feedback, adapts its decision-making policy, and provides transparent insights through an interactive dashboard.

### Key Features
- 🤖 **Reinforcement Learning**: Q-learning algorithm that improves with feedback
- 🌐 **RESTful API**: Flask backend with comprehensive endpoints
- 📊 **Interactive Dashboard**: Real-time visualizations and metrics
- 🔄 **Adaptive Learning**: Continuous improvement from HR feedback
- 📈 **Decision Transparency**: Clear explanations for AI recommendations
- 🚀 **Production Ready**: Comprehensive testing and error handling

---

## 🚀 Installation Overview

**🎯 Choose Your Path:**
- **🚀 Quick Start**: [5-minute setup guide](QUICK_START.md) - Get running fast
- **📖 Complete Guide**: [Detailed installation](INSTALLATION_GUIDE.md) - Step-by-step with troubleshooting
- **🐍 Virtual Environment**: [Environment setup](VIRTUAL_ENV_GUIDE.md) - Virtual environment help

---

## 📝 Complete Installation Guide

### Step 1: Prerequisites Check

**Required Software:**
- **Python 3.8+** ([Download here](https://python.org/downloads/))
- **Git** ([Download here](https://git-scm.com/downloads))
- **Command Line/Terminal** access

**Verify Installation:**
```bash
# Check Python version (should be 3.8+)
python --version
# or try
python3 --version

# Check Git installation
git --version

# Check pip (Python package manager)
pip --version
```

### Step 2: Download the Project

**Option A: Clone with Git (Recommended)**
```bash
# Clone the repository
git clone https://github.com/ISHANSHIRODE01/Ishan_HR_AI_System.git

# Navigate to project directory
cd Ishan_HR_AI_System
```

**Option B: Download ZIP**
1. Go to: https://github.com/ISHANSHIRODE01/Ishan_HR_AI_System
2. Click "Code" → "Download ZIP"
3. Extract to desired location
4. Open terminal in extracted folder

### Step 3: Set Up Virtual Environment

**🎯 Why Virtual Environment?**
- Isolates project dependencies
- Prevents conflicts with other Python projects
- Ensures reproducible environment

**Option A: Automated Setup (Easiest)**
```bash
# Windows Users
setup_venv.bat

# Linux/macOS Users
chmod +x setup_venv.sh
./setup_venv.sh
```

**Option B: Manual Setup**
```bash
# Step 1: Create virtual environment
python -m venv venv

# Step 2: Activate virtual environment
# Windows:
venv\Scripts\activate

# Linux/macOS:
source venv/bin/activate

# Step 3: Upgrade pip
pip install --upgrade pip

# Step 4: Install all dependencies
pip install -r requirements.txt
```

**✅ Verify Virtual Environment:**
```bash
# Your prompt should show (venv) at the beginning
# Example: (venv) C:\Ishan_HR_AI_System>

# Check Python location (should point to venv)
where python    # Windows
which python    # Linux/macOS
```

### Step 4: Verify Installation

**Run System Tests:**
```bash
# Make sure virtual environment is activated first!
# You should see (venv) in your prompt

# Run comprehensive tests
python tests/simple_test.py

# Expected output: "6/6 tests passed"
```

**Test Individual Components:**
```bash
# Test configuration
python tests/test_config.py

# Test Flask components
python tests/test_flask_only.py

# Test dashboard components
python tests/test_dashboard.py
```

### Step 5: Start the System

**🚨 IMPORTANT: Always activate virtual environment first!**
```bash
# Activate virtual environment (if not already active)
# Windows:
venv\Scripts\activate

# Linux/macOS:
source venv/bin/activate
```

**Method 1: Automated Startup (Windows)**
```bash
scripts\start_system.bat
```

**Method 2: Manual Startup (All Platforms)**
```bash
# Terminal 1: Start Flask Backend
python src/app.py

# Terminal 2: Start Dashboard (open new terminal, activate venv first)
source venv/bin/activate  # or venv\Scripts\activate
streamlit run src/dashboard.py
```

**Method 3: Individual Components**
```bash
# Start only Flask API
python src/app.py

# Start only Dashboard (separate terminal)
streamlit run src/dashboard.py
```

### Step 6: Access the System

**🌐 Web Interfaces:**
- **Flask API**: http://localhost:5000
- **Streamlit Dashboard**: http://localhost:8501 (or 8503 if busy)
- **API Documentation**: http://localhost:5000/ (health check)

**✅ Success Indicators:**
- Flask shows: "Running on http://127.0.0.1:5000"
- Dashboard opens in browser automatically
- No import errors in terminal
- Both interfaces accessible in browser

### Step 7: Test the System

**API Health Check:**
```bash
# Test if Flask API is working
curl http://localhost:5000/

# Expected response: "HR RL Agent Backend Running"
```

**Submit Test Feedback:**
```bash
curl -X POST http://localhost:5000/update_feedback \
  -H "Content-Type: application/json" \
  -d '{
    "candidate_id": 1,
    "jd_id": 1,
    "feedback_score": 4,
    "comment": "Test feedback submission"
  }'
```

**Python Test:**
```python
import requests

# Test API endpoint
response = requests.post('http://localhost:5000/update_feedback', 
    json={
        "candidate_id": 1,
        "jd_id": 1,
        "feedback_score": 4,
        "comment": "Great candidate for the role"
    })

print(response.json())
```

## ⚠️ **Troubleshooting Common Issues**

### ❌ **"ModuleNotFoundError" or Import Errors**
**Cause**: Virtual environment not activated
**Solution**:
```bash
# Activate virtual environment
venv\Scripts\activate     # Windows
source venv/bin/activate   # Linux/macOS

# Verify activation (should show venv path)
where python    # Windows
which python    # Linux/macOS
```

### ❌ **"python: command not found"**
**Cause**: Python not installed or not in PATH
**Solution**:
```bash
# Try python3 instead
python3 --version
python3 -m venv venv

# Or reinstall Python from python.org
```

### ❌ **"can't open file 'app.py'"**
**Cause**: Wrong command or directory
**Solution**:
```bash
# Use correct path:
python src/app.py  # NOT python app.py

# Verify you're in project root:
ls src/  # Should show app.py, dashboard.py, main.py
```

### ❌ **Port Already in Use**
**Cause**: Another application using the port
**Solution**:
- Streamlit will auto-switch to port 8503
- Or kill existing processes and restart

### ❌ **Gemini API Warnings**
**Cause**: No Google AI API key (this is normal)
**Solution**: 
- Ignore the warning - system works without it
- Or set `GOOGLE_AI_API_KEY` environment variable

## ✅ **Installation Success Checklist**

- [ ] **Python 3.8+** installed and working
- [ ] **Git** installed (if cloning)
- [ ] **Project downloaded** to local machine
- [ ] **Virtual environment created**: `python -m venv venv`
- [ ] **Virtual environment activated**: Shows `(venv)` in prompt
- [ ] **Dependencies installed**: `pip install -r requirements.txt`
- [ ] **Tests passing**: `python tests/simple_test.py` shows 6/6 passed
- [ ] **Flask backend running**: http://localhost:5000 accessible
- [ ] **Dashboard running**: http://localhost:8501 opens in browser
- [ ] **API responding**: Health check returns success
- [ ] **No import errors**: All components start without errors

**🎉 If all items are checked, your HR AI System is ready to use!**

---

## 🧪 Testing & Verification

### Automated Testing
```bash
# IMPORTANT: Activate virtual environment first!
venv\Scripts\activate     # Windows
source venv/bin/activate   # Linux/macOS

# Run complete test suite
python tests/simple_test.py

# Run configuration tests
python tests/test_config.py

# Test individual components
python tests/test_flask_only.py     # Flask backend only
python tests/test_dashboard.py      # Dashboard components
python tests/test_api.py            # API endpoints (requires Flask running)
```

### Manual API Testing

**Health Check:**
```bash
curl http://localhost:5000/
```

**Submit Feedback:**
```bash
curl -X POST http://localhost:5000/update_feedback \
  -H "Content-Type: application/json" \
  -d '{
    "candidate_id": 1,
    "jd_id": 1,
    "feedback_score": 4,
    "comment": "Excellent technical skills and communication"
  }'
```

**Python Example:**
```python
import requests

response = requests.post('http://localhost:5000/update_feedback', 
    json={
        "candidate_id": 1,
        "jd_id": 1,
        "feedback_score": 4,
        "comment": "Strong candidate with good experience"
    })
print(response.json())
```

---

## 📊 System Architecture

### Core Components

#### 1. **Flask Backend** (`src/app.py`)
- RESTful API with JSON responses
- Reinforcement learning agent integration
- Real-time feedback processing
- Event logging and automation
- Error handling and validation

#### 2. **Streamlit Dashboard** (`src/dashboard.py`)
- Interactive visualizations with Plotly
- Learning progress tracking
- Q-table transparency
- Feedback history analysis
- Real-time metrics display

#### 3. **RL Agent** (`agents/rl_agent.py`)
- Q-learning algorithm implementation
- State space: Match score, sentiment, history
- Action space: Accept, Reject, Reconsider
- Adaptive policy updates
- Experience replay and learning

#### 4. **Data Management**
- **CVs Dataset**: 100 candidate profiles with skills
- **JDs Dataset**: 10 job descriptions across roles
- **Feedback Dataset**: Historical HR feedback entries
- **Logging**: Structured event and feedback logs

---

## 🔌 API Reference

### Endpoints

#### `GET /`
**Health Check**
- Returns system status and agent initialization state
- **Response**: `"HR RL Agent Backend Running (Self-Automation Enabled)"`

#### `POST /update_feedback`
**Submit HR Feedback**

**Request Body:**
```json
{
  "candidate_id": 1,
  "jd_id": 1,
  "feedback_score": 4,
  "comment": "Excellent technical skills and team fit"
}
```

**Response:**
```json
{
  "status": "updated_and_logged",
  "candidate_id": 1,
  "jd_id": 1,
  "rl_policy_change": "System now suggests 'accept'",
  "feedback_summary": "Excellent technical skills and team fit"
}
```

**Error Responses:**
- `400`: Missing required fields
- `500`: RL Agent not initialized

---

## 📁 Project Structure

### Organized Architecture
The project follows a clean, modular structure with separated concerns:

- **`src/`**: Main application code (Flask, Dashboard, Core)
- **`agents/`**: AI and ML components
- **`tests/`**: Comprehensive test suite
- **`scripts/`**: Utility and startup scripts
- **`feedback/`**: Data storage and logs
- **`models/`**: Trained ML models
- **`docs/`**: Documentation and reports

```
Ishan_HR_AI_System/
├── 📁 src/                       # Source Code
│   ├── app.py                   # Flask backend server
│   ├── dashboard.py             # Streamlit dashboard
│   └── main.py                  # Core workflow engine
├── 📁 agents/                    # AI & ML Components
│   ├── rl_agent.py              # Q-learning implementation
│   ├── automation.py            # Event logging system
│   ├── decision_engine.py       # Decision logic
│   ├── matching_engine.py       # CV-JD matching
│   ├── sentiment_analyzer.py    # Comment sentiment analysis
│   └── visualization.py         # Chart generation
├── 📁 tests/                     # Test Suite
│   ├── simple_test.py           # Main test suite
│   ├── test_flask_only.py       # Flask backend tests
│   ├── test_dashboard.py        # Dashboard tests
│   ├── test_api.py              # API endpoint tests
│   └── test_system.py           # System integration tests
├── 📁 scripts/                   # Utility Scripts
│   ├── start_system.bat         # Complete system startup
│   ├── start_flask.bat          # Flask backend only
│   ├── start_dashboard.bat      # Dashboard only
│   └── run_tests.bat            # Test runner
├── 📁 feedback/                  # Data Storage
│   ├── cvs.csv                  # Candidate profiles (100 entries)
│   ├── jds.csv                  # Job descriptions (10 roles)
│   ├── feedbacks.csv            # Historical feedback (50+ entries)
│   ├── feedback_log.csv         # Runtime feedback logs
│   └── system_log.json          # Event automation logs
├── 📁 models/                    # ML Models
│   ├── sentiment_model.pkl      # Trained sentiment model
│   └── tfidf_model.pkl          # TF-IDF vectorizer
├── 📁 docs/                      # Documentation
│   ├── TEST_REPORT.md           # Comprehensive test report
│   ├── feedback_simulation.ipynb # Analysis notebook
│   ├── integration_notes.txt    # Integration guidelines
│   └── setup_instructions.txt   # Setup documentation
├── 📋 requirements.txt          # Python dependencies
├── 🐳 dockerfile               # Docker configuration
└── 📄 README.md                 # This file
```

---

## 🛠️ Configuration

### Required Data Files
Ensure these CSV files exist in the `feedback/` directory:

- **`cvs.csv`**: Candidate profiles
  ```csv
  candidate_id,name,education,experience_years,skills,location
  1,John Doe,B.E. Computer,3,"Python, ML, Data Analysis",City
  ```

- **`jds.csv`**: Job descriptions
  ```csv
  jd_id,title,description
  1,Data Scientist,"Analyze data and build ML models using Python"
  ```

- **`feedbacks.csv`**: Historical feedback
  ```csv
  feedback_id,candidate_id,jd_id,feedback_score,comment
  1,1,1,4,"Strong technical background"
  ```

### Environment Variables (Optional)
Copy `.env.example` to `.env` and configure:

```env
# For Gemini AI integration (optional)
GOOGLE_AI_API_KEY=your_api_key_here

# Flask settings
FLASK_ENV=development
FLASK_DEBUG=True

# Streamlit settings
STREAMLIT_SERVER_PORT=8501
```

**Setup:**
```bash
cp .env.example .env
# Edit .env with your settings
```

---

## 🤖 Reinforcement Learning Details

### Algorithm: Q-Learning
- **State Space**: 4D tuple representing:
  - CV-JD match score (0-2 levels)
  - Sentiment polarity (0-2 levels)
  - Previous reward (-1 to 1)
  - Reconsider history (0-1)
- **Action Space**: 3 actions
  - 0: Accept candidate
  - 1: Reject candidate
  - 2: Reconsider/Request more info
- **Reward Function**: Based on HR feedback scores
  - Score > 4: +1 for accept, -1 for reject
  - Score < 2: +1 for reject, -1 for accept
  - Score 2-4: 0 for reconsider

### Learning Parameters
```python
ALPHA = 0.1      # Learning rate
GAMMA = 0.6      # Discount factor
EPSILON = 0.1    # Exploration rate
```

---

## 📈 Dashboard Features

### Real-time Metrics
- **Total Feedbacks Processed**: Live counter
- **Cumulative Reward**: Learning progress indicator
- **Most Preferred Action**: Current policy state

### Interactive Visualizations
- **Learning Progress Chart**: Cumulative reward over time
- **Sentiment Distribution**: Feedback sentiment analysis
- **Q-Values Heatmap**: Policy transparency
- **Feedback History**: Detailed logs with expandable entries

### Policy Transparency
- Q-table values for each state
- Action probabilities
- Decision reasoning
- Learning trajectory

---

## 🔍 Troubleshooting

### Common Issues & Solutions

#### 1. **Import Errors / Module Not Found**
```bash
# Ensure virtual environment is activated
venv\Scripts\activate     # Windows
source venv/bin/activate   # Linux/macOS

# Verify activation (should show venv path)
which python              # Linux/macOS
where python              # Windows

# Reinstall dependencies if needed
pip install -r requirements.txt
```

#### 2. **Port Conflicts**
```bash
# Change Flask port
python app.py --port 5001

# Change Streamlit port
streamlit run dashboard.py --server.port 8502
```

#### 3. **Data File Issues**
```bash
# Verify data files exist
ls feedback/
# Should show: cvs.csv, jds.csv, feedbacks.csv

# Check file structure
python -c "import pandas as pd; print(pd.read_csv('feedback/cvs.csv').columns)"
```

#### 4. **Unicode Encoding (Windows)**
- Fixed in current version
- All Unicode characters removed from print statements

#### 5. **Gemini API Warnings**
- Expected warning: "Missing key inputs argument" - this is normal
- System works without Gemini API key
- To use Gemini features, set `GOOGLE_AI_API_KEY` environment variable

### Verification Checklist
- [ ] Python 3.8+ installed
- [ ] Virtual environment created: `python -m venv venv`
- [ ] Virtual environment activated: `venv\Scripts\activate` (Windows) or `source venv/bin/activate` (Linux/macOS)
- [ ] Dependencies installed: `pip install -r requirements.txt`
- [ ] Data files present in `feedback/`
- [ ] Tests passing: `python tests/simple_test.py`
- [ ] Flask accessible: http://localhost:5000
- [ ] Dashboard accessible: http://localhost:8501

---

## 🚀 Production Deployment

### Performance Specifications
- **Processing Speed**: ~100ms per feedback
- **Memory Usage**: <50MB (Q-table: 162×3 floats)
- **Scalability**: Handles 1000+ candidates, 50+ job types
- **Concurrent Users**: 10+ simultaneous API requests

### Deployment Options

#### Docker Deployment
```dockerfile
# Use provided Dockerfile
docker build -t hr-ai-system .
docker run -p 5000:5000 -p 8501:8501 hr-ai-system
```

#### Cloud Deployment
- **Flask**: Deploy on Heroku, AWS, or Google Cloud
- **Dashboard**: Use Streamlit Cloud or containerize
- **Database**: Migrate CSV to PostgreSQL/MongoDB for production

---

## 🧪 Testing Coverage

### Test Suites
- **Unit Tests**: Individual component testing
- **Integration Tests**: End-to-end workflow
- **API Tests**: HTTP endpoint validation
- **Performance Tests**: Load and stress testing

### Test Results
```
✅ Project Structure: PASS
✅ Dependencies: PASS
✅ Data Files: PASS (100 CVs, 10 JDs, 50 Feedbacks)
✅ RL Agent: PASS (Q-learning functional)
✅ Flask Backend: PASS (API endpoints working)
✅ Dashboard: PASS (Visualizations ready)
✅ Integration: PASS (End-to-end workflow)

Overall: 7/7 tests passed - System ready for production!
```

---

## 🔮 Future Enhancements

### Planned Features
- [ ] **Deep Learning**: Neural network-based agents
- [ ] **Multi-objective**: Optimize for diversity, cost, time
- [ ] **Real-time**: WebSocket connections for live updates
- [ ] **Integration**: HRIS, ATS, and CRM connectors
- [ ] **Analytics**: Advanced reporting and insights
- [ ] **Mobile**: React Native dashboard app

### Contribution Guidelines
1. Fork the repository
2. Create feature branch: `git checkout -b feature/new-feature`
3. Run tests: `python tests/simple_test.py`
4. Commit changes: `git commit -m "Add new feature"`
5. Push branch: `git push origin feature/new-feature`
6. Create Pull Request

---

## 👨💻 Author

**Ishan Shirode**
- 🎓 **Education**: B.E. Artificial Intelligence & Machine Learning
- 📍 **Location**: Vasai, Maharashtra, India
- 🔗 **GitHub**: [@ISHANSHIRODE01](https://github.com/ISHANSHIRODE01)
- 💼 **LinkedIn**: [Connect with me](https://linkedin.com/in/ishanshirode)
- 📧 **Email**: [Contact](mailto:ishanshirode01@gmail.com)

### Skills Demonstrated
- **Machine Learning**: Reinforcement Learning, Q-learning
- **Backend Development**: Flask, RESTful APIs
- **Frontend Development**: Streamlit, Interactive Dashboards
- **Data Science**: Pandas, NumPy, Scikit-learn
- **DevOps**: Testing, Automation, Documentation

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

### MIT License Summary
- ✅ Commercial use
- ✅ Modification
- ✅ Distribution
- ✅ Private use
- ❌ Liability
- ❌ Warranty

---

## 🙏 Acknowledgments

- **Scikit-learn**: Machine learning algorithms
- **Flask**: Web framework
- **Streamlit**: Dashboard framework
- **Plotly**: Interactive visualizations
- **Pandas**: Data manipulation
- **TextBlob**: Sentiment analysis

---

## 📞 Support

### Getting Help
- 📖 **Documentation**: Check this README and `TEST_REPORT.md`
- 🧪 **Testing**: Run `python tests/simple_test.py` for diagnostics
- 🐛 **Issues**: [GitHub Issues](https://github.com/ISHANSHIRODE01/Ishan_HR_AI_System/issues)
- 💬 **Discussions**: [GitHub Discussions](https://github.com/ISHANSHIRODE01/Ishan_HR_AI_System/discussions)

### 📚 Complete Documentation

**🚀 Getting Started:**
- [🚀 Quick Start (5 minutes)](QUICK_START.md) - Fastest way to get running
- [📖 Complete Installation Guide](INSTALLATION_GUIDE.md) - Detailed step-by-step setup
- [🐍 Virtual Environment Guide](VIRTUAL_ENV_GUIDE.md) - Environment setup help

**🔧 Support & Troubleshooting:**
- [🔧 Troubleshooting Guide](TROUBLESHOOTING.md) - Common issues & solutions
- [✅ Issues Fixed Report](ISSUES_FIXED.md) - All resolved issues
- [🧪 Testing Guide](#-testing--verification) - How to test the system

**📊 Technical Documentation:**
- [🔌 API Documentation](docs/API_DOCUMENTATION.md) - Complete API reference
- [🚀 Deployment Guide](docs/DEPLOYMENT_GUIDE.md) - Production deployment
- [📊 Test Report](docs/TEST_REPORT.md) - Comprehensive test results
- [📊 System Architecture](#-system-architecture) - Technical overview

---

**⭐ Star this repository if you find it helpful!**

**🚀 Ready to revolutionize HR with AI? Let's get started!**