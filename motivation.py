import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Data structure
motivators = {
    'Better features\ncompared to\ncurrent platform': {'count': 37, 'percent': 29},
    'Recommendations\nfrom peers': {'count': 36, 'percent': 28},
    'Integration with\nexisting tools': {'count': 29, 'percent': 23},
    'Free trial\nperiod': {'count': 23, 'percent': 18}
}

def create_motivation_visualization():
    # Set up the figure
    plt.figure(figsize=(10, 8))
    
    # Sort motivators by percentage
    sorted_motivators = dict(sorted(motivators.items(), 
                                  key=lambda x: x[1]['percent'], 
                                  reverse=True))
    
    # Prepare data for plotting
    labels = list(sorted_motivators.keys())
    percentages = [d['percent'] for d in sorted_motivators.values()]
    counts = [d['count'] for d in sorted_motivators.values()]
    
    # Create vertical bar chart
    colors = ['#2ecc71', '#3498db', '#e74c3c', '#f1c40f']
    bars = plt.bar(range(len(labels)), percentages, color=colors, width=0.6)
    
    # Customize the plot
    plt.title('What Would Motivate Students to Try a New Platform?', 
             fontsize=14, pad=20)
    plt.ylabel('Percentage of Respondents', fontsize=12)
    
    # Add percentage and count labels on top of bars
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, height + 1,
                f'{int(height)}%\n({counts[bars.index(bar)]})',
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

def print_motivation_stats():
    total_responses = sum(motivators[m]['count'] for m in motivators)
    
    print("Platform Adoption Motivators Analysis:")
    print("-" * 50)
    print("Total Responses:", total_responses)
    print("\nBreakdown by Motivator:")
    
    sorted_motivators = dict(sorted(motivators.items(), 
                                  key=lambda x: x[1]['percent'], 
                                  reverse=True))
    
    for motivator, data in sorted_motivators.items():
        motivator_name = ' '.join(motivator.split('\n'))
        print("\n" + motivator_name + ":")
        print("  Responses:", data['count'])
        print("  Percentage:", str(data['percent']) + "%")

def main():
    try:
        # Create and save visualization
        fig = create_motivation_visualization()
        plt.savefig('platform_motivators_vertical.png', 
                   bbox_inches='tight', 
                   dpi=300, 
                   facecolor='white', 
                   edgecolor='none')
        plt.close()
        
        # Print statistics
        print_motivation_stats()
            
    except Exception as e:
        print("An error occurred:", str(e))

if __name__ == "__main__":
    main()