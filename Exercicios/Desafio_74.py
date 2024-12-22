"""
Faça um programa que vai gerar cinco números aleatórios dentro de uma
depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla
"""
import random

tupla: tuple = random.randint(1, 1000), random.randint(1, 1000), random.randint(1, 1000), random.randint(1, 1000), random.randint(1, 1000)
print("Números gerados:", *tupla)
print(f"Maior valor da lista: {max(tupla)}")
print(f"Menor valor da lista: {min(tupla)}")