import streamlit as st

from request_palavras import importar_palavras, contar_caracteres
from analise_palavras import analise_caracteres, analise_palavras
from mostrar_dados import mostrar_dados


def tela_streamlit():
    st.title('Análise de palavras em português brasileiro')
    with st.expander('Atualizar base de dados'):
        importar_palavras()
        st.session_state.df_caracteres = contar_caracteres(lista_palavras=st.session_state.lista_palavras)
    st.subheader('Análise das letras')
    # -- tratamento --
    df_caracteres = analise_caracteres(st.session_state.df_caracteres)

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