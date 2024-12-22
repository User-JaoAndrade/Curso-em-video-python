"""
Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500
"""

soma_M3 = 0

for i in range(1, 501, 1):
    if i % 3 == 0:
        if i % 2 != 0:
            soma_M3 += i
    
print(soma_M3)