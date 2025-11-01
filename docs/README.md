# HR-AI Core Autonomy Upgrade

## Overview
Intelligent HR decision system with reinforcement learning and multi-channel automation.

## Features
- **RL-powered matching** - Q-learning algorithm for candidate-job matching
- **Multi-channel automation** - Email, WhatsApp, and voice notifications
- **Feedback loop** - HR feedback trains the RL model
- **Real-time dashboard** - Streamlit interface for system management

## Quick Start

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Start API Server
```bash
uvicorn app.main:app --reload
```

### 3. Launch Dashboard
```bash
streamlit run dashboard/app.py
```

## API Endpoints

### Candidates
- `POST /candidate/add` - Add new candidate
- `GET /candidate/list` - List all candidates
- `POST /candidate/match` - Get RL recommendation

### Feedback
- `POST /feedback/` - Submit system feedback
- `POST /feedback/hr_feedback` - Submit HR feedback
- `GET /feedback/logs` - View feedback history

### Automation
- `POST /trigger/` - Trigger automation events
- `GET /trigger/history/{id}` - View automation history

## Architecture
- **FastAPI** - REST API framework
- **Q-Learning** - Reinforcement learning algorithm
- **Streamlit** - Dashboard interface
- **JSON** - Data storage (easily replaceable with database)

## Event Types
- `shortlisted` - Email + WhatsApp notification
- `rejected` - Email notification only
- `onboarding_completed` - Voice call trigger
- `interview_scheduled` - Email + WhatsApp notification