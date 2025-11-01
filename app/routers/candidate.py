from fastapi import APIRouter, Request
from pydantic import BaseModel
from app.utils.helpers import load_json, save_json, validate_candidate_data
from app.core.sentiment_model import SentimentModel

router = APIRouter(prefix="/candidate", tags=["Candidate"])
sentiment_model = SentimentModel()

class Candidate(BaseModel):
    id: int
    name: str
    skills: list[str]
    match_score: float = 0.0

class JobMatch(BaseModel):
    candidate_id: int
    job_requirements: str

@router.post("/add")
def add_candidate(candidate: Candidate):
    candidates = load_json("data/candidates.json")
    candidate_dict = candidate.dict()
    candidates.append(candidate_dict)
    save_json(candidates, "data/candidates.json")
    return {"status": "Candidate added", "data": candidate}

@router.get("/list")
def list_candidates():
    return load_json("data/candidates.json")

@router.post("/match")
def match_candidate(match_request: JobMatch, request: Request):
    rl_model = request.app.state.rl_model
    candidates = load_json("data/candidates.json")
    
    candidate = next((c for c in candidates if c["id"] == match_request.candidate_id), None)
    if not candidate:
        return {"error": "Candidate not found"}
    
    skills_match = sentiment_model.calculate_match_score(
        " ".join(candidate["skills"]), 
        match_request.job_requirements
    )
    
    recommendation = rl_model.get_recommendation(
        match_request.candidate_id, 
        int(skills_match * 10), 
        5
    )
    
    return {
        "candidate_id": match_request.candidate_id,
        "skills_match": skills_match,
        "recommendation": recommendation
    }