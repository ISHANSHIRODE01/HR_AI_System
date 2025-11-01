import re

class SentimentModel:
    def __init__(self):
        self.positive_words = ["excellent", "great", "good", "outstanding", "skilled", "experienced"]
        self.negative_words = ["poor", "bad", "weak", "inexperienced", "lacking", "insufficient"]
    
    def analyze_feedback(self, text):
        text = text.lower()
        positive_count = sum(1 for word in self.positive_words if word in text)
        negative_count = sum(1 for word in self.negative_words if word in text)
        
        if positive_count > negative_count:
            return {"sentiment": "positive", "score": 0.8}
        elif negative_count > positive_count:
            return {"sentiment": "negative", "score": 0.2}
        else:
            return {"sentiment": "neutral", "score": 0.5}
    
    def calculate_match_score(self, candidate_skills, job_requirements):
        skills = set(candidate_skills.lower().split())
        requirements = set(job_requirements.lower().split())
        overlap = len(skills.intersection(requirements))
        total = len(requirements)
        return overlap / total if total > 0 else 0.0