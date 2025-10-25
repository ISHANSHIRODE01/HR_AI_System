import os
import sys
import pandas as pd

# Add project root to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from agents.rl_agent import RLAgent
from config import CVS_PATH, JDS_PATH, FEEDBACKS_PATH, DATA_DIR, validate_data_files

def main():
    """Main workflow for HR AI System"""
    print("Starting HR AI System Workflow...")
    
    # Initialize RL Agent
    try:
        validate_data_files()
        agent = RLAgent(str(CVS_PATH), str(JDS_PATH))
        print("RL Agent initialized successfully")
    except FileNotFoundError as e:
        print(f"Data files missing: {e}")
        print("Please ensure all required CSV files exist in the feedback/ directory")
        return
    except Exception as e:
        print(f"Error initializing RL Agent: {e}")
        return
    
    # Load and process feedback data
    if FEEDBACKS_PATH.exists():
        feedback_df = pd.read_csv(str(FEEDBACKS_PATH))
        print(f"Loaded {len(feedback_df)} feedback entries")
        
        # Process feedback through RL agent
        for _, feedback in feedback_df.iterrows():
            agent.update_reward(feedback)
        
        print(f"Processed feedback. Total reward: {agent.total_reward_over_time}")
        print(f"Agent history length: {len(agent.history)}")
        
        # Save results
        if agent.history:
            results_df = pd.DataFrame(agent.history)
            output_file = DATA_DIR / "agent_results.csv"
            results_df.to_csv(str(output_file), index=False)
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