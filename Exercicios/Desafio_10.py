"""
Crie um programa que leia quanto de dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar
"""

real: float = float(input("Informe quanto tem de monetário: R$"))

print(f"Você pode comprar US${real / 3.27:.2f}")