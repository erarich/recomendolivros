import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
from src.functions import load_data


st.set_page_config(page_title='Recomendador de Livros', page_icon='📖')

ds = pd.read_csv('mda.csv')
tf = TfidfVectorizer(analyzer='word', ngram_range=(1, 3), min_df=0.0)
tf.stopwords = 'portuguese'
tfidf_matrix = tf.fit_transform(ds['description'])
cosine_similarities = linear_kernel(tfidf_matrix, tfidf_matrix)
results = {}
language = "portuguese"


dat = 'mda.csv'
dados = pd.read_csv(dat)


def main():
    st.title("Recomendador de Livros")

    for idx, row in ds.iterrows():
        similar_indices = cosine_similarities[idx].argsort()[
            :-100:-1]
        similar_items = [
            (cosine_similarities[idx][i], ds['id'][i]) for i in similar_indices]

        results[row['id']] = similar_items[1:]

    def item(id):
        return ds.loc[ds['id'] == id]['description'].tolist()[0].split(' - ')[0]

    item_id = int(st.number_input(
        'Enter the text for test:', min_value=0, step=1, value=1))
    st.write(item_id)

    def recommend(num):
        st.text("Recomendando " + str(num) +
                " livro similar a " + item(item_id) + "...")
        st.text("-------")
        st.text("-------")
        st.text("-------")
        recs = results[item_id][:num]
        for rec in recs:
            st.text("Recomendo: " + item(rec[1]))

    recommend(num=1)


if __name__ == '__main__':
    main()
