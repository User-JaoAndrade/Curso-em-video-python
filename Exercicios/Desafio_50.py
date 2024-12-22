"""
Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
 Se o valor digitado for ímpar, desconsidere-o.
"""
lista_pares: list = []
soma_dos_pares: int = 0

for i in range(1, 7):
    number: int = int(input(f"Número {i}: "))
    if number % 2 == 0:
        lista_pares.append(number)
        soma_dos_pares += number
print("Soma dos números", *lista_pares, f"é {soma_dos_pares}")