import os
import pandas as pd
import pytest
from project import preprocess_imdb_reviews, analyze_sentiment

@pytest.fixture
def sample_json(tmp_path):
    data = [
        {
            "reviewer": "John",
            "movie": "Movie A",
            "rating": 8,
            "review_summary": "Good movie",
            "spoiler_tag": 0,
            "review_detail": "This movie was AMAZING!!! <br> Loved it."
        },
        {
            "reviewer": "Alice",
            "movie": "Movie B",
            "rating": 5,
            "review_summary": "Okay",
            "spoiler_tag": 1,
            "review_detail": "It was okay, nothing special..."
        }
    ]
    with zipfile.ZipFile('sample.json.zip', 'r') as zip_ref:
        zip_ref.extractall()
        
    file_path = "sample.json"
    pd.DataFrame(data).to_json(file_path, orient="records")
    return str(file_path)

def test_preprocess_imdb_reviews(sample_json):
    df = preprocess_imdb_reviews(sample_json)
    assert isinstance(df, pd.DataFrame)
    assert not df.empty
    assert "review_detail" in df.columns
    # Check cleaned text
    assert "<" not in df["review_detail"].iloc[0]
    # Check output file exists
    output_file = f"preprocessed_{os.path.basename(sample_json).replace('.json', '.csv')}"
    assert os.path.exists(output_file)

def test_analyze_sentiment(sample_json):
    """Test that sentiment analysis adds sentiment scores."""
    df = preprocess_imdb_reviews(sample_json)
    analyzed_df = analyze_sentiment(df)
    assert "compound" in analyzed_df.columns
    assert "sentiment" in analyzed_df.columns
    assert analyzed_df["sentiment"].isin(["Positive", "Negative", "Neutral"]).any()

def test_sentiment_analysis_results(sample_json):
    """Test that sentiment analysis produces expected results."""
    df = preprocess_imdb_reviews(sample_json)
    analyzed_df = analyze_sentiment(df)
    
    positive_reviews = analyzed_df[analyzed_df['sentiment'] == 'Positive']
    assert all(positive_reviews['compound'] > 0.05)
    
    neutral_reviews = analyzed_df[analyzed_df['sentiment'] == 'Neutral']
    assert all((neutral_reviews['compound'] >= -0.05) & (neutral_reviews['compound'] <= 0.05))
    
    negative_reviews = analyzed_df[analyzed_df['sentiment'] == 'Negative']
    assert all(negative_reviews['compound'] < -0.05)
    
    assert os.path.exists("sentiment_analysis_results.csv")
