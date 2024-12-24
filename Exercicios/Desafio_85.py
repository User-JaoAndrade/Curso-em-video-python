"""
Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista 
única que mantenha separados os valores pares e ímpares. 
No final, mostre os valores pares e ímpares em ordem crescente
"""

lista_unica: list = [[], []]

for i in range(1, 8):
    numero: int = int(input(f"Numero {i}: "))
    if not numero % 2 == 0:
        lista_unica[1].append(numero)
    else:
        lista_unica[0].append(numero)

print("Lista com números pares:", *lista_unica[0])
print("Lista com números ímpares:", *lista_unica[1])