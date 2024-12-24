"""
Aprimore o desafio anterior mostrando ao final
a) A soma de todos os valores pares digitados
b) a soma dos valores da terceira coluna
c) o maior valor da segunda linha
"""

lista: list = [[None for _ in range(3)] for _ in range(3)]
soma_pares: int = 0
soma_terceira_coluna: int = 0

for indice, value in enumerate(lista):
    for i in range(len(value)):
        value[i] = int(input(f"[{indice}][{i}]: "))

        if value[i] % 2 == 0:
            soma_pares += value[i]
else:
    for i in range(3):
        soma_terceira_coluna+=lista[i][2]

for i in range(len(lista)):
    print(*lista[i])

print(f"\nA Soma de todos os valores pares foi -> {soma_pares}")
print(f"A Soma de todos os valores da terceira coluna foi -> {soma_terceira_coluna}")
print(f"O maior valor da segunda linha foi -> {max(lista[1])}")