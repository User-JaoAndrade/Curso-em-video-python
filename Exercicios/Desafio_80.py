"""Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista 
já na posição correta de inserção (sem usar o sort()). 
No final, mostre a lista ordenada na tela
"""

lista: list = []

for i in range(5):
    numero: int = int(input(f"Numero {i+1}: "))
    if not lista:
        lista.append(numero)
    else:
        pos: int = 0
        while pos < len(lista):
            if numero <= lista[pos]:
                lista.insert(pos, numero)
                break
            pos += 1
        else: 
            lista.insert(pos, numero)

print(*lista)