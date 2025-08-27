import requests as re
import time
import pandas as pd

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

def processar_palavras():
    st.success('Iniciando processamento das palavras...')
    tempo_inicial = time.time()

    with open ('data/palavras_portugues.txt', mode='r',encoding='latin-1') as arquivo:
        conteudo_palavras = arquivo.read()
    lista_palavras: list = conteudo_palavras.splitlines()


    frequencia_caracteres: dict = {}

    for palavra in lista_palavras:
        for caracter in palavra.lower():
            frequencia_caracteres[caracter] = frequencia_caracteres.get(caracter, 0) + 1
        
    tempo_final = time.time()
    st.success(f'tempo inicial: {tempo_inicial}\n tempo final: {tempo_final}\n tempo corrido: {tempo_final-tempo_inicial:.2f}')


    df = pd.DataFrame(list(frequencia_caracteres.items()), columns=['caracter', 'frequencia'])
    df.to_csv('data/frequencia_caracteres.csv', index=False, encoding='latin-1')

    return df

if __name__ == "__main__":
    importar_palavras()