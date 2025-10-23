# ==============================================
# HR RL Agent Dashboard — Optimized for new RLAgent
# ==============================================

import sys
import os
import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

# Ensure project root is in Python path
sys.path.append(os.path.dirname(__file__))

from agents.rl_agent import RLAgent  # Updated path

# --- CONFIGURATION: CSV PATHS ---
CVS_PATH = 'feedback/cvs.csv'
JDS_PATH = 'feedback/jds.csv'
FEEDBACKS_PATH = 'feedback/feedbacks.csv'

st.set_page_config(layout="wide", page_title="HR RL Agent Dashboard")

# --- Load Agent and Apply Feedback ---
@st.cache_resource
def load_agent_and_feedback():
    """Load RLAgent, update Q-table from historical feedbacks, return agent and dataframe."""
    try:
        if not all(os.path.exists(p) for p in [CVS_PATH, JDS_PATH, FEEDBACKS_PATH]):
            raise FileNotFoundError("One or more CSV files are missing. Check paths.")

        agent = RLAgent(CVS_PATH, JDS_PATH)
        feedback_df = pd.read_csv(FEEDBACKS_PATH)

        # Ensure feedback_id exists for logging (optional)
        if 'feedback_id' not in feedback_df.columns:
            feedback_df['feedback_id'] = range(1, len(feedback_df)+1)

        # Update agent with all feedbacks
        for _, feedback in feedback_df.iterrows():
            agent.update_reward(feedback)

        if len(agent.history) == 0:
            st.warning("RLAgent history is empty. Ensure feedback CSV has valid data.")
        return agent, feedback_df

    except Exception as e:
        st.error(f"Failed to load agent or feedback: {e}")
        st.stop()
        return None, None

AGENT, FEEDBACK_DF = load_agent_and_feedback()

# --- PAGE TITLE ---
st.title("🤖 HR RL Agent Transparency Dashboard")

# =========================
# 1️⃣ Metrics & Status
# =========================
if AGENT and AGENT.history:
    history_df = pd.DataFrame(AGENT.history)

    st.header("Agent Status & Key Metrics")
    col1, col2, col3 = st.columns(3)

    # Total feedbacks
    col1.metric("Total Feedbacks Processed", len(FEEDBACK_DF))

    # Cumulative reward
    col2.metric(
        "Cumulative Reward",
        value=f"{AGENT.total_reward_over_time:.2f}",
        delta=f"{AGENT.history[-1]['reward']:.2f}"
    )

    # Most preferred action for most frequent state
    most_freq_state = history_df['s_tuple'].mode().iloc[0]
    best_action_idx = np.argmax(AGENT.q_table[most_freq_state])
    best_action = ['accept', 'reject', 'reconsider'][best_action_idx]
    col3.markdown(f"**Most Preferred Action for State {most_freq_state}:**\n### {best_action.upper()}")

    # =========================
    # 2️⃣ RL Performance Charts
    # =========================
    st.header("RL Performance Trends")
    chart_col1, chart_col2 = st.columns(2)

    # Cumulative Reward
    with chart_col1:
        fig_reward = px.line(
            history_df.reset_index(),
            x='index',
            y='cumulative_reward',
            title="Agent Learning Progress (Cumulative Reward)",
            labels={'index': 'Feedback Entry', 'cumulative_reward': 'Cumulative Reward'}
        )
        st.plotly_chart(fig_reward, use_container_width=True)

    # Feedback Sentiment Distribution
    with chart_col2:
        sentiment_map = {0: 'Negative', 1: 'Neutral', 2: 'Positive'}
        sentiment_counts = history_df['s_tuple'].apply(lambda x: sentiment_map[x[1]]).value_counts().reset_index()
        sentiment_counts.columns = ['Sentiment', 'Count']

        fig_sentiment = px.bar(
            sentiment_counts,
            x='Sentiment',
            y='Count',
            title="Distribution of Feedback Sentiment",
            color='Sentiment',
            color_discrete_map={'Negative': 'red', 'Neutral': 'orange', 'Positive': 'green'}
        )
        st.plotly_chart(fig_sentiment, use_container_width=True)

    # =========================
    # 3️⃣ Policy & Feedback Logs
    # =========================
    st.header("Policy & Feedback Logs")

    st.subheader(f"Q-Values for State {most_freq_state}")
    q_values = AGENT.q_table[most_freq_state]
    q_df = pd.DataFrame(
        q_values.reshape(1, -1),
        columns=['Q(accept)', 'Q(reject)', 'Q(reconsider)'],
        index=[f"State {most_freq_state}"]
    ).T.rename(columns={0: "Q-Value"})
    st.dataframe(q_df.style.background_gradient(cmap='RdYlGn'), use_container_width=True)

    # Latest 10 feedback logs
    st.subheader("Latest 10 Feedback Logs")
    log_df = history_df.merge(
        FEEDBACK_DF[['candidate_id', 'jd_id', 'comment', 'feedback_score']],
        on=['candidate_id', 'jd_id', 'feedback_score', 'comment'],
        how='left'
    )

    for _, row in log_df.sort_values(by='feedback_score', ascending=False).head(10).iterrows():
        color = 'green' if row['feedback_score'] >= 4 else ('orange' if row['feedback_score'] > 2 else 'red')
        st.markdown(f"**Candidate {row['candidate_id']} / Job {row['jd_id']}** - Score: :{color}[{row['feedback_score']}]")
        with st.expander(f"Details (Action: {['accept','reject','reconsider'][row['action_taken']]})"):
            st.json({
                "Comment": row['comment'],
                "Reward Received": row['reward'],
                "State Tuple": row['s_tuple'],
                "Cumulative Reward": f"{row['cumulative_reward']:.2f}"
            })

else:
    st.error("Agent history not available. Check RLAgent or feedback CSV files.")
