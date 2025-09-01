import streamlit as st
import pandas as pd

from request_palavras import importar
from analise_palavras import analise_caracteres, analise_palavras
from filtra_dados import filtra_dados, controles
from mostrar_dados import mostrar_dados_caracteres, mostrar_dados_palavras, mostrar_cache


def tela_streamlit():
    #Configura largura total da tela
    st.set_page_config(layout="wide")

    st.title('Estudos sobre Palavras em português/inglês')
    # -- IMPORTAÇÃO --
    importar()

    # -- FILTROS idioma e tipo caracteres --  
    controles()

    # -- tratamento --
    df_caracteres = analise_caracteres()
    analise_palavras(df_palavras= st.session_state.df_palavras)

    # -- MOSTRAR DADOS CARACTERES --
    st.header('Sobre os caracteres')
    mostrar_dados_caracteres()

    st.header('Sobre as palavras')
    # -- FILTRO DADOS PALAVRAS --
    if 'df_palavras' not in st.session_state:
        st.session_state.df_palavras = pd.read_csv('data/palavras_portugues.csv', encoding='latin-1')
    df_palavras = filtra_dados(st.session_state.df_palavras)

    # -- MOSTRAR DADOS PALAVRAS --
    st.subheader('Distribuição de palavras por tamanho')
    analise_palavras(df_palavras=df_palavras)
    mostrar_dados_palavras(df_palavras=df_palavras)

    # mostrar quais st.session_state estão em cache
    st.subheader("Dados em cache:")
    mostrar_cache()

if __name__ == "__main__":
    tela_streamlit()
