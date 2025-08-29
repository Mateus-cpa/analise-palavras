import pandas as pd
import streamlit as st

def mostrar_dados(df=None):
    col1, col2 = st.columns(2)
    with col1:
        st.metric('Quantidade de caracteres',df.shape[0])
    with col2:
        st.metric('Maior frequência',df['frequencia'].max())

    st.bar_chart(df, x='caracter', y='frequencia', horizontal=False)
    st.dataframe(df)
    return df

if __name__ == "__main__":
    mostrar_dados()

    """
    Tela de visualização dos dados
indicadores de:
- letra mais abundante
- palavra com letras mais comuns
- palavra com letras mais raras
gráfico de barras com frequência das letras

"""