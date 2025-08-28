import time
import pandas as pd

import streamlit as st

def analise_caracteres(df=None):
    
    caracteres_especiais = st.segmented_control('Utilizar caracteres especiais?',
                                                ['SIM','NÃO'], 
                                                key='caracteres_especiais')
    if caracteres_especiais == 'NÃO':
        # replace de caracteres especiais para os normais
        df['caracter'] = df['caracter'].str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')
        df = df[df['caracter'].str.isalpha()]
        df = df.groupby('caracter', as_index=False).sum()
    col1, col2 = st.columns(2)
    with col1:
        st.metric('Quantidade de letras',df.shape[0])
    
    df = df.sort_values(by='frequencia', ascending=False).reset_index(drop=True)

def analise_palavras(df=None):
    # pontuação de palavras pela frequência das letras
    df['pontuacao'] = df['frequencia'] / df['frequencia'].sum()

    return df

if __name__ == "__main__":
    analise_caracteres()
    analise_palavras()
