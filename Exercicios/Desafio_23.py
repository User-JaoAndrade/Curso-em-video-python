"""
Faça um programa que leia um número de 0 a 999 e mostre na tela cada um dos digitos separados
EX:
num: 1834
Unidade: 4
Dezena: 3
Centena: 8
Milhar: 1
"""

numero: int = int(input("Informe um número: "))
unidade: int = numero // 1 % 10
dezena: int = numero // 10 % 10
centena: int = numero // 100 % 10
milhar: int = numero // 1000 % 10

print(f"Unidade: {unidade}\n"
      f"Dezema: {dezena}\n"
      f"Centena: {centena}\n"
      f"Milhar: {milhar}")