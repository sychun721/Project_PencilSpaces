import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Data structure
workshop_preferences = {
    'Not interested in\nnew tools': {'count': 21, 'percent': 30},
    'Maybe, with more\ninformation': {'count': 20, 'percent': 29},
    'Yes, if demo is\nshort & engaging': {'count': 16, 'percent': 23},
    'Yes, with free trials\n& giveaways': {'count': 13, 'percent': 19}
}

def create_workshop_visualization():
    # Set up the figure
    plt.figure(figsize=(10, 8))
    
    # Sort preferences by percentage
    sorted_preferences = dict(sorted(workshop_preferences.items(), 
                                   key=lambda x: x[1]['percent'], 
                                   reverse=True))
    
    # Prepare data for plotting
    labels = list(sorted_preferences.keys())
    percentages = [d['percent'] for d in sorted_preferences.values()]
    counts = [d['count'] for d in sorted_preferences.values()]
    
    # Create vertical bar chart
    colors = ['#e74c3c', '#3498db', '#2ecc71', '#f1c40f']
    bars = plt.bar(range(len(labels)), percentages, color=colors, width=0.6)
    
    # Customize the plot
    plt.title('Interest in Platform Demo/Workshop Attendance', 
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

def print_workshop_stats():
    # Print summary statistics
    total_responses = sum(workshop_preferences[p]['count'] for p in workshop_preferences)
    
    print("Workshop Interest Analysis:")
    print("-" * 50)
    print("Total Responses:", total_responses)
    print("\nBreakdown by Preference:")
    
    sorted_preferences = dict(sorted(workshop_preferences.items(), 
                                   key=lambda x: x[1]['percent'], 
                                   reverse=True))
    
    for preference, data in sorted_preferences.items():
        preference_name = ' '.join(preference.split('\n'))
        print("\n" + preference_name + ":")
        print("  Responses:", data['count'])
        print("  Percentage:", str(data['percent']) + "%")

def main():
    try:
        # Create and save visualization
        fig = create_workshop_visualization()
        plt.savefig('workshop_interest.png', 
                   bbox_inches='tight', 
                   dpi=300, 
                   facecolor='white', 
                   edgecolor='none')
        plt.close()
        
        # Print statistics
        print_workshop_stats()
            
    except Exception as e:
        print("An error occurred:", str(e))

if __name__ == "__main__":
    main()
