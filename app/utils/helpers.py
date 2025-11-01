import json
from datetime import datetime
from pathlib import Path

def load_json(file_path):
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_json(data, file_path):
    Path(file_path).parent.mkdir(exist_ok=True)
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=2)

def calculate_reward(feedback_score, action_taken, actual_outcome):
    if action_taken == actual_outcome:
        return feedback_score / 5.0
    else:
        return -0.5

def format_timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def validate_candidate_data(candidate):
    required_fields = ["id", "name", "skills"]
    return all(field in candidate for field in required_fields)