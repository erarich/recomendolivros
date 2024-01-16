import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
from PIL import Image

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
    """Simple Login App"""

    st.title("Recomendador de Livros")

    menu = ["Página Inicial", "Login", "Inscrever-se", 'Sobre']
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Página Inicial":
        st.subheader("Página Inicial")
        image = Image.open('img.jpg')
        st.image(image, caption='Créditos: pixabay.com/pt/users/geralt-9301/',
                 use_column_width=True)
        st.text(
            "Esta é uma plataforma de recomendação de livros que está em fase inicial. Para poder usá-la, ")
        st.text("utilize a barra lateral,vá em Inscrever-se e depois em Login para acessar a plataforma com a nova conta.")
        st.subheader("Como usar o sistema:")
        st.text(
            "Em Lista de Livros, é possível ter acesso a todos os livros disponíveis no banco de dados.")
        st.text(
            "Pesquise o título do livro no qual deseja usar na plataforma e encontre sua id.")
        st.text("Em Pedir Recomendação, digite a id do livro que escolheu, o sistema recomendará um livro semelhante!")

    elif choice == "Login":
        st.subheader("")

        username = st.sidebar.text_input("Usuário")
        password = st.sidebar.text_input("Senha", type='password')
        if st.sidebar.checkbox("Login"):
            # if password == '12345':
            if result:

                st.success("Logado como {}".format(username))

                task = st.selectbox(
                    "Ferramentas", ["Lista de Livros", "Recomendação", "Perfis"])
                if task == "Lista de Livros":
                    st.subheader(
                        "Use esta lista de livros para saber a ID dos livros")

                    resultado = st.selectbox(
                        'Digite o nome do livro:', dados[['Título']])
                    st.write(resultado)
                    colunas = dados[['id', 'Título']]
                    st.table(colunas)

                elif task == "Recomendação":
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

    elif choice == 'Sobre':
        st.subheader('Informações sobre o projeto!')
        st.text('Esse projeto está sendo realizado para a MOSTRA SESI 2020. '
                'Desenvolvido em setembro de 2020.')


if __name__ == '__main__':
    main()
