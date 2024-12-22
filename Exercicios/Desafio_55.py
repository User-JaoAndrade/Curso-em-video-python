"""
Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos
"""

peso_min: float = float('inf') # Definindo a variavel pra ter o menor valor possivel
peso_max: float = float('-inf') # Definindo a variavel pra ter o maior valor possivel

for i in range(1, 6):
    peso: float = float(input(f"Peso pessoa {i}: "))
    if peso > peso_max:
        peso_max = peso
    elif peso < peso_min:
        peso_min = peso
    else:
        pass

print(f"O menor peso lido foi {peso_min:.2f}\n"
      f"O maior peso lido foi {peso_max:.2f}")