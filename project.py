# Importing the required libraries
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud, STOPWORDS
import time

# Logging function
def log_progress(message):
    """Logs a timestamped message to the code_log.txt file."""
    time_stamp_format = '%Y-%b-%d-%H:%M:%S'
    now = datetime.now()
    time_stamp = now.strftime(time_stamp_format)
    with open("code_log.txt", "a") as f:
        f.write(f"{time_stamp} : {message}\n")

# Set style for plots
sns.set_style("whitegrid")

def plot_rating_distribution(df):
    """Plotting bar graph of rating distribution and saving as PNG."""
    df['rating'] = pd.to_numeric(df['rating'], errors='coerce')
    
    plt.figure(figsize=(8, 5))
    rating_counts = df['rating'].value_counts().sort_index()
    plt.bar(rating_counts.index, rating_counts.values)
    plt.title("Review Rating Trend")
    plt.xlabel("Rating (1-10)")
    plt.ylabel("Total Reviews")
    plt.tight_layout()
    
    figure_name = "reviews_per_rating.png"
    plt.savefig(figure_name, dpi=300, bbox_inches="tight")
    
    plt.show()
    
    log_progress("Rating distribution plotted")
    log_progress(f"Figure saved as: {figure_name}")

def plot_sentiment_heatmap(analyzed_df):
    """Plotting heatmap of sentiment vs rating and saving as PNG."""
    plt.figure(figsize=(10, 6))
    sentiment_rating = pd.crosstab(analyzed_df['rating'], analyzed_df['sentiment'])
    sns.heatmap(sentiment_rating, annot=True, fmt='d', cmap="YlGnBu")
    plt.title("Sentiment vs Rating")
    plt.xlabel("Sentiment")
    plt.ylabel("Rating")
    plt.tight_layout()
    
    figure_name = "sentiment_vs_rating.png"
    plt.savefig(figure_name, dpi=300, bbox_inches="tight")
    
    plt.show()
    
    log_progress("Sentiment vs. rating heatmap plotted")
    log_progress(f"Figure saved as: {figure_name}")

def plot_spoiler_impact(analyzed_df):
    """Plotting boxplot of spoiler tag impact and saving as PNG."""
    plt.figure(figsize=(8, 5))

    if 'spoiler_tag' in analyzed_df.columns:
        analyzed_df['spoiler_tag'] = analyzed_df['spoiler_tag'].map({0: 'No', 1: 'Yes'})
        
    sns.boxplot(x='spoiler_tag', y='compound', data=analyzed_df)
    plt.title("Do Spoilers Affect Sentiment?")
    plt.xlabel("Contains Spoiler?")
    plt.ylabel("Sentiment Score")
    plt.tight_layout()
    
    figure_name = "spoiler_impact.png"
    plt.savefig(figure_name, dpi=300, bbox_inches="tight")
    
    plt.show()
    
    log_progress("Spoiler impact plotted")
    log_progress(f"Figure saved as: {figure_name}")

def view_all_analyses(analyzed_df):
    """Displays a combined dashboard of all visualizations."""
    analyzed_df['rating'] = pd.to_numeric(analyzed_df['rating'], errors='coerce')
    if 'spoiler_tag' in analyzed_df.columns:
        analyzed_df['spoiler_tag'] = analyzed_df['spoiler_tag'].map({0: 'No', 1: 'Yes'})

    plt.figure(figsize=(15, 10))

    # Subplot 1: Rating distribution
    plt.subplot(2, 2, 1)
    rating_counts = analyzed_df['rating'].value_counts().sort_index()
    sns.barplot(x=rating_counts.index, y=rating_counts.values, palette="viridis")
    plt.title("Reviews per Rating (1-10)")
    plt.xlabel("Rating")
    plt.ylabel("Total Reviews")

    # Subplot 2: Sentiment heatmap
    plt.subplot(2, 2, 2)
    sentiment_rating = pd.crosstab(analyzed_df['rating'], analyzed_df['sentiment'])
    sns.heatmap(sentiment_rating, annot=True, fmt='d', cmap="YlGnBu")
    plt.title("Sentiment per Rating")
    plt.xlabel("Sentiment")
    plt.ylabel("Rating")

    # Subplot 3: Spoiler impact
    plt.subplot(2, 1, 2)
    if 'spoiler_tag' in analyzed_df.columns:
        sns.boxplot(x='spoiler_tag', y='compound', data=analyzed_df)
        plt.title("Spoiler Impact on Sentiment")
        plt.xlabel("Contains Spoiler?")
        plt.ylabel("Sentiment Score")
    else:
        plt.text(0.5, 0.5, "No spoiler data available", ha='center')

    plt.tight_layout()
    plt.savefig("analysis_dashboard.png", dpi=300, bbox_inches='tight')
    plt.show()
    
    log_progress("Displayed full analysis dashboard")
    log_progress("Dashboard saved as: analysis_dashboard.png")

def interactive_analysis():
    """Main loop for interactive analysis menu."""
    analyzed_df = pd.read_csv("sentiment_analysis_results.csv")
    df = pd.read_csv("preprocessed_IMDB_REVIEWS.csv")

    while True:
        print("\nIMDb Review Sentiment Analysis Tool")
        print("1. Plot Rating Distribution (1-10)")
        print("2. Plot Sentiment vs. Rating Heatmap")
        print("3. Analyze Spoiler Impact on Sentiment")
        print("4. View All Figures (Dashboard)")
        print("5. Exit")
        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            plot_rating_distribution(df)
        elif choice == "2":
            plot_sentiment_heatmap(analyzed_df)
        elif choice == "3":
            if 'spoiler_tag' not in analyzed_df.columns:
                print("Error: No 'spoiler_tag' column found!")
            else:
                plot_spoiler_impact(analyzed_df)
        elif choice == "4":
            view_all_analyses(analyzed_df)
        elif choice == "5":
            print("\nExiting...")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 6.")
        time.sleep(1)

if __name__ == "__main__":
    interactive_analysis()
