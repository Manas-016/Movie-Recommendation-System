from operator import index

import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

movies_df = pd.read_csv('Dataset/tmdb_5000_movies.csv')
# print(movies_df.head())
# print(movies_df.shape)
required_cols = ['original_title', 'genres', 'overview' , 'tagline']

# print(movies_df[required_cols].isna().sum())

movies_df['overview'] = movies_df['overview'].fillna('')
movies_df['tagline'] = movies_df['tagline'].fillna('')

movies_df['combined_features'] = movies_df['genres'].astype(str) + ' ' + movies_df['overview'] + ' ' + movies_df['tagline']

# print(movies_df[['original_title' , 'combined_features']].head())



tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(movies_df['combined_features'])
# print("TF-IDF Matrix Shape:", tfidf_matrix.shape)


similarity_matrix = cosine_similarity(tfidf_matrix)
# print("Similarity Matrix Shape:", similarity_matrix.shape)


def recommended_movies(movie_name , top_n):
    matches = movies_df.index[movies_df['original_title'].str.casefold() == movie_name.casefold()].tolist()

    if not matches:
        return f"{movie_name} not found in the dataset."


    movie_index = matches[0]

    scores = list(enumerate(similarity_matrix[movie_index]))

    scores = sorted(scores, key=lambda x: x[1], reverse=True)

    scores = [item for item in scores if item[0] != movie_index][: top_n]

    return movies_df.iloc[[index for index, score in scores]][['original_title', 'genres']].assign(
        similarity_score=[score for index, score in scores]).reset_index(names='movie_index')



