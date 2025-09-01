import pandas as pd
import streamlit as st

def mostrar_dados_caracteres():
    df_caracteres = st.session_state.df_caracteres
    df_palavras = st.session_state.df_palavras
    col1, col2 = st.columns(2)
    with col1:
        st.metric('Qtde com especiais:', len(df_caracteres))
        st.metric('Caracter com maior frequência',df_caracteres['caracter'].loc[df_caracteres['frequencia'].idxmax()])
    with col2:
        st.metric('Qtde sem especiais:', len(st.session_state.df_frequencia_caracteres_ascii))
        st.metric('Caracter com menor frequência',df_caracteres['caracter'].loc[df_caracteres['frequencia'].idxmin()])
    st.bar_chart(df_caracteres, x='caracter', y='frequencia', horizontal=False)

def mostrar_dados_palavras(df_palavras: pd.DataFrame = None):
    try:
        st.bar_chart(st.session_state.df_palavras_por_tamanho, x='tamanho', y='quantidade', horizontal=False)
    except ValueError:
        st.warning("Não há dados para mostrar. Por favor, ajuste os filtros ou importe uma base de dados válida.")  
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