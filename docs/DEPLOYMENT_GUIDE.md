# Deployment Guide - HR AI System

## 🚀 **Production Deployment Options**

### **Option 1: Local Production Server**

**Requirements:**
- Linux/Windows Server
- Python 3.8+
- 4GB+ RAM
- 10GB+ Storage

**Setup:**
```bash
# Clone repository
git clone https://github.com/ISHANSHIRODE01/Ishan_HR_AI_System.git
cd Ishan_HR_AI_System

# Setup production environment
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Install production server
pip install gunicorn

# Start Flask with Gunicorn
gunicorn --bind 0.0.0.0:5000 src.app:app

# Start Streamlit
streamlit run src/dashboard.py --server.port 8501 --server.address 0.0.0.0
```

### **Option 2: Docker Deployment**

**Dockerfile:**
```dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000 8501

CMD ["python", "src/app.py"]
```

**Docker Commands:**
```bash
# Build image
docker build -t hr-ai-system .

# Run container
docker run -p 5000:5000 -p 8501:8501 hr-ai-system
```

### **Option 3: Cloud Deployment**

**Heroku:**
```bash
# Install Heroku CLI
# Create Procfile
echo "web: gunicorn src.app:app" > Procfile

# Deploy
heroku create your-hr-ai-system
git push heroku main
```

**AWS/Google Cloud:**
- Use container services (ECS, Cloud Run)
- Deploy Docker image
- Configure load balancer

## 🔧 **Production Configuration**

**Environment Variables:**
```bash
export FLASK_ENV=production
export GOOGLE_AI_API_KEY=your_key_here
export DATABASE_URL=your_db_url
```

**Security:**
- Use HTTPS
- Set up authentication
- Configure firewall
- Regular security updates

## 📊 **Monitoring**

**Health Checks:**
- Flask: `GET /health`
- Dashboard: Monitor Streamlit process
- Database: Connection monitoring

**Logging:**
- Application logs
- Error tracking
- Performance metrics