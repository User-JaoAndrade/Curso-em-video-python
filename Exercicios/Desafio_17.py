"""
Faça um programa que leia o comprimeiro do cateto oposto e do cateto adjacente
de um triângulo retângulo. Calcule e mostre o comprimeiro da hipotenusa
"""

import math

catetA: int = int(input("Cateto Adjacente: "))
catetO: int = int(input("Cateto Oposto: "))

print(f"Hipotenusa: {math.hypot(catetA, catetO):.2f}")