"""
Crie um algoritmo que leia o número e mostre o seu dobro, triplo e raiz quadrada
"""
import math

number: int = int(input("Informe um número: "))
print(f"O Dobro de {number} é {number*2}\n"
      f"O Triplo de {number} é {number*3}\n"
      f"A Raiz quadrade de {number} é {math.sqrt(number)}")