# HR AI System - Flask Backend (Simplified)
from flask import Flask, request, jsonify
import pandas as pd
import os
import json
from datetime import datetime

# RL Agent Import
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from agents.rl_agent import RLAgent
from agents.automation import trigger_event
from config import CVS_PATH, JDS_PATH, FEEDBACKS_PATH, FEEDBACK_LOG_PATH, SYSTEM_LOG_PATH, validate_data_files

app = Flask(__name__)

# Initialize RL Agent
try:
    validate_data_files()
    AGENT = RLAgent(str(CVS_PATH), str(JDS_PATH))
    print("RL Agent initialized successfully.")
except FileNotFoundError as e:
    print(f"Data error: {e}")
    print("Please ensure all required CSV files exist in the feedback/ directory")
    AGENT = None
except Exception as e:
    print(f"Initialization error: {e}")
    AGENT = None

def generate_simple_summary(candidate_id, jd_id, comment, feedback_score):
    """Generate simple feedback summary without external AI"""
    if feedback_score >= 4:
        return f"Positive feedback for candidate {candidate_id} - Score {feedback_score}/5"
    elif feedback_score <= 2:
        return f"Negative feedback for candidate {candidate_id} - Score {feedback_score}/5"
    else:
        return f"Neutral feedback for candidate {candidate_id} - Score {feedback_score}/5"

def internal_automation(candidate_id, jd_id, feedback_score, comment, summary, action):
    """Internal automation trigger for event logging"""
    details = {
        "candidate_id": candidate_id,
        "jd_id": jd_id,
        "feedback_score": feedback_score,
        "comment": comment,
        "summary": summary,
        "action": action,
    }
    trigger_event("feedback_processed", user_id=candidate_id, details=details)
    print(f"Automation Triggered - Candidate {candidate_id}, Policy: {action}")

@app.route("/")
def home():
    status_info = {
        "status": "HR RL Agent Backend Running",
        "automation": "enabled",
        "rl_agent": "initialized" if AGENT else "failed",
        "timestamp": datetime.now().isoformat()
    }
    return jsonify(status_info)

@app.route("/health")
def health_check():
    """System health check for troubleshooting"""
    health_status = {
        "system": "HR AI System",
        "version": "2.0 Simplified",
        "timestamp": datetime.now().isoformat(),
        "components": {
            "rl_agent": {
                "status": "ok" if AGENT else "error",
                "details": "Q-learning agent initialized" if AGENT else "Agent initialization failed"
            },
            "data_files": {
                "status": "checking",
                "cvs_exists": CVS_PATH.exists(),
                "jds_exists": JDS_PATH.exists(),
                "feedbacks_exists": FEEDBACKS_PATH.exists()
            }
        },
        "recommendations": []
    }
    
    # Add recommendations based on status
    if not AGENT:
        health_status["recommendations"].append("Check that all CSV files exist in feedback/ directory")
    
    # Overall health
    health_status["overall"] = "healthy" if AGENT is not None else "degraded"
    
    return jsonify(health_status)

@app.route("/update_feedback", methods=["POST"])
def update_feedback():
    if not AGENT:
        return jsonify({"status": "error", "message": "RL Agent not initialized"}), 500

    data = request.json or {}
    required_keys = ["candidate_id", "jd_id", "feedback_score", "comment"]
    if not all(k in data for k in required_keys):
        return jsonify({"status": "error", "message": "Missing fields"}), 400

    # Trigger Event: Feedback Received
    trigger_event("feedback_received", user_id=data["candidate_id"], details=data)

    # RL Update
    feedback_entry = pd.Series(data)
    AGENT.update_reward(feedback_entry)

    # Simple Summary (no external AI)
    summary = generate_simple_summary(
        data["candidate_id"], data["jd_id"], data["comment"], data["feedback_score"]
    )

    # New Policy Suggestion
    s_tuple = AGENT.get_state(data["candidate_id"], data["jd_id"], data["comment"])
    policy_action = ["accept", "reject", "reconsider"][AGENT.choose_action(s_tuple)]

    # Log Feedback
    try:
        df = pd.DataFrame(
            [
                {
                    "candidate_id": data["candidate_id"],
                    "jd_id": data["jd_id"],
                    "feedback_score": data["feedback_score"],
                    "comment": data["comment"],
                    "feedback_summary": summary,
                    "policy_action": policy_action,
                }
            ]
        )
        if not os.path.exists(FEEDBACK_LOG_PATH):
            df.to_csv(FEEDBACK_LOG_PATH, index=False)
        else:
            df.to_csv(FEEDBACK_LOG_PATH, mode="a", header=False, index=False)
    except Exception as e:
        print(f"CSV log error: {e}")

    # Internal Automation Trigger
    internal_automation(
        data["candidate_id"],
        data["jd_id"],
        data["feedback_score"],
        data["comment"],
        summary,
        policy_action,
    )

    return jsonify(
        {
            "status": "updated_and_logged",
            "candidate_id": data["candidate_id"],
            "jd_id": data["jd_id"],
            "rl_policy_change": f"System now suggests '{policy_action}'",
            "feedback_summary": summary,
        }
    )

if __name__ == "__main__":
    app.run(debug=True, port=5000)