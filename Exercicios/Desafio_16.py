"""
Crie um programa que leia um número real qualquer pelo teclado e mostre
na tela a sua porção inteira

ex: 6.127
O número 6.127 tem a parte inteira 6
"""
import math

number: float = float(input("Número real: "))
print(f"O número {number} tem a parte inteira {math.trunc(number)}")