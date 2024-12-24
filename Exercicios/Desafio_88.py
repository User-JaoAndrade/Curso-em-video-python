"""
Faça um programa que ajude um jogador da MEGASENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60
para cada jogo. Cadastrando tudo em uma lista composta.
"""

import time
import random

numeros_sorteados: list = []
todos_os_jogos: list = []

qtd_sorteios: int = int(input("Quantidade de sorteios: "))

# Eu preferia ter mostrado os sorteios pro usuario já nesse loop, mas o enunciado pede pra guardar em
# uma lista composta
for i in range(qtd_sorteios):
    while len(numeros_sorteados) < 6:
        numero: int = random.randint(1,60)
        if numero not in numeros_sorteados:

            numeros_sorteados.append(numero)
    numeros_sorteados.sort()
    todos_os_jogos.append(numeros_sorteados.copy())
    numeros_sorteados.clear()

for indice, sorteio in enumerate(todos_os_jogos):
    time.sleep(1)
    print(f"Sorteio {indice+1}:", *sorteio)
