"""
Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto
"""

product_price: float = float(input("Preço do produto: R$"))
print(f"Você ganhou 5% de desconto, seu produto agora vale R${product_price - (product_price*5 / 100)}")