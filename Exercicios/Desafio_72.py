"""
Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

Regras:
O programa deve continuar pedindo o número até que o usuário digite um valor válido.
"""

i: int = None
tupla: tuple = 'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezesete', 'dezoito', 'dezenove', 'vinte'

while True:
    i = int(input("Informe um número de 0 a 20: "))
    if i < 0 or i > 20:
        continue
    break

print(f"{tupla[i]}")