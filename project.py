# Importing the required libraries
import pandas as pd
from datetime import datetime
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt
import seaborn as sns
import time

def log_progress(message):
    """This function logs the mentioned message of a given stage of the code execution to a log file."""
    time_stamp_format = '%Y-%b-%d-%H:%M:%S'
    now = datetime.now()
    time_stamp = now.strftime(time_stamp_format)

    with open("code_log.txt", "a") as f:
        f.write(time_stamp + ' : ' + message + '\n')

def preprocess_imdb_reviews(filename):
    """This function Preprocess IMDb review dataset and log the processing details."""
    try:
        df = pd.read_json(filename)
        df = df[['reviewer', 'movie', 'rating', 'review_summary', 'spoiler_tag', 'review_detail']]
        df = df.dropna(subset=['review_detail'])

        df['review_detail'] = df['review_detail'].str.lower().str.strip()
        df['review_detail'] = df['review_detail'].str.replace(r'<.*?>', ' ', regex=True)
        df['review_detail'] = df['review_detail'].str.replace(r'[^a-z\s]', '', regex=True)
        df['review_detail'] = df['review_detail'].str.replace(r'\s+', ' ', regex=True)

        df = df.drop_duplicates(subset='review_detail')
        df = df.reset_index(drop=True)

        output_file = f"preprocessed_{filename.replace('.json', '.csv')}"
        df.to_csv(output_file, index=False)

        message_1 = "Pre processing performed"
        message_2 = f"file saved as : {output_file}\n"

        log_progress(message_1)
        log_progress(message_2)

        print(f"Preprocessing complete. Saved to '{output_file}'")
        return df

    except Exception as e:
        print(f"Error: {e}")
        log_progress(f"Error during preprocessing: {e}")
        return None

def analyze_sentiment(df, text_col='review_detail'):
    """This function perform Sentiment analysis using VADER and returns DataFrame"""
    analyzer = SentimentIntensityAnalyzer()

    sentiments = df[text_col].apply(analyzer.polarity_scores).apply(pd.Series)
    df = pd.concat([df, sentiments], axis=1)

    df['sentiment'] = pd.cut(df['compound'], bins=[-1, -0.05, 0.05, 1], labels=['Negative', 'Neutral', 'Positive'])

    filename = "sentiment_analysis_results.csv"
    df.to_csv(filename, index=False)
    print(f"Saved to ", filename)

    message_1 = "Sentiment Analysis performed"
    message_2 = f"file saved as : {filename}\n"

    log_progress(message_1)
    log_progress(message_2)
    return df

def plot_rating_distribution(df):
    """Plotting Bar graph of rating and saving as png"""
    plt.figure(figsize=(8, 5))
    rating_counts = df['rating'].value_counts().sort_index()
    plt.bar(rating_counts.index, rating_counts.values)
    plt.title("Review Rating trend")
    plt.xlabel("Rating (1-10)")
    plt.ylabel("Total Reviews")
    plt.tight_layout()

    figure_name = "reviews_per_rating.png"
    plt.savefig(figure_name, dpi=300, bbox_inches="tight")

    plt.show()

    message_1 = "Rating distribution (1-10) plotted"
    message_2 = f"Figure saved as: {figure_name}\n"

    log_progress(message_1)
    log_progress(message_2)

def plot_sentiment_heatmap(analyzed_df):
    """plotting Sentiment vs rating heatmap and saving as png"""
    plt.figure(figsize=(10, 6))
    sentiment_rating = pd.crosstab(analyzed_df['rating'], analyzed_df['sentiment'])
    sns.heatmap(sentiment_rating, annot=True, fmt='d', cmap="YlGnBu")
    plt.title("Sentiment vs rating")
    plt.xlabel("Sentiment")
    plt.ylabel("Rating")
    plt.tight_layout()

    figure_name = "Sentiment_vs_rating.png"
    plt.savefig(figure_name, dpi=300, bbox_inches="tight")

    plt.show()

    message_1 = "Sentiment vs. rating heatmap plotted"
    message_2 = f"figure saved as : {figure_name}\n"

    log_progress(message_1)
    log_progress(message_2)

def plot_spoiler_impact(analyzed_df):
    """Plotting line graph of Spoiler impact and saving as pngs"""
    plt.figure(figsize=(8, 5))
    sns.boxplot(x='spoiler_tag', y='compound', data=analyzed_df)
    plt.title("Do Spoilers Affect Sentiment?")
    plt.xlabel("Contains Spoiler?")
    plt.ylabel("Sentiment Score")
    plt.tight_layout()

    figure_name = "spoiler_impact.png"
    plt.savefig(figure_name, dpi=300, bbox_inches="tight")

    plt.show()

    message_1 = "Spoiler impact plotted"
    message_2 = f"figure saved as : {figure_name}\n"

    log_progress(message_1)
    log_progress(message_2)

def view_all_analyses(analyzed_df):
    plt.figure(figsize=(15, 10))

    # Rating distribution
    plt.subplot(2, 2, 1)
    rating_counts = analyzed_df['rating'].value_counts().sort_index()
    sns.barplot(x=rating_counts.index, y=rating_counts.values, palette="viridis")
    plt.title("Reviews per Rating (1-10)")

    # Sentiment heatmap
    plt.subplot(2, 2, 2)
    sentiment_rating = pd.crosstab(analyzed_df['rating'], analyzed_df['sentiment'])
    sns.heatmap(sentiment_rating, annot=True, fmt='d', cmap="YlGnBu")
    plt.title("Sentiment per Rating")

    # Spoiler impact
    plt.subplot(2, 2, 3)
    if 'spoiler_tag' in analyzed_df.columns:
        sns.boxplot(x='spoiler_tag', y='compound', data=analyzed_df)
        plt.title("Spoiler Impact on Sentiment")
    else:
        plt.text(0.5, 0.5, "No spoiler data", ha='center')

    message = "displayed dashboard"
    log_progress(message)

def interactive_analysis():
    df = None
    analyzed_df = None

    while True:
        """Displays the interactive menu options."""
        print("\nIMDb Review Sentiment Analysis Tool")
        print("1. Preprocess & Load Data")
        print("2. Perform Sentiment Analysis")
        print("3. Plot Rating Distribution (1-10)")
        print("4. Plot Sentiment vs. Rating Heatmap")
        print("5. Analyze Spoiler Impact on Sentiment")
        print("6. View all figures at Once")
        print("7. Exit")
        choice = input("Enter your choice (1-9): ").strip()

        if choice == "1":
            print("\nPreprocessing data...")
            df = preprocess_imdb_reviews("IMDB_REVIEWS.json")
            time.sleep(1)

        elif choice == "2":
            if df is None:
                print("Error: Load data first (Option 1)!")
            else:
                print("\nAnalyzing sentiment...")
                analyzed_df = (
                    analyze_sentiment(df))
            time.sleep(1)

        elif choice == "3":
            if df is None:
                print("Error: No data loaded!")
            else:
                plot_rating_distribution(df)
            time.sleep(1)

        elif choice == "4":
            if analyzed_df is None:
                print("Error: Perform sentiment analysis first (Option 2)!")
            else:
                plot_sentiment_heatmap(analyzed_df)
            time.sleep(1)

        elif choice == "5":
            if analyzed_df is None:
                print("Error: Perform sentiment analysis first (Option 2)!")
            elif 'spoiler_tag' not in analyzed_df.columns:
                print("Error: No 'spoiler_tag' column found!")
            else:
                plot_spoiler_impact(analyzed_df)
            time.sleep(1)

        elif choice == "6":
            if analyzed_df is None:
                print("Error: Perform sentiment analysis first (Option 2)!")
            else:
                view_all_analyses(analyzed_df)
            time.sleep(1)

        elif choice == "7":
            print("\nExiting...")
            break

        else:
            print("Invalid choice! Please enter 1-8.")
            time.sleep(1)

if __name__ == "__main__":
    interactive_analysis()