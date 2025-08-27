import streamlit as st

from request_palavras import importar_palavras

def tela_streamlit():
    st.title('Análise de palavras em português brasileiro')
    with st.expander('Atualizar base de dados'):
       importar_palavras()
    st.subheader('Análise das letras')



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