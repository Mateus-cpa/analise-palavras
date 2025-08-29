import streamlit as st

def filtra_dados(df=None):
    if df is None:
        return None
    df = df.dropna().copy()
    # Filtros de palavras
    caracteres = st.session_state.df_caracteres['caracter'].unique().tolist()
    col1, col2 = st.columns([2,8])
    
    # Primeira letra
    col1.write('Palavras que começam com:')
    primeira_letra = col2.segmented_control('', options=caracteres, key='primeira_letra')
    if primeira_letra:
        df = df[df['palavra'].str.startswith(primeira_letra)]

    # Última letra
    col1.write('Palavras que terminam com:')
    ultima_letra = col2.segmented_control('', options=caracteres, key='ultima_letra')    
    if ultima_letra:
        df = df[df['palavra'].str.endswith(ultima_letra)]
    
    st.metric('Quantidade de palavras', len(df))
    st.code(df)
    
    return df

if __name__ == "__main__":
    filtra_dados()

"""selecionar se considera caracteres especiais
criar botões de letras
filtros de palavras que começam com a letra
filtros de palavras que terminam com a letra
filtro de palavras que possuam a letra
filtro de palavras que não possuam a letra
filtro de palavras pelo tamanho
palavras com letra x na posição y"""