"""
Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. 
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista."
"""

lista_de_numeros: list = []

for i in range(5):
    numero: int = int(input(f"Número {i+1}: "))
    lista_de_numeros.append(numero)

print(f"Na posição {lista_de_numeros.index(max(lista_de_numeros))}: Maior número = {max(lista_de_numeros)}\n"
      f"Na posição {lista_de_numeros.index(min(lista_de_numeros))}: Menor número = {min(lista_de_numeros)}")