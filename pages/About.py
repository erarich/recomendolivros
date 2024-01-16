import streamlit as st

st.text(
    "Esta é uma plataforma de recomendação de livros que está em fase inicial. Para poder usá-la, ")
st.text("utilize a barra lateral,vá em Inscrever-se e depois em Login para acessar a plataforma com a nova conta.")
st.subheader("Como usar o sistema:")
st.text(
    "Em Lista de Livros, é possível ter acesso a todos os livros disponíveis no banco de dados.")
st.text(
    "Pesquise o título do livro no qual deseja usar na plataforma e encontre sua id.")
st.text("Em Pedir Recomendação, digite a id do livro que escolheu, o sistema recomendará um livro semelhante!")

st.subheader('Informações sobre o projeto!')
st.text('Esse projeto está sendo realizado para a MOSTRA SESI 2020. '
        'Desenvolvido em setembro de 2020.')
