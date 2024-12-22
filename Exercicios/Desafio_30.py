"""
Crie um programa que diga se um número é par ou impar
"""

number: int = int(input("Número: "))

print("Par" if number % 2 == 0 else "Ímpar")