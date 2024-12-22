"""
Crie um programa que leia o nome completo de uma pessoa e mostre:
- O nome com todas as letras maiusculas e minusculas
- Quantas letras ao todo (sem considerar espaços)
- Quantas letras tem o primeiro nome
"""

nome: str = input("Nome completo: ")

print(f"Nome com todas as letras maiúsculas: {nome.upper()}\n"
      f"Nome com todas as letras minúsculas: {nome.lower()}\n"
      f"Número de letras (ignorando espaços): {len(nome.replace(' ',''))}\n"
      f"Número de letras do primeiro nome: {nome.find(' ')}")