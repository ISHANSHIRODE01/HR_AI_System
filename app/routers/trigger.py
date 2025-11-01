from fastapi import APIRouter, Request
from pydantic import BaseModel
from app.agents import email_agent, whatsapp_agent, voice_agent
from app.feedback.reward_logger import RewardLogger
from datetime import datetime

router = APIRouter(prefix="/trigger", tags=["Automation"])
reward_logger = RewardLogger()

class TriggerEvent(BaseModel):
    candidate_id: int
    event_type: str
    metadata: dict = {}

class AutomationResult(BaseModel):
    candidate_id: int
    actions_taken: list[str]
    timestamp: str

@router.post("/")
def trigger_event(event: TriggerEvent, request: Request) -> AutomationResult:
    actions_taken = []
    
    if event.event_type == "shortlisted":
        email_agent.send_email(event.candidate_id)
        whatsapp_agent.send_whatsapp(event.candidate_id)
        actions_taken = ["email_sent", "whatsapp_sent"]
        
    elif event.event_type == "rejected":
        email_agent.send_email(event.candidate_id)
        actions_taken = ["rejection_email_sent"]
        
    elif event.event_type == "onboarding_completed":
        voice_agent.trigger_voice_call(event.candidate_id)
        actions_taken = ["voice_call_triggered"]
        
    elif event.event_type == "interview_scheduled":
        email_agent.send_email(event.candidate_id)
        whatsapp_agent.send_whatsapp(event.candidate_id)
        actions_taken = ["interview_notification_sent"]
    
    # Log automation event
    reward_logger.log_reward(
        event.candidate_id, 
        f"automation_{event.event_type}", 
        "triggered", 
        1.0, 
        f"Actions: {', '.join(actions_taken)}"
    )
    
    return AutomationResult(
        candidate_id=event.candidate_id,
        actions_taken=actions_taken,
        timestamp=datetime.now().isoformat()
    )

@router.get("/history/{candidate_id}")
def get_automation_history(candidate_id: int):
    logs = reward_logger.get_recent_logs(50)
    candidate_logs = [log for log in logs if int(log.get("candidate_id", 0)) == candidate_id]
    return {"candidate_id": candidate_id, "automation_history": candidate_logs}