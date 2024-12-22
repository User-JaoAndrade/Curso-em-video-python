"""
Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com "SANTO"
"""

cidade: str = input("Informe o nome de uma cidade: ")

print(cidade[:5].upper() == "SANTO")