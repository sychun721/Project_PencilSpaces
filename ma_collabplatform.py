import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Create the data structure
features = [
    'Real-Time Document Collaboration',
    'Interactive Quizzes & Teaching Tools',
    'Meeting Scheduling & Attendance',
    'All-in-One Functionality',
    'Customizable Features',
    'Data Privacy & Security'
]

# Create weights for ranks (rank 1 has highest weight)
weights = {1: 6, 2: 5, 3: 4, 4: 3, 5: 2, 6: 1}

# Data for each feature with ranks and percentages
data = {
    'Real-Time Document Collaboration': 
        {1: 0.21, 2: 0.21, 3: 0.21, 4: 0.15, 5: 0.15, 6: 0.07},
    'Interactive Quizzes & Teaching Tools': 
        {1: 0.10, 2: 0.08, 3: 0.16, 4: 0.23, 5: 0.26, 6: 0.16},
    'Meeting Scheduling & Attendance': 
        {1: 0.10, 2: 0.16, 3: 0.25, 4: 0.16, 5: 0.16, 6: 0.16},
    'All-in-One Functionality': 
        {1: 0.36, 2: 0.20, 3: 0.05, 4: 0.11, 5: 0.13, 6: 0.15},
    'Customizable Features': 
        {1: 0.13, 2: 0.25, 3: 0.26, 4: 0.15, 5: 0.10, 6: 0.11},
    'Data Privacy & Security': 
        {1: 0.10, 2: 0.10, 3: 0.07, 4: 0.20, 5: 0.20, 6: 0.34}
}

def calculate_weighted_scores():
    weighted_scores = {}
    for feature in features:
        score = sum(data[feature][rank] * weights[rank] for rank in weights)
        weighted_scores[feature] = score
    return weighted_scores

def create_ranking_visualization():
    # Set up the figure with two subplots
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(15, 12), height_ratios=[1, 1.5])
    
    # Colors for the bars
    colors = ['#2ecc71', '#3498db', '#9b59b6', '#e74c3c', '#f1c40f', '#1abc9c']
    
    # Plot 1: Weighted Scores
    weighted_scores = calculate_weighted_scores()
    sorted_items = sorted(weighted_scores.items(), key=lambda x: x[1], reverse=True)
    features_sorted = [x[0] for x in sorted_items]
    scores_sorted = [x[1] for x in sorted_items]
    
    bars1 = ax1.bar(range(len(features_sorted)), scores_sorted, color=colors)
    
    # Customize first plot
    ax1.set_title('Overall Priority of Desired Features', fontsize=14, pad=20)
    ax1.set_xlabel('Feature', fontsize=12)
    ax1.set_ylabel('Priority Score', fontsize=12)
    
    # Add value labels on top of bars
    for bar in bars1:
        height = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width()/2., height,
                f'{height:.2f}',
                ha='center', va='bottom')
    
    ax1.set_xticks(range(len(features_sorted)))
    ax1.set_xticklabels([feat.replace('&', '\n&') for feat in features_sorted], 
                        rotation=45, ha='right')
    ax1.grid(axis='y', linestyle='--', alpha=0.7)
    
    # Plot 2: Percentage Breakdown
    x = np.arange(len(features))
    width = 0.12
    
    # Plot bars for each rank
    for rank in range(1, 7):
        percentages = [data[feat][rank] * 100 for feat in features]
        offset = (rank - 3.5) * width
        bars = ax2.bar(x + offset, percentages, width, label=f'Rank {rank}')
        
        # Add percentage labels on the bars
        for bar in bars:
            height = bar.get_height()
            if height > 10:  # Only show label if percentage is > 10%
                ax2.text(bar.get_x() + bar.get_width()/2., height,
                        f'{height:.0f}%',
                        ha='center', va='bottom', fontsize=8)
    
    # Customize second plot
    ax2.set_title('Percentage Breakdown by Rank', fontsize=14, pad=20)
    ax2.set_xlabel('Feature', fontsize=12)
    ax2.set_ylabel('Percentage of Responses', fontsize=12)
    ax2.set_xticks(x)
    ax2.set_xticklabels([feat.replace('&', '\n&') for feat in features], 
                        rotation=45, ha='right')
    ax2.legend(title='Rankings', bbox_to_anchor=(1.05, 1), loc='upper left')
    ax2.grid(axis='y', linestyle='--', alpha=0.7)
    
    plt.tight_layout()
    return fig

def main():
    try:
        # Create and save visualization
        fig = create_ranking_visualization()
        plt.savefig('desired_features_analysis.png', bbox_inches='tight', dpi=300, 
                   facecolor='white', edgecolor='none')
        plt.close()
        
        # Print detailed breakdown
        print("\nDetailed Breakdown of Desired Features:")
        print("-" * 50)
        weighted_scores = calculate_weighted_scores()
        sorted_features = sorted(weighted_scores.items(), key=lambda x: x[1], reverse=True)
        
        for feature, weighted_score in sorted_features:
            print(f"\n{feature}:")
            print(f"Priority Score: {weighted_score:.2f}")
            print("Rank Breakdown:")
            for rank in range(1, 7):
                percentage = data[feature][rank] * 100
                print(f"  Rank {rank}: {percentage:.1f}%")
            
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
