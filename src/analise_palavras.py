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

def analise_palavras(df=None):
    # pontuação de palavras pela frequência das letras
    df['pontuacao'] = df['frequencia'] / df['frequencia'].sum()
    

    return df

if __name__ == "__main__":
    analise_caracteres()
    analise_palavras()
