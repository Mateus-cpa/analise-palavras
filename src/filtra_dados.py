import streamlit as st
import pandas as pd

def controles():
    col1, col2 = st.columns(2)
    #-- Controle Idioma --
    idioma = col1.segmented_control('Idioma:',
                                    ['PTBR','ENUS'],
                                    default='ENUS', 
                                    key='controle_idioma')
    if idioma == 'PTBR':
        st.session_state.df_palavras = pd.read_csv('data/palavras_portugues.csv', encoding='latin-1')
        st.session_state.df_palavras_por_tamanho = st.session_state.df_palavras.groupby('tamanho', as_index=False).count()
        st.session_state.df_caracteres = pd.read_csv('data/frequencia_caracteres_ptbr.csv', encoding='latin-1')
    elif idioma == 'ENUS':
        st.session_state.df_palavras = pd.read_csv('data/palavras_ingles.csv', encoding='latin-1')
        st.session_state.df_palavras_por_tamanho = st.session_state.df_palavras.groupby('tamanho', as_index=False).count()
        st.session_state.df_caracteres = pd.read_csv('data/frequencia_caracteres_enus.csv', encoding='latin-1')

    # -- Controle SIM/NÃO caracteres especiais --
    caracteres_especiais = col2.segmented_control('Utilizar caracteres especiais?',
                                                ['SIM','NÃO'],
                                                default='SIM', 
                                                key='controle_caracteres_especiais')
    if caracteres_especiais == 'SIM':
        df_caracteres = st.session_state.df_caracteres
    else:
        # substitui caracteres especiais pelo ascii de df_caracteres e agrupar os iguais
        df_caracteres = st.session_state.df_caracteres.copy()
        df_caracteres['caracter'] = df_caracteres['caracter'].str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('latin-1')
        df_caracteres = df_caracteres[df_caracteres['caracter'].str.isalpha()]
        df_caracteres = df_caracteres.groupby('caracter', as_index=False).sum()
        df_caracteres = df_caracteres.sort_values(by='frequencia', ascending=False).reset_index(drop=True)

    st.session_state.df_caracteres = df_caracteres

def filtra_dados(df=None):
    if df is None:
        return None
    df = df.dropna().copy()
    
    # Importa listas para filtros
    caracteres = st.session_state.df_caracteres['caracter'].unique().tolist()
    caracteres.sort()

    # -- LIMPAR FILTROS --
    limpar_filtros = st.button('Limpar Filtros')
    if limpar_filtros:
        for key in ['primeira_letra', 'ultima_letra', 'tamanho_palavra', 'letra_nao', 'letra']:
            if key in st.session_state:
                del st.session_state[key]
                
    col1, col2, col3 = st.columns(3)
    
    # Primeira letra
    caracter_inicial = df['palavra'].str[0].unique().tolist()
    col1.write('Palavras que começam com:')
    primeira_letra = col1.segmented_control('', options=caracter_inicial, key='primeira_letra', selection_mode='multi')
    if primeira_letra:
        df = df[df['palavra'].str.startswith(tuple(primeira_letra))]

    # como filtra os segmented_control ultima_letra apenas com caracteres que tenham no final de palavras
    caracteres_final_palavra = df['palavra'].str[-1].unique().tolist()
    caracteres_final_palavra.sort()

    # Última letra
    col2.write('Palavras que terminam com:')
    ultima_letra = col2.segmented_control('', options=caracteres_final_palavra, key='ultima_letra', selection_mode='multi')
    if ultima_letra:
        df = df[df['palavra'].str.endswith(tuple(ultima_letra))]
    
    # Tamanho da palavra
    tamanho_palavra_lista = df['palavra'].str.len().unique().astype(int).tolist()
    tamanho_palavra_lista.sort()
    col3.write('Tamanho da palavra:')
    tamanho_palavra = col3.segmented_control('',tamanho_palavra_lista, key='tamanho_palavra', selection_mode='multi')
    if tamanho_palavra:
        df = df[df['palavra'].str.len().isin(tamanho_palavra)]

    col4, col5, col6 = st.columns(3)    
    
    # listar caracteres existentes nas palavras de df
    caracteres_para_retirar = df[df['palavra'].str.len() > 1]['palavra'].apply(lambda x: list(set(x))).explode().unique().tolist()

    # palavras que não tenham a letra
    col4.write('Palavras que não tenham a letra:')
    letra_nao = col4.segmented_control('', caracteres_para_retirar, key='letra_nao', selection_mode='multi')
    if letra_nao:
        for l in letra_nao:
            df = df[~df['palavra'].str.contains(l, case=False)]
    
    #listar caracteres existentes para o fitro
    caracteres_obrigatorios = df[df['palavra'].str.len() > 1]['palavra'].apply(lambda x: list(set(x))).explode().unique().tolist()

    # palavras que tenham a letra
    col5.write('Palavras que tenham a letra:')
    letra = col5.segmented_control('',caracteres_obrigatorios, key='letra', selection_mode='multi')
    if letra:
        for l in letra:
            df = df[df['palavra'].str.contains(l, case=False)]
        col6.write('Na posição:')
        letra_posicao = col6.segmented_control('',tamanho_palavra_lista)
        # filtrar dataframe pela posição (adapte se necessário para múltiplas letras)

    # -- RESULTADOS --
    st.markdown(f'#### {df.shape[0]} resultados')
    
    col1, col2 = st.columns(2)
    try:
        with col1:
            palavra_mais_comum = df.loc[df['valor_palavra'].idxmax(), 'palavra']
            st.metric('Palavra mais comum', palavra_mais_comum)
        with col2:
            palavra_menos_comum = df.loc[df['valor_palavra'].idxmin(), 'palavra']
            st.metric('Palavra menos comum', palavra_menos_comum)
    except ValueError:
        st.warning("Não foi possível encontrar palavras com as condições aplicadas.")

    st.dataframe(df)

    return df

if __name__ == "__main__":
    filtra_dados()

"""selecionar se considera caracteres especiais
criar botões de letras
palavras com letra x na posição y
criar caixas de texto na quantidade do tamanho da palavra e cada campo ser um filtro de letra naquela posição
filtrar os caracteres dos filtros ao invés do total"""