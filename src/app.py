# -----------------------------------------------------------
# Adaptive AI HR Brain v2 — Flask Backend (Self-Automation + Gemini)
# -----------------------------------------------------------
from flask import Flask, request, jsonify
import pandas as pd
import os
import json
from datetime import datetime

# --- NEW IMPORTS FOR GEMINI ---
from google import genai
from google.genai.errors import APIError

# --- RL Agent Import ---
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from agents.rl_agent import RLAgent
from agents.automation import trigger_event
from config import CVS_PATH, JDS_PATH, FEEDBACK_LOG_PATH, SYSTEM_LOG_PATH, GOOGLE_AI_API_KEY, validate_data_files, ensure_directories

app = Flask(__name__)

# --- Initialize RL Agent ---
try:
    print("🚀 Initializing HR AI System...")
    ensure_directories()
    validate_data_files(auto_create=True)
    AGENT = RLAgent(str(CVS_PATH), str(JDS_PATH))
    print("✅ RL Agent initialized successfully.")
except FileNotFoundError as e:
    print(f"❌ Data error: {e}")
    print("📋 Please ensure all required CSV files exist in the feedback/ directory")
    print("🔧 You can also run the system again to auto-generate sample data")
    AGENT = None
except Exception as e:
    print(f"❌ Initialization error: {e}")
    AGENT = None

# --- Initialize Gemini Client ---
try:
    if GOOGLE_AI_API_KEY:
        GEMINI_CLIENT = genai.Client(api_key=GOOGLE_AI_API_KEY)
        print("Gemini Client initialized successfully.")
    else:
        print("No Google AI API key found. Gemini features disabled.")
        GEMINI_CLIENT = None
except Exception as e:
    print(f"Gemini Client Error: {e}")
    print("Gemini features will be disabled. Set GOOGLE_AI_API_KEY to enable.")
    GEMINI_CLIENT = None


# -----------------------------------------------------------
# Helper: Summarize Feedback using Gemini
# -----------------------------------------------------------
def summarize_feedback_with_gemini(candidate_id, jd_id, comment, feedback_score):
    if not GEMINI_CLIENT:
        return f"Processed feedback with score {feedback_score}"

    prompt = f"""
    HR Feedback Summary Task:
    Candidate ID: {candidate_id}
    Job ID: {jd_id}
    Raw Comment: "{comment}"
    Score (1=Bad, 5=Good): {feedback_score}

    Summarize the reason for the score in <=15 words for an HR Slack channel.
    """

    try:
        resp = GEMINI_CLIENT.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
            config=genai.types.GenerateContentConfig(
                temperature=0.3, max_output_tokens=150
            ),
        )
        return (resp.text or f"Processed feedback with score {feedback_score}").strip()
    except (APIError, Exception) as e:
        print(f"Gemini API Error: {e}")
        return f"Processed feedback with score {feedback_score} (Gemini unavailable)"


# -----------------------------------------------------------
# 🔁 Internal Automation Trigger
# -----------------------------------------------------------
def internal_automation(candidate_id, jd_id, feedback_score, comment, summary, action):
    """Simulates event-driven automation instead of using N8N."""
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


# -----------------------------------------------------------
# Routes
# -----------------------------------------------------------
@app.route("/")
def home():
    return "HR RL Agent Backend Running (Self-Automation Enabled)"


@app.route("/update_feedback", methods=["POST"])
def update_feedback():
    if not AGENT:
        return jsonify({"status": "error", "message": "RL Agent not initialized"}), 500

    data = request.json or {}
    required_keys = ["candidate_id", "jd_id", "feedback_score", "comment"]
    if not all(k in data for k in required_keys):
        return jsonify({"status": "error", "message": "Missing fields"}), 400

    # --- Trigger Event: Feedback Received ---
    trigger_event("feedback_received", user_id=data["candidate_id"], details=data)

    # --- RL Update ---
    feedback_entry = pd.Series(data)
    AGENT.update_reward(feedback_entry)

    # --- Gemini Summary ---
    summary = summarize_feedback_with_gemini(
        data["candidate_id"], data["jd_id"], data["comment"], data["feedback_score"]
    )

    # --- New Policy Suggestion ---
    s_tuple = AGENT.get_state(data["candidate_id"], data["jd_id"], data["comment"])
    policy_action = ["accept", "reject", "reconsider"][AGENT.choose_action(s_tuple)]

    # --- Log Feedback ---
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

    # --- Internal Automation Trigger (replaces N8N) ---
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


# -----------------------------------------------------------
# Run Flask App
# -----------------------------------------------------------
if __name__ == "__main__":
    app.run(debug=True, port=5000)
