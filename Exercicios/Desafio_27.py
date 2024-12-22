"""
Faça um programa que leia seu nome mostrando em seguida o primeiro e o ultimo nome
EX:
João Victor Andrade Lima
Primeiro nome: João
Ultimo nome: Lima
"""

nome: str = input("Informe seu nome: ")
nome = nome.split()

print(f"Primeiro nome: {nome[0]}\n"
      f"Último nome: {nome[-1]}")