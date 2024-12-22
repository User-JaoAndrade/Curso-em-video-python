"""
Faça um programa que mostre a sequencia de fibbonaci
"""

numero = int(input("Numero: "))
count = 0

a, b = 0, 1

print(f"{a} -> {b} -> ", end='')
for i in range(numero-2):
    a, b = b, a + b
    print(f"{b} -> ", end='')
else:
    print("FIM")