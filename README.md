# 🎬 IMDb Review Sentiment Analyzer 🎭

A comprehensive sentiment analysis tool for IMDb movie reviews, developed as a final project for **Harvard's CS50P: Introduction to Programming with Python**.

## 📌 Features

- **Data Preprocessing**: Cleans and prepares raw IMDb review data
- **Sentiment Analysis**: Uses VADER (Valence Aware Dictionary and sEntiment Reasoner)
- **Interactive CLI**: User-friendly command-line interface
- **Visualizations**: Multiple plotting options including:
  - Rating distribution charts
  - Sentiment heatmaps
  - Spoiler impact analysis
  - Word clouds for positive/negative reviews
- **Progress Logging**: Detailed execution logging

## 📦 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/imdb-sentiment-analyzer.git
   cd imdb-sentiment-analyzer
   ```

2. Install required dependencies:
   ```bash
   pip install pandas matplotlib seaborn wordcloud vaderSentiment
   ```

3. Download the dataset from [Kaggle](https://www.kaggle.com/dsv/1836923) and place it in the project directory as `IMDB_REVIEWS.json`

## Usage

Run the interactive analyzer:
```bash
python analyzer.py
```

The CLI menu offers these options:
```
IMDb Review Sentiment Analysis Tool
1. Preprocess & Load Data
2. Perform Sentiment Analysis
3. Plot Rating Distribution (1-10)
4. Plot Sentiment vs. Rating Heatmap
5. Analyze Spoiler Impact on Sentiment
6. Generate Word Clouds (Positive/Negative Reviews)
7. View Plots at Once
8. Exit
```

## 📊 Sample Visualizations

### Rating Distribution
![Rating Distribution](reviews_per_rating.png)

### Sentiment Heatmap
![Sentiment Heatmap](Sentiment_vs_rating.png)

### Word Clouds
![Word Clouds](word_cloud.png)

## 📂 Project Structure
```
imdb-sentiment-analyzer/
├── data/                  # Dataset directory
│   └── IMDB_REVIEWS.json  # Source dataset (not included in repo)
├── analyzer.py            # Main analysis script
├── code_log.txt           # Execution logs
├── README.md              # Project documentation
└── *.png                  # Generated visualization files
```

## 📝 Dataset Information
Each entry includes:

| Field           | Description                                         |
| --------------- | --------------------------------------------------- |
| review\_id      | Unique identifier per review (from IMDb)            |
| reviewer        | Username of the reviewer                            |
| movie           | Name of the show/movie                              |
| rating          | Rating out of 10 (optional)                         |
| review\_summary | Summary of the review                               |
| review\_date    | Date of review posting                              |
| spoiler\_tag    | 1 = spoiler, 0 = not a spoiler                      |
| review\_detail  | Full detail of the review                           |
| helpful         | List with count of helpful votes: \[helpful, total] |

📌 **Total Reviews:** 5,571,499

🎬 **Total Shows:** 453,528

👥 **Users:** 1,699,310

⚠️ **Spoilers:** 1,186,611

📚 **Citation:**

```
@misc{enam biswas_2021, 
title={IMDb Review Dataset - ebD}, 
url={https://www.kaggle.com/dsv/1836923}, 
DOI={10.34740/KAGGLE/DSV/1836923}, 
publisher={Kaggle}, 
author={Enam Biswas}, 
year={2021}
```


## 🛠 Dependencies

- Python 3.8+
- pandas
- matplotlib
- seaborn
- wordcloud
- vaderSentiment

## Acknowledgments

- Harvard University for CS50P course materials
- IMDb for user-generated content
- Kaggle for hosting the dataset
- NLTK project for VADER sentiment analysis tools
