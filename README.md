
# Projeto: Análise de Palavras em Português

Este projeto realiza a análise de palavras em português, contando a frequência de letras e exibindo os resultados em uma interface web utilizando Streamlit.

## Funcionalidades

1. **Importação de arquivo de palavras da internet**
	- O projeto faz o download automático de um arquivo `.txt` contendo uma lista de palavras em português diretamente da internet.
	- O script responsável por essa etapa é o `src/request_palavras.py`.

2. **Tratamento do arquivo e contagem de letras**
	- Após o download, o arquivo é processado para contar a frequência de cada letra presente nas palavras.
	- O processamento e análise são realizados pelo script `src/analise_palavras_python.py`.
	- O resultado é salvo em um arquivo CSV na pasta `data/`.

3. **Visualização dos resultados com Streamlit**
	- Os resultados da análise são exibidos em uma interface interativa utilizando Streamlit.
	- Basta executar o comando abaixo para iniciar a aplicação web.

## Estrutura do Projeto

```
├── README.md
├── data/
│   ├── frequencia_caracteres.csv
│   └── palavras_portugues.txt
├── src/
│   ├── analise_palavras_python.py
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



## Licença
Este projeto é distribuído sob a licença MIT.

