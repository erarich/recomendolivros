import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
from src.functions import load_data


def compute_similarity_matrix(data):
    tf = TfidfVectorizer(analyzer='word', ngram_range=(
        1, 3), min_df=0.0)
    tf.stopwords = 'portuguese'
    tfidf_matrix = tf.fit_transform(data['description'])
    cosine_similarities = linear_kernel(tfidf_matrix, tfidf_matrix)
    return cosine_similarities


def get_item_description(book_id, data):
    return data.loc[data['id'] == book_id]['description'].tolist()[0].split(' - ')[0]


def recommend_books(item_id, data, similarity_matrix, num=1):
    results = {}

    for idx, row in data.iterrows():
        similar_indices = similarity_matrix[idx].argsort()[:-100:-1]
        similar_items = [(similarity_matrix[idx][i], data['id'][i])
                         for i in similar_indices]
        results[row['id']] = similar_items[1:]

    st.text(
        f"Recomendando {num} livro(s) similar a {get_item_description(item_id, data)}...")
    st.text("-------")
    st.text("-------")
    st.text("-------")

    recs = results[item_id][:num]
    for rec in recs:
        st.text(f"Recomendo: {get_item_description(rec[1], data)}")


def main():
    st.set_page_config(page_title='Books Recommender', page_icon='📖')
    st.title("Books Recommender")

    data = load_data('mda.csv')

    similarity_matrix = compute_similarity_matrix(data)

    item_id = int(st.number_input(
        'Digite a ID do livro:', min_value=0, step=1, value=1))

    recommend_books(item_id, data, similarity_matrix, num=1)


if __name__ == '__main__':
    main()
