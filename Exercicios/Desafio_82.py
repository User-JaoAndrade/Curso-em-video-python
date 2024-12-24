"""
Crie um programa que vai ler vários números e colocá-los em uma lista. 
Depois disso, crie duas listas extras que vão conter apenas os valores 
pares e os valores ímpares digitados, respectivamente.
No final, mostre o conteúdo das três listas geradas.
"""

lista_completa: list = []
lista_par: list = []
lista_impar: list = []
opcao: str = ''

while opcao.lower() != 's':
    numero: int = int(input("Número: "))
    lista_completa.append(numero)

    if numero % 2 == 0:
        lista_par.append(numero)
    else:
        lista_impar.append(numero)

    opcao = input("Deseja parar? Aperte 's' para finalizar\n-> ")

print("Lista Completa:", *lista_completa)
print("Lista com números pares:", *lista_par)
print("Lista com números ímpares:", *lista_impar)