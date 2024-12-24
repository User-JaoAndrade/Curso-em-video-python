"""
Crie um programa que tenha a função chamada leiaInt(), 
que vai funcionar de forma semelhante à função input() do Python, 
só que fazendo a validação para aceitar apenas um valor numérico inteiro
"""
def leiaInt(m):
    numero: str = input(f"{m}")
    if not numero.isnumeric():
        print("INFORME UM NÚMERO INTEIRO")
        exit()
    return numero

n = leiaInt("Digite um número inteiro: ")
print(f"Você digitou o número {n}")
