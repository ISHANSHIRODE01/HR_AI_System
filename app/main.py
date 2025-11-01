from fastapi import FastAPI
from app.routers import candidate, feedback, trigger
from app.core.rl_model import RLModel

app = FastAPI(title="HR-AI Core Autonomy Upgrade")

# Initialize RL Model
rl_model = RLModel()
app.state.rl_model = rl_model

app.include_router(candidate.router)
app.include_router(feedback.router)
app.include_router(trigger.router)

@app.get("/")
def root():
    return {"message": "HR-AI Core System is running 🚀", "rl_status": "active"}

@app.get("/health")
def health():
    return {"status": "healthy", "components": ["rl_model", "agents", "routers"]}