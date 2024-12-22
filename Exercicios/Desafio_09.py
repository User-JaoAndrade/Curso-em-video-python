"""
Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada
"""

number: int = int(input("Deseja ver qual tabuada?\n-> "))

for i in range(1, 11):
    print(f"{i:2} x {number} = {number * i}")