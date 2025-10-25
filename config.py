import os
from pathlib import Path

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

# Environment variables
GOOGLE_AI_API_KEY = os.getenv("GOOGLE_AI_API_KEY")

# Validation and auto-generation
def validate_data_files(auto_create=True):
    """Validate that all required data files exist, optionally create them if missing"""
    required_files = [CVS_PATH, JDS_PATH, FEEDBACKS_PATH]
    missing_files = [f for f in required_files if not f.exists()]
    
    if missing_files:
        if auto_create:
            print(f"⚠️  Missing data files detected: {[f.name for f in missing_files]}")
            print("🔧 Auto-generating sample data files...")
            
            try:
                # Import here to avoid circular imports
                import sys
                sys.path.append(str(PROJECT_ROOT))
                from agents.data_generator import ensure_data_files_exist
                
                created_files = ensure_data_files_exist(DATA_DIR)
                if created_files:
                    print(f"✅ Successfully created: {', '.join(created_files)}")
                    return True
            except Exception as e:
                print(f"❌ Failed to auto-generate data files: {e}")
                print("📋 Please manually create the required CSV files in the feedback/ directory")
                raise FileNotFoundError(f"Missing required files: {[f.name for f in missing_files]}")
        else:
            raise FileNotFoundError(f"Missing required files: {[f.name for f in missing_files]}")
    
    return True

def ensure_directories():
    """Ensure all required directories exist"""
    DATA_DIR.mkdir(exist_ok=True)
    MODELS_DIR.mkdir(exist_ok=True)
    print(f"📁 Directories ready: {DATA_DIR.name}/, {MODELS_DIR.name}/")