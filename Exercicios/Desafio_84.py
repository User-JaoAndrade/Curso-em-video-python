"""
Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:

Quantas pessoas foram cadastradas.
Uma listagem com as pessoas mais pesadas.
Uma listagem com as pessoas mais leves.
"""

lista_de_pessoas: list = []
lista_nomes_mais_pesadas: list = []
lista_nomes_mais_leves: list = []

opcao: str = ''

while opcao != 's':
    nome: str = input("Nome: ")
    peso: float = float(input("Peso: "))
    lista_de_pessoas.append([nome, peso])
    opcao = input("\nDeseja parar? [S]im\n-> ")

maior_peso: float = max(pessoa[1] for pessoa in lista_de_pessoas)
menor_peso: float = min(pessoa[1] for pessoa in lista_de_pessoas)

for i in lista_de_pessoas:
    if maior_peso == i[1]:
        lista_nomes_mais_pesadas.append(i[0])
    elif menor_peso == i[1]:
        lista_nomes_mais_leves.append(i[0])

print(f"Foram cadastradas {len(lista_de_pessoas)} pessoas")
print(f"Mais pesados: {maior_peso}kg", *lista_nomes_mais_pesadas)
print(f"Mais leves: {menor_peso}kg", *lista_nomes_mais_leves)