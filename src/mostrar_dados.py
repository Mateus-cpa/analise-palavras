import pandas as pd
import streamlit as st

def mostrar_dados_caracteres(df_caracteres: pd.DataFrame = None, df_palavras: pd.DataFrame = None):
    df_caracteres = st.session_state.df_caracteres
    df_palavras = st.session_state.df_palavras
    col1, col2 = st.columns(2)
    with col1:
        st.metric('Qtde com especiais:', len(df_caracteres))
        st.metric('Caracter com maior frequência',df_caracteres['caracter'].where(df_caracteres['frequencia'] == df_caracteres['frequencia'].max()).values[0])
    with col2:
        st.metric('Qtde sem especiais:', len(st.session_state.df_frequencia_caracteres_ascii))
        st.metric('Caracter com menor frequência',df_caracteres['caracter'].where(df_caracteres['frequencia'] == df_caracteres['frequencia'].min()).values[0])
    st.bar_chart(df_caracteres, x='caracter', y='frequencia', horizontal=False)

def mostrar_dados_palavras(df_palavras: pd.DataFrame = None):
    col1, col2 = st.columns(2)
    with col1:
        st.metric('Palavra mais comum', df_palavras['palavra'].where(df_palavras['valor_palavra'] == df_palavras['valor_palavra'].max()).values[0])
    with col2:
        st.metric('Palavra menos comum', df_palavras['palavra'].where(df_palavras['valor_palavra'] == df_palavras['valor_palavra'].min()).values[0])
    st.bar_chart(df_palavras, x='tamanho', y='quantidade')

if __name__ == "__main__":
    mostrar_dados_caracteres()

    """
    Tela de visualização dos dados
indicadores de:
- letra mais abundante
- palavra com letras mais comuns
- palavra com letras mais raras
gráfico de barras com frequência das letras

"""