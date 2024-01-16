import streamlit as st
import pandas as pd
from src.functions import load_data
from src.recommender import *


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
