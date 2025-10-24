from datetime import datetime
import json, os

LOG_PATH = "feedback/system_log.json"

def trigger_event(event_name, user_id, details=None):
    """Basic event-driven automation + structured logging."""
    event = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "event": event_name,
        "user_id": user_id,
        "details": details or {},
    }
    os.makedirs(os.path.dirname(LOG_PATH), exist_ok=True)
    with open(LOG_PATH, "a") as f:
        f.write(json.dumps(event) + "\n")
    print(f"Event Logged: {event_name} by User {user_id}")
    return event
