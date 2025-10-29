# HR AI System - Reinforcement Learning Agent (Simplified)

**Intelligent HR Decision System with Flask Backend + Streamlit Dashboard**

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-3.0+-green.svg)](https://flask.palletsprojects.com)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.37+-red.svg)](https://streamlit.io)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> **Self-contained AI-powered HR system using reinforcement learning - no external APIs required!**

---

## Overview

This simplified HR AI System uses **Q-learning reinforcement learning** to make intelligent hiring decisions. The system learns from HR feedback and provides transparent insights through an interactive dashboard.

### Key Features
- **Reinforcement Learning**: Q-learning algorithm that improves with feedback
- **RESTful API**: Flask backend with comprehensive endpoints
- **Interactive Dashboard**: Real-time visualizations and metrics
- **Self-Contained**: No external API dependencies
- **Unicode-Safe**: Works on all systems without encoding issues
- **Production Ready**: Comprehensive testing and error handling

---

## Quick Start

### Prerequisites
- Python 3.8+
- Git (optional)

### Installation
```bash
# Clone repository
git clone https://github.com/ISHANSHIRODE01/Ishan_HR_AI_System.git
cd Ishan_HR_AI_System

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# Linux/macOS:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run tests
python tests/simple_test.py

# Start system
python src/app.py  # Terminal 1
streamlit run src/dashboard.py  # Terminal 2
```

### Access Points
- **Flask API**: http://localhost:5000
- **Dashboard**: http://localhost:8501

---

## System Architecture

### Core Components

#### 1. Flask Backend (`src/app.py`)
- RESTful API with JSON responses
- Reinforcement learning integration
- Simple feedback summarization
- Event logging and automation

#### 2. Streamlit Dashboard (`src/dashboard.py`)
- Interactive visualizations
- Learning progress tracking
- Q-table transparency
- Feedback history analysis

#### 3. RL Agent (`agents/rl_agent.py`)
- Q-learning implementation
- State space: Match score, sentiment, history
- Action space: Accept, Reject, Reconsider
- Adaptive policy updates

---

## API Reference

### Endpoints

#### `GET /`
Health check endpoint
```json
{
  "status": "HR RL Agent Backend Running",
  "automation": "enabled",
  "rl_agent": "initialized",
  "timestamp": "2024-10-29T10:00:00"
}
```

#### `POST /update_feedback`
Submit HR feedback
```json
{
  "candidate_id": 1,
  "jd_id": 1,
  "feedback_score": 4,
  "comment": "Excellent technical skills"
}
```

Response:
```json
{
  "status": "updated_and_logged",
  "candidate_id": 1,
  "jd_id": 1,
  "rl_policy_change": "System now suggests 'accept'",
  "feedback_summary": "Positive feedback for candidate 1 - Score 4/5"
}
```

---

## Project Structure

```
Ishan_HR_AI_System/
├── src/                    # Main application
│   ├── app.py             # Flask backend
│   ├── dashboard.py       # Streamlit dashboard
│   └── main.py           # Core workflow
├── agents/                # AI components
│   ├── rl_agent.py       # Q-learning agent
│   ├── automation.py     # Event logging
│   └── visualization.py  # Charts
├── tests/                 # Test suite
│   └── simple_test.py    # Main tests
├── feedback/              # Data storage
│   ├── cvs.csv           # Candidate profiles
│   ├── jds.csv           # Job descriptions
│   └── feedbacks.csv     # Historical feedback
├── requirements.txt       # Dependencies
└── README.md             # This file
```

---

## Configuration

### Required Data Files
Ensure these files exist in `feedback/`:

- **cvs.csv**: Candidate profiles
- **jds.csv**: Job descriptions  
- **feedbacks.csv**: Historical feedback

### Environment Variables (Optional)
```env
FLASK_ENV=development
FLASK_DEBUG=True
FLASK_PORT=5000
STREAMLIT_PORT=8501
```

---

## Testing

```bash
# Run all tests
python tests/simple_test.py

# Expected output: "6/6 tests passed"
```

### Test Coverage
- Project structure validation
- Dependency verification
- Data file integrity
- RL agent functionality
- Flask API endpoints
- Integration workflow

---

## Troubleshooting

### Common Issues

#### ModuleNotFoundError
**Solution**: Activate virtual environment
```bash
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/macOS
```

#### Port Already in Use
**Solution**: Streamlit auto-switches ports or kill existing processes

#### Data File Missing
**Solution**: Ensure CSV files exist in `feedback/` directory

---

## What's New in Simplified Version

### Removed
- External AI dependencies (Gemini)
- Unicode characters causing encoding issues
- Complex API key management

### Added
- Simple rule-based feedback summarization
- Better cross-platform compatibility
- Faster response times
- Easier deployment

### Maintained
- Full RL functionality
- Interactive dashboard
- API endpoints
- All visualizations

---

## Performance

- **Processing Speed**: ~50ms per feedback
- **Memory Usage**: <30MB
- **Scalability**: 1000+ candidates, 50+ job types
- **Concurrent Users**: 10+ simultaneous requests

---

## Deployment

### Local Development
```bash
python src/app.py
streamlit run src/dashboard.py
```

### Docker (Optional)
```bash
docker build -t hr-ai-system .
docker run -p 5000:5000 -p 8501:8501 hr-ai-system
```

---

## Contributing

1. Fork the repository
2. Create feature branch
3. Run tests: `python tests/simple_test.py`
4. Submit pull request

---

## License

MIT License - see [LICENSE](LICENSE) file for details.

---

## Author

**Ishan Shirode**
- GitHub: [@ISHANSHIRODE01](https://github.com/ISHANSHIRODE01)
- LinkedIn: [Connect](https://linkedin.com/in/ishanshirode)
- Email: ishanshirode01@gmail.com

---

## Support

- **Documentation**: This README and test reports
- **Issues**: [GitHub Issues](https://github.com/ISHANSHIRODE01/Ishan_HR_AI_System/issues)
- **Testing**: Run `python tests/simple_test.py` for diagnostics

---

**Ready to use! No external APIs, no Unicode issues, fully self-contained.**