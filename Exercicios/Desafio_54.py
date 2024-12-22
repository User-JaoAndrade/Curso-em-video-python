"""
Crie um programa que leia o ano de nascimento de sete pessoas.
No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores de idade
"""
from datetime import date

ano_atual = date.today().year
maior_de_idade: int = 0
menor_de_idade: int = 0

for i in range(1, 8):
    ano_nascimento: int = int(input(f"Nascimento pessoa {i}: "))
    if ano_atual - ano_nascimento >= 18:
        maior_de_idade += 1
    else:
        menor_de_idade += 1

print(f"{maior_de_idade} pessoas atingiram a maior idade\n{menor_de_idade} pessoas não são maiores de idade")