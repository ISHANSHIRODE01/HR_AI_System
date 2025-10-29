import os
from pathlib import Path

# Load environment variables from .env file
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    # dotenv not installed, try manual .env loading
    env_file = Path(__file__).parent / ".env"
    if env_file.exists():
        with open(env_file) as f:
            for line in f:
                if line.strip() and not line.startswith('#'):
                    key, value = line.strip().split('=', 1)
                    os.environ[key] = value.strip('"\'')

# Project root directory
PROJECT_ROOT = Path(__file__).parent.absolute()

# Data paths
DATA_DIR = PROJECT_ROOT / "feedback"
CVS_PATH = DATA_DIR / "cvs.csv"
JDS_PATH = DATA_DIR / "jds.csv"
FEEDBACKS_PATH = DATA_DIR / "feedbacks.csv"
FEEDBACK_LOG_PATH = DATA_DIR / "feedback_log.csv"
SYSTEM_LOG_PATH = DATA_DIR / "system_log.json"

# Model paths
MODELS_DIR = PROJECT_ROOT / "models"
SENTIMENT_MODEL_PATH = MODELS_DIR / "sentiment_model.pkl"
TFIDF_MODEL_PATH = MODELS_DIR / "tfidf_model.pkl"

# Environment variables - Gemini integration removed for simplicity

# Validation
def validate_data_files():
    """Validate that all required data files exist"""
    required_files = [CVS_PATH, JDS_PATH, FEEDBACKS_PATH]
    missing_files = [f for f in required_files if not f.exists()]
    
    if missing_files:
        raise FileNotFoundError(f"Missing required files: {missing_files}")
    
    return True