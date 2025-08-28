import requests as re
import time
import pandas as pd

import streamlit as st

def importar_palavras():
    """
    Importa a lista de palavras do site da USP.

    """
    importar = st.button('Atualizar base de dados')
    if importar:
        try:
            resposta = re.get('https://www.ime.usp.br/~pf/dicios/br-utf8.txt')
        except Exception as e:
            st.error(f'Erro ao acessar o site: {e}')
            return []

        conteudo_site = resposta.text.encode(encoding='utf-8').decode(encoding='utf-8')

        st.write(f'tipo conteúdo site: {type(conteudo_site)}')
        lista_palavras = conteudo_site.split('\n')
        st.success(f"primeiras palavras: {lista_palavras[:5]}")
        st.success(f'quantidade de palavras: {len(lista_palavras)}')
        st.success('Base de dados atualizada com sucesso!')

        st.session_state.lista_palavras = lista_palavras

def contar_caracteres(lista_palavras: list = None):
    """
    Processa a lista de palavras e retorna um DataFrame com a frequência de caracteres.
    Args:
        lista_palavras (list): Lista de palavras a serem processadas.
    """
    st.success('Iniciando processamento das palavras...')
    tempo_inicial = time.time()

    #salvar em csv
    df_palavras: pd.DataFrame = pd.DataFrame(lista_palavras, columns=['palavra'])
    df_palavras.to_csv('data/palavras_portugues.csv', index=False, encoding='latin-1')

    frequencia_caracteres: dict = {}

    for palavra in lista_palavras:
        for caracter in palavra.lower():
            frequencia_caracteres[caracter] = frequencia_caracteres.get(caracter, 0) + 1

    st.code(frequencia_caracteres)    
    tempo_final = time.time()
    st.success(f'tempo corrido: {tempo_final-tempo_inicial:.2f} segundos')


    df = pd.DataFrame(list(frequencia_caracteres.items()), columns=['caracter', 'frequencia'])
    df.to_csv('data/frequencia_caracteres.csv', index=False, encoding='latin-1')

    return df

if __name__ == "__main__":
    importar_palavras()
    contar_caracteres()