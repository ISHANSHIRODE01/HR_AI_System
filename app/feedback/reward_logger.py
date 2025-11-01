import json
import csv
from datetime import datetime
from pathlib import Path

class RewardLogger:
    def __init__(self):
        self.log_file = Path("data/reward_log.csv")
        self.log_file.parent.mkdir(exist_ok=True)
        self._init_log_file()
    
    def _init_log_file(self):
        if not self.log_file.exists():
            with open(self.log_file, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(["timestamp", "candidate_id", "state", "action", "reward", "feedback"])
    
    def log_reward(self, candidate_id, state, action, reward, feedback=""):
        with open(self.log_file, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([
                datetime.now().isoformat(),
                candidate_id,
                state,
                action,
                reward,
                feedback
            ])
    
    def get_recent_logs(self, limit=10):
        logs = []
        try:
            with open(self.log_file, 'r') as f:
                reader = csv.DictReader(f)
                logs = list(reader)[-limit:]
        except FileNotFoundError:
            pass
        return logs