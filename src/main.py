import streamlit as st
import pandas as pd

from request_palavras import importar_palavras 
from analise_palavras import analise_caracteres, analise_palavras
from filtra_dados import filtra_dados
from mostrar_dados import mostrar_dados_caracteres, mostrar_dados_palavras


def tela_streamlit():
    st.title('Análise de palavras em português brasileiro')
    # -- IMPORTAÇÃO --
    ptbr = ['https://www.ime.usp.br/~pf/dicios/br-utf8.txt','ptbr']
    enus = ['https://raw.githubusercontent.com/dwyl/english-words/refs/heads/master/words.txt','enus']

    with st.expander('Atualizar base de dados'):
        col_ptbr, col_enus = st.columns(2)
        with col_ptbr:
            importar_ptbr = st.button('Atualizar base de dados PT-BR')
            if importar_ptbr:
                df_caracteres = importar_palavras(url = ptbr)
            else:
                df_caracteres = pd.read_csv('data/frequencia_caracteres_ptbr.csv', encoding='latin-1')
        with col_enus:
            importar_enus = st.button('Atualizar base de dados EN-US')
            if importar_enus:
                df_caracteres = importar_palavras(url = enus)
            else:
                df_caracteres = pd.read_csv('data/frequencia_caracteres_enus.csv', encoding='latin-1')

    # -- tratamento --
    df_caracteres = analise_caracteres(df_caracteres)
    df_palavras = pd.read_csv('data/palavras_portugues.csv', encoding='latin-1')
    analise_palavras(df_palavras=df_palavras)

    # -- MOSTRAR DADOS CARACTERES --
    mostrar_dados_caracteres(df_caracteres)
    
    # -- FILTRO DADOS PALAVRAS --
    if 'df_palavras' not in st.session_state:
        st.session_state.df_palavras = pd.read_csv('data/palavras_portugues.csv', encoding='latin-1')
    filtra_dados(st.session_state.df_palavras)

    # -- MOSTRAR DADOS PALAVRAS --
    st.subheader('Distribuição de palavras por tamanho')
    analise_palavras(df_palavras=st.session_state.df_palavras)
    mostrar_dados_palavras(st.session_state.df_palavras_por_tamanho)

    
    
if __name__ == "__main__":
    tela_streamlit()
