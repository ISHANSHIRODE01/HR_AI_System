from datetime import datetime
from app.utils.helpers import load_json

def send_whatsapp(candidate_id, message_type="notification"):
    candidates = load_json("data/candidates.json")
    candidate = next((c for c in candidates if c["id"] == candidate_id), None)
    
    if candidate:
        name = candidate.get("name", "Candidate")
        print(f"[WhatsApp] {message_type} sent to {name} (ID: {candidate_id})")
        return {"status": "sent", "recipient": name, "type": message_type}
    else:
        print(f"[WhatsApp] Failed - Candidate {candidate_id} not found")
        return {"status": "failed", "reason": "candidate_not_found"}