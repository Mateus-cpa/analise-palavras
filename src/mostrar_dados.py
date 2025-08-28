import pandas as pd
import streamlit as st

def mostrar_dados(df=None):
    col1, col2 = st.columns(2)
    with col1:
        st.metric('Quantidade de caracteres',df.shape[0])
    with col2:
        st.metric('Maior frequência',df['frequencia'].max())

    st.bar_chart(df, x='caracter', y='frequencia', horizontal=False)

    return df

if __name__ == "__main__":
    mostrar_dados()