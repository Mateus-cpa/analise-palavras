import streamlit as st
import pandas as pd

from request_palavras import importar_palavras 
from analise_palavras import analise_caracteres
from filtra_dados import filtra_dados
from mostrar_dados import mostrar_dados


def tela_streamlit():
    st.title('Análise de palavras em português brasileiro')
    # -- Importação e atualização
    with st.expander('Atualizar base de dados'):
        importar = st.button('Atualizar base de dados')
        if importar:
            df_caracteres = importar_palavras()
        else:
            df_caracteres = pd.read_csv('data/frequencia_caracteres.csv', encoding='latin-1')
    
    # -- tratamento --
    df_caracteres = analise_caracteres(df_caracteres)

    # -- mostrar dados caracteres --
    mostrar_dados(df_caracteres)
    
    # -- filtro de dados palavras --
    if 'df_palavras' not in st.session_state:
        st.session_state.df_palavras = pd.read_csv('data/palavras_portugues.csv', encoding='latin-1')

    filtra_dados(st.session_state.df_palavras)

    
if __name__ == "__main__":
    tela_streamlit()
