"""
Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar. 
No final, mostre:

Qual é o total gasto na compra.
Quantos produtos custam mais de R$ 1000.
Qual é o nome do produto mais barato.
"""

mais_barato: float = float('inf')
total_gasto: float = 0.0
produtos_mais_de_1000: int = 0
nome_prod_mais_barato: str = None

while True:
    nome_prod: str = input("Nome do produto: ")
    value_prod: float = float(input("Preço do produto: "))

    total_gasto += value_prod
    
    if value_prod < mais_barato:
        nome_prod_mais_barato = nome_prod

    if value_prod > 1000:
        produtos_mais_de_1000 += 1

    nome_prod = input("\nDeseja continuar? [S]im ou [N]ão\n-> ")

    if nome_prod.upper() == 'S':
        continue
    else: 
        break

print(f"\nTotal Gasto R${total_gasto:.2f}\n"
      f"{produtos_mais_de_1000} produtos custaram mais de R$1000,00\n"
      f"Produto mais barato é o/a {nome_prod_mais_barato}")