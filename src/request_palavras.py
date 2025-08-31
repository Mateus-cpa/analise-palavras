import requests as re
import time
import pandas as pd

import streamlit as st

def calcular_valor_palavra(palavra):
    df_caracteres = st.session_state.df_caracteres_ascii
    valor = 0
    for letra in palavra:
        freq = df_caracteres.loc[df_caracteres['caracter'] == letra, 'frequencia']
        if not freq.empty:
            valor += freq.values[0]
    return valor

def importar_palavras(url):
    """
    Importa a lista de palavras do site da USP ou do githbu para inglês.
    Depois, processa a lista de palavras e retorna um DataFrame com a frequência de caracteres.
    """
    st.info('Iniciando importação da base de dados...')

    tempo_inicial = time.time()
    try:
        resposta = re.get(url[0])
    except Exception as e:
        st.error(f'Erro ao acessar o site: {e}')
        return []

    conteudo_site = resposta.text

    st.write(f'tipo conteúdo site: {type(conteudo_site)}')
    lista_palavras = conteudo_site.split('\n')
    st.success(f"primeiras palavras: {lista_palavras[:5]}")
    st.success(f'quantidade de palavras: {len(lista_palavras)}')
    st.success('Base de dados atualizada com sucesso!')

    # salvar lista em csv
    df_palavras: pd.DataFrame = pd.DataFrame(lista_palavras, columns=['palavra']).dropna()
    #df_palavras = df_palavras[:100]

    st.success('Iniciando processamento das palavras...')
    
    frequencia_caracteres: dict = {}

    for palavra in lista_palavras:
        for caracter in palavra.lower():
            frequencia_caracteres[caracter] = frequencia_caracteres.get(caracter, 0) + 1

    
    # calcula tamanho das palavras
    st.success('Calculando tamanho das palavras...')

    df_palavras['tamanho'] = df_palavras['palavra'].str.len()
    
    df_frequencia = pd.DataFrame(list(frequencia_caracteres.items()), columns=['caracter', 'frequencia'])
    df_frequencia.to_csv(f'data/frequencia_caracteres_{url[1]}.csv', index=False, encoding='latin-1')

    # calcula valor a palavra com letras considerando a frequência dos caracteres
    st.success('Calculando valor das palavras...')
    #progresso
    progresso = st.progress(0)
    total_palavras = len(df_palavras)
    percentual_text = st.empty()
    for i, palavra in enumerate(df_palavras['palavra']):
        try:
            df_palavras.at[i, 'valor_palavra'] = calcular_valor_palavra(palavra)
        except Exception as e:
            st.error(f'Erro ao calcular valor da palavra {palavra}: {e}')
            df_palavras.at[i, 'valor_palavra'] = 0
        percentual = ((i + 1) / total_palavras) * 100
        progresso.progress((i + 1) / total_palavras)
        percentual_text.text(f'Progresso: {percentual:.2f}%')
    st.write(df_palavras.sample(10))

    # salvar arquivo atualizado por idioma
    if url[1] == 'ptbr':
        df_palavras.to_csv('data/palavras_portugues.csv', index=False, encoding='latin-1')
        st.session_state.df_palavras_ptbr = df_palavras
        st.session_state.df_frequencia_ptbr = df_frequencia
    else:
        df_palavras.to_csv('data/palavras_ingles.csv', index=False, encoding='latin-1')
        st.session_state.df_palavras_enus = df_palavras
        st.session_state.df_frequencia_enus = df_frequencia

    st.success('Arquivo atualizado com sucesso!')

    tempo_final = time.time()
    tempo_decorrido = tempo_final-tempo_inicial
    if tempo_decorrido <= 60:
       st.success(f'tempo corrido: {tempo_decorrido:.2f} segundos.')
    else:
        st.success(f'tempo corrido: {tempo_decorrido/60:.2f} minutos.')

    

if __name__ == "__main__":
    importar_palavras(url='https://www.ime.usp.br/~pf/dicios/br-utf8.txt')
