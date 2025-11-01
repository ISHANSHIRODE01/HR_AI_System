from datetime import datetime
from app.utils.helpers import load_json

def trigger_voice_call(candidate_id, call_type="onboarding"):
    candidates = load_json("data/candidates.json")
    candidate = next((c for c in candidates if c["id"] == candidate_id), None)
    
    if candidate:
        name = candidate.get("name", "Candidate")
        print(f"[Voice] {call_type} call triggered for {name} (ID: {candidate_id})")
        return {"status": "triggered", "recipient": name, "call_type": call_type}
    else:
        print(f"[Voice] Failed - Candidate {candidate_id} not found")
        return {"status": "failed", "reason": "candidate_not_found"}

def schedule_interview_call(candidate_id):
    return trigger_voice_call(candidate_id, "interview_reminder")