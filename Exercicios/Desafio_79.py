"""
Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. 
Caso o número já exista lá dentro, ele não será adicionado. 
No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
"""

lista_de_numeros: list = []

while True:
    numero: int = int(input("Informe um número: "))
    if numero in lista_de_numeros:
        continue
    lista_de_numeros.append(numero)
    lista_de_numeros.sort()
    
    numero = input("\nDeseja informar outro número? [S]im [any value] Não\n-> ")
    if numero.upper() != 'S':
        break

print(*lista_de_numeros)
