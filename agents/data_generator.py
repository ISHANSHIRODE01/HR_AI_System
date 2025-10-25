"""
Data Generator for HR AI System
Automatically creates sample data files if they're missing
"""
import pandas as pd
import os
from pathlib import Path

def generate_sample_cvs(file_path: str, num_candidates: int = 20):
    """Generate sample CV data"""
    skills_pool = [
        "Python", "Machine Learning", "Data Analysis", "TensorFlow", "Flask",
        "React", "SQL", "Docker", "Git", "Pandas", "Scikit-learn", "NLP",
        "Computer Vision", "Deep Learning", "Statistics"
    ]
    
    educations = ["B.E. Computer", "B.E. IT", "B.Tech AI", "M.Sc Data Science"]
    locations = ["Mumbai", "Delhi", "Bangalore", "Pune", "Chennai"]
    
    data = []
    for i in range(1, num_candidates + 1):
        # Select 3-5 random skills
        import random
        selected_skills = random.sample(skills_pool, random.randint(3, 5))
        
        data.append({
            'candidate_id': i,
            'name': f'Candidate {i}',
            'education': random.choice(educations),
            'experience_years': random.randint(0, 8),
            'skills': ', '.join(selected_skills),
            'location': random.choice(locations)
        })
    
    df = pd.DataFrame(data)
    df.to_csv(file_path, index=False)
    return df

def generate_sample_jds(file_path: str):
    """Generate sample job descriptions"""
    jobs = [
        (1, "Data Scientist", "Analyze data, build ML models, and deliver insights using Python and statistics."),
        (2, "ML Engineer", "Deploy scalable machine learning models using TensorFlow and Docker."),
        (3, "Frontend Developer", "Develop responsive UIs using React and integrate with backend APIs."),
        (4, "Backend Developer", "Build RESTful APIs using Flask or FastAPI and manage databases with SQL."),
        (5, "Data Analyst", "Perform exploratory data analysis and create visual reports with Pandas."),
        (6, "AI Researcher", "Work on deep learning models, optimization, and new AI architectures."),
        (7, "DevOps Engineer", "Automate deployment pipelines, manage Docker containers, and CI/CD processes."),
        (8, "NLP Engineer", "Develop NLP pipelines for sentiment analysis and chatbot systems."),
        (9, "Computer Vision Engineer", "Design and implement object detection and image classification models."),
        (10, "Full Stack Developer", "Build complete web solutions integrating frontend and backend technologies.")
    ]
    
    df = pd.DataFrame(jobs, columns=['jd_id', 'title', 'description'])
    df.to_csv(file_path, index=False)
    return df

def generate_sample_feedbacks(file_path: str, num_feedbacks: int = 20):
    """Generate sample feedback data"""
    comments = [
        "Excellent technical skills and good communication",
        "Strong background but needs more experience",
        "Perfect fit for the role requirements",
        "Good candidate with room for improvement",
        "Outstanding problem-solving abilities",
        "Lacks some key technical skills",
        "Great team player with solid experience",
        "Needs improvement in specific areas",
        "Exceptional candidate with strong portfolio",
        "Average performance in technical assessment"
    ]
    
    data = []
    import random
    for i in range(1, num_feedbacks + 1):
        data.append({
            'feedback_id': i,
            'candidate_id': random.randint(1, 20),
            'jd_id': random.randint(1, 10),
            'feedback_score': random.randint(1, 5),
            'comment': random.choice(comments)
        })
    
    df = pd.DataFrame(data)
    df.to_csv(file_path, index=False)
    return df

def ensure_data_files_exist(data_dir: Path):
    """Ensure all required data files exist, create them if missing"""
    cvs_path = data_dir / "cvs.csv"
    jds_path = data_dir / "jds.csv"
    feedbacks_path = data_dir / "feedbacks.csv"
    
    created_files = []
    
    # Create data directory if it doesn't exist
    data_dir.mkdir(exist_ok=True)
    
    # Generate CVs if missing
    if not cvs_path.exists():
        print(f"Creating sample CVs file: {cvs_path}")
        generate_sample_cvs(str(cvs_path))
        created_files.append("cvs.csv")
    
    # Generate JDs if missing
    if not jds_path.exists():
        print(f"Creating sample JDs file: {jds_path}")
        generate_sample_jds(str(jds_path))
        created_files.append("jds.csv")
    
    # Generate feedbacks if missing
    if not feedbacks_path.exists():
        print(f"Creating sample feedbacks file: {feedbacks_path}")
        generate_sample_feedbacks(str(feedbacks_path))
        created_files.append("feedbacks.csv")
    
    if created_files:
        print(f"✅ Created missing data files: {', '.join(created_files)}")
        print("🚀 System is now ready to run!")
    
    return created_files

if __name__ == "__main__":
    # Test the data generator
    from pathlib import Path
    test_dir = Path("test_data")
    ensure_data_files_exist(test_dir)