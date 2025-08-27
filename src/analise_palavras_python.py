import time
import csv

tempo_inicial = time.time()

with open ('data/palavras_portugues.txt', mode='r',encoding='latin-1') as arquivo:
    conteudo_palavras = arquivo.read()
lista_palavras: list = conteudo_palavras.splitlines()
total_palavras = len(lista_palavras)


frequencia_caracteres: dict = {}

contador = 0

for palavra in lista_palavras:
    for caracter in palavra.lower():
        frequencia_caracteres[caracter] = frequencia_caracteres.get(caracter, 0) + 1
    contador += 1
    if contador % 10000 == 0:
        print(f'{contador} palavras lidas')

tempo_final = time.time()
print(f'tempo inicial: {tempo_inicial}\n tempo final: {tempo_final}\n tempo corrido: {tempo_final-tempo_inicial:.2f}')


with open('data/frequencia_caracteres.csv', 'w', newline='',encoding='latin-1') as arquivo_csv:
    for k, v in frequencia_caracteres.items():
        arquivo_csv.write(f'{k},{v}\n')
