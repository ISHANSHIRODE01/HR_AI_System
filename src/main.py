import os
import sys
import pandas as pd

# Add project root to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from agents.rl_agent import RLAgent

# Define paths
CVS_PATH = "feedback/cvs.csv"
JDS_PATH = "feedback/jds.csv"
FEEDBACKS_PATH = "feedback/feedbacks.csv"
OUTPUT_DIR = "feedback"

def main():
    """Main workflow for HR AI System"""
    print("Starting HR AI System Workflow...")
    
    # Initialize RL Agent
    try:
        agent = RLAgent(CVS_PATH, JDS_PATH)
        print("RL Agent initialized successfully")
    except Exception as e:
        print(f"Error initializing RL Agent: {e}")
        return
    
    # Load and process feedback data
    if os.path.exists(FEEDBACKS_PATH):
        feedback_df = pd.read_csv(FEEDBACKS_PATH)
        print(f"Loaded {len(feedback_df)} feedback entries")
        
        # Process feedback through RL agent
        for _, feedback in feedback_df.iterrows():
            agent.update_reward(feedback)
        
        print(f"Processed feedback. Total reward: {agent.total_reward_over_time}")
        print(f"Agent history length: {len(agent.history)}")
        
        # Save results
        if agent.history:
            results_df = pd.DataFrame(agent.history)
            output_file = os.path.join(OUTPUT_DIR, "agent_results.csv")
            results_df.to_csv(output_file, index=False)
            print(f"Results saved to {output_file}")
            
        # Test decision making
        state = agent.get_state(1, 1, "Excellent candidate")
        action = agent.choose_action(state)
        actions = ['accept', 'reject', 'reconsider']
        print(f"Sample decision for candidate 1, job 1: {actions[action]}")
        
    else:
        print(f"Feedback file not found: {FEEDBACKS_PATH}")

if __name__ == "__main__":
    main()