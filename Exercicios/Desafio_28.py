"""
Faça um programa que faça o computador gerar um número entre 0 e 5 e peça para o usuário tentar advinhar o número
Mostre na tela se acertou ou não
"""

import random

random_number: int = random.randint(0, 5)
user_number: int = int(input("PENSEI EM UM NÚMERO, TENTE ADVINHAR...\n-> "))

print("Acertou" if user_number == random_number else "Perdeu")