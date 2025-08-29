def filtra_dados(df=None):
    if df is None:
        return None

    # Filtros de palavras
    palavras_filtradas = df['palavra'].str.contains('a', case=False)
    df = df[palavras_filtradas]

    return df

if __name__ == "__main__":
    filtra_dados()
