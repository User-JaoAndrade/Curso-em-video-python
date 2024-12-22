"""
Peça 3 números e mostre qual é o maior e o menor entre eles
"""
lista: list = []

for i in range(3):
    numero: int = int(input(f"Numero {i+1}: "))
    lista.append(numero)

print(f"Maior: {max(lista)}\n"
      f"Menor: {min(lista)}")