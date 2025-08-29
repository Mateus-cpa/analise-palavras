import streamlit as st

def filtra_dados(df=None):
    if df is None:
        return None
    df = df.dropna().copy()
    # Filtros de palavras
    caracteres = st.session_state.df_caracteres['caracter'].unique().tolist()
    col1, col2, col3 = st.columns(3)
    
    # Primeira letra
    col1.write('Palavras que começam com:')
    primeira_letra = col1.segmented_control('', options=caracteres, key='primeira_letra')
    if primeira_letra:
        df = df[df['palavra'].str.startswith(primeira_letra)]

    # Última letra
    col2.write('Palavras que terminam com:')
    ultima_letra = col2.segmented_control('', options=caracteres, key='ultima_letra')    
    if ultima_letra:
        df = df[df['palavra'].str.endswith(ultima_letra)]
    
    # Tamanho da palavra
    col3.write('Tamanho da palavra:')
    tamanho_palavra_lista = st.session_state.df_palavras_por_tamanho['tamanho'].unique().astype(int).tolist()
    tamanho_palavra = col3.segmented_control('',tamanho_palavra_lista, key='tamanho_palavra')
    if tamanho_palavra:
        df = df[df['palavra'].str.len() == int(tamanho_palavra)]

    # mostrar resultados
    st.metric('Quantidade de palavras', len(df))
    st.code(df)

    return df

if __name__ == "__main__":
    filtra_dados()

"""selecionar se considera caracteres especiais
criar botões de letras
filtro de palavras que possuam a letra
filtro de palavras que não possuam a letra
filtro de palavras pelo tamanho
palavras com letra x na posição y"""