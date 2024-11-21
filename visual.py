import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Set style for better visualizations
plt.style.use('seaborn')
sns.set_palette("husl")

def clean_and_process_data(df):
    # Process platform usage rankings
    usage_cols = ['Club Meetings/ Syncs', 'Peer Tutoring/ Office Hours', 
                 'Academic Group Projects', 'Online Lectures', 'Social Purposes']
    
    usage_data = []
    for _, row in df.iterrows():
        uses = row['For which purpose(s) do you use Zoom or other online collaboration platforms the most often at Harvard? (Rank)'].split(',')
        for use in uses:
            use = use.strip()
            if any(keyword in use for keyword in usage_cols):
                usage_data.append(use)
    
    return pd.Series(usage_data).value_counts()

def create_visualizations(df):
    # Create a figure with multiple subplots
    plt.figure(figsize=(20, 15))
    
    # 1. Platform Usage Analysis
    plt.subplot(2, 2, 1)
    usage_counts = clean_and_process_data(df)
    usage_counts.plot(kind='bar')
    plt.title('Platform Usage Distribution at Harvard', fontsize=14, pad=20)
    plt.xlabel('Usage Type')
    plt.ylabel('Number of Students')
    plt.xticks(rotation=45, ha='right')
    
    # 2. Important Features Analysis
    plt.subplot(2, 2, 2)
    features_data = []
    for features in df['What features do you find most important in an online collaboration platform? (Rank)']:
        features_list = features.split(',')
        features_data.extend([f.strip() for f in features_list])
    
    feature_counts = pd.Series(features_data).value_counts()
    feature_counts.plot(kind='barh')
    plt.title('Most Important Features for Students', fontsize=14, pad=20)
    plt.xlabel('Number of Students')
    
    # 3. Motivation Analysis
    plt.subplot(2, 2, 3)
    motivation_data = []
    for motivations in df['What would motivate you to try a new collaboration online platform?']:
        if isinstance(motivations, str):
            motivation_list = motivations.split(',')
            motivation_data.extend([m.strip() for m in motivation_list])
    
    motivation_counts = pd.Series(motivation_data).value_counts()
    plt.pie(motivation_counts, labels=motivation_counts.index, autopct='%1.1f%%')
    plt.title('Factors Motivating Platform Adoption', fontsize=14, pad=20)
    
    # 4. Challenges Analysis
    plt.subplot(2, 2, 4)
    challenges_data = []
    for challenges in df['What challenges do you currently face with your online collaboration platform?']:
        if isinstance(challenges, str):
            challenge_list = challenges.split(',')
            challenges_data.extend([c.strip() for c in challenge_list])
    
    challenge_counts = pd.Series(challenges_data).value_counts()
    challenge_counts.plot(kind='barh')
    plt.title('Current Platform Challenges', fontsize=14, pad=20)
    plt.xlabel('Number of Students')
    
    plt.tight_layout()
    plt.show()

def analyze_peer_tutoring(df):
    # Specific analysis for peer tutoring
    plt.figure(figsize=(15, 6))
    
    # Filter for tutoring-related responses
    tutoring_data = []
    for _, row in df.iterrows():
        if 'Peer Tutoring' in row['For which purpose(s) do you use Zoom or other online collaboration platforms the most often at Harvard? (Rank)']:
            tutoring_data.append(row['Which year are you in (if you are not a student, please specify your position at Harvard)?'])
    
    tutoring_by_year = pd.Series(tutoring_data).value_counts()
    
    plt.subplot(1, 2, 1)
    tutoring_by_year.plot(kind='bar')
    plt.title('Peer Tutoring Usage by Year Level')
    plt.xlabel('Year')
    plt.ylabel('Number of Students')
    plt.xticks(rotation=45)
    
    plt.tight_layout()
    plt.show()

def analyze_marketing_channels(df):
    # Analysis for marketing channels effectiveness
    plt.figure(figsize=(12, 6))
    
    referral_data = []
    for motivations in df['What would motivate you to try a new collaboration online platform?']:
        if isinstance(motivations, str) and 'Recommendations from friends or peers' in motivations:
            referral_data.append('Peer Recommendations')
        if isinstance(motivations, str) and 'Better features' in motivations:
            referral_data.append('Feature Marketing')
        if isinstance(motivations, str) and 'Free trial' in motivations:
            referral_data.append('Free Trial')
    
    channel_counts = pd.Series(referral_data).value_counts()
    channel_counts.plot(kind='bar')
    plt.title('Effective Marketing Channels')
    plt.xlabel('Channel')
    plt.ylabel('Number of Students')
    plt.xticks(rotation=45)
    
    plt.tight_layout()
    plt.show()

def main():
    # Read the data
    df = pd.read_csv('survey_data.csv')
    
    # Create main visualizations
    create_visualizations(df)
    
    # Create specific analyses
    analyze_peer_tutoring(df)
    analyze_marketing_channels(df)
    
    # Print key insights
    print("\nKey Marketing Insights:")
    print("-" * 50)
    print("1. Platform Usage Distribution")
    print("2. Feature Preferences")
    print("3. Marketing Channel Effectiveness")
    print("4. Current Pain Points")

if __name__ == "__main__":
    main()
