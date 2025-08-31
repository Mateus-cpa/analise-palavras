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

    col1, col2, col3, col4 = st.columns(4)
    col1.metric('Qtde com especiais:', len(st.session_state.df_caracteres))
    col2.metric('Qtde sem especiais:', len(st.session_state.df_caracteres_ascii))

    # -- Controle SIM/NÃO --
    col5, col6 = st.columns(2)
    caracteres_especiais = col5.segmented_control('Utilizar caracteres especiais?',
                                                ['SIM','NÃO'],
                                                default='SIM', 
                                                key='controle_caracteres_especiais')
    if caracteres_especiais == 'SIM':
        df_caracteres = st.session_state.df_caracteres
    else:
        df_caracteres = st.session_state.df_caracteres_ascii

    #-- Controle Idioma --
    idioma = col6.segmented_control('Idioma:',
                                    ['PTBR','ENUS'],
                                    default='PTBR', 
                                    key='controle_idioma')
    if idioma == 'PTBR':
        st.session_state.df_palavras_ptbr = pd.read_csv('data/palavras_portugues.csv', encoding='latin-1')
        st.session_state.palavras_por_tamanho_ptbr = st.session_state.df_palavras_ptbr.groupby('tamanho', as_index=False).count()
    elif idioma == 'ENUS':
        st.session_state.df_palavras_enus = pd.read_csv('data/palavras_ingles.csv', encoding='latin-1')
        st.session_state.palavras_por_tamanho_enus = st.session_state.df_palavras_enus.groupby('tamanho', as_index=False).count()

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
