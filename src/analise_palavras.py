import pandas as pd
import streamlit as st

def analise_caracteres(df_caracteres=None):
    st.session_state.df_caracteres = df_caracteres
    # replace de caracteres especiais para os normais
    try:
        df_caracteres['caracter'] = df_caracteres['caracter'].str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('latin-1')
        df_caracteres = df_caracteres[df_caracteres['caracter'].str.isalpha()]
    except ValueError:
        df_caracteres = st.session_state.df_caracteres
    df_caracteres = df_caracteres.groupby('caracter', as_index=False).sum()
    df_caracteres = df_caracteres.sort_values(by='frequencia', ascending=False).reset_index(drop=True)
    st.session_state.df_caracteres_ascii = df_caracteres

    col1, col2 = st.columns(2)
    col1.metric('Quantidade de caracteres com especiais:', len(st.session_state.df_caracteres))
    col2.metric('Quantidade de caracteres sem especiais:', len(st.session_state.df_caracteres_ascii))

    # -- Controle SIM/NÃO --
    caracteres_especiais = st.segmented_control('Utilizar caracteres especiais?',
                                                ['SIM','NÃO'],
                                                default='SIM', 
                                                key='controle_caracteres_especiais')
    if caracteres_especiais == 'SIM':
        df_caracteres = st.session_state.df_caracteres
    else:
        df_caracteres = st.session_state.df_caracteres_ascii

    return df_caracteres

def analise_palavras(df_palavras=None):
    if df_palavras is None:
        df_palavras = pd.read_csv('data/palavras_portugues.csv', encoding='latin-1')
    df_palavras['tamanho'] = df_palavras['palavra'].str.len()
    df_palavras.to_csv('data/palavras_portugues.csv', index=False, encoding='latin-1')

    df_palavras_por_tamanho = df_palavras.groupby('tamanho', as_index=False).count()
    df_palavras_por_tamanho = df_palavras_por_tamanho.rename(columns={'palavra': 'quantidade'})
    df_palavras_por_tamanho.to_csv('data/palavras_por_tamanho.csv', index=False, encoding='latin-1')
    st.session_state.df_palavras_por_tamanho = df_palavras_por_tamanho


if __name__ == "__main__":
    analise_caracteres()
    analise_palavras()
