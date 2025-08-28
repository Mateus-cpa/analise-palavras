import pandas as pd
import streamlit as st

def analise_caracteres(df_caracteres=None):
    
    caracteres_especiais = st.segmented_control('Utilizar caracteres especiais?',
                                                ['SIM','NÃO'], 
                                                key='caracteres_especiais')
    if caracteres_especiais == 'NÃO':
        # replace de caracteres especiais para os normais
        df_caracteres['caracter'] = st.session_state.df_caracteres['caracter'].str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')
        df_caracteres = df_caracteres[df_caracteres['caracter'].str.isalpha()]
    df_caracteres = df_caracteres.groupby('caracter', as_index=False).sum()
    
    df_caracteres = df_caracteres.sort_values(by='frequencia', ascending=False).reset_index(drop=True)

    return df_caracteres

def analise_palavras(df=None):
    # pontuação de palavras pela frequência das letras
    df['pontuacao'] = df['frequencia'] / df['frequencia'].sum()
    

    return df

if __name__ == "__main__":
    analise_caracteres()
    analise_palavras()
