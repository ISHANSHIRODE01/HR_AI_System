import json
from pathlib import Path
import random

class RLModel:
    def __init__(self):
        self.q_table = {}
        self.learning_rate = 0.1
        self.discount_factor = 0.9
        self.epsilon = 0.1
        self.actions = ["accept", "reject", "reconsider"]
        
    def get_state(self, candidate_id, skills_match, experience_level):
        return f"{candidate_id}_{skills_match}_{experience_level}"
    
    def choose_action(self, state):
        if state not in self.q_table:
            self.q_table[state] = [0.0] * len(self.actions)
        
        if random.random() < self.epsilon:
            return random.randint(0, len(self.actions) - 1)
        return self.q_table[state].index(max(self.q_table[state]))
    
    def update_q_value(self, state, action, reward, next_state):
        if state not in self.q_table:
            self.q_table[state] = [0.0] * len(self.actions)
        if next_state not in self.q_table:
            self.q_table[next_state] = [0.0] * len(self.actions)
            
        current_q = self.q_table[state][action]
        max_next_q = max(self.q_table[next_state])
        new_q = current_q + self.learning_rate * (reward + self.discount_factor * max_next_q - current_q)
        self.q_table[state][action] = new_q
    
    def get_recommendation(self, candidate_id, skills_match, experience_level):
        state = self.get_state(candidate_id, skills_match, experience_level)
        action_idx = self.choose_action(state)
        return self.actions[action_idx]