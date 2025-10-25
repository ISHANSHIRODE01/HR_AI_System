# Security Guidelines - HR AI System

## 🔐 **Environment Variables Security**

### **API Key Protection**
- **Never commit API keys** to version control
- Use `.env` file for local development (ignored by git)
- Use environment variables in production
- Rotate API keys regularly

### **Setup Instructions**
```bash
# Copy template
cp .env.example .env

# Edit with your keys (this file is git-ignored)
nano .env

# Add your API key
GOOGLE_AI_API_KEY=your_actual_api_key_here
```

## 🛡️ **Production Security**

### **Environment Variables**
```bash
# Set in production environment
export GOOGLE_AI_API_KEY=your_key
export FLASK_ENV=production
export SECRET_KEY=your_secret_key
```

### **API Security**
- Implement authentication for production
- Use HTTPS in production
- Rate limiting for API endpoints
- Input validation and sanitization

### **Data Security**
- Encrypt sensitive data at rest
- Use secure database connections
- Regular security audits
- Access logging

## 🔍 **Security Checklist**

- [ ] `.env` file not committed to git
- [ ] API keys stored securely
- [ ] Production uses environment variables
- [ ] HTTPS enabled in production
- [ ] Authentication implemented
- [ ] Input validation in place
- [ ] Regular security updates
- [ ] Access logs monitored

## 📞 **Reporting Security Issues**

If you discover a security vulnerability, please:
1. **Do not** create a public GitHub issue
2. Email security concerns privately
3. Provide detailed information about the vulnerability
4. Allow time for fixes before public disclosure