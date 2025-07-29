# 🎬 IMDb Review Sentiment Analyzer 🎭

A final project for **Harvard's CS50P: Introduction to Programming with Python**, this command-line based tool performs **sentiment analysis** on IMDb reviews using the **VADER** sentiment analysis tool from the Python Standard Library (`nltk`-like scoring approach via `collections.Counter`) and offers basic **data insights and visualization** using `matplotlib`.

---

## 📌 Description

**IMDb Review Sentiment Analyzer** helps analyze thousands of IMDb movie reviews and classify them as positive, negative, or neutral using sentiment scores derived from **VADER** (Valence Aware Dictionary and sEntiment Reasoner) logic.

Key features include:

* Load and parse large IMDb review data from a `.json` file.
* `Preprocess data` keeping relevent collumns 
* Perform sentiment scoring using a custom analyzer built with `collections.Counter`.
* Display overall `sentiment distribution`.
* Visualize results with pie charts using `matplotlib`.
* `Log progress` through each execution stage in a log file.

---

## 🗃 Dataset

The dataset used is:

📁 `data/IMDB_REVIEW.json`

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

---

## ⚙️ Features

* 📂 **Data Loading**: Reads JSON file and parses review entries.
* 😃 **Sentiment Analysis**: Classifies review sentiment using rule-based logic.
* 📊 **Visualization**: Generates chart showing sentiment breakdown.
* 📜 **Logging**: Logs execution steps and analysis progress to `logfile.txt`.

---

## 🔍 Example Usage

```bash
$ python main.py
```

You will see output like:

```
[INFO] 2025-Jul-29-14:23:12 - Loading dataset...
[INFO] 2025-Jul-29-14:23:13 - Performing sentiment analysis...
[INFO] 2025-Jul-29-14:23:15 - Plotting results...
[INFO] 2025-Jul-29-14:23:16 - Task Completed Successfully.
```

📊 A pie chart will pop up showing the distribution of positive, negative, and neutral reviews.

---

## 🧪 File Structure

```
.
├── data/
│   └── IMDB_REVIEW.json
├── main.py                # Main CLI and logic
├── logfile.txt            # Progress log
├── requirements.txt       # Python standard libraries (documentation only)
├── README.md              # You are here
```
---

## Acknowledgements

* [IMDb](https://www.imdb.com) for providing user-generated content.
* [Kaggle](https://www.kaggle.com/dsv/1836923) for hosting the dataset.
* Harvard CS50P for laying the foundation of this project.

---
