# -----------------------------------------------------------
<<<<<<< HEAD
# Adaptive AI HR Brain v2 — Flask Backend (Self-Automation + Gemini)
# -----------------------------------------------------------
from flask import Flask, request, jsonify
import pandas as pd
import os, json
from datetime import datetime
=======
# Adaptive AI HR Brain v2 — Flask Backend (with Gemini + N8N)
# -----------------------------------------------------------
from flask import Flask, request, jsonify
import pandas as pd
import os
import json
import requests
>>>>>>> 90fd1c683f3143c460f89c1fb13f7de7c899c2b6

# --- NEW IMPORTS FOR GEMINI ---
from google import genai
from google.genai.errors import APIError

# --- RL Agent Import ---
<<<<<<< HEAD
from agents.rl_agent import RLAgent  # your RL class

# --- Internal Automation Import (NEW) ---
from agents.automation import trigger_event   # <-- we'll create this file next
=======
from utils.rl_agent import RLAgent  # Assuming RLAgent is in utils/
>>>>>>> 90fd1c683f3143c460f89c1fb13f7de7c899c2b6

app = Flask(__name__)

# --- File Paths ---
<<<<<<< HEAD
CVS_PATH = "feedback/cvs.csv"
JDS_PATH = "feedback/jds.csv"
FEEDBACK_LOG_PATH = "feedback/feedback_log.csv"
SYSTEM_LOG_PATH = "feedback/system_log.json"
=======
CVS_PATH = 'data/cvs.csv'
JDS_PATH = 'data/jds.csv'
FEEDBACK_LOG_PATH = 'data/feedback_log.csv'  # Optional log for dashboard tracking
>>>>>>> 90fd1c683f3143c460f89c1fb13f7de7c899c2b6

# --- Initialize RL Agent ---
try:
    AGENT = RLAgent(CVS_PATH, JDS_PATH)
    print("✅ RL Agent initialized successfully.")
except FileNotFoundError as e:
<<<<<<< HEAD
    print(f"❌ Data error: {e}")
=======
    print(f"❌ Error loading data: {e}. Ensure data/cvs.csv and data/jds.csv exist.")
>>>>>>> 90fd1c683f3143c460f89c1fb13f7de7c899c2b6
    AGENT = None

# --- Initialize Gemini Client ---
try:
<<<<<<< HEAD
    GEMINI_CLIENT = genai.Client()
    print("✅ Gemini Client initialized successfully.")
except Exception as e:
    print(f"⚠️ Gemini Client Error: {e}")
=======
    GEMINI_CLIENT = genai.Client()  # Uses GEMINI_API_KEY or GOOGLE_API_KEY automatically
    print("✅ Gemini Client initialized successfully.")
except Exception as e:
    print(f"⚠️ Gemini Client Error: {e}. Check GEMINI_API_KEY environment variable.")
>>>>>>> 90fd1c683f3143c460f89c1fb13f7de7c899c2b6
    GEMINI_CLIENT = None


# -----------------------------------------------------------
# Helper: Summarize Feedback using Gemini
# -----------------------------------------------------------
def summarize_feedback_with_gemini(candidate_id, jd_id, comment, feedback_score):
    if not GEMINI_CLIENT:
        return "Gemini client not initialized."

    prompt = f"""
    HR Feedback Summary Task:
    Candidate ID: {candidate_id}
    Job ID: {jd_id}
    Raw Comment: "{comment}"
    Score (1=Bad, 5=Good): {feedback_score}

<<<<<<< HEAD
    Summarize the reason for the score in <=15 words for an HR Slack channel.
=======
    Analyze the Raw Comment, determine the core reason for the score, and provide
    a concise sentence summary (max 15 words) suitable for an HR Slack channel.
>>>>>>> 90fd1c683f3143c460f89c1fb13f7de7c899c2b6
    """

    try:
        resp = GEMINI_CLIENT.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
            config=genai.types.GenerateContentConfig(
                temperature=0.3, max_output_tokens=150
            ),
        )
<<<<<<< HEAD
        return (resp.text or "No summary").strip()
    except (APIError, Exception) as e:
        return f"⚠️ Gemini Error: {e}"


# -----------------------------------------------------------
# 🔁 Replace N8N Workflow with Internal Event System
# -----------------------------------------------------------
def internal_automation(candidate_id, jd_id, feedback_score, comment, summary, action):
    """Simulates event-driven automation instead of using N8N."""
    details = {
=======

        if response.text:
            return response.text.strip()

        if response.candidates and response.candidates[0].finish_reason:
            reason = response.candidates[0].finish_reason.name
            if reason == 'SAFETY':
                return "⚠️ Gemini Summary blocked by safety filters."
            return f"⚠️ Gemini Summary incomplete (Reason: {reason})."

        return "⚠️ Gemini Summary empty or unparseable."

    except APIError as e:
        return f"⚠️ Gemini API Error: {e}"
    except Exception as e:
        return f"⚠️ Unexpected Error: {e}"


# -----------------------------------------------------------
# Helper: Send Feedback Data to N8N Workflow
# -----------------------------------------------------------
def send_feedback_to_n8n(candidate_id, jd_id, feedback_score, comment, summary):
    """
    Sends feedback data to N8N webhook for automation (e.g., summary → Slack/email).
    """
    webhook_url = "http://localhost:5678/webhook/feedback_update"  # Replace with your actual N8N webhook URL

    payload = {
>>>>>>> 90fd1c683f3143c460f89c1fb13f7de7c899c2b6
        "candidate_id": candidate_id,
        "jd_id": jd_id,
        "feedback_score": feedback_score,
        "comment": comment,
<<<<<<< HEAD
        "summary": summary,
        "action": action,
    }
    trigger_event("feedback_processed", user_id=candidate_id, details=details)
    print(f"📢 Automation Triggered → Candidate {candidate_id}, Policy: {action}")


# -----------------------------------------------------------
# Routes
# -----------------------------------------------------------
@app.route("/")
def home():
    return "✅ HR RL Agent Backend Running (Self-Automation Enabled)"


@app.route("/update_feedback", methods=["POST"])
=======
        "summary": summary
    }

    try:
        response = requests.post(webhook_url, data=json.dumps(payload), headers={"Content-Type": "application/json"})
        if response.status_code == 200:
            print(f"[N8N ✅] Feedback sent successfully → Candidate {candidate_id}, Job {jd_id}")
        else:
            print(f"[N8N ⚠️] Failed to send feedback: Status {response.status_code}")
    except Exception as e:
        print(f"[N8N ❌] Error sending feedback: {e}")


# -----------------------------------------------------------
# Route: Home (Simple Health Check)
# -----------------------------------------------------------
@app.route('/')
def home():
    return "✅ HR RL Agent Backend is Running! Use /update_feedback (POST) to send feedback."


# -----------------------------------------------------------
# Route: POST /update_feedback
# -----------------------------------------------------------
@app.route('/update_feedback', methods=['POST'])
>>>>>>> 90fd1c683f3143c460f89c1fb13f7de7c899c2b6
def update_feedback():
    if not AGENT:
        return jsonify({"status": "error", "message": "RL Agent not initialized"}), 500

<<<<<<< HEAD
    data = request.json or {}
    req_keys = ["candidate_id", "jd_id", "feedback_score", "comment"]
    if not all(k in data for k in req_keys):
        return jsonify({"status": "error", "message": "Missing fields"}), 400

    # --- Trigger Event: Feedback Received ---
    trigger_event("feedback_received", user_id=data["candidate_id"], details=data)

    # --- RL Update ---
    feedback_entry = pd.Series(data)
=======
    data = request.json
    required_keys = ['candidate_id', 'jd_id', 'feedback_score', 'comment']
    if not all(key in data for key in required_keys):
        return jsonify({"status": "error", "message": "Missing one or more required fields."}), 400

    # --- Update RL Agent with Feedback ---
    feedback_entry = pd.Series({
        'candidate_id': data['candidate_id'],
        'jd_id': data['jd_id'],
        'feedback_score': data['feedback_score'],
        'comment': data['comment']
    })
>>>>>>> 90fd1c683f3143c460f89c1fb13f7de7c899c2b6
    AGENT.update_reward(feedback_entry)

    # --- Gemini Summary ---
    summary = summarize_feedback_with_gemini(
        data["candidate_id"], data["jd_id"], data["comment"], data["feedback_score"]
    )

<<<<<<< HEAD
    # --- New Policy Suggestion ---
    s_tuple = AGENT.get_state(data["candidate_id"], data["jd_id"], data["comment"])
    policy_action = ["accept", "reject", "reconsider"][AGENT.choose_action(s_tuple)]

    # --- Log Feedback ---
=======
    # --- Get New Policy Suggestion ---
    s_prime_tuple = AGENT.get_state(data['candidate_id'], data['jd_id'], data['comment'])
    best_action_index = AGENT.choose_action(s_prime_tuple)
    policy_action = ['accept', 'reject', 'reconsider'][best_action_index]

    # --- Log Feedback to CSV ---
>>>>>>> 90fd1c683f3143c460f89c1fb13f7de7c899c2b6
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
<<<<<<< HEAD
            df.to_csv(FEEDBACK_LOG_PATH, mode="a", header=False, index=False)
    except Exception as e:
        print(f"⚠️ CSV log error: {e}")

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
=======
            new_entry.to_csv(FEEDBACK_LOG_PATH, mode='a', header=False, index=False)

    except Exception as e:
        print(f"⚠️ Failed to log feedback: {e}")

    # --- Send to N8N for Workflow Automation ---
    send_feedback_to_n8n(
        data['candidate_id'],
        data['jd_id'],
        data['feedback_score'],
        data['comment'],
        summary
    )

    # --- Return Response to Client ---
    return jsonify({
        "status": "updated_and_summarized",
        "candidate_id": data['candidate_id'],
        "jd_id": data['jd_id'],
        "rl_policy_change": f"New policy suggests '{policy_action}' for this candidate.",
        "feedback_summary": summary
    })
>>>>>>> 90fd1c683f3143c460f89c1fb13f7de7c899c2b6


# -----------------------------------------------------------
# Run Flask App
# -----------------------------------------------------------
<<<<<<< HEAD
if __name__ == "__main__":
=======
if __name__ == '__main__':
>>>>>>> 90fd1c683f3143c460f89c1fb13f7de7c899c2b6
    app.run(debug=True, port=5000)
