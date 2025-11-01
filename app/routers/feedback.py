from fastapi import APIRouter, Request
from pydantic import BaseModel
from app.feedback.reward_logger import RewardLogger
from app.core.sentiment_model import SentimentModel
from app.utils.helpers import calculate_reward

router = APIRouter(prefix="/feedback", tags=["Feedback"])
reward_logger = RewardLogger()
sentiment_model = SentimentModel()

class Feedback(BaseModel):
    candidate_id: int
    action: str
    reward: float
    comment: str = ""

class HRFeedback(BaseModel):
    candidate_id: int
    feedback_score: int
    comment: str
    actual_outcome: str

@router.post("/")
def post_feedback(feedback: Feedback, request: Request):
    rl_model = request.app.state.rl_model
    
    state = rl_model.get_state(feedback.candidate_id, 5, 5)
    action_idx = ["accept", "reject", "reconsider"].index(feedback.action)
    
    rl_model.update_q_value(state, action_idx, feedback.reward, state)
    reward_logger.log_reward(feedback.candidate_id, state, feedback.action, feedback.reward, feedback.comment)
    
    return {"status": "Feedback logged successfully", "data": feedback}

@router.post("/hr_feedback")
def hr_feedback(feedback: HRFeedback, request: Request):
    rl_model = request.app.state.rl_model
    
    sentiment = sentiment_model.analyze_feedback(feedback.comment)
    reward = calculate_reward(feedback.feedback_score, "accept", feedback.actual_outcome)
    
    state = rl_model.get_state(feedback.candidate_id, 5, 5)
    action_idx = 0 if feedback.actual_outcome == "accept" else 1
    
    rl_model.update_q_value(state, action_idx, reward, state)
    reward_logger.log_reward(feedback.candidate_id, state, feedback.actual_outcome, reward, feedback.comment)
    
    return {
        "status": "HR feedback processed",
        "sentiment": sentiment,
        "reward": reward
    }

@router.get("/logs")
def get_feedback_logs():
    return reward_logger.get_recent_logs()