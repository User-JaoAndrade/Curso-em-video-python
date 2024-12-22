"""
Desenvolva um programa que leia as duas notas de um alino, calcule e mostre a sua média
"""
notas: list = [None, None]
notas[0] = float(input("Primeira nota: "))
notas[1] = float(input("Segunda nota: "))

print(f"A média entre {notas[0]} e {notas[1]} é {sum(notas) / 2:.1f}")