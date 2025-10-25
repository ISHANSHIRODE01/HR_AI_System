import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from textblob import TextBlob

# --- RL CONFIG ---
ALPHA = 0.1
GAMMA = 0.6
EPSILON = 0.1
NUM_ACTIONS = 3  # 0: accept, 1: reject, 2: reconsider

MATCH_THRESHOLDS = [0.2, 0.5]
SENTIMENT_THRESHOLDS = [-0.1, 0.1]

# --- Helper Functions ---
def calculate_match_score(cv_text: str, jd_text: str, vectorizer: TfidfVectorizer) -> float:
    """Compute cosine similarity between CV and JD texts."""
    tfidf = vectorizer.fit_transform([cv_text, jd_text])
    score = cosine_similarity(tfidf[0], tfidf[1])[0][0]
    return float(score)

def discretize_state(match_score: float, sentiment_score: float, prev_reward: float, reconsider_count: int) -> tuple:
    """Convert continuous features to discrete levels for Q-Table indexing."""
    match_level = 0 if match_score < MATCH_THRESHOLDS[0] else (1 if match_score < MATCH_THRESHOLDS[1] else 2)
    sentiment_level = 0 if sentiment_score < SENTIMENT_THRESHOLDS[0] else (1 if sentiment_score < SENTIMENT_THRESHOLDS[1] else 2)
    prev_reward_level = int(prev_reward + 1)
    history_level = 1 if reconsider_count >= 2 else 0
    return (match_level, sentiment_level, prev_reward_level, history_level)

# --- RL Agent ---
class RLAgent:
    def __init__(self, cvs_path: str, jds_path: str):
        try:
            self.cvs = pd.read_csv(cvs_path)
            self.jds = pd.read_csv(jds_path)
            print(f"✅ Loaded {len(self.cvs)} candidates and {len(self.jds)} job descriptions")
        except FileNotFoundError as e:
            raise FileNotFoundError(f"Data file not found: {e}. Please ensure CSV files exist in feedback/ directory")
        except Exception as e:
            raise Exception(f"Error loading data files: {e}")
            
        self.vectorizer = TfidfVectorizer(stop_words='english', max_features=100)

        # Q-table dimensions: Match x Sentiment x PrevReward x History x Actions
        self.q_table = np.zeros((3, 3, 3, 2, NUM_ACTIONS))
        self.pair_tracking = {}  # Tracks previous rewards and reconsider counts per candidate-job pair
        self.history = []
        self.total_reward_over_time = 0

    def get_state(self, candidate_id: int, jd_id: int, comment: str) -> tuple:
        """Compute discrete state tuple for candidate-job pair."""
        cv_text = self.cvs.loc[self.cvs['candidate_id'] == candidate_id, 'skills'].iloc[0]
        jd_text = self.jds.loc[self.jds['jd_id'] == jd_id, 'description'].iloc[0]

        match_score = calculate_match_score(cv_text, jd_text, self.vectorizer)
        sentiment_score = TextBlob(comment).sentiment.polarity

        key = (candidate_id, jd_id)
        if key not in self.pair_tracking:
            self.pair_tracking[key] = {'prev_reward': 0, 'reconsider_count': 0}

        prev_reward = self.pair_tracking[key]['prev_reward']
        reconsider_count = self.pair_tracking[key]['reconsider_count']

        return discretize_state(match_score, sentiment_score, prev_reward, reconsider_count)

    def choose_action(self, state_tuple: tuple) -> int:
        """Epsilon-greedy policy: explore or exploit Q-table."""
        if np.random.rand() < EPSILON:
            return np.random.randint(NUM_ACTIONS)
        return int(np.argmax(self.q_table[state_tuple]))

    def calculate_reward(self, action: int, feedback_score: float) -> int:
        """Compute reward based on action and HR feedback score."""
        if feedback_score > 4: outcome = 'GOOD'
        elif feedback_score < 2: outcome = 'BAD'
        else: outcome = 'NEUTRAL'

        if action == 0:  # accept
            return 1 if outcome == 'GOOD' else -1
        elif action == 1:  # reject
            return 1 if outcome == 'BAD' else -1
        return 0  # reconsider

    def update_reward(self, feedback_entry: pd.Series):
        """Update Q-table and history based on feedback entry."""
        candidate_id = feedback_entry['candidate_id']
        jd_id = feedback_entry['jd_id']
        comment = feedback_entry['comment']
        feedback_score = feedback_entry['feedback_score']

        key = (candidate_id, jd_id)

        s = self.get_state(candidate_id, jd_id, comment)
        action = self.choose_action(s)
        reward = self.calculate_reward(action, feedback_score)

        # Update tracking
        self.pair_tracking[key]['prev_reward'] = reward
        if action == 2:
            self.pair_tracking[key]['reconsider_count'] += 1

        s_prime = self.get_state(candidate_id, jd_id, comment)

        # Q-Learning update
        old_q = self.q_table[s][action]
        self.q_table[s][action] = old_q + ALPHA * (reward + GAMMA * np.max(self.q_table[s_prime]) - old_q)

        self.total_reward_over_time += reward
        self.history.append({
            'candidate_id': candidate_id,
            'jd_id': jd_id,
            's_tuple': s,
            'action_taken': action,
            'reward': reward,
            'cumulative_reward': self.total_reward_over_time,
            'feedback_score': feedback_score,
            'comment': comment
        })
