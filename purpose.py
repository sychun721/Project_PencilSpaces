import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Create the data structure
categories = ['Club Meetings/Syncs', 'Peer Tutoring/Office Hours', 
             'Social Purposes', 'Online Lectures', 'Academic Group Projects']

# Create weights for ranks (rank 1 has highest weight)
weights = {1: 5, 2: 4, 3: 3, 4: 2, 5: 1}

# Data for each category with ranks and percentages
data = {
    'Club Meetings/Syncs': {1: 0.40, 2: 0.42, 3: 0.13, 4: 0.03, 5: 0.02},
    'Peer Tutoring/Office Hours': {1: 0.22, 2: 0.17, 3: 0.29, 4: 0.17, 5: 0.14},
    'Social Purposes': {1: 0.10, 2: 0.08, 3: 0.25, 4: 0.29, 5: 0.27},
    'Online Lectures': {1: 0.19, 2: 0.19, 3: 0.22, 4: 0.22, 5: 0.17},
    'Academic Group Projects': {1: 0.10, 2: 0.16, 3: 0.12, 4: 0.24, 5: 0.39}
}

def calculate_weighted_scores():
    weighted_scores = {}
    for category in categories:
        score = sum(data[category][rank] * weights[rank] for rank in weights)
        weighted_scores[category] = score
    return weighted_scores

def create_ranking_visualization():
    # Set up the figure with two subplots
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(15, 12), height_ratios=[1, 1.5])
    
    # Colors for the bars
    colors = ['#2ecc71', '#3498db', '#9b59b6', '#e74c3c', '#f1c40f']
    
    # Plot 1: Weighted Scores
    weighted_scores = calculate_weighted_scores()
    sorted_items = sorted(weighted_scores.items(), key=lambda x: x[1], reverse=True)
    categories_sorted = [x[0] for x in sorted_items]
    scores_sorted = [x[1] for x in sorted_items]
    
    bars1 = ax1.bar(range(len(categories_sorted)), scores_sorted, color=colors)
    
    # Customize first plot
    ax1.set_title('Overall Weighted Importance of Platform Uses', fontsize=14, pad=20)
    ax1.set_xlabel('Platform Use Category', fontsize=12)
    ax1.set_ylabel('Weighted Importance Score', fontsize=12)
    
    # Add value labels on top of bars
    for bar in bars1:
        height = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width()/2., height,
                f'{height:.2f}',
                ha='center', va='bottom')
    
    ax1.set_xticks(range(len(categories_sorted)))
    ax1.set_xticklabels([cat.replace('/', '\n') for cat in categories_sorted])
    ax1.grid(axis='y', linestyle='--', alpha=0.7)
    
    # Plot 2: Percentage Breakdown
    x = np.arange(len(categories))
    width = 0.15  # Width of the bars
    
    # Plot bars for each rank
    for rank in range(1, 6):
        percentages = [data[cat][rank] * 100 for cat in categories]
        offset = (rank - 3) * width
        bars = ax2.bar(x + offset, percentages, width, label=f'Rank {rank}')
        
        # Add percentage labels on the bars
        for bar in bars:
            height = bar.get_height()
            if height > 5:  # Only show label if percentage is > 5%
                ax2.text(bar.get_x() + bar.get_width()/2., height,
                        f'{height:.0f}%',
                        ha='center', va='bottom', fontsize=8)
    
    # Customize second plot
    ax2.set_title('Percentage Breakdown by Rank', fontsize=14, pad=20)
    ax2.set_xlabel('Platform Use Category', fontsize=12)
    ax2.set_ylabel('Percentage', fontsize=12)
    ax2.set_xticks(x)
    ax2.set_xticklabels([cat.replace('/', '\n') for cat in categories])
    ax2.legend(title='Rankings')
    ax2.grid(axis='y', linestyle='--', alpha=0.7)
    
    plt.tight_layout()
    return fig

def main():
    try:
        # Create and save visualization
        fig = create_ranking_visualization()
        plt.savefig('platform_usage_analysis.png', bbox_inches='tight', dpi=300)
        plt.close()
        
        # Print detailed breakdown
        print("\nDetailed Breakdown of Platform Usage:")
        print("-" * 50)
        weighted_scores = calculate_weighted_scores()
        sorted_categories = sorted(weighted_scores.items(), key=lambda x: x[1], reverse=True)
        
        for category, weighted_score in sorted_categories:
            print(f"\n{category}:")
            print(f"Weighted Score: {weighted_score:.2f}")
            print("Rank Breakdown:")
            for rank in range(1, 6):
                percentage = data[category][rank] * 100
                print(f"  Rank {rank}: {percentage:.1f}%")
            
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()