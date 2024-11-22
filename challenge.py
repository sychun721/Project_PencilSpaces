import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Data structure
challenges = {
    'Technical\nissues': {'count': 42, 'percent': 43},
    'Lack of\nspecific tools': {'count': 16, 'percent': 16},
    'Scheduling\ndifficulties': {'count': 14, 'percent': 14},
    'Limited UI/\nnavigation': {'count': 18, 'percent': 19},
    'Privacy\nconcerns': {'count': 7, 'percent': 7}
}

def create_challenges_visualization():
    # Set up the figure
    plt.figure(figsize=(10, 8))
    
    # Sort challenges by percentage
    sorted_challenges = dict(sorted(challenges.items(), 
                                  key=lambda x: x[1]['percent'], 
                                  reverse=True))
    
    # Prepare data for plotting
    labels = list(sorted_challenges.keys())
    percentages = [d['percent'] for d in sorted_challenges.values()]
    counts = [d['count'] for d in sorted_challenges.values()]
    
    # Create vertical bar chart
    colors = ['#e74c3c', '#3498db', '#2ecc71', '#f1c40f', '#9b59b6']
    bars = plt.bar(range(len(labels)), percentages, color=colors, width=0.6)
    
    # Customize the plot
    plt.title('Current Platform Challenges Faced by Harvard Students', 
             fontsize=14, pad=20)
    plt.ylabel('Percentage of Respondents', fontsize=12)
    
    # Add percentage and count labels on top of bars
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, height + 1,
                f'{int(height)}%\n({counts[bars.index(bar)]} responses)',
                ha='center', va='bottom', fontsize=10)
    
    # Customize x-axis
    plt.xticks(range(len(labels)), labels, fontsize=10)
    
    # Add grid for better readability
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    
    # Set y-axis limits to leave room for labels
    plt.ylim(0, max(percentages) + 10)
    
    # Adjust layout
    plt.tight_layout()
    
    # Add a light box around the plot
    plt.box(True)
    
    return plt.gcf()

def print_challenge_stats():
    # Print summary statistics
    total_responses = sum(challenges[c]['count'] for c in challenges)
    
    print("Platform Challenges Analysis:")
    print("-" * 50)
    print("Total Responses:", total_responses)
    print("\nBreakdown by Challenge:")
    
    sorted_challenges = dict(sorted(challenges.items(), 
                                  key=lambda x: x[1]['percent'], 
                                  reverse=True))
    
    for challenge, data in sorted_challenges.items():
        challenge_name = ' '.join(challenge.split('\n'))
        print("\n" + challenge_name + ":")
        print("  Responses:", data['count'])
        print("  Percentage:", str(data['percent']) + "%")

def main():
    try:
        # Create and save visualization
        fig = create_challenges_visualization()
        plt.savefig('platform_challenges_vertical.png', 
                   bbox_inches='tight', 
                   dpi=300, 
                   facecolor='white', 
                   edgecolor='none')
        plt.close()
        
        # Print statistics
        print_challenge_stats()
            
    except Exception as e:
        print("An error occurred:", str(e))

if __name__ == "__main__":
    main()