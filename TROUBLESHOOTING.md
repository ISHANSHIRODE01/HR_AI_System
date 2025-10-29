# Troubleshooting Guide - HR AI System (Simplified)

## Common Issues and Solutions

### Installation Issues

#### 1. "python: command not found"
**Symptoms**: Command not recognized
**Cause**: Python not installed or not in PATH
**Solution**:
```bash
# Try python3 instead
python3 --version

# Or download Python from python.org
# Ensure "Add to PATH" is checked during installation
```

#### 2. "ModuleNotFoundError" or Import Errors
**Symptoms**: Cannot import required modules
**Cause**: Virtual environment not activated
**Solution**:
```bash
# Activate virtual environment
# Windows:
venv\Scripts\activate

# Linux/macOS:
source venv/bin/activate

# Verify activation (should show (venv) in prompt)
# Reinstall if needed:
pip install -r requirements.txt
```

#### 3. "Permission denied" Errors
**Symptoms**: Cannot create files or install packages
**Cause**: Insufficient permissions
**Solution**:
```bash
# Windows: Run as Administrator
# Linux/macOS: Use sudo for system-wide installs
sudo pip install -r requirements.txt

# Or use user install:
pip install --user -r requirements.txt
```

### Runtime Issues

#### 4. "Port already in use"
**Symptoms**: Flask or Streamlit won't start
**Cause**: Another application using the port
**Solution**:
```bash
# Streamlit automatically switches to 8503
# Or manually specify different ports:
python src/app.py --port 5001
streamlit run src/dashboard.py --server.port 8502

# Kill existing processes (Windows):
netstat -ano | findstr :5000
taskkill /PID <process_id> /F

# Kill existing processes (Linux/macOS):
lsof -ti:5000 | xargs kill -9
```

#### 5. "CSV file not found" or Data Errors
**Symptoms**: FileNotFoundError for CSV files
**Cause**: Missing data files or wrong directory
**Solution**:
```bash
# Verify you're in project root:
ls feedback/
# Should show: cvs.csv, jds.csv, feedbacks.csv

# Check file structure:
python -c "import pandas as pd; print(pd.read_csv('feedback/cvs.csv').columns)"
```

#### 6. "RL Agent not initialized"
**Symptoms**: API returns 500 error
**Cause**: Data files missing or corrupted
**Solution**:
```bash
# Run tests to diagnose:
python tests/simple_test.py

# Check data file integrity:
python -c "
import pandas as pd
try:
    cvs = pd.read_csv('feedback/cvs.csv')
    jds = pd.read_csv('feedback/jds.csv')
    print('Data files OK')
except Exception as e:
    print(f'Data error: {e}')
"
```

### System-Specific Issues

#### 7. Windows Encoding Issues (Fixed in Simplified Version)
**Symptoms**: Unicode characters not displaying
**Cause**: Terminal encoding issues
**Solution**: 
- **Fixed**: All Unicode characters removed in simplified version
- System now uses only ASCII characters

#### 8. Streamlit Not Opening in Browser
**Symptoms**: Dashboard doesn't auto-open
**Cause**: Browser configuration or firewall
**Solution**:
```bash
# Manually open: http://localhost:8501
# Or try different port:
streamlit run src/dashboard.py --server.port 8502

# Check if Streamlit is running:
curl http://localhost:8501
```

#### 9. Slow Performance
**Symptoms**: System responds slowly
**Cause**: Large dataset or insufficient resources
**Solution**:
- Reduce dataset size for testing
- Ensure virtual environment is activated
- Close unnecessary applications
- Check system resources

### Testing and Validation

#### 10. Tests Failing
**Symptoms**: `python tests/simple_test.py` shows failures
**Cause**: Various configuration issues
**Solution**:
```bash
# Run individual test components:
python tests/test_config.py
python tests/test_flask_only.py

# Check specific error messages and fix accordingly
```

#### 11. API Not Responding
**Symptoms**: curl or HTTP requests fail
**Cause**: Flask not running or wrong URL
**Solution**:
```bash
# Verify Flask is running:
curl http://localhost:5000/

# Check Flask logs for errors
# Restart Flask if needed:
python src/app.py
```

### Development Issues

#### 12. Code Changes Not Reflected
**Symptoms**: Modifications don't appear
**Cause**: Caching or not restarting services
**Solution**:
```bash
# Restart Flask (Ctrl+C then restart):
python src/app.py

# Restart Streamlit (Ctrl+C then restart):
streamlit run src/dashboard.py

# Clear Streamlit cache:
streamlit cache clear
```

## Diagnostic Commands

### System Health Check
```bash
# Run comprehensive tests:
python tests/simple_test.py

# Check Python environment:
python -c "import sys; print(sys.executable)"

# Verify virtual environment:
pip list | grep -E "(flask|streamlit|pandas)"
```

### Quick Diagnostics
```bash
# Check project structure:
ls -la

# Verify data files:
ls -la feedback/

# Test imports:
python -c "
import pandas as pd
import flask
import streamlit
print('All imports successful')
"
```

### Performance Check
```bash
# Memory usage:
python -c "
import psutil
print(f'Memory: {psutil.virtual_memory().percent}%')
print(f'CPU: {psutil.cpu_percent()}%')
"
```

## Getting Help

### Self-Diagnosis Steps
1. **Run Tests**: `python tests/simple_test.py`
2. **Check Logs**: Look at terminal output for errors
3. **Verify Environment**: Ensure virtual environment is activated
4. **Check Files**: Confirm all required files exist
5. **Restart Services**: Stop and restart Flask/Streamlit

### When to Seek Help
- All tests failing after following troubleshooting steps
- Persistent errors not covered in this guide
- System-specific issues not documented

### How to Report Issues
1. **Run Diagnostics**: Include output of `python tests/simple_test.py`
2. **Environment Info**: Python version, OS, error messages
3. **Steps to Reproduce**: What you were doing when error occurred
4. **Expected vs Actual**: What should happen vs what actually happens

## Prevention Tips

### Best Practices
- Always activate virtual environment before running commands
- Keep dependencies updated: `pip install -r requirements.txt --upgrade`
- Regular testing: Run tests after any changes
- Backup data: Keep copies of your CSV files
- Monitor resources: Ensure adequate memory and disk space

### Maintenance
```bash
# Weekly health check:
python tests/simple_test.py

# Monthly dependency update:
pip install -r requirements.txt --upgrade

# Clean up logs periodically:
# Check feedback/system_log.json size
```

**Most issues are resolved by ensuring the virtual environment is activated and all dependencies are properly installed.**