"""
Faça um programa que tenha uma função chamada maior(), 
que receba uma lista de números e retorne o maior número dessa lista.

Requisitos:
A função deve receber uma lista de números como parâmetro.
O programa deve verificar se a lista contém pelo menos um número.
O programa deve retornar o maior número presente na lista.
"""
def maior(lista) -> int:
    maior: int = 0
    for i in range(len(lista)):
        if lista[i] > maior:
            maior = lista[i]
    return maior

if __name__ == '__main__':
    lista_de_numeros: list = []
    numero: int = 0

    while numero != 999:
        lista_de_numeros.append(numero)
        numero = int(input("Número (999 para parar): "))
    
    maior_numero: int = maior(lista_de_numeros)

    print(f"{maior_numero}")