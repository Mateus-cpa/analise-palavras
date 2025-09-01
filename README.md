
# Projeto: Análise de Palavras (Português e Inglês)

Este projeto realiza a análise de palavras em português e inglês, permitindo importar listas de palavras, processar frequências de caracteres, aplicar filtros e visualizar os resultados em uma interface web interativa com Streamlit.

O painel se contra disponível no [link](https://tratamento-palavras.streamlit.app/).

## Funcionalidades Desenvolvidas

- **Importação de listas de palavras da internet**
	- Baixa automaticamente arquivos de palavras em português (USP) e inglês (GitHub).
	- Script principal: `src/request_palavras.py`.

- **Processamento e análise de dados**
	- Conta a frequência de cada caractere nas palavras importadas.
	- Gera arquivos CSV com os resultados.
	- Scripts: `src/analise_palavras.py`, `src/request_palavras.py`.

- **Filtros e controles interativos**
	- Permite escolher idioma (PTBR/ENUS) e incluir/excluir caracteres especiais.
	- Filtra dados conforme seleção do usuário.
	- Script: `src/filtra_dados.py`.

- **Visualização dos resultados**
	- Exibe gráficos de frequência de caracteres e distribuição de palavras por tamanho.
	- Mostra métricas como letra mais frequente, menos frequente, etc.
	- Scripts: `src/mostrar_dados.py`, `src/main.py`.

- **Interface Web**
	- Aplicação construída com Streamlit, layout responsivo e controles dinâmicos.
	- Basta executar o projeto para acessar a interface.

## Estrutura do Projeto

```
├── README.md
├── data/
│   ├── frequencia_caracteres_enus.csv
│   ├── frequencia_caracteres_ptbr.csv
│   ├── palavras_ingles.csv
│   ├── palavras_por_tamanho.csv
│   ├── palavras_portugues.csv
├── src/
│   ├── analise_palavras.py
│   ├── filtra_dados.py
│   ├── main.py
│   ├── mostrar_dados.py
│   └── request_palavras.py
```

## Como executar

1. Configure e ative o ambiente virtual:
	``` bash
	pyenv install 3.10.11             # Instale o Python 3.10.11 se ainda não tiver 
    pyenv local 3.10.11               # Defina a versão local do projeto
    python -m venv .venv              # Crie o ambiente virtual
    source .venv/Scripts/activate     # No Windows
    poetry init
    poetry shell
    ```
	
    Instalar dependências e Iniciar aplicativo
    ``` bash
    poetry install
    poetry run streamlit run src/main.py


	```


# Observações
O projeto permite fácil expansão para outros idiomas e tipos de análise.
Todos os dados processados ficam disponíveis na pasta data.
O código está modularizado para facilitar manutenção e evolução.