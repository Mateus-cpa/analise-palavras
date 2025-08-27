import requests as re

import streamlit as st

def importar_palavras():
    importar = st.button('Atualizar base de dados')
    if importar:
        resposta = re.get('https://www.ime.usp.br/~pf/dicios/br-utf8.txt')

        conteudo_site = resposta.text.encode(encoding='utf-8').decode(encoding='utf-8')

        st.write(f'tipo conteúdo site: {type(conteudo_site)}')
        lista_palavras = conteudo_site.split('\n')[0:5]
        st.success(f"primeiras palavras: {lista_palavras}")
        st.success(f'quantidade de palavras: {len(conteudo_site.split())}')
        with open('data/palavras_portugues.txt', 'w') as palavras:
            palavras.write(conteudo_site)
        st.success('Base de dados atualizada com sucesso!')

if __name__ == "__main__":
    importar_palavras()