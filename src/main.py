import streamlit as st

from request_palavras import importar_palavras, processar_palavras
from analise_palavras_python import analise_palavras

def tela_streamlit():
    st.title('Análise de palavras em português brasileiro')
    with st.expander('Atualizar base de dados'):
        importar_palavras()
        df = processar_palavras()
    st.subheader('Análise das letras')
    df = analise_palavras(df)
    st.dataframe(df)
    st.bar_chart(df, x='caracter', y='frequencia')


if __name__ == "__main__":
    tela_streamlit()
"""
selecionar se considera caracteres especiais
criar botões de letras
indicadores de:
- letra mais abundante
- palavra com letras mais comuns
- palavra com letras mais raras
gráfico de barras com frequência das letras

"""