import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
import streamlit as st



# Function to recommend similar apartments
def recommend_similar_apartments(prop_details_url):
    # Load data for recommender system
    df = pd.read_csv('module/data.csv')
    df['PROP_DETAILS_URL'] = 'https://www.99acres.com/' + df['PROP_DETAILS_URL']

    # Vectorize the descriptions
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(df['DESCRIPTION'])

    # Compute cosine similarity
    cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

    idx = df.index[df['PROP_DETAILS_URL'] == prop_details_url].tolist()[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[0:6]
    apartment_indices = [i[0] for i in sim_scores]
    return df.iloc[apartment_indices]