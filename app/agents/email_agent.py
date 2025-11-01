from datetime import datetime
from app.utils.helpers import load_json

def send_email(candidate_id, template="default"):
    candidates = load_json("data/candidates.json")
    candidate = next((c for c in candidates if c["id"] == candidate_id), None)
    
    if candidate:
        name = candidate.get("name", "Candidate")
        print(f"[Email] Sent to {name} (ID: {candidate_id}) at {datetime.now()}")
        return {"status": "sent", "recipient": name, "timestamp": datetime.now().isoformat()}
    else:
        print(f"[Email] Failed - Candidate {candidate_id} not found")
        return {"status": "failed", "reason": "candidate_not_found"}

def send_rejection_email(candidate_id):
    return send_email(candidate_id, "rejection")

def send_interview_email(candidate_id):
    return send_email(candidate_id, "interview")