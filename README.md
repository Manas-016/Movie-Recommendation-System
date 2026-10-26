# 🎬 Movie Recommendation System

A content-based Movie Recommendation System built using Python, Pandas, and Scikit-learn. It recommends movies similar to a user's selected movie by analyzing movie genres, plot overviews, and taglines using TF-IDF vectorization and cosine similarity.

## 🚀 Features

- Recommends the top 5 similar movies based on a selected movie.
- Uses TF-IDF to convert textual movie information into numerical vectors.
- Uses cosine similarity to measure similarity between movies.
- Displays recommended movie titles, genres, and similarity scores.
- Handles missing text data and invalid movie titles.

## 🛠️ Technologies Used

- **Python** — Core programming language
- **Pandas** — Data loading and preprocessing
- **NumPy** — Numerical operations
- **Scikit-learn** — TF-IDF vectorization and cosine similarity

## 📂 Project Structure

```text
Movie Recommendation/
├── Dataset/
│   └── tmdb_5000_movies.csv
├── recommender.py
├── requirements.txt
├── .gitignore
└── README.md
```

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/Manas-016/Movie-Recommendation-System.git
cd Movie-Recommendation-System
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Prepare the dataset

Download the TMDB 5000 Movie Dataset from Kaggle:

https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata

Place the required CSV file in the appropriate project directory and update the file path in the code if necessary.

### 4. Run the project

```bash
python recommender.py
```

## 🧠 How It Works

1. **Data Preprocessing:** Loads movie metadata and handles missing values.
2. **Feature Combination:** Combines genres, plot overviews, and taglines into a single text feature.
3. **TF-IDF Vectorization:** Converts the combined text into numerical vectors.
4. **Cosine Similarity:** Calculates similarity scores between movie vectors.
5. **Recommendation:** Sorts movies by similarity and returns the top recommendations, excluding the selected movie.

## 💻 Example Usage

```python
recommend_movies("Interstellar")
```

The function returns a table containing the recommended movie titles, genres, and similarity scores.

## 📊 Recommendation Method

This project uses **content-based filtering**. Recommendations are generated from movie metadata rather than user ratings or viewing history.

A higher cosine similarity score indicates greater similarity between the textual features of two movies. It does not necessarily indicate user preference.

## 👨‍💻 Author

**Manas**

If you find this project useful, consider giving the repository a ⭐ on GitHub.