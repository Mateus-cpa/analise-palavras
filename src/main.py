import streamlit as st

from request_palavras import importar_palavras, processar_palavras
from analise_palavras import analise_caracteres, analise_palavras

def tela_streamlit():
    st.title('Análise de palavras em português brasileiro')
    with st.expander('Atualizar base de dados'):
        lista_palavras = importar_palavras()
        df_caracteres = processar_palavras(lista_palavras=lista_palavras)
    st.subheader('Análise das letras')
    df = analise_caracteres(df_caracteres)
    st.dataframe(df)
    st.bar_chart(df, x='caracter', y='frequencia', horizontal=False)


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