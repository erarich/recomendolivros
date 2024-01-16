import streamlit as st
import pandas as pd


def main():
    st.title('Dataset')
    df = pd.read_csv('mda.csv')
    resumed_df = df[['id', 'Título']]

    selectbox_options = ['Resumed', 'Complete']

    dataframe_options = st.selectbox(
        'Select the option', selectbox_options)

    if (dataframe_options == 'Resumed'):
        st.dataframe(resumed_df)
    else:
        st.dataframe(df)


if __name__ == '__main__':
    main()
