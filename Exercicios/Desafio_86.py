"""
Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado. 
No final, mostre a matriz na tela, com a formatação correta
"""

lista: list = [[None for _ in range(3)] for _ in range(3)]

for indice, value in enumerate(lista):
    for i in range(len(value)):
        value[i] = input(f"[{indice}][{i}]: ")

for i in range(len(lista)):
    print(*lista[i])