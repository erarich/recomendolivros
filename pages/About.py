import streamlit as st


def main():
    st.set_page_config(page_title='About', page_icon='📖')
    st.title('About')
    st.markdown('This project was developed for a school project in September 2020 to emphasize'
                ' the impact of Recommender Systems on users\' daily activities.')

    st.markdown('It was created during my third year of high school for the "Mostra SESI",'
                ' a pedagogic event aimed at strengthening basic education with quality.'
                ' The theme for that year (2020) was Artificial Intelligence, and the context'
                ' was the Covid-19 pandemic. Consequently, my team chose a theme that combines'
                ' AI with that context, characterized by the prevalence of digital content and'
                ' social media. Hence, the sub-theme Recommenders Systems was chosen.')

    st.markdown('The original dataset consists of a list of 138 books, all carefully selected by the team,'
                ' and each book includes a description column created by us.')


if __name__ == '__main__':
    main()
