import pandas as pd
import streamlit as st


def analise_caracteres():
    df_caracteres = st.session_state.df_caracteres.copy()
    # replace de caracteres especiais para os normais
    try:
        df_caracteres['caracter'] = df_caracteres['caracter'].str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('latin-1')
        df_caracteres = df_caracteres[df_caracteres['caracter'].str.isalpha()]
    except ValueError:
        df_caracteres = st.session_state.df_caracteres
    df_caracteres = df_caracteres.groupby('caracter', as_index=False).sum()
    df_caracteres = df_caracteres.sort_values(by='frequencia', ascending=False).reset_index(drop=True)
    st.session_state.df_frequencia_caracteres_ascii = df_caracteres

    

    
    return df_caracteres

def analise_palavras(df_palavras=None):
    if df_palavras is None:
        df_palavras = pd.read_csv('data/palavras_portugues.csv', encoding='latin-1')

    df_palavras_por_tamanho = df_palavras.groupby('tamanho', as_index=False).count()
    df_palavras_por_tamanho = df_palavras_por_tamanho.rename(columns={'palavra': 'quantidade'})
    st.session_state.df_palavras_por_tamanho = df_palavras_por_tamanho

    
if __name__ == "__main__":
    analise_caracteres()
    analise_palavras()
