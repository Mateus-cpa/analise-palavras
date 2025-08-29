import streamlit as st
import pandas as pd

from request_palavras import importar_palavras 
from analise_palavras import analise_caracteres, analise_palavras
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

if __name__ == "__main__":
    tela_streamlit()
"""
selecionar se considera caracteres especiais
criar botões de letras
filtros de palavras que começam com a letra
filtros de palavras que terminam com a letra
filtro de palavras que possuam a letra
filtro de palavras que não possuam a letra
filtro de palavras pelo tamanho
indicadores de:
- letra mais abundante
- palavra com letras mais comuns
- palavra com letras mais raras
gráfico de barras com frequência das letras

"""