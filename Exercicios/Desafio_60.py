"""
Escreva um programa que peça um numero inteiro e mostre o seu fatorial na tela
"""

numero = int(input("Numero: "))
fatorial = 1

for i in range(1, numero + 1):
    fatorial*=i

print(f"Fatorial de {numero} é {fatorial}")