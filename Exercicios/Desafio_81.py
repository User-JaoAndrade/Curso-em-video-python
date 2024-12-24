"""
Crie um programa que vai ler vários números e colocá-los em uma lista. Depois disso, mostre:

Quantos números foram digitados.
A lista de valores ordenada de forma decrescente.
Se o valor 5 foi digitado e está ou não na lista.
"""

lista: list = []
opcao: str = ''

while opcao.lower() != 's':
    numero: int = int(input("Número: "))
    lista.append(numero)
    lista.sort(reverse=True)
    opcao = input("Deseja parar? Aperte 's' para finalizar\n-> ")

print("\nLista em ordem decrescente:", *lista, "\n"
      f"Foram digitados {len(lista)} números")
print("5 está na lista" if 5 in lista else "5 não está na lista")