import streamlit as st
import requests
import pandas as pd
import json
from datetime import datetime

st.set_page_config(page_title="HR-AI Dashboard", layout="wide")

API_BASE = "http://localhost:5000"

st.title("🚀 HR-AI Core Dashboard")

# Sidebar
st.sidebar.header("Navigation")
page = st.sidebar.selectbox("Choose Page", ["Overview", "Candidates", "Feedback", "Automation"])

if page == "Overview":
    st.header("System Overview")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("System Status", "Active", "🟢")
    with col2:
        st.metric("RL Model", "Learning", "📈")
    with col3:
        st.metric("Automation", "Enabled", "⚡")
    
    # Recent logs
    try:
        response = requests.get(f"{API_BASE}/feedback/logs")
        if response.status_code == 200:
            logs = response.json()
            if logs:
                st.subheader("Recent Activity")
                df = pd.DataFrame(logs)
                st.dataframe(df)
    except:
        st.warning("Could not connect to API")

elif page == "Candidates":
    st.header("Candidate Management")
    
    # Add new candidate
    with st.expander("Add New Candidate"):
        name = st.text_input("Name")
        skills = st.text_area("Skills (comma-separated)")
        
        if st.button("Add Candidate"):
            if name and skills:
                candidate_data = {
                    "id": int(datetime.now().timestamp()),
                    "name": name,
                    "skills": skills.split(","),
                    "match_score": 0.0
                }
                
                try:
                    response = requests.post(f"{API_BASE}/candidate/add", json=candidate_data)
                    if response.status_code == 200:
                        st.success("Candidate added successfully!")
                    else:
                        st.error("Failed to add candidate")
                except:
                    st.error("Could not connect to API")
    
    # List candidates
    try:
        response = requests.get(f"{API_BASE}/candidate/list")
        if response.status_code == 200:
            candidates = response.json()
            if candidates:
                st.subheader("Current Candidates")
                df = pd.DataFrame(candidates)
                st.dataframe(df)
    except:
        st.warning("Could not load candidates")

elif page == "Feedback":
    st.header("HR Feedback System")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Submit Feedback")
        candidate_id = st.number_input("Candidate ID", min_value=1)
        feedback_score = st.slider("Feedback Score", 1, 5, 3)
        comment = st.text_area("Comment")
        actual_outcome = st.selectbox("Actual Outcome", ["accept", "reject", "reconsider"])
        
        if st.button("Submit Feedback"):
            feedback_data = {
                "candidate_id": candidate_id,
                "feedback_score": feedback_score,
                "comment": comment,
                "actual_outcome": actual_outcome
            }
            
            try:
                response = requests.post(f"{API_BASE}/feedback/hr_feedback", json=feedback_data)
                if response.status_code == 200:
                    result = response.json()
                    st.success("Feedback submitted!")
                    st.json(result)
                else:
                    st.error("Failed to submit feedback")
            except:
                st.error("Could not connect to API")
    
    with col2:
        st.subheader("Feedback Logs")
        try:
            response = requests.get(f"{API_BASE}/feedback/logs")
            if response.status_code == 200:
                logs = response.json()
                if logs:
                    df = pd.DataFrame(logs)
                    st.dataframe(df)
        except:
            st.warning("Could not load feedback logs")

elif page == "Automation":
    st.header("Automation Control")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Trigger Event")
        candidate_id = st.number_input("Candidate ID", min_value=1, key="auto_candidate")
        event_type = st.selectbox("Event Type", [
            "shortlisted", "rejected", "onboarding_completed", "interview_scheduled"
        ])
        
        if st.button("Trigger Automation"):
            event_data = {
                "candidate_id": candidate_id,
                "event_type": event_type,
                "metadata": {}
            }
            
            try:
                response = requests.post(f"{API_BASE}/trigger/", json=event_data)
                if response.status_code == 200:
                    result = response.json()
                    st.success("Automation triggered!")
                    st.json(result)
                else:
                    st.error("Failed to trigger automation")
            except:
                st.error("Could not connect to API")
    
    with col2:
        st.subheader("Automation History")
        history_candidate_id = st.number_input("Candidate ID for History", min_value=1)
        
        if st.button("Load History"):
            try:
                response = requests.get(f"{API_BASE}/trigger/history/{history_candidate_id}")
                if response.status_code == 200:
                    history = response.json()
                    if history.get("automation_history"):
                        df = pd.DataFrame(history["automation_history"])
                        st.dataframe(df)
                    else:
                        st.info("No automation history found")
            except:
                st.error("Could not load history")