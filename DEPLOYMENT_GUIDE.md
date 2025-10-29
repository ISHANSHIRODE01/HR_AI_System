# Deployment Guide - HR AI System (Simplified)

## Overview
This guide covers deployment options for the simplified HR AI System, from local development to production environments.

## Local Development Deployment

### Quick Setup
```bash
# Clone and setup
git clone https://github.com/ISHANSHIRODE01/Ishan_HR_AI_System.git
cd Ishan_HR_AI_System
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/macOS
pip install -r requirements.txt

# Start services
python src/app.py  # Terminal 1
streamlit run src/dashboard.py  # Terminal 2
```

### Access Points
- **Flask API**: http://localhost:5000
- **Dashboard**: http://localhost:8501

## Production Deployment Options

### Option 1: Docker Deployment (Recommended)

#### Create Dockerfile
```dockerfile
FROM python:3.9-slim

WORKDIR /app

# Copy requirements first for better caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Expose ports
EXPOSE 5000 8501

# Create startup script
RUN echo '#!/bin/bash\npython src/app.py &\nstreamlit run src/dashboard.py --server.port 8501 --server.address 0.0.0.0' > start.sh
RUN chmod +x start.sh

CMD ["./start.sh"]
```

#### Build and Run
```bash
# Build image
docker build -t hr-ai-system .

# Run container
docker run -p 5000:5000 -p 8501:8501 hr-ai-system

# Or with docker-compose
```

#### Docker Compose (docker-compose.yml)
```yaml
version: '3.8'
services:
  hr-ai-system:
    build: .
    ports:
      - "5000:5000"
      - "8501:8501"
    volumes:
      - ./feedback:/app/feedback
    environment:
      - FLASK_ENV=production
    restart: unless-stopped
```

### Option 2: Cloud Platform Deployment

#### Heroku Deployment
```bash
# Install Heroku CLI
# Create Procfile
echo "web: python src/app.py" > Procfile
echo "dashboard: streamlit run src/dashboard.py --server.port \$PORT" >> Procfile

# Deploy
heroku create your-hr-ai-system
git push heroku main
```

#### AWS EC2 Deployment
```bash
# Launch EC2 instance (Ubuntu)
# SSH into instance
ssh -i your-key.pem ubuntu@your-ec2-ip

# Install dependencies
sudo apt update
sudo apt install python3 python3-pip python3-venv git

# Clone and setup
git clone https://github.com/ISHANSHIRODE01/Ishan_HR_AI_System.git
cd Ishan_HR_AI_System
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Create systemd service
sudo nano /etc/systemd/system/hr-ai-flask.service
```

#### Systemd Service File
```ini
[Unit]
Description=HR AI Flask Backend
After=network.target

[Service]
Type=simple
User=ubuntu
WorkingDirectory=/home/ubuntu/Ishan_HR_AI_System
Environment=PATH=/home/ubuntu/Ishan_HR_AI_System/venv/bin
ExecStart=/home/ubuntu/Ishan_HR_AI_System/venv/bin/python src/app.py
Restart=always

[Install]
WantedBy=multi-user.target
```

#### Enable and Start Service
```bash
sudo systemctl daemon-reload
sudo systemctl enable hr-ai-flask
sudo systemctl start hr-ai-flask
sudo systemctl status hr-ai-flask
```

### Option 3: Nginx + Gunicorn (Production)

#### Install Gunicorn
```bash
pip install gunicorn
```

#### Create WSGI Entry Point (wsgi.py)
```python
from src.app import app

if __name__ == "__main__":
    app.run()
```

#### Gunicorn Configuration (gunicorn.conf.py)
```python
bind = "127.0.0.1:5000"
workers = 2
worker_class = "sync"
timeout = 30
keepalive = 2
max_requests = 1000
max_requests_jitter = 100
```

#### Start with Gunicorn
```bash
gunicorn --config gunicorn.conf.py wsgi:app
```

#### Nginx Configuration
```nginx
server {
    listen 80;
    server_name your-domain.com;

    location / {
        proxy_pass http://127.0.0.1:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }

    location /dashboard {
        proxy_pass http://127.0.0.1:8501;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
    }
}
```

## Environment Configuration

### Production Environment Variables
```env
# Production settings
FLASK_ENV=production
FLASK_DEBUG=False
FLASK_PORT=5000

# Streamlit settings
STREAMLIT_PORT=8501
STREAMLIT_SERVER_ADDRESS=0.0.0.0

# Security (if needed)
SECRET_KEY=your-secret-key-here
```

### Security Considerations
```bash
# Create non-root user
sudo useradd -m -s /bin/bash hraiuser
sudo usermod -aG sudo hraiuser

# Set proper permissions
chmod 755 /home/hraiuser/Ishan_HR_AI_System
chmod 644 feedback/*.csv

# Firewall configuration
sudo ufw allow 22  # SSH
sudo ufw allow 80  # HTTP
sudo ufw allow 443 # HTTPS
sudo ufw enable
```

## Monitoring and Logging

### Application Logging
```python
# Add to src/app.py
import logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s',
    handlers=[
        logging.FileHandler('logs/app.log'),
        logging.StreamHandler()
    ]
)
```

### System Monitoring
```bash
# Monitor system resources
htop
df -h
free -m

# Monitor application logs
tail -f logs/app.log

# Monitor system logs
journalctl -u hr-ai-flask -f
```

### Health Check Endpoint
The system includes `/health` endpoint for monitoring:
```bash
# Check system health
curl http://your-domain.com/health

# Expected response includes system status
```

## Backup and Recovery

### Data Backup
```bash
# Backup CSV files
tar -czf backup-$(date +%Y%m%d).tar.gz feedback/

# Automated backup script
#!/bin/bash
DATE=$(date +%Y%m%d_%H%M%S)
tar -czf /backups/hr-ai-backup-$DATE.tar.gz feedback/
find /backups -name "hr-ai-backup-*.tar.gz" -mtime +7 -delete
```

### Recovery Process
```bash
# Restore from backup
tar -xzf backup-20241029.tar.gz
# Restart services
sudo systemctl restart hr-ai-flask
```

## Performance Optimization

### System Requirements
- **Minimum**: 1 CPU, 512MB RAM, 1GB storage
- **Recommended**: 2 CPU, 1GB RAM, 5GB storage
- **High Load**: 4 CPU, 2GB RAM, 10GB storage

### Optimization Tips
```bash
# Increase worker processes for high load
gunicorn --workers 4 --config gunicorn.conf.py wsgi:app

# Enable gzip compression in Nginx
gzip on;
gzip_types text/plain application/json;

# Use SSD storage for better I/O performance
```

## SSL/HTTPS Setup

### Let's Encrypt (Free SSL)
```bash
# Install certbot
sudo apt install certbot python3-certbot-nginx

# Get certificate
sudo certbot --nginx -d your-domain.com

# Auto-renewal
sudo crontab -e
# Add: 0 12 * * * /usr/bin/certbot renew --quiet
```

## Scaling Considerations

### Horizontal Scaling
- Deploy multiple instances behind load balancer
- Use shared storage for CSV files
- Consider database migration for high volume

### Vertical Scaling
- Increase CPU and memory as needed
- Monitor resource usage and scale accordingly

### Database Migration (Future)
```python
# For high volume, consider migrating from CSV to database
# PostgreSQL or MongoDB recommended
```

## Troubleshooting Production Issues

### Common Production Issues
1. **Port conflicts**: Use different ports or kill conflicting processes
2. **Permission errors**: Check file permissions and user access
3. **Memory issues**: Monitor and increase if needed
4. **Network issues**: Check firewall and security groups

### Debug Commands
```bash
# Check service status
sudo systemctl status hr-ai-flask

# View logs
journalctl -u hr-ai-flask --since "1 hour ago"

# Check ports
netstat -tlnp | grep :5000

# Monitor resources
top -p $(pgrep -f "python src/app.py")
```

## Maintenance

### Regular Maintenance Tasks
- Monitor disk space and clean logs
- Update dependencies monthly
- Backup data weekly
- Monitor system performance
- Review security updates

### Update Process
```bash
# Backup current version
tar -czf backup-before-update.tar.gz .

# Pull updates
git pull origin main

# Update dependencies
pip install -r requirements.txt --upgrade

# Run tests
python tests/simple_test.py

# Restart services
sudo systemctl restart hr-ai-flask
```

**Your HR AI System is now ready for production deployment!**